# Lu et al. — The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

```

@misc{lu_ai_2024,
	title = {The {AI} {Scientist}: {Towards} {Fully} {Automated} {Open}-{Ended} {Scientific} {Discovery}},
	shorttitle = {The {AI} {Scientist}},
	url = {http://arxiv.org/abs/2408.06292},
	doi = {10.48550/arXiv.2408.06292},
	abstract = {One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. for brainstorming ideas, writing code, or prediction tasks, they still conduct only a small part of the scientific process. This paper presents the first comprehensive framework for fully automatic scientific discovery, enabling frontier large language models to perform research independently and communicate their findings. We introduce The AI Scientist, which generates novel research ideas, writes code, executes experiments, visualizes results, describes its findings by writing a full scientific paper, and then runs a simulated review process for evaluation. In principle, this process can be repeated to iteratively develop ideas in an open-ended fashion, acting like the human scientific community. We demonstrate its versatility by applying it to three distinct subfields of machine learning: diffusion modeling, transformer-based language modeling, and learning dynamics. Each idea is implemented and developed into a full paper at a cost of less than \$15 per paper. To evaluate the generated papers, we design and validate an automated reviewer, which we show achieves near-human performance in evaluating paper scores. The AI Scientist can produce papers that exceed the acceptance threshold at a top machine learning conference as judged by our automated reviewer. This approach signifies the beginning of a new era in scientific discovery in machine learning: bringing the transformative benefits of AI agents to the entire research process of AI itself, and taking us closer to a world where endless affordable creativity and innovation can be unleashed on the world's most challenging problems. Our code is open-sourced at https://github.com/SakanaAI/AI-Scientist},
	urldate = {2024-09-04},
	publisher = {arXiv},
	author = {Lu, Chris and Lu, Cong and Lange, Robert Tjarko and Foerster, Jakob and Clune, Jeff and Ha, David},
	month = aug,
	year = {2024},
	note = {arXiv:2408.06292 [cs]},
	keywords = {Computer Science - Artificial Intelligence, Computer Science - Computation and Language, Computer Science - Machine Learning},
	file = {arXiv Fulltext PDF:/Users/prof.biu/Zotero/storage/PNTDRNV5/Lu et al. - 2024 - The AI Scientist Towards Fully Automated Open-End.pdf:application/pdf},
}

```

# One Sentence

This paper describes the use of language models to automate machine learning research process: provided with some initial code and paper template, the AI scientist is able to brainstorm ideas, design and conduct experiments, and write up the results into a paper, which is then reviewed by AI reviewers.

# More Sentences

> Given a broad research direction and a simple initial codebase, The AI Scientist seamlessly performs ideation, a literature search, experimental planning, experiment iterations, manuscript writing, and peer reviewing to produce insightful papers.
> 

# Key Points

### The limitation of existing AI for Science

> Traditional approaches to automating research projects have so far relied on carefully constraining the search space of potential discoveries, which severely limits the scope of exploration and requires substantial human expertise and design.
> 

# Other Notes

# Take-Away

Is this considered success?

> … can generate hundreds of interesting, medium-quality papers over the course of a week.
>

What can we learn from this work? That current LLM can be put together to do "medium quality" research?

This is a success as a proof of concept for automating the research pipeline: it demonstrates end-to-end autonomy and high, inexpensive throughput. But it is weak evidence of successful scientific discovery, which requires independently verified novelty, correctness, reproducibility, and meaningful impact. Generating papers faster than they can be critically evaluated may instead increase noise, shifting the bottleneck from producing research to verifying it.
