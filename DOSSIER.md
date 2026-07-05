# Combination-Therapy Research Dossier — Recurrent Glioblastoma (IDH-wildtype, RTK1)

**Purpose.** A structured, evidence-linked map from this tumor's specific molecular
vulnerabilities to blood-brain-barrier (BBB)-penetrant drug combinations — spanning
both oncology agents and repurposable, pharmacy-accessible drugs — designed to attack
multiple survival pathways *simultaneously*. Built to be re-run and updated as new
evidence appears.

> **This is decision-support material to discuss with your treating oncologist — not a
> prescription or a treatment plan.** I am not a physician. Every combination here,
> especially off-label and non-standard ones, must be evaluated by your oncologist
> against the full clinical picture: performance status, prior treatments (radiation,
> temozolomide, surgery), current labs, organ function, and drug–drug interactions.
> Several of these drugs have serious toxicities and interactions when combined. The
> value of this document is that it organizes the evidence so that conversation is as
> productive as possible.

---

## 1. The tumor's vulnerability fingerprint

Derived directly from the 2026-05-21 genomic profiling summary. Each is a lever a
therapy could pull.

| # | Alteration (from your report) | Clonality | What it does | Druggable node |
|---|------------------------------|-----------|--------------|----------------|
| V1 | **TERT** promoter C250T | Truncal driver (VAF 23%) | Reactivates telomerase → immortality | Telomere replication stress (ATR), telomerase substrate |
| V2 | **TP53** loss — splice + Y163N + G245S + P152L | Truncal / co-clonal (~24–25%) | G1/S checkpoint gone → tumor leans on the **G2/M checkpoint** to survive DNA damage | **WEE1, CHK1, ATR, PLK1** |
| V3 | **PTEN** R130\* + **chr10 loss** | Subclonal PTEN on broad chr10 loss | Unleashes **PI3K/AKT/mTOR** | Brain-penetrant PI3K/mTOR, AMPK |
| V4 | **NFKBIA** deletion (14q13.2) | Focal deletion | Loss of IκB-α → constitutive **NF-κB** survival signaling | NF-κB, proteasome axis, stemness |
| V5 | **MGMT** promoter **unmethylated** | Biomarker | Active MGMT repairs alkylation → **temozolomide resistance** | MGMT-independent routes; sensitizers |
| V6 | **TCF7L2** deletion (10q25) | Focal deletion | Wnt/β-catenin perturbation (context-dependent) | Wnt/GSK3 (exploratory, low priority) |
| V7 | GBM **metabolic** phenotype | Lineage-level | Warburg glycolysis, mevalonate/cholesterol dependence, autophagy survival | OXPHOS, HMG-CoA, autophagy/lysosome |
| V8 | **Immunologically cold** (TMB 4.7, MSS, HRD−, PD-L1 0) | Biomarker | Low neoantigen load → single-agent checkpoint blockade unlikely | Microenvironment / myeloid modulation |

**Live-evidence confirmation (queried this session).** In the Open Targets Platform,
the tumor's altered genes rank among the top targets associated with glioblastoma:
**TP53 (score 0.72), PTEN (0.64), TERT (0.54)** — i.e., the drivers this profile carries
are the genes the field most associates with the disease. In CIViC, **TERT** promoter
mutation carries *poor-outcome* prognostic evidence in glioblastoma (4 of 5 records,
direction SUPPORTS; 3 at Level B, 1 at Level D), and **TP53** carries *temozolomide-resistance* evidence —
independently reinforcing that TMZ alone is a weak lever here (consistent with
MGMT-unmethylated status). Note: for **PTEN**, the one prognostic CIViC record (EID343)
is direction *DOES_NOT_SUPPORT* — i.e., PTEN mutation is reported as **not** prognostic in
GBM; PTEN's therapeutic relevance here is as a **predictive** node (PI3K/mTOR pathway
activation), not a prognostic one.

---

## 2. Design logic — "cover the drivers, block the escapes"

The recurrent-GBM literature that matches your goal (attack *all* weaknesses at once)
converges on a layered design. This dossier follows it:

1. **Truncal drivers first.** TERT (V1) and TP53 loss (V2) are truncal — present in
   essentially every tumor cell. A regimen that ignores them treats only part of the tumor.
