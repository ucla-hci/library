# Zamfirescu-Pereira et al. — Why Johnny Can’t Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts

```
@inproceedings{10.1145/3544548.3581388,
author = {Zamfirescu-Pereira, J.D. and Wong, Richmond Y. and Hartmann, Bjoern and Yang, Qian},
title = {Why Johnny Can’t Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts},
year = {2023},
isbn = {9781450394215},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3544548.3581388},
doi = {10.1145/3544548.3581388},
abstract = {Pre-trained large language models (“LLMs”) like GPT-3 can engage in fluent, multi-turn instruction-taking out-of-the-box, making them attractive materials for designing natural language interactions. Using natural language to steer LLM outputs (“prompting”) has emerged as an important design technique potentially accessible to non-AI-experts. Crafting effective prompts can be challenging, however, and prompt-based interactions are brittle. Here, we explore whether non-AI-experts can successfully engage in “end-user prompt engineering” using a design probe—a prototype LLM-based chatbot design tool supporting development and systematic evaluation of prompting strategies. Ultimately, our probe participants explored prompt designs opportunistically, not systematically, and struggled in ways echoing end-user programming systems and interactive machine learning systems. Expectations stemming from human-to-human instructional experiences, and a tendency to overgeneralize, were barriers to effective prompt design. These findings have implications for non-AI-expert-facing LLM-based tool design and for improving LLM-and-prompt literacy among programmers and the public, and present opportunities for further research.},
booktitle = {Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems},
articleno = {437},
numpages = {21},
keywords = {design tools, end-users, language models},
location = {Hamburg, Germany},
series = {CHI '23}
}
```

# One Sentence

---

This paper conducted a design probe where non-AI-expert participants used prompting to create a language model based chatbot, surfacing how and why non-AI-experts struggled with effective prompting practices.

# More Sentences

---

> … our probe participants explored prompt designs opportunistically, not systematically, and struggled in ways echoing end-user programming systems and interactive machine learning systems.
> 

> Additional barriers to effective prompt design stem from limited conceptions of LLMs’ prompt understanding and execution abilities and their understandable inclinations to design prompts that resemble human-to-human instructions.
> 

# Key Points

---

### Challenges in end-user prompt design

> First, participants over-generalized from single data points, whether positive or negative.
> 
- They gave up testing with more data too soon and assume success or failure based on few examples

> Second, participants filtered their prompts and observations through a lens based on behavioral expectations drawn from human-human interactions
> 
- Assuming LM can understand direct instructions like humans do; as such, they are reluctant to use less-intuitive approaches such as giving examples

# Other Notes

---

### The old workflow prior to LM

> (i) identify the chatbot’s functionality or persona and draft ideal user-bot conversations, for example, through Wizard-of-Oz or having experts drafting scripts; 
(ii) create a dialogue fow template (e.g., “(1) greeting message; (2) questions to
collect user intention; (3) ...”); 
(iii) flll the template with supervised NLP models (e.g., user intent classifier, response generator, etc.);
(iv) iterate on these components to achieve a desired conversational experience.
> 

### Common barriers for non-experts in end-user programming and interactive machine learning

> • Design barriers: “I don’t even know what I want the computer to do...”
• Selection barriers: “I know what I want the computer to do, but I don’t know what to use...”
• Coordination barriers: “I know what things to use, but I don’t know how to make them work together...”
• Use barriers: “I know what to use, but I don’t know how to use it...”
• Understanding barriers: “I thought I knew how to use this, but it didn’t do what I expected...”
• Information barriers: “I know why it didn’t do what I expected, but I don’t know how to check...”
> 

# Take-Away

---