# Mega Notes

UI has three kinds of representations:

- pixels, e.g., screenshots
- a layout of elements, DOM tree, graph
    - different approaches differ in how they solve for the constraints, e.g., optimization or deep generative models
- code, e.g., HTML/CSS, JavaScript, Java

### SUPPLE: automatically generating user interfaces

```latex
@inproceedings{10.1145/964442.964461,
author = {Gajos, Krzysztof and Weld, Daniel S.},
title = {SUPPLE: automatically generating user interfaces},
year = {2004},
isbn = {1581138156},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/964442.964461},
doi = {10.1145/964442.964461},
abstract = {In order to give people ubiquitous access to software applications, device controllers, and Internet services, it will be necessary to automatically adapt user interfaces to the computational devices at hand (eg, cell phones, PDAs, touch panels, etc.). While previous researchers have proposed solutions to this problem, each has limitations. This paper proposes a novel solution based on treating interface adaptation as an optimization problem. When asked to render an interface on a specific device, our supple system searches for the rendition that meets the device's constraints and minimizes the estimated effort for the user's expected interface actions. We make several contributions: 1) precisely defining the interface rendition problem, 2) demonstrating how user traces can be used to customize interface rendering to particular user's usage pattern, 3) presenting an efficient interface rendering algorithm, 4) performing experiments that demonstrate the utility of our approach.},
booktitle = {Proceedings of the 9th International Conference on Intelligent User Interfaces},
pages = {93–100},
numpages = {8},
keywords = {user trace, user interface generation, optimization, decision theory, constraint satisfaction, adaptive user interfaces},
location = {Funchal, Madeira, Portugal},
series = {IUI '04}
}
```

GenUI as interface adaptation via solving a constrained optimization problem

> When asked to render an interface on a specific device, our SUPPLE system searches for the rendition that meets the device’s constraints and minimizes the estimated effort for the user’s expected interface actions.
> 

More technical details:

> … uses constrained decision-theoretic optimization to automatically generate user interfaces. As input, SUPPLE takes a functional specification of the interface, which describes the types of information that need to be communicated between the application and the user, the device-specific *constraints*, such as screen **size and a list of available interactors, a typical *usage trace*, and a *cost function*. … optimization algorithm, a branch-and-bound search with constraint propagation and a novel admissible heuristic, is guaranteed to find the user interface which minimizes the cost function while also satisfying all device constraints.
> 

### Decision-Theoretic User Interface Generation

```latex
@inproceedings{10.5555/1620270.1620326,
author = {Gajos, Krzysztof Z. and Weld, Daniel S. and Wobbrock, Jacob O.},
title = {Decision-theoretic user interface generation},
year = {2008},
isbn = {9781577353683},
publisher = {AAAI Press},
booktitle = {Proceedings of the 23rd National Conference on Artificial Intelligence - Volume 3},
pages = {1532–1536},
numpages = {5},
location = {Chicago, Illinois},
series = {AAAI'08}
}
```

> SUPPLE++ first performs a one-time assessment of a person’s motor abilities and then automatically generates user interfaces adapted to that user’s abilities.
> 

### Automatic Generation of User Interface Layouts for Alternative Screen Orientations

```latex
@InProceedings{10.1007/978-3-319-67744-6_2,
author="Zeidler, Clemens
and Weber, Gerald
and Stuerzlinger, Wolfgang
and Lutteroth, Christof",
editor="Bernhaupt, Regina
and Dalvi, Girish
and Joshi, Anirudha
and K. Balkrishan, Devanuj
and O'Neill, Jacki
and Winckler, Marco",
title="Automatic Generation of User Interface Layouts for Alternative Screen Orientations",
booktitle="Human-Computer Interaction - INTERACT 2017",
year="2017",
publisher="Springer International Publishing",
address="Cham",
pages="13--35",
abstract="Creating multiple layout alternatives for graphical user interfaces to accommodate different screen orientations for mobile devices is labor intensive. Here, we investigate how such layout alternatives can be generated automatically from an initial layout. Providing good layout alternatives can inspire developers in their design work and support them to create adaptive layouts. We performed an analysis of layout alternatives in existing apps and identified common real-world layout transformation patterns. Based on these patterns we developed a prototype that generates landscape and portrait layout alternatives for an initial layout. In general, there is a very large number of possibilities of how widgets can be rearranged. For this reason we developed a classification method to identify and evaluate ``good'' layout alternatives automatically. From this set of ``good'' layout alternatives, designers can choose suitable layouts for their applications. In a questionnaire study we verified that our method generates layout alternatives that appear well structured and are easy to use.",
isbn="978-3-319-67744-6"
}
```

