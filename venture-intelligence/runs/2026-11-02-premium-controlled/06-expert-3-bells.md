# Expert 3: Tuned cast bronze bells (acoustic and foundry feasibility)

Date 2026-11-01. Scope: acoustic and foundry feasibility only. Commercial questions are out of scope.

**Source access warning.** WebFetch failed on every host tried (en.wikipedia.org, www.hibberts.co.uk: "getaddrinfo ENOTFOUND", host not in the session's allowed network domains). No page was opened. Every sourced fact below rests on a search summary and is marked `[S#, unverified at source]`. Under OPPORTUNITY.md the best possible outcome for this concept is therefore INVESTIGATE. The hosts en.wikipedia.org and www.hibberts.co.uk need to be allowed in the session network settings before a re-check.

Calculation script: `06-expert-3-bells-calc.py` (output `06-expert-3-bells-calc.out`), same folder. Calibration inputs marked `[A]` there are mine, not sourced.

## 1. Disciplines and deciding questions

| Discipline | Deciding question |
|---|---|
| Acoustics / modal physics | Can the partial ladder (hum, prime, tierce, quint, nominal) be set by profile and wall thickness, and how many partials can a foundry hit? |
| Metallurgy | Does 78/22 bell metal cast sound (no porosity, no cracks) in Indian sand/loam practice? |
| Manufacturing | Is the as-cast frequency scatter small enough that turning after casting can finish the tuning? Who in India owns a suitable vertical lathe and a measurement rig? |
| Music theory | Which pitch system for 12 bells owned separately, given that bells are inharmonic? |
| Supply chain | Which foundries, which cost per kg, which lead time? |
| IP / regulation | Minor here; no bell-specific BIS rule was searched (see section 7). |

## 2. Findings by discipline

### 2.1 Acoustics (verified, via search summary only)
- The ideal lowest five partials of a European tuned bell: hum two octaves below the nominal, prime one octave below, tierce a minor third above the prime, quint a fifth above the prime, nominal on top. `[S2] (unverified at source)` Wikipedia's strike-tone entry lists the same names. `[S1] (unverified at source)`
- The strike note sits near the prime in a well-tuned bell `[S1] (unverified at source)`. Hibberts argues the strike note comes mainly from the nominal and superquint with only a small effect from the lower partials. `[S2] (unverified at source)` The two sources disagree on the mechanism; both agree the strike pitch is about the prime.
- Tuning by location: lip work sharpens nominal, prime and tierce; sound-bow work flattens nominal and tierce; mid-waist work mainly moves the quint; shoulder work mainly moves the prime. `[S3] (unverified at source)`
- The tierce cannot be moved much on the tuning machine and depends mainly on the sound-bow design. `[S2] (unverified at source)` So the profile must be right in the pattern, not corrected afterwards.
- Seventeenth-century Hemony founders could measure and tune partials to about 3 cents. `[S2] (unverified at source)`
- Ratios on the ladder (calc section 1): tierce/prime = 6/5, 315.6 cents just, 300 cents in equal temperament. `[I]` A conventional tuned bell sounds minor by design. `[K]`

### 2.2 Indian bells versus European tuned bells
- Kalinga/Odisha bell-metal (kansa) craft centres on Balakati (about 13 km from Bhubaneswar), with other kansari clusters in Ganjam, Puri and Sambalpur districts. Products are mostly utensils, made by casting in moulds or by beating. About 1,500 artisans were working in 2017. The summaries describe hammering, filing and polishing, and give no tuning process. `[S4] (unverified at source)` Odisha has sought a GI tag for brass and bell-metal wares; the outcome was not found. `[S4] (unverified at source)`
- Tamil Nadu: Kumbakonam and Nachiarkoil are known for temple bell craft `[S9] (unverified at source)`. A 613 kg bronze bell was attributed to Kumbakonam. `[S6] (unverified at source)` Jalesar (Etah, Uttar Pradesh) is the other large temple-bell cluster; a 2,100 kg "ashtadhatu" bell for Ayodhya was cast there, reported at 6 ft high and 5 ft across, at about INR 21 lakh (another outlet says INR 25 lakh). `[S6] (unverified at source)`
- Not found after 6 searches (queries on "Kalinga bell tuning", "temple bell frequency analysis", "ghanta partials", "kansa bell acoustics" and the listed foundry searches): any measured partial spectrum of an Indian temple bell, or any Indian foundry that states it tunes bells to partials. Treat Indian practice as ear-voiced and unmeasured until shown otherwise. `[H]`
- Differences, hypotheses: Indian temple bells are often made in non-alloy-standard "ashtadhatu" or brass, struck on a fixed clapper for a long, beating, inharmonic ring that is culturally prized. European tuned bells use a fixed 78/22-type profile, a lathe-tuned partial ladder and low beating. `[H]` The cheapest check is the test in section 10.
- Metallurgy: bell metal is about 78% copper and 22% tin `[S4] (unverified at source)` (kansa is often quoted nearer 80/20 `[K]`).

### 2.3 Foundries and costs (all weak)
- India: AICS Bell Foundry, Tirunelveli, advertises bronze church bells from 30 kg to 5,000 kg; listings show a 1,000 kg brass temple bell at INR 2,500/kg and a 175 kg bronze temple bell at INR 22,000/kg. `[S5] (unverified at source)` The second figure looks like a data-entry artefact and I do not rely on it. Moradabad and Bengaluru sellers list brass church bells at INR 580 to 750/kg and a copper bell-metal church bell at INR 2,200/kg. `[S5] (unverified at source)` These are asking prices from listings, not transactions, and include no tuning.
- Ayodhya bell: INR 21 lakh for 2,100 kg is about INR 1,000/kg all-in `[I]`. That is below the raw metal value of 78/22 bronze at current prices (section 3.5), so that bell cannot be 78/22 tin bronze, or the price is wrong. `[I]`
- Abroad: Royal Eijsbouts (Asten, Netherlands) absorbed Petit & Fritsen in 2014. `[S8] (unverified at source)` Other tuning foundries I know by name only: Whitechapel and John Taylor (UK), Paccard (France), Grassmayr (Austria), Perner (Germany), Verdin (USA). `[K]` Not found after 3 searches (queries: "Eijsbouts bell price per kg", "tuned bell cost per kg carillon", "Whitechapel bell price"): any current price per kg or lead time. Only a 1960s-era American carillon cost point turned up, which is stale. `[S8] (unverified at source)`
- My lead-time view for a first tuned bell from a European foundry: months, not weeks, and the foundry will want a commission contract. `[H]`; the ask is one email, outside this run's no-contact rule.

## 3. Calculations (saved script)

Inputs. Calibration `[A]`: a 1.00 m diameter, 78/22 bell of English profile weighs about 600 kg and has prime near 196 Hz (G3); basis recollection of ring tenors, uncertain by about 20% on mass; test: weigh and measure any real bell. Metal prices `[S7] (unverified at source)`: LME copper cash about USD 14,415/t and tin about USD 50,855/t on 2026-10-23. Exchange rate INR 88 per USD `[A]` (not checked). Search results gave inconsistent older figures for tin (about USD 20,800/t) which I discarded as a different year.

### 3.1 Scaling
For a geometrically similar bell, frequency is proportional to 1/D and mass to D^3. `[K]` Result: one semitone lower costs 1.189 times the mass; one octave lower costs 8 times. `[I]`

| Prime | Diameter | Mass (78/22) |
|---|---|---|
| 110 Hz (A2) | 1.78 m | about 3,400 kg |
| 131 Hz (C3) | 1.50 m | about 2,000 kg |
| 165 Hz (E3) | 1.19 m | about 1,000 kg |
| 196 Hz (G3) | 1.00 m | 600 kg `[A]` |
| 262 Hz (C4) | 0.75 m | about 250 kg |

Cross-check: scaling a 2,100 kg bell gives D = 1.52 m and a prime near 129 Hz `[I]`; the Ayodhya report says about 5 ft (1.52 m). `[S6] (unverified at source)` That agrees, but one comparison with a bell of unknown alloy proves little.

### 3.2 Twelve-bell set, chromatic octave, equal temperament
- Tabletop set C5 to B5: total about 173 kg, heaviest 31.5 kg (D 0.37 m), lightest 4.7 kg (D 0.20 m). `[I]`
- Hall set G3 to F#4: total about 3,300 kg, heaviest 600 kg, lightest 89 kg. `[I]`

### 3.3 Frequency tolerance, casting alone versus turning
- 1% change in frequency is 17.2 cents. `[K]` A thin-shell model has frequency changing roughly with wall thickness; local changes have a weight of about 0.5 to 1. `[A]` Basis: standard shell scaling; test: modal analysis (section 11).
- Sound-bow thickness guessed as D/15 `[A]`. Then a 1 mm thickness error moves a 1.0 m bell by about 13 to 26 cents, and a 0.4 m bell by about 33 to 66 cents. A 3 mm error on the small bell gives 100 to 207 cents.
- If sand casting holds thickness to plus or minus 3% (core shift, pattern wear, ramming) `[A]`, the as-cast pitch error is about plus or minus 52 cents. `[I]`
- Conclusion `[I]`: casting alone gives roughly plus or minus 50 to 100 cents (half to one semitone) per partial and different partials drift separately, so the ladder ratios are off by ear-obvious amounts. Turning inside the bell, with an allowance cast on purpose, can bring each partial to the 3 to 10 cent range, as Hemony-type practice shows (about 3 cents). `[S2] (unverified at source)` Turning removes metal only, so bells are cast low and tuned up in pitch by cutting. `[K]`
- Beating: a 5 cent split between a doublet at 196 Hz beats at 0.57 Hz; at 523 Hz it beats at 1.5 Hz. `[I]` Casting asymmetry creates such splits; small bells beat faster and so show it more.

### 3.4 Pitch system for 12 bells
- The twelve swarasthanas (Sa, re, Re, ga, Ga, ma, Ma, Pa, dha, Dha, ni, Ni) map to 12 bells. Equal temperament versus a 5-limit just set differs by up to 15.6 cents (calc section 7). `[I]`
- The 22 shrutis cannot be covered by 12 bells. `[I]` A bell's partials are inharmonic, so what the ear calls the pitch is the strike note (about the prime); just ratios among strike notes will not make chords sound pure because tierces are minor thirds. `[K]`
- Recommended for feasibility: equal temperament with the prime (strike note) as the set pitch, A4 or Sa fixed by the buyer; just intonation adds a 15-cent spread that sits near the realistic tuning floor. Decision for the founder, `[H]`: ET is the only choice a foundry can certify with a reference tuner. The test: have the Hindustani musician who would use the set play the finished bell against a drone; no such listener was consulted.

### 3.5 How many partials can be tuned
Traditional European tuning sets about five (hum, prime, tierce, quint, nominal), with the superquint and above uncontrolled. `[S2] (unverified at source)` Modern founders tune more using finite-element profiles; I cannot cite a count. `[K]` Treat 4 to 5 as proven, 6 to 8 as plausible and needing a foundry with a computed profile.

### 3.6 Weight and metal cost of a large bell
- Raw 78/22 metal: 0.78 x 14.415 + 0.22 x 50.855 = USD 22.43/kg, about INR 1,974/kg at INR 88/USD `[I]`. Tin is half the cost. If tin falls by half it is INR 1,482/kg; up 25% it is INR 2,220/kg.
- With 8% melt and gating loss `[A]`: 600 kg bell about INR 12.8 lakh; 1,000 kg about INR 21.3 lakh; 2,100 kg about INR 44.8 lakh, metal only. `[I]` Excluding fuel, labour, moulding, turning, GST (rate not checked), carriage.
- A 1,000 kg bell is a reasonable size for one large temple bell `[I]`. The metal cost is a range, not a result: the listings differ by 2.5x among themselves `[I]`.

## 4. Feasibility class and confidence

| Item | Class | Confidence |
|---|---|---|
| (a) single large tuned temple bell, tuned to prime and 2 to 3 other partials | Plausible (proven in Europe, unproven at any named Indian foundry) | Medium-low: no source opened, no Indian tuning evidence found |
| (a) as a conventional Indian temple bell sound only (no partial control) | Proven | High [K] |
| (b) 12 tuned bells, each within about 10 cents on the strike note | Plausible | Medium-low |
| (b) 12 bells with the full 5-partial ladder in tune on each | Plausible but unproven locally; requires a tuning lathe and a measurement rig | Low |

## 5. Production routes compared

| Route | Setup | Unit cost driver | Quality risk | Lead time |
|---|---|---|---|---|
| Indian sand or loam foundry, no tuning (listings INR 580 to 2,500/kg) `[S5] (unverified at source)` | Pattern or sweep; low | Metal | Off-pitch by about half to one semitone `[I]`; partial ladder unknown | Days to weeks `[H]` |
| Indian foundry cast with a turning allowance, then turned and tuned on a vertical lathe at a machine shop (founder-designed) | Profile drawing, allowance, jig; the lathe is hired | Metal, turning hours, measurement | Cracks while turning; porosity; learning curve | Weeks per bell for the first, then faster `[H]` |
| Established European foundry (Eijsbouts, Whitechapel, Taylor, Paccard, Grassmayr) | Commission; tuned in-house | Not found | Lowest | Months `[H]`; not found |
| Alternative: hand-held tuned bar or bowl instruments (not cast bells) | None | Not in scope | n/a | n/a |

## 6. Bill of materials / delivery cost sketch (metal and process only)

| Line | Amount | Tag |
|---|---|---|
| 78/22 alloy metal, per kg | INR 1,974 (range 1,482 to 2,220) | `[I]` from `[S7] (unverified at source)` |
| Listed asking price, tuned-free church bells | INR 580 to 2,500/kg | `[S5] (unverified at source)` |
| 1,000 kg bell metal incl 8% loss | INR 21.3 lakh | `[I]` |
| Tabletop 12-bell set metal, 173 kg plus 8% loss | about INR 3.7 lakh | `[I]` |
| Turning and tuning labour, measurement rig, pattern, scrap | Not found; founder must obtain quotes | missing |
| Casting scrap rate for tuned bells | Not found | missing |

## 7. Safety, compliance, certification
- Pouring tin bronze at about 1,100 degrees C is a foundry safety matter handled by the foundry. `[K]` A large bell hung overhead needs a qualified structural engineer for the frame and mounting. `[K]`
- Not found after 2 searches: any BIS or Indian standard for bell tuning or for temple bells. Absence is not proof; I have not checked.

## 8. Intellectual property
Bell profiles from historical founders (Hemony, Simpson, Taylor) are old; I did not search patents. Not found after 0 searches: patent landscape for modern tuned-bell profiles. A design registration for an original profile and a brand are the only likely protections. `[K]`

## 9. Critical technical risks
1. As-cast partial scatter at the chosen foundry is unknown. Driven by the pattern and mould method.
2. Brittleness: 22% tin bronze is hard and brittle `[K]`; cracks can appear in cooling, in turning, or in service when struck hard. Thin small bells are less forgiving of porosity.
3. Doublet splitting from wall asymmetry, giving beats `[I]`.
4. The tierce is fixed by the profile, not the lathe `[S2] (unverified at source)`; a profile designed without modal analysis can land in the wrong place.
5. No Indian foundry is known to measure partials or own a bell-tuning lathe.
6. A founder with no skills cannot judge the sound by ear alone; the pitch is ear-judged with a drone, partials need an FFT on a recording. Open software such as a laptop spectrum analyser is enough for measurement `[K]`.

What a founder with no foundry skills needs: a foundry partner that accepts a drawing and a turning allowance; a machine shop with a vertical lathe and a skilled turner; a measurement kit (microphone, laptop FFT, reference tone); a modal-analysis run or a borrowed proven profile; time to tune a first bell by cut-and-measure.

## Single most important unknown (Even-if-true check)
**Unknown. Driven by the as-cast frequency scatter and ring quality of an Indian foundry's bells, which sets whether turning can finish the job.** If scatter is within about plus or minus 100 cents and the metal rings cleanly, the craft route works and the set is feasible. If bells arrive porous, cracked or with asymmetry splits above about 10 cents, tuning by turning fails and only a European foundry can deliver. `[H]`

## 10. Cheapest test to retire the biggest risk

- Method: (1) Buy 3 to 5 existing cast bells of 3 to 10 kg, ideally from two Indian clusters (Kumbakonam, Jalesar, Moradabad). Record each struck on a soft hanging with a phone and a laptop, and run an FFT; list the partials against the ideal ladder in section 2.1 and measure the doublet splits. (2) Then ask one foundry to cast 3 identical bells of about 5 kg from one profile with a 2 to 3 mm turning allowance in the same pour; measure each. (3) If the spread is under about 100 cents, have one turned on a hired lathe and re-measure.
- Cost, estimate `[A]`: step 1, INR 5,000 to 25,000 (at INR 580 to 2,500/kg `[S5] (unverified at source)` for about 30 kg total); step 2 to 3, INR 30,000 to 80,000 including pattern and lathe hire (no quote found; basis: small-job guess). Note: this run does no spending or contact; the figures are a plan.
- Duration: step 1, 2 to 3 weeks; step 2 to 3, 6 to 10 weeks `[H]`.
- Pass: spread of strike note across the 3 as-cast bells at or under 100 cents, both doublet splits at or under 10 cents, prime/tierce/quint within 30 cents of the ladder after cutting. Fail: any crack, strike-note spread above 150 cents, or doublet splits above 20 cents.

## 11. What a qualified expert or lab must review
- A bell-tuning expert or an acoustician: the profile and modal analysis (axisymmetric finite elements) before any pattern is made.
- A metallurgist or the foundry: alloy analysis (spectrometer), porosity check, pouring temperature, anneal.
- A structural engineer: hanging frame for the large bell.
- Not checked: standards, patents, the INR/USD rate, GST, and every price above.

## Comparison across concepts
(a) The single large bell tolerates a rough tuning: one bell can be turned until it matches, and Indian demand for the large temple bell sound exists without tuning. Its metal bill is about INR 21 lakh for 1,000 kg `[I]`; the cost of failure is one expensive bell. (b) The 12-bell set needs 12 successful castings and a repeatable process; the tabletop size (173 kg total) keeps a failure cheap, about INR 3.7 lakh of metal `[I]`. Technically (b) tests repeatability, (a) tests only one hit. Feasibility verdict: **INVESTIGATE** for both, gated by the test in section 10; sources unopened so no stronger verdict is allowed.

## Missing information
No opened source; no current European per-kg price or lead time; no Indian partial measurements; no turning or tuning cost; no BIS rule check; no patent search; the INR/USD rate; the calibration in section 3 (bell mass at a pitch) not checked against a measured bell.

## Sources

| # | Title | Publisher | URL | Published | Retrieved | Used for | Via |
|---|---|---|---|---|---|---|---|
| 1 | Strike tone | Wikipedia | https://en.wikipedia.org/wiki/Strike_tone | n/a | 2026-11-01 | partial names, strike near prime | search summary |
| 2 | The upper partials of bells; The musical pitch of bells | Hibberts | https://www.hibberts.co.uk/the-upper-partials-of-bells/ | n/a | 2026-11-01 | ideal ladder, tierce not tunable by lathe, Hemony 3 cents | search summary |
| 3 | Tuning chart | Keltek Trust | https://keltektrust.org.uk/sob13.html | n/a | 2026-11-01 | where to cut to move which partial | search summary |
| 4 | Bell metal craft reflects our rich heritage; Odisha Review 2017 | OrissaPOST; Odisha Government | https://www.orissapost.com/bell-metal-craft-reflects-our-rich-heritage-singh-deo/ | 2017 | 2026-11-01 | Kalinga/Balakati craft, artisan count, alloy | search summary |
| 5 | AICS Bell Foundry and church bell listings | IndiaMART | https://m.indiamart.com/aicsbellfoundry | 2026 | 2026-11-01 | asking prices INR/kg, size range | search summary |
| 6 | Hindu, Muslim artisans cast bell for Ram Temple; Alt News fact check; India.com | Tribune India; Alt News | https://www.tribuneindia.com/news/nation/hindu-muslim-artisans-cast-bell-for-ram-temple-124482 | 2019 | 2026-11-01 | Jalesar bell size, cost, Kumbakonam 613 kg | search summary |
| 7 | Market data (LME copper and tin) | Westmetall | https://www.westmetall.com/en/markdaten.php?action=showtable | 2026-10-23 | 2026-11-01 | metal prices | search summary |
| 8 | Petit and Fritsen | Wikipedia | https://en.wikipedia.org/wiki/Petit_%26_Fritsen | n/a | 2026-11-01 | Eijsbouts acquisition 2014 | search summary |
| 9 | Bell Metal Casting of Tamil Nadu | Global Inch | https://globalinch.org/?p=913 | n/a | 2026-11-01 | Kumbakonam, Nachiarkoil | search summary |
