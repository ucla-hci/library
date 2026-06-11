<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Nigam et al.: An interactive co-pilot for accelerated research ideation

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
This paper presents a workflow for LLM to assist with research ideation via two main processes: Motivation Validation and Method Synthesis.

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

<!-- ### Here is a point -->
### Motivation Validation pipeline
Input: title and abstract of a research proposal
Main steps:
- system: identify motivation and retrieve articles
- researcher: review & edit selections of articles
- system: generate binary questions to validate the proposal's motivation against the retrieved articles
- researcher: review & edit
- system: retrieve relevant sections from the selected articles to answer these questions


### Method Synthesis pipeline
- *college* agent: extract and define the proposal's problem
- *mentor* agent: generate similar research problems and decompose each main problem into sub-tasks
- researcher: refine generated problems
- *college* agent: consolidate similar problems and their solutions from these retrieved articles
- researcher: select preferred methods
- *mentor* agent: update proposal
- researcher: review & finalize proposal

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->