2. **The p53-null synthetic-lethal handle (V2) is the strongest targeted opportunity.**
   With the G1/S checkpoint gone, cells depend on the **G2/M checkpoint** (WEE1/ATR/CHK1)
   to survive DNA damage. Removing that checkpoint *while* applying a DNA-damage source
   (radiation or an alkylator) pushes cells into lethal mitotic catastrophe. This is a
   genuine, gene-matched vulnerability — not a generic cytotoxic.
3. **Shut the growth and survival pumps (V3, V4).** PI3K/mTOR and NF-κB are the two
   activated survival axes; brain-penetrant inhibitors + repurposed dampeners hit both.
4. **Starve the metabolic/autophagy escape routes (V7).** Tumors under targeted stress
   survive via autophagy and metabolic flexibility — the repurposing layer (metformin,
   statin, chloroquine, disulfiram) closes those doors.
5. **Don't over-invest in immunotherapy (V8).** The cold profile predicts little from
   single-agent checkpoint inhibitors; microenvironment modulators (e.g. celecoxib) are
   adjuncts, not anchors.

---

## 3. Candidate drug library (mapped to vulnerabilities + BBB)

See the coverage matrix figure. Tier **R** = repurposable/pharmacy-accessible;
tier **O** = oncology/targeted (trial or off-label oncologist supervision).

### Repurposable, BBB-permeable (tier R)
- **Metformin** — AMPK activation → mTOR suppression; complex-I inhibition lowers OXPHOS. *Hits V3, V7.* BBB: moderate.
- **Disulfiram + copper** — Cu-DDC aggregates NPL4/p97 → proteotoxic stress; NF-κB & ALDH (stemness) inhibition. *Hits V4, V7.* BBB: good. (DIRECT trial NCT02678975; CUSP9 NCT02770378.)
- **Chloroquine / Hydroxychloroquine** — autophagy/lysosome blockade removes a key survival mechanism under therapy stress. *Hits V4, V7.* BBB: good. (Randomized adjuvant trial NCT00224978.)
- **Atorvastatin** (lipophilic statin) — mevalonate blockade → impairs prenylation & cholesterol supply. *Hits V7.* BBB: moderate.
- **Celecoxib** — COX-2/PGE2 suppression → microenvironment. *Hits V8, V4.* Component of CUSP9. BBB: moderate.
- **Mebendazole** — microtubule destabilization; GBM preclinical + Johns Hopkins trials. *Hits V2, V7.* BBB: variable.
- **Valproic acid** — HDAC inhibition; possible radiosensitization (evidence mixed). *Hits V2, V5.* BBB: good.

### Oncology / targeted (tier O)
- **Paxalisib (GDC-0084)** — dual PI3K/mTOR inhibitor **engineered to cross the BBB**; PTEN-loss rationale. *Hits V3.* (GBM AGILE NCT03970447; paxalisib+metformin+keto NCT05183204.)
- **Adavosertib (AZD1775, WEE1 inhibitor)** — abrogates G2/M arrest in p53-null cells → mitotic catastrophe. *Hits V2.* (GBM Phase 0 NCT02207010; +RT/TMZ NCT01849146.)
- **ATR inhibitor (ceralasertib / berzosertib)** — exploits replication stress from p53 loss + telomere stress. *Hits V2, V1.*
- **6-thio-2'-deoxyguanosine** — telomerase substrate → telomere dysfunction selectively in TERT+ cells; preclinical CNS activity. *Hits V1.* (Experimental, not pharmacy-available.)
- **Temozolomide (context)** — standard alkylator, but MGMT-unmethylated = reduced benefit → use as a *sensitized/combination* DNA-damage source, not a standalone lever. *Context for V5.*

---

## 4. Candidate combination regimens

Three regimens spanning the access spectrum. Ordered from lowest to highest access barrier.

### Regimen A — Repurposing backbone (all pharmacy-accessible)
**Metformin + Disulfiram/Cu + Chloroquine + Atorvastatin + Celecoxib.**
Covers V3, V4, V7, V8. Broad pathway suppression using only generic oral, BBB-permeable
drugs. **Precedent:** the **CUSP9\*** protocol (NCT02770378) demonstrated that a
9-drug repurposing cocktail + metronomic TMZ is *feasible and tolerable* in recurrent GBM.
**Gap:** does not directly hit the p53-null G2/M dependency (V2) or telomere axis (V1);
leans cytostatic.

