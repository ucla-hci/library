# Dayama et al. — GRIDS: Interactive Layout Design with Integer Programming

```
@inproceedings{10.1145/3313831.3376553,
author = {Dayama, Niraj Ramesh and Todi, Kashyap and Saarelainen, Taru and Oulasvirta, Antti},
title = {GRIDS: Interactive Layout Design with Integer Programming},
year = {2020},
isbn = {9781450367080},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3313831.3376553},
doi = {10.1145/3313831.3376553},
abstract = {Grid layouts are used by designers to spatially organise user interfaces when sketching and wireframing. However, their design is largely time consuming manual work. This is challenging due to combinatorial explosion and complex objectives, such as alignment, balance, and expectations regarding positions. This paper proposes a novel optimisation approach for the generation of diverse grid-based layouts. Our mixed integer linear programming (MILP) model offers a rigorous yet efficient method for grid generation that ensures packing, alignment, grouping, and preferential positioning of elements. Further, we present techniques for interactive diversification, enhancement, and completion of grid layouts. These capabilities are demonstrated using GRIDS, a wireframing tool that provides designers with real-time layout suggestions. We report findings from a ratings study (N = 13) and a design study (N = 16), lending evidence for the benefit of computational grid generation during early stages of design.},
booktitle = {Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems},
pages = {1–13},
numpages = {13},
keywords = {computational design, creativity support, design tools, grid layouts, mixed-initiative, optimisation},
location = {Honolulu, HI, USA},
series = {CHI '20}
}
```

# One Sentence

---

![image.png](../../_assets/dayama-grids-1.png)

# More Sentences

---

# Key Points

---

### Desirable properties of a good layout

**Proper packing**:

> … all elements fit on the canvas without overflowing or overlapping
> 

Additional properties:

> (1) the outer hull is rectangular [**rectangularity**]
(2) there are no holes [**convexity**]
(3) elements are well-aligned [**alignment**]
(4) related elements are grouped together [**grouping**]
(5) preferred positions are obeyed to provide visual connectivity
> 

### How integer programming (IP) realize the above properties

> As IP provides bounds for its range (say within 5%) from the best achievable design. We exploit this for generation of controllably diverse designs.
> 

### The formalized objectives of these properties

1. **Overall alignment**: A well-formatted layout places as many/most of its elements aligned to each other edge-wise.
2. **Rectangular outline**: An outline with jagged edges, a lopsided hull, or any non-convex arrangement, is aesthetically undesirable. The overall outline induced by the layout of
elements must approach a rectangular external hull.
3. **Placement**: We prefer to place interrelated elements in close proximity to each other. This transition objective manifests itself in three ways:
    1. Traversal Distance: If users often need to navigate between a pair of UI elements (for example, a text box and an associated button), it is preferable that the distance between these elements be minimised.
    2. Grouping: A contiguous placement should be ensured for semantically or otherwise related items.
    3. Preferential Placement: A designer may want a specific element be placed definitely on a specific side of some other element, or at a specific point (locked) on the canvas. 

### The mixed integer linear programming (MILP) approach

MILP first ensures the core requirements: a layout with proper packing of elements, i.e., elements not overflowing or overlapping; then additional requirements (e.g., alignment, rectangularity, placement) are “plugged in”.

The **core requirements are the following constraints** that define a feasible space (cf. paper for technical details):

![image.png](../../_assets/dayama-grids-2.png)

![image.png](../../_assets/dayama-grids-3.png)

Then **additional requirements are objective functions** to maximize/minimize within the feasible space.

# Other Notes

---

### Related work: grid generation by constraint solving

> Layout constraints can define bounds on elements, or relationship between elements. A constraint solver manipulates element properties to best satisfy the specified constraints.
> 

> … no constraints-based method has been proposed that ensures proper packing of elements and takes care of objectives like alignment, rectangularity, and grouping
> 

### Related work: grid generation by combinatorial optimization

> Typically, these approaches compute a single point-optimal solution. Following earlier findings, we believe it is necessary to present designers with a diverse range of solutions.
> 

### Related work: interactive layout generation

> DesignSpace supports enhancement and exploration of single-page layouts using energy-based optimization
> 

The deep model approach:

> Data-driven approaches enable layout generation without requiring problem specification
> 

# Take-Away

---
