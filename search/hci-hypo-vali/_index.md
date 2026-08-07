<!-- generated: 2026-06-24 -->
<!-- research framing: Klahr & Dunbar's SDDS dual-space theory (hypothesis space + experiment space); focus = hypothesis validation phase -->

# HCI + Hypothesis Validation — Literature Index

## Paper List by Angle


### Angle 1 — Theoretical Foundation (SDDS / Dual-Space)

| Paper | Venue | Year | File |
|---|---|---|---|
| Klahr & Dunbar — Dual Space Search During Scientific Reasoning | *Cognitive Science* 12(1) | 1988 | `klahr_sdds-dual-space.md` |
| Hullman & Gelman — Designing for Interactive EDA Requires Theories of Graphical Inference | *Harvard Data Science Review* 3.3 | 2021 | `hullman_graphical-inference.md` |

**Note:** The researcher's context memo cites "Kahn's dual-space theory." The originating theory is Klahr & Dunbar's SDDS (1988), which is distinct and has 1,100+ citations. No "Kahn dual-space" theory was found in the literature; Klahr & Dunbar is the correct anchor.


### Angle 2 — Confirmatory / Hypothesis-Driven Visual Analytics Systems

| Paper | Venue | Year | File |
|---|---|---|---|
| Choi et al. — Concept-Driven Visual Analytics | CHI | 2019 | `choi_concept-driven-va.md` |
| Choi et al. — Visual (dis)Confirmation | IV (IEEE) | 2019 | `choi_visual-disconfirmation.md` |
| Suh et al. — A Grammar of Hypotheses for Visualization, Data, and Analysis | IEEE VIS / TVCG | 2022 | `suh_grammar-of-hypotheses.md` |
| Kale et al. — EVM: Incorporating Model Checking into Exploratory Visual Analysis | IEEE VIS / TVCG | 2023 | `kale_evm-model-checking.md` |
| Guo et al. — VMC: A Grammar for Visualizing Statistical Model Checks | IEEE VIS / TVCG | 2024 | `guo_vmc-grammar-model-checks.md` |

