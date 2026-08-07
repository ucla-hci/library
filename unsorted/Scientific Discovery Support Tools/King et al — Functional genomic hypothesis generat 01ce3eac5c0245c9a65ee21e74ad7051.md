# King et al. — Functional genomic hypothesis generation and experimentation by a robot scientist

```

@article{king_functional_2004,
	title = {Functional genomic hypothesis generation and experimentation by a robot scientist},
	volume = {427},
	copyright = {2004 Macmillan Magazines Ltd.},
	issn = {1476-4687},
	url = {https://www.nature.com/articles/nature02236},
	doi = {10.1038/nature02236},
	abstract = {The question of whether it is possible to automate the scientific process is of both great theoretical interest1,2 and increasing practical importance because, in many scientific areas, data are being generated much faster than they can be effectively analysed. We describe a physically implemented robotic system that applies techniques from artificial intelligence3,4,5,6,7,8 to carry out cycles of scientific experimentation. The system automatically originates hypotheses to explain observations, devises experiments to test these hypotheses, physically runs the experiments using a laboratory robot, interprets the results to falsify hypotheses inconsistent with the data, and then repeats the cycle. Here we apply the system to the determination of gene function using deletion mutants of yeast (Saccharomyces cerevisiae) and auxotrophic growth experiments9. We built and tested a detailed logical model (involving genes, proteins and metabolites) of the aromatic amino acid synthesis pathway. In biological experiments that automatically reconstruct parts of this model, we show that an intelligent experiment selection strategy is competitive with human performance and significantly outperforms, with a cost decrease of 3-fold and 100-fold (respectively), both cheapest and random-experiment selection.},
	language = {en},
	number = {6971},
	urldate = {2024-08-06},
	journal = {Nature},
	author = {King, Ross D. and Whelan, Kenneth E. and Jones, Ffion M. and Reiser, Philip G. K. and Bryant, Christopher H. and Muggleton, Stephen H. and Kell, Douglas B. and Oliver, Stephen G.},
	month = jan,
	year = {2004},
	note = {Publisher: Nature Publishing Group},
	keywords = {Humanities and Social Sciences, multidisciplinary, Science},
	pages = {247--252},
	file = {Full Text PDF:/Users/xac/Zotero/storage/9FXSS57B/King et al. - 2004 - Functional genomic hypothesis generation and exper.pdf:application/pdf},
}

```

# One Sentence


This paper describes an end-to-end software/hardware robot scientist that can automatically generate hypotheses, design experiments, carry out the experiments, and measure the results.

# More Sentences


### The software platform …

> … consists of background knowledge about the biological problem, a logical inference engine, hypothesis generation code (abduction), experiment selection code (deduction), and the Laboratory Information Management System (LIMS) code that integrates the whole system.
> 

# Key Points


### The gist of experiments run by the system

> … automatically determine the function of genes from the performance of knockout mutants (strains in which one gene has been removed).
> 

### How the system represents knowledge

> The structure of the metabolic pathway is that of a directed graph, with metabolites as nodes and enzymes as arcs. An arc corresponds to a reaction. The compounds at each node are the set of all metabolites that can be synthesized by the reactions leading to it. Reactions are modeled as unidirectional transformations.
> 

### How the system generates a hypothesis

A hypothesis is which path is sufficient and necessary for a knock-out mutant to grow

> The model infers (deduces) that a knock-out mutant will grow if, and only if, a path can be found from the input metabolites to the three aromatic amino acids. This allows the model to compute the phenotype of a particular knockout or to be used to infer missing reactions that could explain an observed phenotype (abduction).
> 

### The importance of experiment selection

AI probably can’t predict the results so that experiments are unnecessary; but maybe AI can help selecting more cost-effective experiments.

> Our results show that different experiment selection strategies can have significantly different results in terms of cost, even for the solution of a simple problem. This suggests that there remains scope to improve the general cost-effectiveness of science by developing better tools to help choose efficient experiments
> 

# Other Notes


### The background of the scientific field: functional genomics

> … functional genomics … in which laboratory automation is already mature. The current state of the art in functional genomics is to use highly automated robotics to generate data, and then to use data-mining systems to extract knowledge from that data.
> 

# Take-Away


- Does not involve human in the loop
- To support a given scientific field, it is important to define the representation of hypothesis, thus the hypothesis space.