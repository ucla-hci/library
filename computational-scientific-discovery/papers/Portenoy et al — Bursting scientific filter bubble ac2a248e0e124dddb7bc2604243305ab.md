---
activities:
  - problem-formulation
  - literature-discovery
  - collaboration
contributions:
  - system
  - empirical-study
domains:
  - science-of-science
scope: multi-activity
coding_status: coded
---

# Portenoy et al. —  Bursting scientific filter bubbles: Boosting innovation via novel author discovery

```
@inproceedings{portenoy2022bursting,
intro={Isolated silos of scientific research and the growing challenge of information overload limit awareness across the literature and hinder innovation. Algorithmic curation and recommendation, which often prioritize relevance, can further reinforce these informational “filter bubbles.” In response, we describe Bridger, a system for facilitating the discovery of scholars and their work. We construct a faceted representation of authors with information gleaned from their papers and inferred author personas and use it to develop an approach that locates commonalities and contrasts between scientists to balance relevance and novelty. In studies with computer science researchers, this approach helps users discover authors considered useful for generating novel research directions. We also demonstrate an approach for displaying information about authors, boosting the ability to understand the work of new, unfamiliar scholars. Our analysis reveals that Bridger connects authors who have different citation profiles and publish in different venues, raising the prospect of bridging diverse scientific communities.},
  title={Bursting scientific filter bubbles: Boosting innovation via novel author discovery},
  author={Portenoy, Jason and Radensky, Marissa and West, Jevin D and Horvitz, Eric and Weld, Daniel S and Hope, Tom},
  booktitle={Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems},
  pages={1--13},
  year={2022}
}

```

# One Sentence


The authors suggested Bridger, which is an AI-based interface to provide a faceted representation of authors with information gleaned from their papers and inferred author personas, using it to develop an approach that locates commonalities and contrasts between scientists to balance relevance and novelty. 

# More Sentences


This tool helps users discover authors considered useful for generating novel research directions.

# Key Points


Bridger's approach to burst scientific filter bubbles and promote a more interconnected scholarly community is a pivotal development in how academic literature and collaborations can be fostered.

![스크린샷 2024-08-13 오후 5.35.56.png](../../_assets/portenoy_et_al_bursting_scientific_filter_bubble_ac2a248e0e124dddb7bc2604243305ab-screenshot.png)

### How do they define success? How did they evaluate their approach?

The paper defines success less as "did the model predict the right label" and more as "did this actually help a researcher discover someone worth knowing about, whom they wouldn't have found otherwise." That's operationalized across two studies with CS researchers:

- **Study 1 (author depiction):** 13 participants judged whether the system's faceted summary (tasks, methods, resources) of a *known* author matched their actual understanding, then did the same for 5 unfamiliar authors — testing whether the facets are accurate and useful for making sense of a stranger's work.
- **Study 2 (author discovery):** 20 participants compared Bridger's facet-based matching (which explicitly balances relevance and contrast) against a Specter-embedding relevance baseline, rating recommended authors on cards and giving think-aloud/interview feedback on whether each recommendation was useful for sparking novel research directions.

Concretely, "success" is measured by:
- **Preference:** 78% of participants preferred Bridger's recommendations over the relevance-only baseline; 96% preferred Bridger's facet items specifically.
- **Structural diversity:** whether the recommended authors are actually novel relative to the user — measured via citation distance, publication-venue distance, and co-authorship-graph hop distance. Bridger's picks scored higher on all three (e.g., 4.7 vs. 2.9 co-authorship hops away) than the relevance baseline, i.e., it surfaces people outside the user's existing network, not just topically-similar ones.
- **Qualitative signal:** thematic analysis of interviews on whether users could articulate *why* a recommended author was useful (novel angle, transferable method, etc.), not just that they liked the card.

So the definition of success is explicitly two-pronged — perceived usefulness (would a researcher actually want this) *and* measured novelty/distance (is this actually outside their filter bubble) — rather than a single benchmark metric, which fits the paper's broader framing (per the intro) that relevance-optimized recommenders can reinforce filter bubbles even while looking "accurate."

# Other Notes


# Take-Away


Author’s preference based