This paper approaches GenUI as layout generation—

> … layout alternatives can be generated automatically from an initial layout
> 

Based on patterns extracted from a layout analysis of existing apps, the authors …

> … developed a prototype that generates landscape and portrait layout alternatives … a classification method to identify and evaluate “good” layout alternatives automatically.
> 

### Seeking the user interface

```latex
@inproceedings{reiss2014seeking,
  title={Seeking the user interface},
  author={Reiss, Steven P},
  booktitle={Proceedings of the 29th ACM/IEEE international conference on Automated software engineering},
  pages={103--114},
  year={2014}
}
```

Approaching GenUI as a code search problem

> … start with a simple sketch of the desired interface along with a set of keywords describing the application context … then use existing code search engines to find results based on the keywords … apply a series of code transformations to the solutions to generate derivative solutions, aiming to get solutions that constitute only the user interface and that will compile and run
> 

### Creating user interface mock-ups from high-level text descriptions with deep-learning models

```latex
@article{huang2021creating,
  title={Creating user interface mock-ups from high-level text descriptions with deep-learning models},
  author={Huang, Forrest and Li, Gang and Zhou, Xin and Canny, John F and Li, Yang},
  journal={arXiv preprint arXiv:2110.07775},
  year={2021}
}
```

> … three deep-learning techniques to create low-fidelity UI mock-ups from a natural language phrase that describes the high-level design goal (e.g., “pop up displaying an image and other options”)
> 

The three techniques:

- “*UI Generator* … deep generative model … to generate UI mock-ups from scratch with only a high-level text description about the desired UI”
- *“Multi-model Retriever* … deep-learning model that learns cross-modality correspondence and latent representation to retrieve design examples from a large UI corpus using a high-level text description about the desired UI”
- “*Text-only Retriever* … retrieves design examples from a UI corpus based on the similarity between the text description coupled to each UI in the corpus and a high-level text description about the desired UI*”*

![image.png](../../_assets/generative-ai-ux-mega-notes-1.png)

Other similar approaches

- LayoutGAN “utilizes a differentiable renderer to generate realistic layouts with adversarial learning”
- Neural Design Networks “took an alternative approach of encoding elements and inter-element relations of layouts as graphs and subsequently using a Graph Convolutional Neural-network to generate designs with coherent inter-element relations”
- LayoutTransformer “uses a Transformer decoder-only network to decode UI elements as discrete tokens” and Variational Transformer Network “builds upon LayoutTransformer and adds an encoder to build a gaussian-like latent space for better generative performance and interpolating between UIs”

### Creating Highly-Interactive and graphical user interfaces by demonstration

```latex
@inproceedings{10.1145/15922.15914,
author = {Myers, Brad A. and Buxton, William},
title = {Creating highly-interactive and graphical user interfaces by demonstration},
year = {1986},
isbn = {0897911962},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/15922.15914},
doi = {10.1145/15922.15914},
abstract = {It is very time-consuming and expensive to create the graphical, highly-interactive styles of user interfaces that are increasingly common. User Interface Management Systems (UIMSs) attempt to make the creation of user interfaces easier, but most existing UIMSs cannot create the low-level interaction techniques (pop-up pull-down and fixed menus, on-screen "light buttons", scroll-bars, elaborate feedback mechanisms and animations, etc.) that are frequently used. This paper describes Peridot, a system that automatically creates the code for these user interfaces while the designer demonstrates to the system how the interface should look and work. Peridot uses rule-based inferencing so no programming by the designer is required, and Direct Manipulation techniques are used to create Direct Manipulation interfaces, which can make full use of a mouse and other input devices. This allows extremely rapid prototyping of user interfaces.},
booktitle = {Proceedings of the 13th Annual Conference on Computer Graphics and Interactive Techniques},
pages = {249–258},
numpages = {10},
series = {SIGGRAPH '86}
}
```

> This paper describes Peridot, a system that automatically creates the code for these user interfaces while the designer *demonstrates* to the system how the interface should look and work.
> 

Related:

