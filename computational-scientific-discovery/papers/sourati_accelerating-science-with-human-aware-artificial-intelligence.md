---
activities:
  - literature-discovery
  - hypothesis-generation
contributions:
  - method
  - empirical-study
domains:
  - science-of-science
scope: focused
coding_status: coded
---

# Sourati et al.: Accelerating Science with Human-Aware Artificial Intelligence

## One Sentence
> ... incorporating the distribution of human expertise by training unsupervised models on simulated inferences that are cognitively accessible to experts dramatically improves (by up to 400%) AI prediction of future discoveries beyond models focused on research content alone, especially when relevant literature is sparse.

Reading the following figure is key to understand this paper:

![[Pasted image 20260323093702.png]]
## More Sentences

## Key Points
### Limitations of existing AI for science
> ... such efforts typically ignore the distribution of scientists and inventors--the human prediction engines who continuously alter the landscape of discovery and invention.
### Definition of discovery
>a newly established relationship between a material and a property

Where:
- **Material** = “thing” (drug, compound, molecule)
- **Property** = “what it can do”
### To motivate mapping hypothesis space
> AI should model _cognitive accessibility of hypotheses to scientists_, not just semantic plausibility.

The paper implicitly defines discovery as:
- **Plausible** (fits physics/biology/chemistry)
- **Accessible** (someone can _think of it_)
### Hypergraph and random walk to simulate accessible discovery
Hypergraph:
- Nodes: **materials, properties, AND scientists**
- Edges: co-occurrence in papers
Simulate _human thinking_ as **random walks over this graph**
- Author ↔ author → collaboration / conversation
- Author ↔ material → expertise
- Material ↔ property → literature reading
### Human-like vs. human-avoiding discovery
The density of certain areas in the graph indicates popularity of discovery. By computationally walking the graph we can control whether/how discovery can follow a more human-like or human-avoiding path.

## Other Notes

## Take-Away
- I wonder how the hypergraph+random walk approach can be pivoted into something with humans in the loop
- Source code: https://github.com/jsourati/accelerate-discoveries

