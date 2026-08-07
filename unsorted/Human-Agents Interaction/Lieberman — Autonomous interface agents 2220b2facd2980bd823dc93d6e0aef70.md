# Lieberman — Autonomous interface agents

```
@inproceedings{lieberman1997autonomous,
  title={Autonomous interface agents},
  author={Lieberman, Henry},
  booktitle={Proceedings of the ACM SIGCHI Conference on Human factors in computing systems},
  pages={67--74},
  year={1997}
}

```

# One Sentence

---

This paper proposes autonomous interface agents—a concept that unifies two existing types of agents: interface agents that help users operate an interactive interface and autonomous agents that automate users’ tasks “behind the scene”.

# More Sentences

---

> … *interface agents*, software that actively assists a user in operating an interactive interface, and *autonomous agents*, software that takes action without user intervention and operates concurrently, either while the user is idle or taking other actions.
> 

# Key Points

---

### Definition of agents

> … an agent is any program that can be considered by the user to be acting as an assistant or helper, rather than as a tool in the manner of a conventional direct-manipulation interface.
> 

> An agent should display some (but perhaps not all) of the characteristics that we associate with human intelligence: learning, inference, adaptability, independence, creativity.
> 

### Technical definition of interface agents

> … an *interface agent* to be  a program that  can also affect the objects in a direct manipulation interface, but without explicit instruction from the user. The interface agent reads input that the user presents to the interface, and it can make changes to the objects the user sees on the screen, though not necessarily one-to-one with user actions.
> 

Why is interface agent not enough?

> An assistant may not be of much practical help if he or she needs very explicit instruction all the time and constant supervision while carrying out actions.
> 

### Technical definition of autonomous agents

> An *autonomous agent* is an agent program that operates in parallel with the user. Autonomy says that the agent is, conceptually at least, always running. The agent may discover a condition that might interest the user and independently decide to notify him or her. The agent may remain active based on previous input long after the user has issued other commands or has even turned the computer off.
> 

### An example of autonomous interface agents

Letizia is an autonomous interface agents that accompanies users who are searching for web pages on the internet. It displays two side panels: the top right shows **what the agent is working on**—candidate web pages Letizia is going through to identify recommendations for the user; and the bottom right shows **the results of the agent’s work**—recommended web pages relevant to the user’s search.

In general, this could be an example of how to present agents’ work to users.

![image.png](Lieberman%20%E2%80%94%20Autonomous%20interface%20agents/image.png)

# Other Notes

---

### How agents traditionally appear on an interface

> Traditional interface design is oriented toward *conversational* interfaces, where the user and the agent “take turns” acting.
> 

# Take-Away

---

### Conceptual limitation of autonomous interface agents

… is still limited by the assumption that certain interfaces are complex enough to require agents’ help. But agents do not need user interfaces; they just need an interface to communicate with users.