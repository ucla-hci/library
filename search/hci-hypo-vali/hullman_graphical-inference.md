<!-- source: https://hdsr.mitpress.mit.edu/pub/w075glo6/release/1 | DOI: 10.1162/99608f92.3ab8a587 -->

# Hullman & Gelman: Designing for Interactive EDA Requires Theories of Graphical Inference

## One Sentence
A 2021 Harvard Data Science Review position paper arguing that interactive exploratory data analysis tools must be grounded in theories of statistical inference — specifically Bayesian model checks — to avoid contradictory interface design objectives and misleading uncertainty representations.

## More Sentences
Without a theoretical grounding in human statistical inference, exploratory visual analysis tools can produce interfaces with contradictory affordances: encouraging exploration while discouraging the formal model checking that gives discoveries meaning. The authors propose viewing interactive analysis through the lens of Bayesian model checks, which unites exploratory and confirmatory phases: every visualization is implicitly a check of some prior model. This framing implies that interfaces should enable users to specify and compare data against null and reference distributions, and should be empirically tested against actual user inferential outcomes.

## Key Points

### EDA as Implicit Hypothesis Testing
> "Without a grounding in theories of human statistical inference, research in exploratory visual analysis can lead to contradictory interface objectives."

Every visual query during EDA implicitly tests a hypothesis — the authors argue for making this explicit in interface design.

### Bayesian Model Check as Unifying Framework
The model-check framing unites exploratory and confirmatory analysis within a single theoretical account, providing a principled basis for designing hypothesis validation affordances in visualization.

### Empirical Testing Requirement
The paper calls for evaluation of visualization tools against inferential outcomes (do users draw correct conclusions?), not just usability — a methodological implication for HCI research on hypothesis validation.

## Other Notes
Authors: Jessica Hullman, Andrew Gelman. Published in Harvard Data Science Review, Issue 3.3 (2021). Theoretical position paper, not a systems contribution. Closely related to EVM and VMC (both by Hullman's group), which operationalize the model-check idea. Also related to the Visual Belief Elicitation work (Koonchanok et al.).

## Take-Away
Provides the theoretical rationale for the full research program on hypothesis validation in visualization: the goal is not just to make EDA faster but to ensure that interactive exploration leads to *valid* inferences — requiring deliberate hypothesis-checking affordances.
