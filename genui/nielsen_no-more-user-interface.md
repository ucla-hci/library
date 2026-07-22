<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Nielsen: No More User Interface?

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
> This may mean the end of UI design in the traditional sense, refocusing designers' work on orchestrating the experience at a deeper level

## More Sentences
<!-- additional sentences -->
> We're trading wireframes for operating manuals to codify the rules that govern agent behavior ...

## Key Points
<!-- the most important things in this paper -->

### A quite clear chronicle of AI product development in recent years

Nielsen summarizes Luke Wroblewski's account as six stages in which AI moves from an invisible implementation detail to the principal actor in the experience:

| Stage | What changed | Example | Core UX challenge |
|---|---|---|---|
| 1. ML behind the scenes (2016–2022) | Models quietly power features inside conventional interfaces. | Google Translate; YouTube recommendations | Make AI output fit established UI patterns and feel native. |
| 2. Chat interfaces (late 2022) | The model moves into the foreground and conversation becomes the product. | ChatGPT; image/video chat products | Design conversations, scaffold prompts, and support error recovery. |
| 3. Retrieval-augmented products (2023) | External sources and context improve relevance and trust. | “Ask LukeW”; ChatGPT with web access | Communicate provenance and citations and let users control sources. |
| 4. Tool use and foreground agents (2024–2025) | Models plan and execute multi-step tool use while users remain involved. | Augment Agent; Bench workspace | Make plans visible, permit mid-task changes, and expose tool boundaries. |
| 5. Background agents (2025 onward) | Multiple workflows run in parallel with little continuous supervision. | Bench scheduling; early multi-agent demos | Provide monitoring, alerts, status, and confidence signals. |
| 6. Agent-to-agent ecosystems (emerging) | Agents coordinate or negotiate across products and organizations. | Google's A2A protocol; otherwise still speculative | Define handoffs, permissions, data boundaries, and audit trails. |

The progression is also a progression of design responsibility. UX moves from fitting probabilistic output into a familiar interface, through helping users converse with and steer a model, to governing work that happens out of sight. As autonomy increases, error handling becomes more consequential and trust depends less on the polish of an individual answer than on visibility into sources, plans, actions, costs, and recovery mechanisms. This is Nielsen's synthesis and forecast, not a taxonomy validated by a research study. ([Nielsen, 2025](https://www.uxtigers.com/post/no-more-ui))

### Designing agentic experiences is similar to service design

Service design concerns the end-to-end delivery of a service across people, processes, technologies, and touchpoints. A service blueprint commonly distinguishes the user's visible journey (the *frontstage*) from employee actions, organizational processes, and infrastructure that make it possible (the *backstage*). The object being designed is therefore not a single screen or encounter, but a coordinated system that produces a coherent experience over time.

Agentic experience design has a similar object of attention. The user's prompt, approval request, progress notification, or result is only the frontstage. Backstage, one or more agents may decompose a goal, select tools, retrieve data, spend resources, communicate with other systems, retry failures, and escalate exceptions. Specifying an agent's behavior consequently resembles designing a service blueprint:

- **Actors and responsibilities:** define which work belongs to the user, agent, model, tool, human operator, or external service.
- **Handoffs and orchestration:** specify when control or information passes between actors and how context survives the transition.
- **Policies and boundaries:** encode permissions, spending limits, privacy rules, prohibited actions, and conditions requiring consent.
- **Failure and recovery:** plan for unavailable tools, uncertain results, conflicting agents, partial completion, escalation, rollback, and compensation.
- **Visibility and trust:** decide which backstage actions become visible through plans, provenance, status, costs, logs, and explanations.
- **Service character:** specify how proactive, patient, interruptive, cautious, or autonomous the agent should be in different situations.

The key shift is from specifying the arrangement of controls to specifying a behavioral operating model: what the agent may do, when it should act or ask, how it coordinates, and how the user can inspect or reverse its work. Nielsen calls the corresponding design objects *policy surfaces*, *confidence conveyors*, and *system temperament*. His analogy is useful, but agentic systems add complications beyond conventional service design: behavior is probabilistic, the set and order of steps may be generated at runtime, and autonomous actions can scale errors before a person sees them. The blueprint must therefore be paired with runtime guardrails, observability, and intervention points—not merely an intended journey.

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->