> **⚠ Evidence-grade update on disulfiram (added this iteration).** The **DIRECT randomized
> trial** (NCT02678975; JAMA Netw Open 2023, n=88 recurrent GBM) found that adding
> disulfiram + copper to alkylating chemotherapy **did *not* significantly improve 6-month
> survival** versus chemotherapy alone, and caused significantly **more toxicity** (grade ≥3
> adverse events 34% vs 11%; serious adverse events 41% vs 16%). The authors concluded it
> **should not be recommended** for recurrent GBM. This is the highest-grade evidence in the
> whole library and it is *negative* — disulfiram should be **de-prioritized** as a backbone
> anchor. It does not invalidate the multi-target *concept*, but the specific disulfiram+Cu
> arm did not deliver, so a repurposing backbone should not lean on it. Consider substituting
> or dropping it, and discuss with the oncologist given the toxicity signal.

### Regimen B — Targeted synthetic-lethal core (needs onc/trial access)
**Paxalisib + (Adavosertib *or* ATR inhibitor) + a DNA-damage source (RT or alkylator).**
Covers V2, V3, V1. This is the gene-matched heart of the strategy: brain-penetrant
PI3K/mTOR blockade + G2/M-checkpoint abrogation in a p53-null tumor. **Precedent:**
paxalisib GBM AGILE (NCT03970447); adavosertib GBM Phase 0/1 (NCT02207010, NCT01849146).
**Gap:** access-limited; overlapping myelosuppression demands careful dosing/sequencing.

### Regimen C — Integrated (backbone + one targeted anchor) — *most realistic*
**Paxalisib + Metformin + ketogenic metabolic pressure + Disulfiram/Cu + Chloroquine.**
Covers V2(partial via metabolic/replication stress), V3, V4, V7. **Precedent:** an actual
trial tested **paxalisib + ketogenic diet + metformin** in GBM (NCT05183204) — a direct
real-world analog of this exact combination. **Status caveat: NCT05183204 is listed as
SUSPENDED on ClinicalTrials.gov** (reason not confirmed here — verify before relying on it;
suspension may reflect funding, enrollment, or safety/administrative causes). It establishes
that this combination was designed and initiated, not that it was completed with positive
results. This is a plausible actionable starting point to discuss — one accessible targeted
anchor (paxalisib) layered onto a generic metabolic/survival-suppression backbone — but its
supporting precedent is a suspended trial, not mature outcome data.

---

## 5. Key safety flags to raise with the oncologist
- **Overlapping toxicities:** myelosuppression (alkylators + checkpoint inhibitors),
  QT prolongation (several agents), hepatotoxicity (disulfiram, statins, valproate),
  retinopathy (chloroquine, cumulative dose).
- **Drug–drug interactions:** disulfiram–alcohol reaction (strict avoidance), valproate
  enzyme effects, statin–CYP interactions.
- **The ERCC5 P19L VUS (VAF 78%)** is at germline-analysis threshold — worth confirming
  germline status, as nucleotide-excision-repair genes can affect platinum/alkylator handling.
- **Sequencing and timing matter** as much as drug choice (e.g., checkpoint-inhibitor
  timing relative to radiation).

---

---

## 7. Literature evidence layer (verified via OpenAlex, primary GBM references)

Each candidate drug is anchored to its best clinical or mechanistic reference in the GBM context. Evidence *grade* matters as much as existence — a randomized negative trial outweighs a promising preclinical signal.

