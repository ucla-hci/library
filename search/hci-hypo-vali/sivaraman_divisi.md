<!-- source: https://dl.acm.org/doi/10.1145/3706598.3713103 | arXiv: 2502.10537 -->

# Sivaraman et al.: Divisi — Interactive Search and Visualization for Scalable Exploratory Subgroup Analysis

## One Sentence
A CHI 2025 system and user study introducing Divisi, a notebook-integrated tool for discovering, evaluating, and curating data subgroups, showing through a think-aloud study with 13 practitioners that it uncovers surprising patterns and encourages more thorough exploration of dataset subtypes.

## More Sentences
Divisi addresses the difficulty of subgroup analysis in high-dimensional datasets where user-defined or static subgroups limit unexpected discoveries. A fast approximate subgroup discovery algorithm surfaces candidate subgroups that analysts then re-rank, refine, and visualize via a novel "Subgroup Map" showing overlap and coverage. The think-aloud study found that Divisi revealed interactions between features that practitioners had not anticipated, effectively supporting both hypothesis validation (checking expected subgroup differences) and hypothesis generation (discovering new subtypes).

## Key Points

### Subgroup Analysis as Hypothesis Testing
Discovering whether a subgroup has a different outcome distribution is a form of hypothesis testing — Divisi structures this process interactively and at scale.

### Subgroup Map Visualization
> "Divisi's interface allows data scientists to interactively re-rank and refine subgroups and to visualize their overlap and coverage in the novel Subgroup Map."

### Mixed Generation-Validation Workflow
The tool supports both confirmatory (does my hypothesized subgroup show the expected pattern?) and exploratory (what subgroups exist?) modes within one interface.

## Other Notes
Authors: Venkatesh Sivaraman, Zexuan Li, Adam Perer. Published at CHI 2025. From the CMU Data Interaction Group (DIG, Adam Perer). Complementary to GuidedStats and EVM — all three address how data scientists validate analytical claims interactively. [full text available via arXiv 2502.10537]

## Take-Away
Demonstrates that interactive subgroup discovery is a practical hypothesis validation task in data science, and that tooling can support it at scale — relevant for HCI research on supporting scientists working with complex heterogeneous datasets.
