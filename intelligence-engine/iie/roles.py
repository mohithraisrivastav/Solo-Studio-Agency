"""Specialist responsibilities. Roles are functions with tools and evidence duties, not chat personas."""
from __future__ import annotations

ROLES: dict[str, dict] = {
    "opportunity_scout": {"title": "Opportunity Scout", "stage": "discovery",
                          "duty": "Find unmet needs, recurring problems, and underserved segments from evidence."},
    "research_investigator": {"title": "Research Investigator", "stage": "research",
                              "duty": "Gather current sources, store citations, extract claims with exact quotes."},
    "inventor": {"title": "Inventor", "stage": "invention",
                 "duty": "Generate distinct concepts with structured invention methods."},
    "cross_disciplinary_researcher": {"title": "Cross-Disciplinary Researcher", "stage": "invention",
                                      "duty": "Transfer working mechanisms from other fields with a credible advantage."},
    "product_designer": {"title": "Product Designer", "stage": "technical",
                         "duty": "Form, function, user experience, and design intent."},
    "engineering_analyst": {"title": "Engineering Analyst", "stage": "technical",
                            "duty": "Technical feasibility, physical limits, failure modes, safety review needs."},
    "materials_manufacturing": {"title": "Materials and Manufacturing Specialist", "stage": "technical",
                                "duty": "Processes, sourcing, tooling, in-house versus outsourced production."},
    "buyer_researcher": {"title": "Buyer Researcher", "stage": "commercial",
                         "duty": "Buyer behaviour, motivations, and purchase evidence on the evidence ladder."},
    "commercial_analyst": {"title": "Commercial Analyst", "stage": "commercial",
                           "duty": "Revenue, costs, margins, cash needs, and operating risks with real numbers."},
    "originality_investigator": {"title": "Originality Investigator", "stage": "comparison",
                                 "duty": "Search for competing products, patents, papers, and prior solutions."},
    "critical_reviewer": {"title": "Critical Reviewer", "stage": "critique",
                          "duty": "Try to disprove claims and find weaknesses, with sources or stated reasoning."},
    "experiment_designer": {"title": "Experiment Designer", "stage": "validation",
                            "duty": "Design cheap tests for the assumptions that would change the decision."},
    "decision_director": {"title": "Decision Director", "stage": "decision",
                          "duty": "Apply evidence gates, reconcile disputes, record what stays unresolved."},
    "extractor": {"title": "Deterministic Extractor", "stage": "research",
                  "duty": "Rule-based claims that need no model (forum titles, explicit prices)."},
    "user": {"title": "User", "stage": "any", "duty": "Records direct evidence, approves actions, makes final calls."},
}


def title(role: str) -> str:
    return ROLES.get(role, {}).get("title", role)
