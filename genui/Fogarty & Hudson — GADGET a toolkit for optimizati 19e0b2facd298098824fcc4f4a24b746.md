# Fogarty & Hudson — GADGET: a toolkit for optimization-based approaches to interface and display generation

```
@inproceedings{10.1145/964696.964710,
author = {Fogarty, James and Hudson, Scott E.},
title = {GADGET: a toolkit for optimization-based approaches to interface and display generation},
year = {2003},
isbn = {1581136366},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/964696.964710},
doi = {10.1145/964696.964710},
abstract = {Recent work is beginning to reveal the potential of numerical optimization as an approach to generating interfaces and displays. Optimization-based approaches can often allow a mix of independent goals and constraints to be blended in ways that would be difficult to describe algorithmically. While optimization-based techniques appear to offer several potential advantages, further research in this area is hampered by the lack of appropriate tools. This paper presents GADGET, an experimental toolkit to support optimization for interface and display generation. GADGET provides convenient abstractions of many optimization concepts. GADGET also provides mechanisms to help programmers quickly create optimizations, including an efficient lazy evaluation framework, a powerful and configurable optimization structure, and a library of reusable components. Together these facilities provide an appropriate tool to enable exploration of a new class of interface and display generation techniques.},
booktitle = {Proceedings of the 16th Annual ACM Symposium on User Interface Software and Technology},
pages = {125–134},
numpages = {10},
keywords = {display generation, layout algorithms, numerical optimization, perceptually optimized displays, toolkits},
location = {Vancouver, Canada},
series = {UIST '03}
}
```

# One Sentence


This paper describes GADGET—a programming toolkit that make it easier and more customizable to use numeric optimization for UI layout.

# More Sentences


# Key Points


### The three inputs to the GADGET toolkit

**Initializer** “creates an initial solution to be optimized”

**Iteration** **specifies how to change UI elements’ attributes to explore the design space, “that indicate how GADGET should generate different possible solutions”, “transforming one potential solution into another, typically using methods that are at least partially random”

- GADGET provides a library of iterations, e.g., nudging an element’s position along X/Y axes

**Evaluation** **specifies how to evaluate whether a given UI layout solution meets the objective, “judging the different notions of goodness in a solution”

- GADGET provides a library of evaluations, e.g., calculating the overlap between elements
- programmers can implement their own evaluations
- each evaluation can be weighted

### The back-end: simulated annealing

> Simulated annealing is a general approach that is characterized by a temperature variable. This temperature variable is initially high, indicating a “hot” system, and decreases over time, representing the system gradually “cooling” into an optimal state. This temperature variable is used to probabilistically accept changes that do not appear to represent an improvement. By randomly accepting these changes, an optimization is less likely to become trapped in local maxima.
> 

### Programmers see and edit optimization as a finite state machine

> An optimization structure is represented as a finite-state machine. Each state in the machine represents an action in the optimization, such as sending an event notification, executing an evaluation, or decaying the temperature variable.
> 

> … allows changes to be made to an optimization structure by adding new states and changing the transitions associated with exit conditions.
> 

### Programmers’ default workflow of using GADGET

> … a single function call to a Builder object that creates a simulated annealing optimization based on a handful of parameters, including a list of the evaluations to execute, a list of the iterations to use, and the rate at which the temperature should decay.
> 

# Other Notes


# Take-Away
