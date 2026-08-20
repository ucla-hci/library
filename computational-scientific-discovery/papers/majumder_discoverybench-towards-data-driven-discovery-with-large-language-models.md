---
activities:
  - data-representation
  - hypothesis-generation
  - data-analysis
  - evidence-evaluation
contributions:
  - benchmark
  - empirical-study
domains:
  - general
  - data-science
scope: multi-activity
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Majumder et al.: DiscoveryBench: Towards Data-Driven Discovery with Large Language Models

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

<!-- ### Here is a point -->

## Other Notes
<!-- other things, not so important, but good to know -->

### What is the type of "discovery" in this paper
The task in question here is really only a part of the entire discovery process and would be an invalid setting for drug discovery--
> ... *data-driven discovery*, where both search and verification of hypotheses may be carried out using a dataset alone (i.e., after physical experiments and data collection).

### Formalization of data-driven discovery
The following doesn't seem fundamentally different from QA? (Speculative QA?)
> ... a pragmatic formalization of data-driven discovery, namely the search for a *relationship* that may hold between *variables* in a *context*, where (importantly) the description of those facets may not be in the language of the dataset.


## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### Motivating a benchmarking work
This paper starts with a question that sums up what it is trying to benchmark:
> Can the rapid advances in code generation, function calling, and data analysis using large language models (LLMs) help automate the search and verification of hypotheses purely from a set of provided datasets?

Subsequently it shows how it is hard to answer this question given the existing literature, thus motivating the need of this work.

### Show room of improvement
It is compelling to show how the task in question is challenging. Even SOTA models only achieve a low performance, thus leaving room for future models to improve.