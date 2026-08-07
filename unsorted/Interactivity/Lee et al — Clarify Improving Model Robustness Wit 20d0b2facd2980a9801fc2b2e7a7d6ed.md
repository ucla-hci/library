# Lee et al.— Clarify: Improving Model Robustness With Natural Language Corrections

```
@inproceedings{10.1145/3654777.3676362,
author = {Lee, Yoonho and Lam, Michelle S. and Vasconcelos, Helena and Bernstein, Michael S. and Finn, Chelsea},
title = {Clarify: Improving Model Robustness With Natural Language Corrections},
year = {2024},
isbn = {9798400706288},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3654777.3676362},
doi = {10.1145/3654777.3676362},
abstract = {The standard way to teach models is by feeding them lots of data. However, this approach often teaches models incorrect ideas because they pick up on misleading signals in the data. To prevent such misconceptions, we must necessarily provide additional information beyond the training data. Prior methods incorporate additional instance-level supervision, such as labels for misleading features or additional labels for debiased data. However, such strategies require a large amount of labeler effort. We hypothesize that people are good at providing textual feedback at the concept level, a capability that existing teaching frameworks do not leverage. We propose Clarify, a novel interface and method for interactively correcting model misconceptions. Through Clarify, users need only provide a short text description of a model’s consistent failure patterns. Then, in an entirely automated way, we use such descriptions to improve the training process. Clarify is the first end-to-end system for user model correction. Our user studies show that non-expert users can successfully describe model misconceptions via Clarify, leading to increased worst-case performance in two datasets. We additionally conduct a case study on a large-scale image dataset, ImageNet, using Clarify to find and rectify 31 novel hard subpopulations.},
booktitle = {Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology},
articleno = {133},
numpages = {19},
keywords = {Dataset Bias, Fairness, Human-in-the-Loop Machine Learning, Interactive Model Correction, Labeling Efficiency, Model Robustness, Natural Language Feedback},
location = {Pittsburgh, PA, USA},
series = {UIST '24}
}
```

# One Sentence

---

This paper proposes Clarify—an interface that takes in a user’s natural language feedback to a model’s errors, which is then used to re-weigh the training examples to improve model performance.

![image.png](Lee%20et%20al%20%E2%80%94%20Clarify%20Improving%20Model%20Robustness%20Wit/image.png)

# More Sentences

---

> Clarify, a novel interface and method for interactively correcting model misconceptions. Through Clarify, users need only provide a short text description of a model’s conssitent failure patterns. Then, in an entirely automated way, we use such descriptions to improve the training process.
> 

# Key Points

---

# Other Notes

---

# Take-Away

---