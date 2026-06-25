<!-- source: https://arxiv.org/abs/2308.13024 | DOI: 10.1109/TVCG.2023.3327163 (IEEE VIS 2023 / TVCG 30(1)) -->

# Kale et al.: EVM — Incorporating Model Checking into Exploratory Visual Analysis

## One Sentence
A 2023 IEEE VIS system and user study showing that embedding statistical model checks into an exploratory visual analysis tool prompts data scientists to scrutinize their data-generating assumptions and better validate their interpretations.

## More Sentences
EVM renders distributions of model predictions alongside user-generated data views, making the gap between user interpretation and formal statistical model explicit. A user study with data scientists from private and public sectors characterized how model checks alter thinking during exploratory work — participants used them to scrutinize expectations about the data-generating process. The work bridges the long-standing gap between visualization-based exploration and formal hypothesis validation.

## Key Points

### Model Checks as Inline Hypothesis Tests
EVM surfaces "visualization-based model checks" that show users the predictive distribution of their current model against actual data, converting hypothesis evaluation into a visual comparison task.

### Qualitative User Study Findings
> Participants "leverage model checks to scrutinize expectations about data generating process."

### Scaffolding Opportunities
The study identifies areas where further scaffolding is needed — users needed help interpreting model check outputs, pointing to an interface design gap.

## Other Notes
Authors: Alex Kale, Ziyang Guo, Xiao Li Qiao, Jeffrey Heer, Jessica Hullman. Published in IEEE TVCG, Vol. 30, Issue 1 (2024) as a VIS 2023 paper. Closely related to VMC (Guo et al. 2024) by the same Mu Collective / UW group, which formalizes a grammar for model check visualizations. EVM is the empirical complement to VMC's formal grammar.

## Take-Away
One of the strongest direct operationalizations of hypothesis validation in HCI: a working tool with user study evidence that model-checking visualizations alter how analysts evaluate their analytical conclusions.
