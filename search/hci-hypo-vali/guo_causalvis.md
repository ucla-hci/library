<!-- source: https://dl.acm.org/doi/10.1145/3544548.3581236 | arXiv: 2303.00617 -->

# Guo et al.: Causalvis — Visualizations for Causal Inference

## One Sentence
A CHI 2023 system paper presenting four interactive visualization modules that support the complete causal inference workflow — from causal structure modeling through cohort construction to treatment effect exploration — developed iteratively with domain experts.

## More Sentences
Causal inference is a statistical paradigm for estimating causal effects from observational data; it is inherently hypothesis-driven (the analyst posits a causal graph and tests whether data support the estimated effect). Causalvis's four modules correspond to the main validation steps: causal graph specification, propensity score matching/cohort refinement, and treatment effect visualization. An evaluation with causal inference experts found the tool effectively supported the iterative process and enabled communication between domain experts and analysts.

## Key Points

### Causal Graphs as Hypothesis Statements
A causal diagram is a formal hypothesis about the data-generating process; Causalvis makes that hypothesis explicit and testable through interactive refinement and cohort analysis.

### Full Workflow Coverage
> Modules cover three steps: "Causal Structure Modeling, Cohort Construction/Refinement, and Treatment Effect Exploration" — mapping to hypothesis specification, data conditioning, and evidence evaluation.

### Expert-Centered Iterative Design
Design was driven by close collaboration with causal inference practitioners, ensuring the tool's affordances match real hypothesis validation needs.

## Other Notes
Authors: Grace Guo, Ehud Karavani, Alex Endert, Bum Chul Kwon. Published at CHI 2023. Causal inference is one of the most formal operationalizations of hypothesis validation in empirical science — Causalvis is the HCI counterpart to that methodology. [full text via arXiv 2303.00617]

## Take-Away
Shows how HCI systems can support a rigorous, structured approach to hypothesis validation (causal inference) through interactive visualization — particularly relevant for scientific and clinical research contexts where causal claims require explicit testing.
