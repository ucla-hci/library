# Gajos & Weld — SUPPLE: automatically generating user interfaces

```
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
keywords = {adaptive user interfaces, constraint satisfaction, decision theory, optimization, user interface generation, user trace},
location = {Funchal, Madeira, Portugal},
series = {IUI '04}
}
```

# One Sentence

---

This paper describes a method to formulate user interface design as an optimization problem: searching for UI widgets based an interface specification while satisfying device constraints and minimizing users’ effort.

# More Sentences

---

> When asked to render an interface on a specific device, our SUPPLE system searches for the rendition that meets the device’s constraints and minimizes the estimated effort for the user’s expected interface actions.
> 

# Key Points

---

We can parameterize the design of a UI into three sets of variables:

- Interface specification
- Device model
- User model

### Interface Specification

We define an interface as the following—-

1. A set of *interface elements*, which are “units of information that need to be conveyed via the interface between the user and the controlled appliance or application”
    1. Each element is not a specific widget but rather the kinds of value that a user needs to provide as input or see as output
    2. Example below (each node is an interface element, which can be nested):
    3. 💡 Can we instruct LM to output such an interface specification?
    
    ![image.png](../../_assets/gajos-weld-supple.png)
    
2. A set of *interface constraints* specified by a designer
    1. A constraint is a function to test the UI design, i.e., mapping “a full or partial rendering … to either true or false”

### Device Model

We define a device model as the following—

1. A set of *UI widgets*
    1. A widget (e.g., a spinner or a slider) can enable an interface element (e.g., inputting light intensity)
    2. Similar to the nested nature of interface elements, some widgets are containers while the others are primitive
2. A set of *device constraints*
    1. Similar to how interface constraints work
3. A device-specific *matching function* to measure “how appropriate each widget is for manipulating state variables of a given type”
    1. For example, a spinner is more appropriate for adjusting a value with small rather than large changes
4. A function to evaluate the *cost of navigation* from one widget to another
    1. As a user navigates from w1 to w2, there are three cases: w1 and w2 are siblings, w1 is a container of w2, and w2 is a container of w1.

### User Model

We represent a user model as a set of *traces*, each of which is a sequence of interface elements a user accesses to accomplish a task

- Each “step” in the sequence needs to consider not just the element but also the old and new values of that element, which a user causes to change (if there is any)

### Solving the optimization problem

To generate a UI, a designer needs to provide the three sets of input variables described above.

The UI design now becomes the problem of searching for the *mapping* from the interface elements to widgets to minimize the cost of carrying out the traces of navigating and interacting with each element (via its widget).

# Other Notes

---

# Take-Away

---
