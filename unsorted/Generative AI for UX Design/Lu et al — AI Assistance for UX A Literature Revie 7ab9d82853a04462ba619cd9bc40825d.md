# Lu et al. — AI Assistance for UX: A Literature Review Through Human-Centered AI

```

@misc{lu_ai_2024,
	title = {{AI} {Assistance} for {UX}: {A} {Literature} {Review} {Through} {Human}-{Centered} {AI}},
	shorttitle = {{AI} {Assistance} for {UX}},
	url = {http://arxiv.org/abs/2402.06089},
	doi = {10.48550/arXiv.2402.06089},
	abstract = {Recent advancements in HCI and AI research attempt to support user experience (UX) practitioners with AI-enabled tools. Despite the potential of emerging models and new interaction mechanisms, mainstream adoption of such tools remains limited. We took the lens of Human-Centered AI and presented a systematic literature review of 359 papers, aiming to synthesize the current landscape, identify trends, and uncover UX practitioners' unmet needs in AI support. Guided by the Double Diamond design framework, our analysis uncovered that UX practitioners' unique focuses on empathy building and experiences across UI screens are often overlooked. Simplistic AI automation can obstruct the valuable empathy-building process. Furthermore, focusing solely on individual UI screens without considering interactions and user flows reduces the system's practical value for UX designers. Based on these findings, we call for a deeper understanding of UX mindsets and more designer-centric datasets and evaluation metrics, for HCI and AI communities to collaboratively work toward effective AI support for UX.},
	urldate = {2024-06-21},
	publisher = {arXiv},
	author = {Lu, Yuwen and Yang, Yuewen and Zhao, Qinyi and Zhang, Chengzhi and Li, Toby Jia-Jun},
	month = feb,
	year = {2024},
	note = {arXiv:2402.06089 [cs]},
	keywords = {Computer Science - Human-Computer Interaction},
	file = {arXiv Fulltext PDF:/Users/xac/Zotero/storage/8VR7PGD2/Lu et al. - 2024 - AI Assistance for UX A Literature Review Through .pdf:application/pdf;arXiv.org Snapshot:/Users/xac/Zotero/storage/978MHQCW/2402.html:text/html},
}

```

# One Sentence

---

This paper reviews literature on different ways AI supports the UX design process and maps their findings on the double diamond model.

# More Sentences

---

# Key Points

---

### What is fundamentally unique about UX design

> A central goal of UX methodologies and processes is *empathy building*. … UX practitioners view methodologies as “*mindsets*”, rather than actual rigorous methods, to scaffold listening to users and considering diverse user inputs.
> 

### AI for UX design: what doesn’t work

> … existing research that uses AI for simplistic automation, … is generally not desired by UX practitioners and hard to integrate into existing workflows.
> 

Also doesn’t work (or not enough to be helpful) is generating artifacts (e.g., persona), which often shortcuts the valuable empathy building process.

# Other Notes

---

### The double diamond model

![Double Diamond design process](../../_assets/lu-double-diamond-design-process.png)

[https://www.designcouncil.org.uk/our-resources/framework-for-innovation/](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/)

- **Discover.** The first diamond helps people understand, rather than simply assume, what the problem is. It involves speaking to and spending time with people who are affected by the issues.
- **Define.** The insight gathered from the discovery phase can help you to define the challenge in a different way.
- **Develop.** The second diamond encourages people to give different answers to the clearly defined problem, seeking inspiration from elsewhere and co-designing with a range of different people.
- **Deliver.** Delivery involves testing out different solutions at small-scale, rejecting those that will not work and improving the ones that will.

# Take-Away

---

- Genux (or any text-to-UI models) only covers a small part of the UX design process (mostly “Develop”?) and can’t even serve as the dominant part.
- For Genux literature review, refer to 4.3.1 UI Generation, which is categorized into
    - Generating full-screen UIs (which mostly is about laying out UI elements?)
    - Generating (individual?) UI components
    - Fidelity conversion (e.g., paper sketches to wireframes)

### One reason text-to-UI might mismatch UX designers’ needs

There is an increasing trend of companies providing pre-defined libraries of UI elements.

> … designers are constrained in changing the visual aspects of design, while freed to focus more on crafting friendly, seamless user experiences with pre-defined UI elements.
> 

Text-to-UI generation currently cannot start from a library of UI elements. Thus the output cannot be directly transferrable to the designers’ project.
