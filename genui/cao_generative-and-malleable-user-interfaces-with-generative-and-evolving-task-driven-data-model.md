<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Cao et al.: Generative and Malleable User Interfaces with Generative and Evolving Task-Driven Data Model

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
This paper proposes using an evolvable task-driven data model as an intermediate step between a user's prompt (e.g., hosting a dinner party) and the generation of UI (e.g., UI elements that support dinner-party-related activities).

![Figure 1: Generative and malleable UIs with evolving task-driven data models](https://ar5iv.labs.arxiv.org/html/2503.04084/assets/figures/teaser.png)

## More Sentences
<!-- additional sentences -->
> ... we propose leveraging Large Language Models (LLMs) to interpret users' prompts and generate a *task-driven data model*--a structured representation of the essential entities, relationships, and data properties relevant to the intended task. This model serves as the foundation for generating UI specifications that define the components and composition of the interface.

## Key Points
<!-- the most important things in this paper -->

### The key move is to generate a malleable model, not only malleable code
Cao et al. argue that direct prompt-to-code UI generation makes iteration brittle: each revision can produce a discontinuous codebase, and end users have little ability to inspect or steer the relationship between prompt, data, and interface. Their alternative is to make the generated task-driven data model the durable substrate. The UI can then be regenerated, adapted, and inspected through changes to that model.

### The task-driven data model has three parts
The model consists of:

- an object-relational schema: task objects, entities, attributes, and references among entities;
- a dependency graph: validation and update relationships among entities/attributes;
- structured data: concrete values that instantiate the schema.

This is useful because it separates "what information structure does this task need?" from "how should the interface render it?"

### The UI is generated through specifications and patterns
The generated schema is annotated with UI mapping rules: data types, functional roles, render types, editability, thumbnails, summary/expanded list behavior, etc. This specification layer is where design-pattern knowledge enters the pipeline. In other words, the model does not directly become arbitrary UI code; it is mapped through a constrained vocabulary of UI representations and state-management rules.

### Malleability happens through model updates
Follow-up prompts and direct manipulation are translated into operations over the schema and/or data: add, remove, update, cluster, filter, sort. This is the paper's strongest connection to malleable UI: user changes do not merely patch the surface UI; they modify the underlying representation that future UI generation depends on.

### The evaluations show promise, but also narrow scope
In the technical evaluation, GPT-4o generated task models for 50 task requests. Most entities and attributes were rated "necessary and expected," and dependency relationships were usually correct. The user study involved 8 participants, who used Jelly for two open-ended tasks each. Participants generally liked the continuity, personalization, and transparency of a persistent model-driven information space. The main limitations were the need for repeated prompting, limited schema-manipulation interactions, and a limited UI specification vocabulary.

## Other Notes
<!-- other things, not so important, but good to know -->

The prototype is called **Jelly**. It combines a schema view, chat view, and generated interface panels. The schema view matters because it exposes the otherwise-hidden intermediate representation, giving users a way to inspect what the AI changed.

The paper explicitly scopes out full solutions for external data integration and context awareness. The present system mainly evaluates task representation, UI generation, and model evolution.

The paper frames generative and malleable UIs as especially relevant for open-ended information tasks: planning, sensemaking, learning about a domain, and multi-factor decision-making.


## Take-Away
<!-- critiques, ideas, actionable things, etc. -->
### Related to the transparency issue that motivates PatternGenUI
> The opaque relationship between user prompts and the resulting code further complicates interpretability and control, limiting end-users' ability to steer the generation process effectively.

### Prompt --> data model --> pattern --> UI
The proposed task-driven data model can be used to retrieve a pattern (amongst many) before generating the UI.

PatternGenUI is another layer that can be complementarily plugged into the data-model-driven UI generation process.

### The comparison study
The comparison is not framed as a strict performance comparison against an equivalent baseline. That would be hard to justify because Jelly is aimed at a different interaction paradigm: persistent, model-driven, task-evolving information spaces rather than either one-shot generated UIs, chat responses, or fixed-purpose applications. Instead, the paper frames the user study around whether the new paradigm enables qualities that existing paradigms struggle to provide: continuity across task shifts, local editability, inspectability of the underlying structure, and flexible organization of personal information.

That framing is probably what makes the study defensible to reviewers. The paper does not ask, "is Jelly faster than ChatGPT or apps on the same task?" It asks whether users can generate and adapt open-ended information spaces, what kinds of schema/data changes they make while doing so, and how they understand the experience relative to familiar tools. For an early systems paper, this makes the comparison more about *positioning and experiential contrast* than benchmark superiority.

Useful lessons for us:

- Justify the study around the contribution's mechanism, not around generic productivity. For PatternGenUI, the claim is not simply "patterns make better UIs"; it is "patterns create an inspectable and steerable layer between task model and generated UI."
- Define comparison dimensions that follow from the conceptual gap: transparency, controllability, ability to choose among alternatives, predictability of revisions, recoverability after bad generations, and preservation of task structure across changes.
- Use baselines carefully. If we include a baseline, it should test the layer we add: e.g., GenUI without explicit patterns vs. GenUI with pattern selection/inspection/editing. A generic chat or app baseline can contextualize user expectations, but it should not carry the main causal claim.
- Log and code interaction traces. Cao et al.'s schema-vs-data distinction is useful because it shows what participants are actually changing. For us, an analogous coding could distinguish task-model edits, pattern-selection edits, pattern-parameter edits, and surface-level UI edits.
- Track prompt specificity. Fully specified / underspecified / unspecified prompts help reveal whether the system supports direct execution only, or whether the intermediate layer helps users refine vague intent.
- Separate task types. Cao et al. distinguish learning/sensemaking from planning/logistical tasks; PatternGenUI may need a similar split because patterns may matter differently for exploration, comparison, decision-making, and monitoring.
- Make claims proportional. Without an equivalent controlled baseline, claim that the study demonstrates feasibility, interaction possibilities, perceived value, and emergent use patterns. With a matched ablation, we can claim more about the effect of the pattern layer itself.

For PatternGenUI, the reviewer-convincing version is: "We evaluate whether an explicit pattern layer gives users meaningful leverage over GenUI generation." The study should show that participants can understand why a UI was generated, compare pattern alternatives, make local changes at the pattern level, and preserve task/data continuity while iterating.

### Another motivation for PatternUI
A limitation discussed by participants: a limited UI specification vocabulary.
