# Marks et al. — Design galleries: A general approach to setting parameters for computer graphics and animation

```
@inproceedings{marks1997design,
  title={Design galleries: A general approach to setting parameters for computer graphics and animation},
  author={Marks, Joe and Andalman, Brad and Beardsley, Paul A and Freeman, William and Gibson, Sarah and Hodgins, Jessica and Kang, Thomas and Mirtich, Brian and Pfister, Hanspeter and Ruml, Wheeler and others},
  booktitle={Proceedings of the 24th annual conference on Computer graphics and interactive techniques},
  pages={389--400},
  year={1997}
}
```

# One Sentence


This paper describes a general framework of producing and displaying a gallery of examples that supports user exploration.

> *Design Gallery* (DG) interfaces present the user with the broader selection, automatically generated and organized, of perceptually different graphics or animations that can be produced by varying a given input-parameter vector.
> 

# More Sentences


### How Design Gallery compares with optimization-based approach

> ... the DG approach requires only a measure of similarity between graphics, which can often be quantified even when optimality cannot.
> 

### Six key elements of Design Gallery

- **Input vector (#1)**: a list of parameters that control the generation of the output graphic via a **mapping (#2)** process;
- **Output vector (#3)**: a list of values that summarizes the subjectively relevant qualities of the output graphic;
- **Distance metric (#4)**: on the space of output vectors approximates the perceptual similarity of the corresponding output graphics;
- **Dispersion (#5)**: ... is used to find a set of input vectors that map to a well-distributed set of output vectors;
- **Arrangement (#6)**: the presentation of the dispersed graphics to the user;

### Case study: light selection and placement

- The dispersion algorithm ... finds a set $I \subset L$ with good spread among output vectors;
    - Start with eliminating (obviously) bad options, e.g., "... the elimination of lights that dimly illuminate the visible part of the scene";
    - Then emphasize diversity—"The subset *I* is assembled by repeatedly adding to *I* the light in *L* whose output vector is most different from its closest match in the nascent *I*"

### Case study: opacity and color transfer functions for volume rendering

Dispersion method:

> These vectors are then perturbed randomly. Perturbed vectors are substituted for existing vectors in the set if the substitution improves dispersion.
> 

Arrangement:

> Thumbnail layout is accomplished using a multidimensional scaling (MDS) ... Given a matrix of distances between points, MDS procedures compute an embedding of the points in a low-dimensional Euclidean space (2D in our case) such that the interpoint distances in the embedding closely match those in the given matrix.
> 

# Key Points


### Related approaches

> One such computer-assisted methodology is interactive evolution [11, 21, 23]: the computer explore the space of possible parameter settings, and the user acts as an objective-function oracle, interactively selecting computer-suggested alternatives for further exploration.
> 

# Other Notes


# Take-Away
