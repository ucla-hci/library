# Karpatne et al. — Theory-Guided Data Science: A New Paradigm for Scientific Discovery from Data

```

@article{karpatne_theory-guided_2017,
	title = {Theory-{Guided} {Data} {Science}: {A} {New} {Paradigm} for {Scientific} {Discovery} from {Data}},
	volume = {29},
	issn = {1558-2191},
	shorttitle = {Theory-{Guided} {Data} {Science}},
	url = {https://ieeexplore.ieee.org/abstract/document/7959606},
	doi = {10.1109/TKDE.2017.2720168},
	abstract = {Data science models, although successful in a number of commercial domains, have had limited applicability in scientific problems involving complex physical phenomena. Theory-guided data science (TGDS) is an emerging paradigm that aims to leverage the wealth of scientific knowledge for improving the effectiveness of data science models in enabling scientific discovery. The overarching vision of TGDS is to introduce scientific consistency as an essential component for learning generalizable models. Further, by producing scientifically interpretable models, TGDS aims to advance our scientific understanding by discovering novel domain insights. Indeed, the paradigm of TGDS has started to gain prominence in a number of scientific disciplines such as turbulence modeling, material discovery, quantum chemistry, bio-medical science, bio-marker discovery, climate science, and hydrology. In this paper, we formally conceptualize the paradigm of TGDS and present a taxonomy of research themes in TGDS. We describe several approaches for integrating domain knowledge in different research themes using illustrative examples from different disciplines. We also highlight some of the promising avenues of novel research for realizing the full potential of theory-guided data science.},
	number = {10},
	urldate = {2024-07-08},
	journal = {IEEE Transactions on Knowledge and Data Engineering},
	author = {Karpatne, Anuj and Atluri, Gowtham and Faghmous, James H. and Steinbach, Michael and Banerjee, Arindam and Ganguly, Auroop and Shekhar, Shashi and Samatova, Nagiza and Kumar, Vipin},
	month = oct,
	year = {2017},
	note = {Conference Name: IEEE Transactions on Knowledge and Data Engineering},
	keywords = {Atmospheric modeling, Biological system modeling, Data models, Data science, domain knowledge, interpretability, knowledge discovery, Knowledge discovery, Mathematical model, Numerical models, physical consistency, scientific theory},
	pages = {2318--2331},
	file = {IEEE Xplore Abstract Record:/Users/prof.biu/Zotero/storage/IB9XME8K/7959606.html:text/html;IEEE Xplore Full Text PDF:/Users/prof.biu/Zotero/storage/LXYXTIPX/Karpatne et al. - 2017 - Theory-Guided Data Science A New Paradigm for Sci.pdf:application/pdf},
}

```

# One Sentence

---

This paper introduced a new paradigm of using scientific theories to guide the design, learning, inference, and usage of data science methods.

# More Sentences

---

# Key Points

---

### Why conventional data science  might be insufficient for scientific discovery

Two main reasons:

> First, scientific problems are often under-constrained … physical variables commonly show complex and non-stationary patterns that dynamically change over time. … the limited number of labeled instances … often fail to represent the true nature of relationships in scientific problems.
> 

> … the process of knowledge discovery … is the translation of learned patterns and relationships to *interpretable* theories and hypotheses that leads to advancement of scientific knowledge … a black-box model achieves somewhat more accurate performance … cannot be used as a basis for subsequent scientific developments.
> 

### The limitation/weakness of theory-driven approaches

> … scientific problems involve processes that are not completely understood by our current body of knowledge, because of the inherent complexity of the processes. … theory-based models are often forced to make a number of simplifying assumptions about the physical processes, which not only leads to poor performance but also renders the model difficult to comprehend and analyze
> 

### What is theory-guided design of data science models

> … if the domain knowledge suggests a particular form of relationship between the inputs and outputs, care must be taken to ensure that the same form of relationship is used in the data science model.
> 

### What is theory-guided learning of data science models

1. “… use physically consistent solutions as initial points in iterative learning algorithms” (e.g., gradient descent)
2. restrict the search space based on “theory-guided priors and relationships”
3. scientific knowledge as constraints in optimization schemes
4. scientific knowledge encoded as regularization terms in objective functions

### What is theory-guided refinement of data science outputs

> … the outputs of any data science models are made consistent with domain knowledge … in the form of closed-form equations (explicit) … in the form of latent constraints (implicit)
> 

### What is hybrid models of theory and data science

An example:

> … a two-component model where the outputs of the theory-based component are used as inputs in the data science component. … climate model simulations, available at coarse spatial and temporal resolutions, are used as inputs in a statistical models to predict the climate variables at finer resolutions.
> 

### Examples of using data science methods to augment theory-driven work

1. Data assimilation in theory-based models
    1. Data assimilation, often used in climate science or hydrology, where the scientific problem involves a dynamic system
    2. The dynamic system is “represented as a sequence of physical states in numerical models
    3. Data assimilation is a way to infer the most likely sequence of states such that the model outputs are in agreement with the observations available at every time-step
2. Calibrating theory-based models using data
    1. “Theory-based models often involve a large number of parameters in their equations that need to be calibrated in order to provide an accurate representation of the physical system”

# Other Notes

---

### A common problem in scientific domains …

> … is to represent relationships among physical variables, e.g., the combustion pressure and launch velocity of a rocket or the shape of an aircraft wing and its resultant air drag.
> 

# Take-Away

---