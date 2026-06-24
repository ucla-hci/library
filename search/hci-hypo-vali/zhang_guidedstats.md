<!-- source: https://arxiv.org/abs/2410.00365 | IEEE VIS 2024 -->

# Zhang et al.: GuidedStats — Guided Statistical Workflows with Interactive Explanations and Assumption Checking

## One Sentence
A 2024 IEEE VIS system that scaffolds hypothesis testing workflows (e.g., regression, t-tests) inside computational notebooks by decomposing them into guided interactive steps with automatic assumption checking and visualizations.

## More Sentences
GuidedStats encapsulates each statistical procedure — including building regression models and running hypothesis tests — into interactive step-by-step workflows with built-in assumption verification and automatic visualizations. Users can iterate on input choices and receive recommended next actions, with results exportable back to code. Case studies demonstrate that the system surfaces assumption violations that would otherwise invalidate hypothesis tests, improving the validity of statistical conclusions.

## Key Points

### Statistical Hypothesis Testing as Guided Process
GuidedStats treats formal hypothesis testing (t-test, regression) not as a single operation but as a multi-step workflow requiring verification of preconditions — exactly the "evaluate evidence" stage of SDDS.

### Assumption Checking as Hypothesis Validation Support
> "GuidedStats offers valuable instructions for conducting fluid statistical analyses while finding possible assumption violations in the underlying data."

### Notebook Integration
Embedding the tool in Jupyter notebooks meets data scientists and scientists in their existing workflow, reducing the barrier to rigorous hypothesis validation.

## Other Notes
Authors: Yuqi Zhang, Adam Perer, Will Epperson. Published at IEEE VIS 2024, presented at CHI 2025 workshop on HCI+Health. Complements EVM and VMC but focuses on frequentist statistical testing workflows rather than Bayesian model checking. The CMU Data Interaction Group (DIG) paper.

## Take-Away
Demonstrates a practical HCI approach to supporting the formal statistical hypothesis testing phase — especially relevant for scientists who need to validate data-driven hypotheses using standard statistical workflows.
