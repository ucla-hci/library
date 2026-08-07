# Nichols et al. — Generating remote control interfaces for complex appliances

```
@inproceedings{10.1145/571985.572008,
author = {Nichols, Jeffrey and Myers, Brad A. and Higgins, Michael and Hughes, Joseph and Harris, Thomas K. and Rosenfeld, Roni and Pignol, Mathilde},
title = {Generating remote control interfaces for complex appliances},
year = {2002},
isbn = {1581134886},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/571985.572008},
doi = {10.1145/571985.572008},
abstract = {The personal universal controller (PUC) is an approach for improving the interfaces to complex appliances by introducing an intermediary graphical or speech interface. A PUC engages in two-way communication with everyday appliances, first downloading a specification of the appliance's functions, and then automatically creating an interface for controlling that appliance. The specification of each appliance includes a high-level description of every function, a hierarchical grouping of those functions, and dependency information, which relates the availability of each function to the appliance's state. Dependency information makes it easier for designers to create specifications and helps the automatic interface generators produce a higher quality result. We describe the architecture that supports the PUC, and the interface generators that use our specification language to build high-quality graphical and speech interfaces.},
booktitle = {Proceedings of the 15th Annual ACM Symposium on User Interface Software and Technology},
pages = {161–170},
numpages = {10},
keywords = {appliances, handheld computers, pebbles, personal digital assistants (PDAs), personal universal controller (PUC), remote control, universal speech interface (USI)},
location = {Paris, France},
series = {UIST '02}
}
```

# One Sentence


This paper presents *personal universal controller* (PUC) —a method to automatically generate user interfaces on a remote device to control different complex appliances based on individual appliances’ functional specifications.

![image.png](../../_assets/nichols-remote-control-interfaces-1.png)

# More Sentences


# Key Points


### Specification Language

> There must be a description of an appliance’s functions so the PUC can automatically generate an interface. This description must contain enough information to generate a good user interface, but it should not containi any information about look or feel.
> 
1. A UI boils down to a collection of **state variables and commands**:
- State variables allow users to specify values as input to the system, e.g.., to alter its behavior like increasing the volume;
- Commands involve more actions than changing a state variable, some of which might involve internal variables not exposed to the users.

1. A UI hierarchically groups state variables and commands in a **group tree**:

> Interfaces are always more intuitive when similar elements are grouped close together and different elements are kept apart
> 

> We encourage designers to make the group tree as deep as possible, in order to help space constrained interface generators.
> 

1. Dependency information

> … describes the availability of each function relative to the appliance’s state.
> 

Dependency information has two purposes:

- Let the UI convey which function might be unavailable because of a specific state. For example, a thermostat’s “Eco” mode allows a user to change two temperature values (min and max) to trigger heating and cooling, respectively; but other modes only allow for changing one temperature value.
- Help interface generators organize functions. If the availabilities of two sets of UI elements are mutually exclusive and depend one a state variable, then the UI can put them on separate tabs/panes rather than on the same tab/pane.

![image.png](../../_assets/nichols-remote-control-interfaces-2.png)

### Generating Graphical UI

Given a group tree, this paper takes a rule-based approach to generate the corresponding UI. The high-level generative rules are:

- Each leaf node is a panel that is either for a state variable (e.g., a spinner with a textual/numeric label) or a command (e.g., a button with a label);
- Each non-leaf node is a group (or container), which can be put on separate tabs/panes if mutually-exclusive with its sibling non-leaf nodes;
- For siblings to be put on the same tab/pane, rules need to determine its layout, which can be row-by-row, column-by-column, or a mix.

# Other Notes


# Take-Away

