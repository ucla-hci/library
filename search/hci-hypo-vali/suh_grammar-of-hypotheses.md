<!-- source: https://arxiv.org/abs/2204.14267 | IEEE VIS 2022 / TVCG -->

# Suh et al.: A Grammar of Hypotheses for Visualization, Data, and Analysis

## One Sentence
A 2022 IEEE VIS framework paper formalizing hypotheses in visual data analysis into three unified spaces — data, analysis, and visualization — to operationalize abstract notions of "analysis tasks" as testable propositions.

## More Sentences
The grammar defines what a dataset can express (data hypothesis space H_D), what a user wants to verify (analysis hypothesis space H_A), and what a visualization design can support (visualization hypothesis space H_V), using shared notation. Analyzing intersections between spaces reveals four outcomes: successful hypothesis validation, inappropriate visualization, insufficient data, and under/over-powered visualizations. A case study applies the grammar to the 2017 VAST Challenge, showing how it identifies necessary data transformations and unanswerable questions.

## Key Points

### Hypothesis Space Formalization
The grammar moves "analysis tasks" from abstract descriptions to concrete, operationalized hypothesis statements — a prerequisite for building systems that explicitly support hypothesis validation.

### Three-Space Intersection Analysis
> "The intersection analysis reveals successful solutions, inappropriate visualizations, insufficient data, and under/over-powered visualization scenarios."

### Connection to Analytic Provenance
The grammar supports analytic provenance tracking by recording which hypotheses were tested, rejected, or confirmed during analysis.

## Other Notes
Authors: Ashley Suh, Ab Mosca, Eugene Wu, Remco Chang (Tufts + Columbia). Published in IEEE Transactions on Visualization and Computer Graphics (TVCG), VIS 2022. The formal complement to EVM/VMC's empirical and grammar work — addresses the visualization design level. [abstract only for full paper — fetched via ar5iv]

## Take-Away
Provides the theoretical vocabulary for describing what hypothesis validation means in a visualization context — essential reference for any HCI researcher designing confirmatory analysis tools or studying hypothesis evaluation in visual analytics.
