# Mozannar et al. — When to Show a Suggestion? Integrating Human Feedback in AI-Assisted Programming

```

@article{mozannar_when_2024,
	title = {When to {Show} a {Suggestion}? {Integrating} {Human} {Feedback} in {AI}-{Assisted} {Programming}},
	volume = {38},
	copyright = {Copyright (c) 2024 Association for the Advancement of Artificial Intelligence},
	issn = {2374-3468},
	shorttitle = {When to {Show} a {Suggestion}?},
	url = {https://ojs.aaai.org/index.php/AAAI/article/view/28878},
	doi = {10.1609/aaai.v38i9.28878},
	abstract = {AI powered code-recommendation systems, such as Copilot and CodeWhisperer, provide code suggestions inside a programmer's environment (e.g., an IDE) with the aim of improving productivity. We pursue mechanisms for leveraging signals about programmers' acceptance and rejection of code suggestions to guide recommendations. We harness data drawn from interactions with GitHub Copilot, a system used by millions of programmers, to develop interventions that can save time for programmers. We introduce a utility-theoretic framework to drive decisions about suggestions to display versus withhold. The approach, conditional suggestion display from human feedback (CDHF), relies on a cascade of models that provide the likelihood that recommended code will be accepted. These likelihoods are used to selectively hide suggestions, reducing both latency and programmer verification time. Using data from 535 programmers, we perform a retrospective evaluation of CDHF and show that we can avoid displaying a significant fraction of suggestions that would have been rejected. We further demonstrate the importance of incorporating the programmer's latent unobserved state in decisions about when to display suggestions through an ablation study. Finally, we showcase how using suggestion acceptance as a reward signal for guiding the display of suggestions can lead to suggestions of reduced quality, indicating an unexpected pitfall.},
	language = {en},
	number = {9},
	urldate = {2024-05-03},
	journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
	author = {Mozannar, Hussein and Bansal, Gagan and Fourney, Adam and Horvitz, Eric},
	month = mar,
	year = {2024},
	note = {Number: 9},
	keywords = {HAI: Planning and Decision Support for Human-Machine Teams},
	pages = {10137--10144},
	file = {Full Text PDF:/Users/prof.biu/Zotero/storage/TMH8Y2PG/Mozannar et al. - 2024 - When to Show a Suggestion Integrating Human Feedb.pdf:application/pdf},
}
```

# One Sentence

---

# More Sentences

---

# Key Points

---

### Expected utility of displaying a suggestion

> … a value that measures the impact of showing a suggestion on the overall time to write a specific piece of code
> 

(i.e., how showing this suggestion will reduce/increase time taken to write some code

### Conditional suggestion Display from Human Feedback (CDHF)

> … employs a cascade of models that predict acceptance of suggestions. The optimization procedure guarantees that any suggestion that was hidden (or not generated) would have been rejected if it was shown with a probability of at least *p*, where, e.g., *p* can be 0.99.
> 

# Other Notes

---

### Ghost text

A name for the “grayed-out code suggestion inline inside the IDE”

### How code generation works, in one sentence

> Code-recommendation systems are powered by large language models (LLMs) such as GPT that are trained on standard language modeling objectives using the Common Crawl data […], and then fine-tuned on public code repositories […]
> 

# Take-Away

---