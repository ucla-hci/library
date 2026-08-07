# Lu & Yin — Human Reliance on Machine Learning Models When Performance Feedback is Limited: Heuristics and Risks

```
@inproceedings{10.1145/3411764.3445562,
author = {Lu, Zhuoran and Yin, Ming},
title = {Human Reliance on Machine Learning Models When Performance Feedback is Limited: Heuristics and Risks},
year = {2021},
isbn = {9781450380966},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3411764.3445562},
doi = {10.1145/3411764.3445562},
abstract = {This paper addresses an under-explored problem of AI-assisted decision-making: when objective performance information of the machine learning model underlying a decision aid is absent or scarce, how do people decide their reliance on the model? Through three randomized experiments, we explore the heuristics people may use to adjust their reliance on machine learning models when performance feedback is limited. We find that the level of agreement between people and a model on decision-making tasks that people have high confidence in significantly affects reliance on the model if people receive no information about the model’s performance, but this impact will change after aggregate-level model performance information becomes available. Furthermore, the influence of high confidence human-model agreement on people’s reliance on a model is moderated by people’s confidence in cases where they disagree with the model. We discuss potential risks of these heuristics, and provide design implications on promoting appropriate reliance on AI.},
booktitle = {Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems},
articleno = {78},
numpages = {16},
keywords = {human-AI interaction, appropriate reliance, Machine learning},
location = {<conf-loc>, <city>Yokohama</city>, <country>Japan</country>, </conf-loc>},
series = {CHI '21}
}
```

# One Sentence


This paper studied humans’ reliance on machine learning models when they have no or limited information about the model’s performance.

# More Sentences


### The key finding

> When they have no information about a model’s performance at all, people’s reliance on the model is significantly influenced by the level of agreement between the model and themselves on tasks that they have high confidence in.
> 

> However, once people have obtained some aggregate-level performance information about the model, people’s reliance on the model is mostly affected by the model’s observed performance, but not the level of high confidence agreement with the model any more.
> 

# Key Points


### Why people might have limited information about model performance

> … model designers may fail to transparently communicate the model’s performance to its end-users
> 

> Significant time delays may exist before one can meaningfully evaluatre the performance of a model (e.g., … college admission …)
> 

> Sometimes, it is even impossible to fully observe the model’s performance due to the decision made [my note: not admitting a student == unable to know if this decision is correct]
> 

# Other Notes


### What information can ML models provide to enable proper reliance?

- “… the objective feedback on the model’s performance”, e.g., accuracy
- People’s mental models of when ML is likely to err
- “Information on model’s confidence”

### Social psychology theory related to human decision making when unable to judge model performance

> … “*naive realism*” … suggests that people often consider their own judgment to be objective reflections of reality and tend to discount advice that is more different from their own opinion.
> 

"agreement-in-confidence heuristic" refers to a cognitive bias where individuals increase their confidence in their own opinion when they learn that others agree with them, regardless of the actual validity or reliability of the opinion or the expertise of those who agree. 

# Take-Away
