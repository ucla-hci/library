<!-- source: https://arxiv.org/abs/2408.16702 | DOI: 10.1109/TVCG.2024.3456402 (IEEE VIS 2024) -->

# Guo et al.: VMC — A Grammar for Visualizing Statistical Model Checks

## One Sentence
A 2024 IEEE VIS paper introducing a formal four-component grammar for specifying model check visualizations, implemented as an R package, validated against canonical examples and expert modeler interviews.

## More Sentences
VMC defines a model check visualization through (1) samples from model distributions, (2) transformations on observed data to facilitate comparison, (3) visual encodings of distributions, and (4) layouts enabling side-by-side model-vs-data comparison. The grammar enables concise specification that reduces edit distance relative to existing visualization toolkits. An interview study with three expert modelers surfaced challenges in exploring the space of correct and effective model checks.

## Key Points

### Grammar as Scaffolding for Hypothesis Testing
> "Some transformations on the observed data are meant to help test a hypothesis, e.g., whether the model's predictive distribution captures the mean or median of the observed data."

### Reducing Specification Complexity
VMC shows that encoding model check logic formally reduces the authoring burden — a key barrier to routine hypothesis validation in practice.

### Expert Modeler Challenges
The interview study reveals that even experts struggle to identify what model check is appropriate, suggesting that tool guidance (not just expressiveness) is needed.

## Other Notes
Authors: Ziyang Guo, Alex Kale, Matthew Kay, Jessica Hullman. The theoretical companion to EVM (Kale et al. 2023). VMC addresses the grammar/language level; EVM addresses the user behavior level. Together they constitute a cohesive program on model-checking as hypothesis validation in visual analytics.

## Take-Away
Formalizes what it means to "check a hypothesis" against a statistical model in visualization — provides a principled design vocabulary for HCI researchers building confirmatory analysis tools.
