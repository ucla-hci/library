<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Gao et al.: AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
This paper employs an agentic framework where agents dynamically form teams to explore multiple hypotheses in parallel, interpret and exchange results, then self-reorganize teams for the next iteration, demonstrating superior performance over multiple domains of tasks compared to a single-agent, convergence-before-exploration approach.

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### One key difference: in prior work, often hypotheses are converged before further exploration
What's limited in prior work is agents that---
> ... explore competing hypotheses in parallel.

> Multi-agent systems ... distribute work across agents, but still coordinate through a central structure: a planner decomposes the problem, a search algorithm ranks proposals, or agents converge through discussion or voting ...

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### The need of validation on multiple domains/benchmarks
... is almost a must-have for this type of agentic framework paper.

## Q&A; To-Do
<!-- - [x] Add AIDE and Autoresearch to the to-read.txt. -->

Q: Overall, what's unique in the agentic framework--i.e., what's the "secret sauce" that makes things work?

A: The secret sauce is not just "many agents." It is the combination of:

1. a shared experimental state (champion, experiment log, research forum, team queues, dead-end registries),
2. decentralized team formation around hypotheses instead of a fixed task decomposition,
3. parallel execution of competing directions,
4. critique before spending experimental compute,
5. memory of failures, so dead ends become reusable negative knowledge, and
6. reorganization after stagnation.

The important bit: discussion is not used to collapse everyone onto one consensus hypothesis. It is used to filter weak proposals and distribute effort across multiple plausible hypotheses.

Q: When forming/reorganizing teams, how are teams differ from each other?

A: Teams differ primarily by research direction / hypothesis, not by having different underlying LLMs. In the default implementation all agents use the same base coding agent/LLM backend, but they are assigned roles:

- analyst agents maintain the team's search knowledge, audit untested directions, rank proposal queues, and generate experiments;
- experiment agents claim queued experiments, edit/run code, evaluate results, and write outcomes back to the shared state.

During discussion, agents propose directions, critique each other, and eventually produce a roster. In the GPT nanochat example, the emergent teams corresponded to directions like architecture, schedule, and optimizer/throughput. When a team stagnates, agents can propose to create, merge, split, retire, or rebalance teams.

Q: What's the rationale against having a central orchestrator agent?

A: Their argument is that long-running science does not have a stable search decomposition known at the beginning. A central planner, search algorithm, or consensus/voting stage tends to assume the search space can be partitioned or ranked up front. But in real experimentation, the useful directions shift as evidence accumulates; failures need to be remembered; and new hypotheses often only become visible after partial results.

So AutoScientists replaces a central orchestrator with shared state plus local agent decisions. This lets agents independently interpret the evidence, pursue different hypotheses in parallel, and reorganize when a direction is exhausted. The tradeoff is higher coordination and token cost; the paper explicitly says it is optimizing experimental-search quality under fixed experimental compute, not LLM-call efficiency.

Q: Is human in the loop?

A: Mostly no. Humans provide the task, dataset/evaluation setup, starting code when available, and compute budget. The run itself is autonomous: agents form teams, propose experiments, run them, update the champion, track failures, and write reports/model cards. In the ProteinGym/Kermut experiment, they emphasize a 10-cycle run with no human intervention, and then freeze the discovered recipe before evaluating on all 217 assays.

**Perhaps one research opportunity is whether/how introducing humans in the loop of such a decentralized, self-organizing agenic framework might further augment it (or not)**

Q: How is consensus reached? Voting?

A: Not in the usual "everyone votes on the one answer" sense. Consensus is local and operational:

- proposals are posted to shared forums/queues and critiqued before execution;
- later discussion rounds consolidate a team roster;
- team changes require endorsement from affected teams;
- experimental truth is decided by measured performance, with a noise-aware promotion gate for champion updates.

So the mechanism is closer to conference/workshop coordination plus empirical gating than deliberative majority vote. The system tries to preserve pluralism across hypotheses rather than force consensus too early.

<!-- Q: Which papers in 2.1 AI Agents for Scientific Research are worth reading?

A: Priority reading list:

1. Autoresearch (Karpathy, 2026) - must-read baseline because this paper repeatedly contrasts against its single-agent, single-trajectory loop, especially on GPT nanochat.
2. AIDE (Jiang et al., 2025) - another key single-agent/code-exploration baseline; useful for understanding what AutoScientists claims to improve over.
3. Towards an AI Co-Scientist (Gottweis et al., 2025) - closest conceptual neighbor for hypothesis generation, debate, and refinement in scientific discovery.
4. BioML-Bench (Miller et al., 2025) - important if judging the benchmark/evaluation side rather than the agent architecture itself.
5. Biomni (Huang et al., 2025) and STELLA (Jin et al., 2026) - relevant biomedical-agent baselines used in the BioML-Bench comparison.
6. Agent Laboratory (Schmidgall et al., 2025) and AstaBench (Bragg et al., 2025) - useful for the broader "agents as research assistants / scientific benchmark" context.
7. The Virtual Lab (Swanson et al., 2025), ROBIN (Ghareeb et al., 2025), and CASCADE / AlphaEvolve / AI-Researcher style systems - worth skimming for alternative multi-agent or code-evolution approaches, but less central to the specific AutoScientists claim than AIDE, Autoresearch, and AI Co-Scientist. -->

