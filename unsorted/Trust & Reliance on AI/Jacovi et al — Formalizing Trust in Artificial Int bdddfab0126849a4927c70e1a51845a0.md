# Jacovi et al. — Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI

```
@inproceedings{10.1145/3442188.3445923,
author = {Jacovi, Alon and Marasovi\'{c}, Ana and Miller, Tim and Goldberg, Yoav},
title = {Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI},
year = {2021},
isbn = {9781450383097},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3442188.3445923},
doi = {10.1145/3442188.3445923},
abstract = {Trust is a central component of the interaction between people and AI, in that 'incorrect' levels of trust may cause misuse, abuse or disuse of the technology. But what, precisely, is the nature of trust in AI? What are the prerequisites and goals of the cognitive mechanism of trust, and how can we promote them, or assess whether they are being satisfied in a given interaction? This work aims to answer these questions. We discuss a model of trust inspired by, but not identical to, interpersonal trust (i.e., trust between people) as defined by sociologists. This model rests on two key properties: the vulnerability of the user; and the ability to anticipate the impact of the AI model's decisions. We incorporate a formalization of 'contractual trust', such that trust between a user and an AI model is trust that some implicit or explicit contract will hold, and a formalization of 'trustworthiness' (that detaches from the notion of trustworthiness in sociology), and with it concepts of 'warranted' and 'unwarranted' trust. We present the possible causes of warranted trust as intrinsic reasoning and extrinsic behavior, and discuss how to design trustworthy AI, how to evaluate whether trust has manifested, and whether it is warranted. Finally, we elucidate the connection between trust and XAI using our formalization.},
booktitle = {Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency},
pages = {624–635},
numpages = {12},
keywords = {artificial intelligence, distrust, contractual trust, formalization, trustworthy, warranted trust, sociology, trust},
location = {Virtual Event, Canada},
series = {FAccT '21}
}
```

# One Sentence

---

This paper formalizing a number of different concepts related to trust in AI.

# More Sentences

---

The key model of trust ...

> ... rests on two key properties: the *vulnerability* of the user, and the ability to *anticipate* the impact of the AI model’s decisions.
> 

# Key Points

---

### How this paper defines AI

> We consider ‘artificial intelligence’ to be any automation that is attributed with intent by the user ... , i.e., anthropomorphized with a human-like reasoning process.
> 

### How this paper defines trust (in general)

> ... the trustor must be *vulnerable* to the agent’s actions, and the trustor’s goal in developing trust is to *anticipate* the impact of the AI model’s decisions.
> 

### Trust in model correctness

> ... it is in fact not trust in the general performance ability of the model, but that *the patterns that distinguish the model’s correct and incorrect cases are available to the user*.
> 

### Contractual trust

> Contractual trust is when a trustor has a belief that the trustee will stick to a specific contract.
> 

> The formalization of contracts allows us to clarify the goal of anticipation in Human-AI trust: contracts specify the behavior to be anticipated, and to trust the AI is to believe that a set of contracts will be upheld.
> 

### AI’s trustworthiness

> ... distinguishes “trust” (an attitude of the trustor) from being “trustworthy” (a property of the trustee) ... and we say that an AI model is trustworthy to some contract if it is capable of maintaining this contract.
> 

### Warranted/unwarranted trust

> ... trust is *warranted* if it is the result of trustworthiness, and otherwise it is *unwarranted.*
> 

### Intrinsic trust

> A model is more trustworthy when the observable decision process of the model matches user priors on what this process should be.
> 

Example:

> ... a doctor that is considered more trustworthy because they are citing various respectable studies to justify their claims.
> 

To gain intrinsic trust:

> (1) the user successfully comprehends the true reasoning process of the model, and (2) the reasoning process of the model matches the user’s priors of agreeable reasoning ...
> 

Corollary:

> If the user has no prior on what behaviors is trustworthy for the given task, intrinsic trust will not be gained, even if the AI is easy to understand.
> 

### Extrinsic trust

> ... the source of trust is not the decision process of the model, but *the evaluation methodology* or *the evaluation data*.
> 

Example:

> ... a doctor who is considered more trustworthy because they have a long history of making correct diagnoses; or because they graduated from a prestigious institute that is considered to have rigorous student evaluation.
> 

### A more complete and in-depth description of XAI v.s trust

> A key motivation of XAI and interpretability is to (1) increase the trustworthiness of the AI, (2) increase the trust of the user in a trustworthy AI, or (3) increase the distrust of the user in a non-trustworthy AI, all corresponding to a stated contract, so that the user develops warranted trust or distrust in that contract.
> 

> The goal of developing trust, from the user’s perspective, is to enable the ability to anticipate behavior in the presence of risk. Then XAI is a method of allowing the user easier access to the signals that enable this anticipation.
> 

### Cannot just ask users about trust ...

> ... experiments that simply ask the users whether they trust the model for some trivial task evaluate neither trust nor trustworthiness.
> 

### Advice on evaluating trust

> ... only use-cases that can be attributed with both considerable required human effort and vulnerability, are used to target, evaluate and discuss trust.
> 

To measure whether there is a causal relationship between trustworthiness and trust

> (1) Measure the level of trust in an interaction.
(2) Manipulate the real trustworthiness of the model (e.g., by handicapping it in some way; by improving its predictions; or even by replacing the model with an oracle).
(3) Measure the level of trust after the manipulation.
> 

# Other Notes

---

### “Risk is a prerequisite to the existence of Human-AI trust”

> We refer to risk as a disadvantageous or otherwise undesirable event to the trustor.
> 

> A distrusts B if A does not accept vulnerability to B’s actions, because A believes that B may not act in A’s best interest ... distrust is trust in the negative scenario.
> 

# Take-Away

---