- https://dl.acm.org/doi/pdf/10.1145/3379337.3415848
- [https://dl.acm.org/doi/abs/10.1145/3025453.3025483](https://dl.acm.org/doi/abs/10.1145/3025453.3025483)

### LayoutGAN: Generating Graphic Layouts with Wireframe Discriminators

```latex
@inproceedings{lilayoutgan,
  title={LayoutGAN: Generating Graphic Layouts with Wireframe Discriminators},
  author={Li, Jianan and Yang, Jimei and Hertzmann, Aaron and Zhang, Jianming and Xu, Tingfa},
  booktitle={International Conference on Learning Representations}
}
```

> The generator of LayoutGAN takes as input a set of randomly-placed 2D graphic elements and uses self-attention modules to refine their labels and geometric parameters jointly to produce a realistic layout.
> 

### LayoutPrompter: Awaken the Design Ability of Large Language Models

```latex
@inproceedings{NEURIPS2023_88a129e4,
 author = {Lin, Jiawei and Guo, Jiaqi and Sun, Shizhao and Yang, Zijiang and Lou, Jian-Guang and Zhang, Dongmei},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {A. Oh and T. Naumann and A. Globerson and K. Saenko and M. Hardt and S. Levine},
 pages = {43852--43879},
 publisher = {Curran Associates, Inc.},
 title = {LayoutPrompter: Awaken the Design Ability of Large Language Models},
 url = {https://proceedings.neurips.cc/paper_files/paper/2023/file/88a129e44f25a571ae8b838057c46855-Paper-Conference.pdf},
 volume = {36},
 year = {2023}
}
```

A “meta” method use three existing layout generation methods to perform in-context learning by LLM, which involves three components:

- “the input-output serialization component meticulously designs the input and output formats for each layout generation task”
- “Dynamic exemplar selection is responsible for selecting the most helpful prompting exemplar for a given input”
- “… a layout ranker is used to pick the highest quality layout from multiple outputs of LLMs”

![image.png](../../_assets/generative-ai-ux-mega-notes-2.png)

### A Parse-Then-Place Approach for Generating Graphic Layouts from Textual Descriptions

```latex
@InProceedings{Lin_2023_ICCV,
    author    = {Lin, Jiawei and Guo, Jiaqi and Sun, Shizhao and Xu, Weijiang and Liu, Ting and Lou, Jian-Guang and Zhang, Dongmei},
    title     = {A Parse-Then-Place Approach for Generating Graphic Layouts from Textual Descriptions},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2023},
    pages     = {23622-23631}
}
```

> The approach introduces an intermediate representation (IR) between text and layout to represent diverse layout constraints … IR, in which the implicit constraints from the text are transformed into explicit ones. The place stage generates layouts based on the IR.
> 

---

### UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset

```latex
@inproceedings{10.1145/3654777.3676381,
author = {Duan, Peitong and Cheng, Chin-Yi and Li, Gang and Hartmann, Bjoern and Li, Yang},
title = {UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset},
year = {2024},
isbn = {9798400706288},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3654777.3676381},
doi = {10.1145/3654777.3676381},
abstract = {Automated UI evaluation can be beneficial for the design process; for example, to compare different UI designs, or conduct automated heuristic evaluation. LLM-based UI evaluation, in particular, holds the promise of generalizability to a wide variety of UI types and evaluation tasks. However, current LLM-based techniques do not yet match the performance of human evaluators. We hypothesize that automatic evaluation can be improved by collecting a targeted UI feedback dataset and then using this dataset to enhance the performance of general-purpose LLMs. We present a targeted dataset of 3,059 design critiques and quality ratings for 983 mobile UIs, collected from seven designers, each with at least a year of professional design experience. We carried out an in-depth analysis to characterize the dataset’s features. We then applied this dataset to achieve a 55\% performance gain in LLM-generated UI feedback via various few-shot and visual prompting techniques. We also discuss future applications of this dataset, including training a reward model for generative UI techniques, and fine-tuning a tool-agnostic multi-modal LLM that automates UI evaluation.},
booktitle = {Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology},
articleno = {46},
numpages = {17},
keywords = {Dataset, Large Language Models, UI Design Feedback},
location = {Pittsburgh, PA, USA},
series = {UIST '24}
}
```

> We present a targeted dataset of 3,059 design critiques and quality ratings for 983 mobile UIs, collected from seven designers, each with at least a year of professional design experience.
> 

This can be a blueprint for a dataset paper
