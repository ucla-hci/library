---
activities:
  - hypothesis-generation
  - experiment-design
  - experiment-execution
  - data-analysis
  - evidence-evaluation
  - workflow-orchestration
contributions:
  - framework
  - method
  - system
  - empirical-study
domains:
  - general
scope: multi-activity
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Huang et al.: Automated Hypothesis Validation with Agentic Sequential Falsifications

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

![Figure 1: POPPER's sequential falsification workflow](../_assets/huang-popper-figure-1.png)

*Figure 1. Illustration of POPPER. Given a hypothesis and a pre-defined significance level $\alpha \in (0,1)$, POPPER constructs sequential experiments to falsify the hypothesis. In each iteration, an experiment-design agent proposes and self-critiques a falsification experiment; a relevance checker assesses its alignment with the main hypothesis; and an experiment-execution agent implements it and returns a p-value. The framework converts p-values from multiple experiments into sequential e-values and aggregates them. If the aggregate exceeds $1/\alpha$, it rejects the null hypothesis; otherwise, it proceeds to another falsification test. Source: [Huang et al. (2025), Figure 1](https://proceedings.mlr.press/v267/huang25n.html).*

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

<!-- ### Here is a point -->

## Other Notes
<!-- other things, not so important, but good to know -->

### A simple (and elegant) way of defining hypothesis
> A hypothesis is a theory or an explanation based on limited evidence.

## Karl Popper's philosophy of falsification
> ... rather than trying to directly prove a hypothesis of interest, one can attempt to *refute* its logical implications through experiments.

## Take-Away 
<!-- critiques, ideas, actionable things, etc. -->

## Q&A

Q: When applying POPPER to different domains, some would need to perform experiments in the physical labs, which can't be done by the experiment agents right? So what happened then?
A: **Yes, for the implementation evaluated in this paper.** The general framework could connect the execution agent to lab robots or ask human technicians to follow a protocol, but the reported experiments only analyzed existing, static datasets with Python. Wet-lab execution was left for future work; an unavailable or failed experiment was skipped.

Q: "a measurable implication (sub-hypothesis)" Are these the same concept? How to properly define "measurable implication"?
A: **They are used almost interchangeably here, but they are not strictly identical.** A *measurable implication* is a concrete, observable consequence that should hold if the main hypothesis holds. A *sub-hypothesis* is the formal, testable statement of that consequence, including explicit null and alternative versions. POPPER requires the null sub-hypothesis to be implied by the main null hypothesis.

Q: "a novel sequential testing framework" What's the rationale of doing such sequential tests? Is it imitating how human researchers validate hypotheses?
A: **The main rationale is statistical, not psychological imitation.** A broad hypothesis can have many measurable implications, so POPPER adaptively tests several of them and accumulates evidence. Sequential e-values let it combine potentially dependent, adaptively chosen tests and stop when evidence is sufficient while retaining Type-I error control (under the paper's assumptions). The loop resembles iterative research, but the authors do not present it as a cognitive model of human scientists.

Q: Are the sequential tests correspond to a sequence of sub-hypotheses? Or a sequence of tests only deal with one sub-hypothesis until falsifying it?
A: **Normally, they correspond to a sequence of sub-hypotheses.** Each round proposes a new sub-hypothesis and falsification test, informed by earlier rounds; the proposal may be revised before execution. POPPER then aggregates evidence across rounds and stops when the threshold is crossed or the experiment budget is exhausted.

Q: Use lay language to explain the relationship between p- and e-values
A: **A p-value asks, “If the null were true, how surprising would this result be?”** Smaller is stronger evidence against the null. **An e-value is more like an evidence score or betting payoff:** values above 1 favor rejection, and larger values mean stronger evidence. POPPER converts each valid p-value into an e-value so the e-values can be multiplied across rounds and checked at any time. An e-value is neither $1/p$ nor the probability that the hypothesis is true.