| Drug | Best GBM reference | Year | Evidence grade | Finding / note |
|------|-------------------|------|----------------|----------------|
| Paxalisib | [Wen et al., paxalisib in newly diagnosed GBM, unmeth](https://doi.org/10.1200/jco.2022.40.16_suppl.2047) | 2022 | Clinical (Phase 2, ASCO) | Brain-penetrant PI3K/mTOR inhibitor; the pivotal GBM program behind Regimen B/C anchor. |
| Metformin | [Sato et al., Glioma-initiating cell elimination by m](https://doi.org/10.5966/sctm.2012-0058) | 2012 | Preclinical mechanism | Metformin depletes glioma stem cells via AMPK-FOXO3. |
| Metformin | [Metformin inhibits growth of human GBM cells & enhan](https://doi.org/10.1371/journal.pone.0123721) | 2015 | Preclinical | Supports metformin as a chemo/RT sensitizer in GBM. |
| Disulfiram+Cu **⚠ NEGATIVE** | [DIRECT: Disulfiram+Copper + chemo vs chemo alone in ](https://doi.org/10.1001/jamanetworkopen.2023.4149) | 2023 | Clinical (Randomized, JAMA Netw Open) | KEY NEGATIVE RESULT: DIRECT randomized trial (n=88, recurrent GBM) — disulfiram+Cu added to chemotherapy did NOT significantly improve 6-month surviva |
| Disulfiram+Cu | [Skrott et al. mechanism — disulfiram/Cu targets NPL4](https://doi.org/10.3390/cells9020469) | 2020 | Preclinical mechanism | Molecular basis: Cu-DDC aggregates NPL4 -> proteotoxic stress. |
| Chloroquine/HCQ | [Phase I/II hydroxychloroquine + RT/TMZ in newly diag](https://doi.org/10.4161/auto.28984) | 2014 | Clinical (Phase I/II) | Autophagy inhibition; defined tolerable HCQ dose with chemoradiation (dose-limiting toxicity noted). |
| Atorvastatin | [Anticancer effects of mevalonate-pathway modulation ](https://doi.org/10.1038/bjc.2014.431) | 2014 | Preclinical | Statin/mevalonate blockade rationale in glioma. |
| Celecoxib | [CUSP9* protocol for recurrent GBM (celecoxib is a co](https://doi.org/10.18632/oncotarget.2408) | 2014 | Protocol / rationale | Celecoxib as one of 9 repurposed drugs in the multi-target CUSP9 design. |
| Mebendazole | [Antiparasitic mebendazole shows survival benefit in ](https://doi.org/10.1093/neuonc/nor077) | 2011 | Preclinical | Foundational GBM efficacy signal that launched clinical interest (JHU). |
| Valproic acid | [Postradiation sensitization by HDAC inhibitor valpro](https://doi.org/10.1158/1078-0432.ccr-08-0643) | 2008 | Preclinical (radiosensitization) | HDAC-i radiosensitization; clinical GBM data later mixed — interpret cautiously. |
| Adavosertib(WEE1) | [WEE1 inhibitor adavosertib with radiation in diffuse](https://doi.org/10.1093/noajnl/vdac073) | 2022 | Clinical (early-phase) | WEE1 abrogation + RT in glioma; the p53-null synthetic-lethal handle in action. |
| ATR inhibitor | [DNA damage response inhibitors (ATR-CHK1-WEE1) for g](https://doi.org/10.1093/noajnl/vdab015) | 2021 | Review (mechanism/clinical landscape) | Frames ATR inhibition against replication stress from p53 loss + telomere stress. |
| 6-thio-dG | [Telomerase-targeted strategies incl. 6-thio-dG (telo](https://doi.org/10.1186/s13073-016-0324-x) | 2016 | Review / mechanism | Rationale for exploiting TERT+ status; 6-thio-dG is experimental, not pharmacy-available. |
| CUSP9 protocol | [Kast et al., conceptual multi-drug 'Coordinated Unde](https://doi.org/10.18632/oncotarget.969) | 2013 | Concept / rationale | The original framework for the exact all-weaknesses-at-once strategy you're pursuing. |
| CUSP9 protocol | [Efficacy of coordinated pharmacological blockade in ](https://doi.org/10.1007/s00432-019-02920-4) | 2019 | Preclinical validation | Preclinical support that the combined blockade hits GBM stem cells. |

---

## 6. How this is a *system*, not a one-off
Files in this dossier are machine-readable and re-runnable:
- `vulnerability_map.json` — the tumor's vulnerabilities and their druggable nodes
- `drug_candidates.json` — candidate drugs mapped to vulnerabilities + BBB + access
- `candidate_regimens.json` — combination regimens with precedent trials
- `combination_engine.py` — re-scores coverage, flags gaps, and re-queries live evidence
- `coverage_matrix.png` — the drug × vulnerability visual

Re-running the engine after any new result (new mutation, new trial, a drug that becomes
inaccessible) regenerates the ranked regimens and the evidence links. **Next iterations**
can: (1) add ADMET/BBB quantitation from ChEMBL, (2) pull full eligibility for the specific
recruiting trials to check fit, (3) add drug–drug interaction scoring, (4) expand the
repurposing library (e.g., the full CUSP9 set).