**Cluster summary:** This is the richest cluster. Concept-Driven VA and Visual (dis)Confirmation (both Khairi Reda's group) address the natural-language-to-visualization pipeline for hypothesis checking. Suh et al. formalize the hypothesis space as a grammar. EVM and VMC (Hullman/Kale group) operationalize model checks as a form of visual hypothesis validation, with EVM providing empirical user study evidence and VMC providing the formal grammar.


### Angle 3 — Belief Elicitation and Prior Specification

| Paper | Venue | Year | File |
|---|---|---|---|
| Koonchanok et al. — Data Prophecy: Effects of Belief Elicitation in Visual Analytics | CHI | 2021 | `koonchanok_data-prophecy.md` |
| Koonchanok et al. — Visual Belief Elicitation Reduces the Incidence of False Discovery | CHI | 2023 | `koonchanok_visual-belief-elicitation.md` |

**Cluster summary:** Both from Khairi Reda's group at IUPUI/IIT. Data Prophecy is the discovery study; Visual Belief Elicitation is the controlled experiment with quantified effect sizes (21% improvement in correct inferences, 12% reduction in false discoveries). Together they constitute strong evidence for lightweight belief-elicitation as a hypothesis validation intervention.


### Angle 4 — Statistical Workflow Support and Assumption Checking

| Paper | Venue | Year | File |
|---|---|---|---|
| Zhang et al. — GuidedStats: Guided Statistical Workflows with Interactive Explanations and Assumption Checking | IEEE VIS | 2024 | `zhang_guidedstats.md` |
| Sivaraman et al. — Divisi: Interactive Search and Visualization for Scalable Exploratory Subgroup Analysis | CHI | 2025 | `sivaraman_divisi.md` |

**Cluster summary:** GuidedStats addresses frequentist hypothesis test workflows (t-test, regression) with notebook-integrated guided steps. Divisi addresses hypothesis validation through subgroup discovery — testing whether hypothesized data subgroups behave differently. Both integrate into computational notebooks (the primary scientist workflow environment).


### Angle 5 — Causal Inference as Hypothesis Validation

| Paper | Venue | Year | File |
|---|---|---|---|
| Guo et al. — Causalvis: Visualizations for Causal Inference | CHI | 2023 | `guo_causalvis.md` |

**Cluster summary:** Causal inference is one of the most rigorous instantiations of hypothesis validation in observational science. Causalvis provides HCI tooling for the full causal inference pipeline, making it directly relevant to scientists who need to move from causal hypotheses to validated effect estimates.


### Angle 6 — Domain-Specific Scientific Tools (Biomedical / Climate)

| Paper | Venue | Year | File |
|---|---|---|---|
| Corvo et al. — IIComPath: Visual Analytics for Hypothesis-Driven Exploration in Computational Pathology | IEEE TVCG | 2021 | `corvo_iicompath.md` |
| Mirel & Görg — Scientists' Sensemaking when Hypothesizing about Disease Mechanisms | *BMC Bioinformatics* | 2014 | `mirel_sensemaking-disease-hypotheses.md` |
| Kehrer et al. — Hypothesis Generation in Climate Research with Interactive Visual Data Exploration | IEEE TVCG | 2008 | `kehrer_climate-hypothesis-generation.md` |
| Jing et al. — VIADS: A Visual Analytic Tool to Assist Hypothesis Generation in Clinical Research | *JMIR Human Factors* | 2023 | `jing_viads.md` |

**Cluster summary:** Domain-specific implementations and studies. Corvo et al. show how a VA system can structure the hypothesis-formulation-to-pipeline-execution cycle in cancer pathology. Mirel & Görg provide the only longitudinal observational study of a scientist's full hypothesis-validation workflow (bioinformatics). Kehrer et al. is the foundational "visual exploration → statistical validation" pipeline paper. Jing et al. is a clinical research usability study — heavier on generation than validation.


## Coverage Note

**Well covered:**
- Visual analytics systems for hypothesis-driven analysis (Angles 2–3 are saturated)
- Statistical model checking interfaces (EVM, VMC, GuidedStats)
- The Khairi Reda / Hullman lab research programs — two of the most active groups on this topic
- Biomedical domain applications (pathology, bioinformatics, clinical research)

**Gaps / what is missing:**
- No papers found from CSCW on collaborative hypothesis validation (multi-user or team science contexts)
- No papers from IUI on intelligent hypothesis validation assistants using AI
- No papers on qualitative/interpretive hypothesis validation (e.g., grounded theory, qualitative coding)
- No direct engagement with SDDS in a CHI paper: papers in this collection are informed by the dual-space framing but do not cite Klahr & Dunbar explicitly (the theoretical bridge is implicit, not cited)
- No papers on hypothesis validation for non-expert users or citizen science contexts
- The Mirel & Görg study (n=1) is the only naturalistic longitudinal study — more ecological studies are needed


## Suggested Follow-Up Queries

1. `site:dl.acm.org CSCW "hypothesis" "team science" "collaborative" validation` — to find collaborative hypothesis validation at CSCW
2. `IUI "hypothesis" "intelligent assistant" "scientist" 2020 2021 2022 2023 2024` — IUI papers on AI-assisted hypothesis evaluation
3. `"analytic provenance" "hypothesis" visualization CHI VIS` — provenance tracking as hypothesis history
4. `"Bayesian" "prior" "visualization" "uncertainty" CHI 2022 2023 2024 user study` — Bayesian prior elicitation tools beyond Reda group
5. `"pre-registration" "open science" visualization tool HCI CHI` — HCI tools for formal hypothesis pre-registration
6. `"sensemaking" "hypothesis" "scientists" CSCW 2019 2020 2021` — observational studies of hypothesis work in scientific teams
7. `"Klahr" "Dunbar" HCI cited tools "scientific discovery" system` — papers that explicitly cite SDDS in an HCI context
