---
activities:
  - hypothesis-generation
  - evidence-evaluation
  - collaboration
  - workflow-orchestration
contributions:
  - framework
  - design-guidance
  - perspective
domains:
  - general
scope: field-level
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Valdes-Perez et al.: Principles of human-computer collaboration for knowledge discovery in science

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

> Discovery in science is the generation of novel, interesting, plausible, and intelligible knowledge about the objects of study

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### Plausibility, not validity
> ... we prefer the term *plausible* over the term *valid* because the latter connotes *certain* inference fields such as formal logic

"Validity" might have a narrower scope of application---
> ... only deductive, non-ampliative inference yields "valid" (certain) results, but these do not go beyond the limited content represented by the premises or the data.

### Data is not necessary
> There are many knowledge-driven (also known as theory-driven) tasks in science

### Case study: ARROWSMITH
A program that---
> ... notices connections between drugs or dietary factors and diseases in medicine.

How ARROWSMITH implemented the four dimensions:

- Novelty: ARROWSMITH used citation analysis to check that the two relevant MEDLINE subliteratures were disjoint or rarely co-cited. If no one had connected them, the output counted as “undiscovered public knowledge.” Source: Valdés-Pérez lines 194-198.  
- Interestingness: It used heuristics/stoplists to remove overly broad C terms, such as “hormone,” “pressure,” “lipid,” or “membrane,” unless they appeared in a more meaningful phrase. So it pushed toward specific, actionable biomedical factors. Lines 199-202.  
- Plausibility: The A-B-C chain was plausible because many biomedical associations are causal, and causal relations often support transitive reasoning. Even when the link was similarity rather than causality, the short path C -> B -> A made the conjecture more credible. Lines 203-206.  
- Intelligibility: The outputs were simple biomedical hypotheses, e.g. “C may treat or cause A,” which a medical scientist could understand and potentially test clinically. Lines 207-208.

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### The four criteria seem more appropriate for evaluating support
> ... any discovery program should be qualitatively evaluated along these dimensions.