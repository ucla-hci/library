---
activities:
  - hypothesis-generation
  - evidence-evaluation
contributions:
  - empirical-study
  - benchmark
domains:
  - social-science
scope: focused
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Banker et al.: Machine-Assisted Social Psychology Hypothesis Generation

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
Key findings:

- **GPT-3 (fine-tuned Curie) vs. human**: Clarity and impact did not differ significantly; humans scored higher on originality overall (p = .025), particularly at temperature 0.8. The authors also reported equivalence on all three dimensions within a ±0.2 standardized-effect margin. [Results, pp. 793–794](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=5).
- **GPT-4 (without fine-tuning) vs. human**: Experts rated generated hypotheses higher on all five dimensions (all p < .001); some temperature-specific comparisons were nonsignificant. [Results and Table 2, pp. 795–796](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=7).

The human baseline comprised hypotheses extracted from published/preprint abstracts. These are expert quality ratings, not experimental confirmation of the hypotheses. [Methods, pp. 793–794](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=5).

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### Key characterization of social psychology
> The unit of observation in social psychology is a human who is less consistent in their behavior and who interacts with their surroundings and other people in quite a varied manner.

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### Potentially reusable metrics for hypotheses (in humanity and social sciences?)
Paraphrased from the [supplement's participant instructions, p. 13](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=21):

| Metric | Meaning |
| --- | --- |
| Clarity | Precision and ease of understanding the central idea. |
| Originality | Innovativeness or creativity. |
| Impact | Importance for theory or practice in social psychology and neighboring fields. |
| Plausibility | Perceived credibility. |
| Relevance | Pertinence to social psychology. |

Each used a five-point scale from very low to very high. GPT-3 was evaluated on the first three; GPT-4 on all five. [Methods, pp. 793–794](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=5).

## Q&A
Q: The paper claims that social psychology relies on verbal models---what is that?

A: A verbal model expresses a theory and its proposed relationships in words rather than equations. It can still be tested with quantitative data. This is my interpretation of the paper’s usage. [p. 790](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=2).

Q: The paper then claims that because social psychology relies on verbal models, it follows naturally that we can use language models to generate hypotheses of social psychology research. Is this a logical argument?

A: It is a reasonable motivation, but not a logical guarantee. Language models can generate statements in the same form as these theories, but fluent wording does not ensure a hypothesis is novel, testable, or scientifically useful. Those qualities need separate checks. This is my assessment of the argument on [p. 790](https://gwern.net/doc/ai/nn/transformer/gpt/3/nonfiction/2024-banker.pdf#page=2).
