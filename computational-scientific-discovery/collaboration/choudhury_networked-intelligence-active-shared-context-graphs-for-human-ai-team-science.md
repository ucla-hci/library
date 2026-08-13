<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Choudhury et al.: Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

Networked intelligence:
> ... scaling the connections between humans and AI systems so that a result or hypothesis produced in one context reaches another person, agent, instrument or robot that can act on it.

Mycelium:
> ... an active shared workspace that automatically connects researchers and AI agents. As human users and agents work, the system captures important observations and hypotheses, tracks how they relate to the team's evolving knowledge model, and routes them to the person or agent whose next decision they can inform.

## Key Points
<!-- the most important things in this paper -->

### A more technical description of Mycelium
> Mycelium makes three operations explicit. It routes context across users when one participant's work is relevant to another. It preserves the team's evolving knowledge model across sessions and actors. And it keeps every routed claim tied to the evidence and reasoning that produced it. Human users and AI agents can read from and write to this shared graph through chat interfaces. As human and agentic users modify the graph through their work, Mycelium periodically discovers new connections among entries, updates the network state, and surfaces goal-relavant context to the users or agents whose next decision it can inform.

## Other Notes
<!-- other things, not so important, but good to know -->

### Findings from evaluating Mycelium

One multi-omics campaign (gluconate in *Pseudomonas putida*), three experts working asynchronously for a week. Baselines B and C were *standalone* Claude Opus 4.8 runs — so the comparison is "3 experts + Mycelium" vs. "one model alone," not "team with" vs. "team without." 26 artifacts extracted and scored 0–4.

- **Breadth up:** 25 of 26 artifacts surfaced vs. 17/18. Experiment-ready: 17 vs. 9/11.
- **Depth per artifact flat:** specificity 2.72 vs. 2.47/2.61 — "increased artifact breadth while preserving comparable specificity." The network finds more of the space, not deeper answers.
- **Two routing events carry the qualitative argument.** User-E's silent Entner–Doudoroff pathways explained User-L's missing proteomic signals; User-J's HPLC strain separation reframed L's analysis.
- **Authors scored their own system**, no independent raters or IRR. Their hedge: "strictly an audit of explicit evidence-to-action coverage rather than a measure of latent capability."

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### How much do we really need networked intelligence
1. Why not just share everything? Models can have access to everyone's contexts. Google has a version of Gemini that has all the context of a user's org.

Sharing solves **access**; routing claims to solve **attention** — reaching you when you didn't know to ask. Both routing events have that shape: User-L had no reason to query "has anyone found the Entner–Doudoroff pathway silent?" Total retrievability just moves the bottleneck from "who has the data" to "who thought to look."

The paper's defense (Supplementary Note) is three-part: contexts that can't be merged (firewalls, partner-institution policy); a single model producing correlated errors and so unable to "mathematically corroborate itself"; and tacit context only humans hold. Two are contingent — context windows grow, enterprise RAG erodes the merge problem yearly. The durable one, correlated error, isn't an argument about context at all; it's an argument for independent evaluators, which a shared graph doesn't automatically deliver.

So the value sits entirely in the routing layer — which is the one thing never evaluated. No routing precision or recall, no misrouted items, no interruption cost. And since the baselines have no humans, the artifact delta also includes "three domain experts exist." Cf. Oleksik et al.: the shortage in a real lab was never access to files, it was the context around them.

2. Does networked intelligence amount to a version-control problem---a team of humans contribute to a centralized knowledge graph?

Largely yes, and the analogy exposes what's missing. The ACG is a repo, typed entries are commits, provenance edges are parent pointers, and the grounding rule is a refusal to accept a commit with no base. §4.1's claim-attribution worry is `git blame` renamed.

What VCS has and the paper doesn't address: **branching** (incompatible hypotheses held in parallel), **merge conflicts** (routed context contradicts a claim already in the graph — fork, flag, or silently coexist?), **review** (who gates a claim into trunk?), and **garbage collection** (stale and superseded claims). A one-week, three-person run can't surface any of these, and they're what kills shared knowledge bases in practice.

The analogy breaks on initiative: git is pull-based with syntactic conflicts; here conflicts are semantic and the hard part is deciding whether two entries conflict at all. Closer to "git plus a CI job that assigns reviewers." That framing also names the sharper evaluation — conflict rate, resolution latency, graph decay, not artifact counts.

### The "functional requirements" seem haphazard
Maybe I am too used to a user-centered approach where you first understand how team members collaborate, identify pain points, and arrive at a list of requirements. Without the user-centered process, what Mycelium offers seems haphazard.

Right about the provenance, though "haphazard" may be the wrong charge. There's no formative study and no section that even claims to be requirements — the three operations are asserted from the team-science literature plus a diagnosis of what multi-agent systems fail at, with the authors' own colleagues as users. Requirements look reverse-engineered from the system.

But they aren't arbitrary; they're coupled. Routing without provenance is rumor, provenance without persistence is a log, persistence without routing is a wiki nobody reads. A coherent derivation — just derived from **the failure modes of agent architectures, not the pain points of scientists**. The tell is in the requirements themselves: each is a property of state (routed, persistent, grounded), none of people. Nothing on trust, credit, when to interrupt, or the right not to be seen.

A user-centered pass would have raised what Mycelium has no answer for: when is a half-formed observation *not* ready to be visible? Who gets credit for a hypothesis that formed only because something was routed in? What happens when the system broadcasts a junior person's dead end? These resurface in §4.1 as discussion rather than requirements — discovered after building, which is what happens when requirements come from architecture.

Framing for a review: system requirements presented as team requirements, evaluated only on system properties. The systems contribution stands on its own (Engelbart-style, artifact-as-argument). The team-science claim wrapped around it doesn't.

### The real take-away
Three interleaved requirements for supporting a team's use of agents: routing, provenance, persistence. These are generalizable themes across other systems and this paper's technical approach can also serve as references.
<!-- Note the paper states three operations ("cross-user state routing, persistent hypothesis state, provenance-bounded propagation") but implements four primitives (provenance, bounded autonomy, state-routing, grounding); the lists don't line up. -->

- **Routing** moves *typed entries*, not raw updates — eight types (`dataset`, `observation`, `interpretation`, `hypothesis`, `finding`, `open_question`, `recommendation`, `experiment_proposal`), so what crosses between people is a committed claim of a known kind, and `open_question` lets routing carry a request rather than a result. Relevance comes from **epistemic utility scoring** against "localized belief states—determining if a new observation supports, refines, or introduces tension." Delivery is the gap: no notification model, only findings that "cleanly surfac[e] ... upon their next session" — pull at session start, not push.
- **Provenance** tracks what a claim derives *from*, not who changed what: `generated_by` / `derived_from` / `supports` edges binding each claim to "the exact data, user, agent, or tool execution that produced it." Actor identity rides along, but the function is re-checkability — a routed claim arrives auditable rather than trusted, which is what makes a stranger's finding usable. Credit is the part left unsolved (§4.1).
- **Persistence** is really *grounding*: every entry "must be explicitly grounded in existing graph nodes," which stops "ungrounded, unstructured prose" from accumulating and keeps the graph a knowledge representation rather than chat logs. It also has to hold under a system that writes on its own — the runtime "launches autonomous exploratory analyses between active user sessions," so the graph changes while everyone is asleep.