# [→HFAI] Friedman & Nissenbaum — Bias in Computer Systems

```
@article{friedman1996bias,
  title={Bias in computer systems},
  author={Friedman, Batya and Nissenbaum, Helen},
  journal={ACM Transactions on information systems (TOIS)},
  volume={14},
  number={3},
  pages={330--347},
  year={1996},
  publisher={ACM New York, NY, USA}
}

```

# One Sentence

---

# More Sentences

---

# Key Points

---

### Definition of bias

> … bias to refer to computer systems that *systematically* and *unfairly discriminate* against certain individuals or groups of individuals in favor of others.
> 

Note: both being systematic and unfair are necessary for bias to occur

> … unfair discrimination alone does not give rise to bias unless it occurs systematically
> 

> … systematic discrimination does not establish bias unless it is joined with an unfair outcome
> 

### Categories of bias

**Preexisting bias**

> … has its roots in social institutions, practices, and attitudes.
> 
- Individuals’ own bias:
    
    > Bias that originates from individuals who have significant input into the design of the system
    > 
- Societal bias (e.g., most AI biases that stem from training data):
    
    > Bias that originates from society at large, … institutions, … or culture at large
    > 

**Technical bias**

> … arises from technical constraints or technical considerations
> 

The classic example is small terminal display only shows a small number of search results per screen, thus heavily favoring the few that appear on the first page or two.

**Emergent bias**

Bias that arises after a system is developed and deployed, “in a context of use with real users”.

> User interfaces are likely to be particularly prone to emergent bias because interfaces by design seek to reflect the capacities, character, and habits of prospective users. Thus, a shift in context of use may well create difficulties for a new set of users.
> 

> … bias is not so much a feature inherent in the system independent of the context of use, but an aspect of a system in use.
> 

Examples:

- A system is not updated to incorporate new knowledge, thus unable to help certain groups of users whose cases depend on those knowledge
- A system is used by someone outside the intended user groups. Such unintended users might have different expertise and values than what the system assumes. Thus the system might exhibit biased difficulty (expertise) or inappropriate behavior (values).

# Other Notes

---

### Case Study: Multilevel Scheduling Algorithm (MSLA)

The goal is to schedule limited processor resources for a multitude of tasks.

In addition to “first come, first serve”, there is a policy that is bias against long running job:

> If the process is not completed in this larger quantum of time, then it is placed in yet another queue of “even longer running processes.” And again, the processor returns to execute any new commands and, after that, any processes in the queue for longer-running processes …
> 

> … by systematically favoring short jobs, the MSLA violates the fairness preserved int he “first-come, first-served” strategy
> 

# Take-Away

---