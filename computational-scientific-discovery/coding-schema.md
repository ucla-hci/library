# Coding Schema

The collection uses multi-valued metadata because papers often address several parts of scientific inquiry. A code indicates that the topic is a substantive object of the paper, not merely mentioned in passing.

## Research activities

| Code | Meaning |
| --- | --- |
| `problem-formulation` | Selecting, constructing, or reframing research questions and goals. |
| `literature-discovery` | Finding, connecting, or synthesizing relevant prior knowledge. |
| `data-representation` | Choosing or constructing the objects, variables, formats, or visualizations through which data are understood. |
| `hypothesis-generation` | Proposing, revising, or prioritizing explanations, relationships, models, or discovery candidates. |
| `experiment-design` | Choosing experimental paradigms, interventions, measurements, controls, or parameter settings. |
| `experiment-execution` | Carrying out physical or computational experiments and simulations. |
| `data-analysis` | Transforming, exploring, or modeling data to extract patterns and results. |
| `evidence-evaluation` | Assessing support, validity, novelty, plausibility, or competing claims and candidates. |
| `communication` | Writing, reviewing, explaining, or otherwise sharing research outputs. |
| `collaboration` | Coordinating people, agents, expertise, artifacts, or shared understanding. |
| `workflow-orchestration` | Integrating multiple research activities into a managed computational, robotic, or agentic process. |
| `reproducibility` | Supporting provenance, replication, data stewardship, or reuse. |

## Contribution types

| Code | Meaning |
| --- | --- |
| `theory` | An explanatory or predictive account of scientific discovery or behavior. |
| `framework` | An organizing set of concepts, stages, dimensions, or relationships. |
| `method` | A procedure, algorithm, or analytical technique. |
| `system` | An implemented interface, software system, agent, or robot. |
| `benchmark` | A task, dataset, or metric intended for systematic comparison. |
| `empirical-study` | Evidence from experiments, observations, interviews, deployments, or user studies. |
| `review` | A synthesis of prior literature or approaches. |
| `perspective` | An argument, critique, agenda, or commentary. |
| `design-guidance` | Principles or recommendations for designing tools and practices. |

## Scope

| Code | Meaning |
| --- | --- |
| `focused` | Concentrates on one or two closely related research activities. |
| `multi-activity` | Substantively connects several activities without covering the full research loop. |
| `end-to-end` | Implements or studies a near-complete iterative discovery pipeline. |
| `field-level` | Discusses scientific discovery broadly rather than implementing one bounded pipeline. |

## Domains

`general` denotes a cross-domain account. Other domain codes name the scientific setting directly and may be combined when useful; for example, a therapeutic-target paper may receive both `biomedicine` and `drug-discovery`.

## Front matter format

```yaml
---
activities:
  - hypothesis-generation
  - experiment-design
  - evidence-evaluation
contributions:
  - theory
  - empirical-study
domains:
  - general
scope: multi-activity
coding_status: coded
---
```

