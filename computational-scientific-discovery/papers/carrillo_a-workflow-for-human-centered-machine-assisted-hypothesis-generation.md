---
activities:
  - problem-formulation
  - literature-discovery
  - hypothesis-generation
  - evidence-evaluation
contributions:
  - framework
  - design-guidance
  - perspective
domains:
  - general
  - social-science
scope: multi-activity
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Carrillo et al.: A Workflow for Human-Centered Machine-Assisted Hypothesis Generation

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### Analogic reasoning drives hypothesis generation
> To generate hypotheses, researchers rely on analogic reasoning--the recombination of existing information in novel ways.

### Human limitation when using LM for hypothesis generation
> Humans, ..., are prone to confirmation bias and tend to cognitively disengage when interacting with more sophisticated artificial intelligence systems ...

The consequence (also relevant to other fields like drug discovery):
> ... hypothesis generation without appropriate guardrails could lead naïve researchers to waste time and resources pursuing irrelevant research avenues.

## Other Notes
<!-- other things, not so important, but good to know -->

### Echoing the novelty-plausibility joint objective
> ... social psychological scientists have a unanimous desire for "counterintuitive, yet plausible hypotheses"

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### The inner-outer world dichotomy
This commentary distinguishes two sets of considerations when prompting and when evaluating a generated hypothesis:
- Inner world, e.g., values, goals, prior knowledge
- Outer world, e.g., resources, literature

### Prompt elements for hypothesis generation with GPT-4

| Prompt element | What to specify |
| --- | --- |
| Request | The number of hypotheses and the kind wanted, such as directional, counterintuitive, testable, plausible, or falsifiable. |
| Additional information | Desired rationale, fit with the researcher's program, and useful keywords for follow-up database searches. |
| Inner world: interests | Topical or methodological interests, optionally supported by abstracts, introductions, or other background material. |
| Inner world: values | Scientific or social values to optimize for, such as fairness, reproducibility, generalizability, novelty, precision, or internal validity. |
| Inner world: current goals | Short- or long-term goals tied to a research question, study, article, or broader research program. |
| Outer world: study context | Project stage, publication type, and intended venue or outlet. |
| Outer world: resources | Available assets, such as samples, datasets, collaborators, and constraints, such as budget. |
| Outer world: knowledge landscape | Recent trends and active debates in the field. |
| Outer world: discipline-specific issues | Current methodological, conceptual, or theoretical concerns, such as sample representativeness. |

Note: Adapted from Table 1. Researchers should consider copyright and privacy when giving external systems article text, data, or other sensitive materials.

### Further readings
- Banker et al. 2024
- Hope et al. 2023
- Nuzzo, 2015
- Dell'Acqua, 2021
