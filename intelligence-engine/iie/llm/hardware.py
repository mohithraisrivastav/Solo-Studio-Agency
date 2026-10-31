"""Detect real hardware and benchmark installed local models before choosing defaults."""
from __future__ import annotations

import os
import platform
import re
import shutil
import subprocess
from pathlib import Path

from ..util import now_iso
from . import GenTask, OllamaProvider


def detect_hardware() -> dict:
    info: dict = {
        "os": f"{platform.system()} {platform.release()}",
        "machine": platform.machine(),
        "cpu_count": os.cpu_count(),
        "cpu_model": None,
        "ram_gb": None,
        "gpus": [],
        "accelerator": "none detected",
    }
    cpuinfo = Path("/proc/cpuinfo")
    if cpuinfo.exists():
        m = re.search(r"model name\s*:\s*(.+)", cpuinfo.read_text(errors="replace"))
        info["cpu_model"] = m.group(1).strip() if m else None
    meminfo = Path("/proc/meminfo")
    if meminfo.exists():
        m = re.search(r"MemTotal:\s+(\d+) kB", meminfo.read_text())
        if m:
            info["ram_gb"] = round(int(m.group(1)) / 1024 / 1024, 1)
    elif platform.system() == "Darwin":
        try:
            out = subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, timeout=5).stdout
            info["ram_gb"] = round(int(out.strip()) / 1024**3, 1)
            info["cpu_model"] = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True,
                                               text=True, timeout=5).stdout.strip() or None
        except Exception:  # noqa: BLE001
            pass
    if shutil.which("nvidia-smi"):
        try:
            out = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"],
                capture_output=True, text=True, timeout=10,
            ).stdout
            for line in out.strip().splitlines():
                name, mem = [x.strip() for x in line.split(",")[:2]]
                info["gpus"].append({"name": name, "vram_gb": round(float(mem) / 1024, 1), "vendor": "nvidia"})
        except Exception:  # noqa: BLE001
            pass
    if shutil.which("rocm-smi"):
        info["gpus"].append({"name": "AMD GPU (rocm-smi present)", "vram_gb": None, "vendor": "amd"})
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        info["accelerator"] = "Apple Silicon (Metal, unified memory)"
    elif info["gpus"]:
        info["accelerator"] = ", ".join(g["name"] for g in info["gpus"])
    info["recommendation"] = recommend(info)
    return info


def recommend(info: dict) -> str:
    ram = info.get("ram_gb") or 0
    vram = max([g.get("vram_gb") or 0 for g in info.get("gpus", [])] or [0])
    budget = vram if vram else (ram if info.get("accelerator", "").startswith("Apple") else ram * 0.6)
    if budget >= 40:
        size = "up to ~32B parameters (4-bit)"
    elif budget >= 20:
        size = "up to ~14B parameters (4-bit)"
    elif budget >= 10:
        size = "up to ~8B parameters (4-bit)"
    elif budget >= 5:
        size = "~3B to 4B parameters (4-bit)"
    else:
        size = "~1B to 1.5B parameters; expect weak reasoning"
    mode = "GPU" if vram else ("unified memory" if info.get("accelerator", "").startswith("Apple") else "CPU only")
    return f"{mode}: {size}. Benchmark installed models before relying on any of them."


BENCH_SCHEMA = {
    "type": "object",
    "properties": {
        "sum": {"type": "integer"},
        "cheapest_item": {"type": "string"},
        "currency": {"type": "string"},
        "risk": {"type": "string"},
    },
    "required": ["sum", "cheapest_item", "currency", "risk"],
}

BENCH_PROMPT = (
    "A workshop buys: brass sheet at INR 1,450, walnut board at INR 2,300, and glue at INR 380.\n"
    "1) What is 17 + 25? Put it in 'sum'.\n2) Which item is cheapest? Put its name in 'cheapest_item'.\n"
    "3) Put the currency code in 'currency'.\n4) Name one business risk for a small workshop in 'risk'.\n"
    "Return JSON only."
)


def benchmark_ollama(db, url: str, models: list[str] | None = None) -> list[dict]:
    """Run a fixed structured task on each installed model. Records speed, JSON validity, correctness."""
    probe = OllamaProvider(url)
    hw = detect_hardware()
    results = []
    try:
        installed = [m["name"] for m in probe.list_models()]
    except Exception as e:  # noqa: BLE001
        return [{"error": f"Ollama not reachable: {e}"}]
    for name in models or installed:
        p = OllamaProvider(url, name, timeout=600)
        rec = {"provider": "ollama", "model": name, "hardware": hw, "ran_at": now_iso()}
        try:
            out = p.generate(GenTask(role="benchmark", purpose="benchmark", system="You return JSON.",
                                     prompt=BENCH_PROMPT, schema=BENCH_SCHEMA, temperature=0.0, max_tokens=200))
            rec.update(json_valid=1, latency_s=p.last_stats.get("latency_s"),
                       tokens_per_sec=p.last_stats.get("tokens_per_sec"))
            rec["correct"] = int(out.get("sum") == 42 and "glue" in str(out.get("cheapest_item", "")).lower()
                                 and str(out.get("currency", "")).upper() == "INR")
        except Exception as e:  # noqa: BLE001
            rec.update(json_valid=0, correct=0, error=f"{type(e).__name__}: {str(e)[:200]}")
        if db is not None:
            with db.tx():
                db.insert("benchmarks", rec)
        results.append(rec)
    return results


def choose_default(results: list[dict], min_tps: float = 4.0) -> str | None:
    """Pick the best usable model: correct + valid JSON, preferring larger models that are fast enough."""
    good = [r for r in results if r.get("json_valid") and r.get("correct")]
    if not good:
        return None
    usable = [r for r in good if (r.get("tokens_per_sec") or 0) >= min_tps] or good

    def size(r: dict) -> float:
        m = re.search(r"(\d+(?:\.\d+)?)b", r["model"].lower())
        return float(m.group(1)) if m else 0.0

    return max(usable, key=lambda r: (size(r), r.get("tokens_per_sec") or 0))["model"]
