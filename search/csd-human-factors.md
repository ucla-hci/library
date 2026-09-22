# Human Limitations in Scientific Discovery: Theories in the CSD Collection

*Searched 2026-09-21 across all 69 notes in [computational-scientific-discovery/papers/](../computational-scientific-discovery/papers/).*

**Scope.** Each entry is one theory from psychology or cognitive science that explains why humans are bad at some part of discovery. Each entry has:

- **Theory:** the name and an original reference.
- **Mechanism:** why the limitation arises.
- **In discovery:** what it hurts.
- **Collection:** the notes where it appears.
- **Grounding:** how directly the collection supports it.
  - **Named:** a note names the theory or cites its source.
  - **Mapped:** a note describes the phenomenon, and I added the theory label. These are my inferences.

**Excluded** because they are not individual-cognition theories:

- Structural holes and "undiscovered public knowledge" (Swanson, Chen). These are sociological.
- Scientific monocultures (Messeri & Crockett). This is a systemic effect.
- Motivation, incentives, and usability (Feger, Khanal, Deelman).

## Summary

| # | Theory | Why humans are bad at it | Grounding |
|---|---|---|---|
| L1 | Working-memory capacity limit | Only a few items can be held and combined at once when comprehending and integrating | Named |
| L2 | Bounded rationality: heuristic search and satisficing | Limited processing means only a sliver of the space is searched. Heuristics decide which sliver, and search stops at the first good-enough answer | Named (satisficing: Mapped) |
| L3 | Ill-structured problem solving | Goals and operators are unspecified, so the problem must first be structured | Named |
| L4 | Domain-specificity of expertise | People can only generate hypotheses their knowledge represents | Named |
| L5 | Availability heuristic | What comes to mind easily or recently gets over-explored | Mapped |
| L6 | Information foraging | People follow the information scent near known patches | Mapped |
| L7 | Effort–accuracy tradeoff | People choose low-effort strategies over informative ones | Mapped |
| L8 | Positive test strategy (confirmation bias) | People test cases their hypothesis predicts will succeed | Named |
| L9 | Single-hypothesis focus | People track one hypothesis and ignore the alternatives' diagnosticity | Named |
| L10 | Motivated reasoning / disconfirmation bias | Unwelcome evidence gets more scrutiny than welcome evidence | Named |
| L11 | Hindsight bias | Outcomes feel predictable after the fact, which invites post-hoc stories | Mapped |
| L12 | Goal shielding | An active goal suppresses attention to other goals and features | Named |
| L13 | Anomalous-data responses | Contradicting data get ignored, rejected, or reinterpreted | Mapped |
| L14 | Einstellung (mental set) | A familiar method blocks finding a better one | Named |
| L15 | Functional fixedness | Things are seen only in their usual role | Named |
| L16 | Design fixation | Examples in view constrain new ideas | Named |
| L17 | Representational change impasse | A wrong initial representation hides the solution | Mapped |
| L18 | Schema-driven interpretation | Prior schemas decide what a representation means | Mapped |
| L19 | Automation bias | People defer to automated output and stop checking | Named |
| L20 | Illusion of explanatory depth | People overestimate how well they understand a mechanism | Named |
| L21 | Omission neglect | What is not shown is treated as not existing | Mapped |
| L22 | Naïve realism / bias blind spot | People see their own view, or the AI's, as objective | Mapped |
| L23 | Curse of knowledge | Experts cannot model what others don't know | Mapped |
| L24 | Knowledge compilation | Practiced expertise becomes hard to put into words | Mapped |

---

## A. Capacity

### L1. Working-memory capacity limit (comprehension and integration)
- **Theory:** Miller (1956); Cowan (2001). Working memory holds about 4±1 chunks, and attention is a scarce resource.
- **Scope:** This entry covers *processing information that is already in front of the person*: reading, comparing, and combining. Deciding *which* options get generated or examined, and when to stop, is covered by L2.
- **Mechanism:** Integrating evidence, comparing a few candidates side by side, and composing ideas all need several items active at once. Load beyond capacity causes items to be dropped or processed shallowly.
- **In discovery:** People cannot take in the literature at the pace it grows. They also cannot hold several idea facets or lines of evidence together well enough to combine them without external support.
- **Collection:**
  - [Gil](<../computational-scientific-discovery/papers/Gil — Thoughtful artificial intelligence Forging a 305d6e6e02d4435d8a703a1292c0d18a.md>): "resource limited in attention span, memory, and processing time"
  - [Hope et al.](<../computational-scientific-discovery/papers/Hope et al — A Computational Inflection for Scient 0e09b88b233b4f229210c8e32859691e.md>): "severe limitations in the capacity to find, assimilate, and manipulate information"
  - [Radensky et al.](../computational-scientific-discovery/papers/radensky_sideator-human-llm-compound-system-for-scientific-ideation-through-facet-recombination-and-novelty-evaluation.md): applying inspirations and judging novelty are "cognitively taxing"
  - [Pu et al.](../computational-scientific-discovery/papers/pu_ideasynth.md): composing facets into a coherent idea is "effortful"
- **Grounding:** Named. The notes name the capacity limit, but none cites Miller or Cowan.

### L2. Bounded rationality: selective heuristic search and satisficing
- **Theory:** Simon (1955); Newell & Simon (1972). The human information-processing system works one step at a time. It has a small working memory and needs several seconds to store each new chunk in long-term memory. As a result, people can examine only a tiny fraction of any large problem space. A space with *b* branches over *m* moves has *b^m* paths.
- **Mechanism:** Humans cope in two ways:
  1. **Selective search.** Heuristics decide which branches get explored at all. Examples are means–ends analysis, divide-and-conquer, and generate-and-test guided by knowledge.
  2. **Satisficing.** Search stops at the first solution that is good enough, not the best one.
- **What this makes people bad at:**
  - **Coverage.** Anything a heuristic prunes is never considered, and nothing signals that it was skipped.
  - **Optimality.** Early stopping locks in the first acceptable answer.
  - **Robustness.** Whether a heuristic works depends on how well it fits the structure of the task (Simon's "scissors," 1990). A heuristic that fits the domain makes discovery efficient. One that doesn't fit leads to confident search in the wrong region.
- **Note:** Exhaustive search is also infeasible for machines. What is specific to humans is how small the fraction they can search is, which follows from the processing limits above. Heuristics are the *adaptation*, and the limitation shows up in what they leave out.
- **In discovery:** The hypothesis and experiment spaces are covered only in part, and the areas left out are shaped by the heuristics in use. Scientists also cannot screen thousands of candidates by hand, and a law that "fits the data" gets accepted without anyone checking whether a better one exists.
- **Collection:**
  - [Klahr & Simon](<../computational-scientific-discovery/papers/Klahr & Simon - Studies of Scientific Discovery Co 371e92e0bdaa45dc85dad99547ddbaea.md>): the *b^m* growth of problem spaces
  - [Stanford SEP](<../computational-scientific-discovery/papers/Stanford Philosophy Department — Scientific Discov 090a5c887f904fa88888bfd4abe635f0.md>): heuristic search yields "results that are merely provisional and plausible" and is "more efficient than exhaustive random trial and error"
  - [Magnani](../computational-scientific-discovery/papers/magnani_creative-processes-in-scientific-discovery.md): heuristic search replaces "exhaustive enumeration"
  - [Simon, *Reply to critics*](<../computational-scientific-discovery/papers/Simon — Scientific discovery as problem solving re 59ef68e21d6b4f61bc519acf5c0022b8.md>): the task is "to induce a law that fits the data," not a guaranteed-valid one. This is close to satisficing, but the note does not use the word.
  - [Pun et al.](../computational-scientific-discovery/papers/pun_target-identification-and-assessment-in-the-era-of-ai.md): scientists "cannot manually inspect thousands of candidate targets"
- **Grounding:** Named for heuristic search. Satisficing and the ecological-fit ("scissors") point are Mapped: both are Simon's, but no note mentions them.

## B. Knowledge and retrieval

### L4. Domain-specificity of expertise
- **Theory:** Chi, Feltovich & Glaser (1981); Klahr & Dunbar (1988). Knowledge is organized by domain. Experts retrieve a solution frame from memory (Theorists), while novices must search the experiment space (Experimenters).
- **Mechanism:** Hypothesis generation retrieves from long-term memory. A hypothesis whose variables or relations the person has never represented cannot be generated. To go beyond that boundary, the person has to acquire new knowledge first.
- **In discovery:** The searched space is a small subset of the possible space (universal ⊃ learner ⊃ effective search space). Klahr & Dunbar observed that none of their subjects started with the correct frame.
- **Collection:**
  - [Klahr & Dunbar](<../computational-scientific-discovery/papers/Klahr & Dunbar — Dual Space Search During Scientif ab068a86252640bca9a4045f9f78b8f6.md>)
  - [Joolingen](<../computational-scientific-discovery/papers/Joolingen — An Extended Dual Search Space Model of 0e3b643e3d374b7c80fa4f05b0355e83.md>)
  - [Gottweis et al.](../computational-scientific-discovery/papers/gottweis_accelerating-scientific-discovery-with-co-scientist.md): the "breadth and depth conundrum"
  - [Sourati et al.](../computational-scientific-discovery/papers/sourati_accelerating-science-with-human-aware-artificial-intelligence.md): "cognitive accessibility" of hypotheses
- **Grounding:** Named, via Klahr & Dunbar and Joolingen.

### L5. Availability heuristic
- **Theory:** Tversky & Kahneman (1973). People judge frequency and promise by how easily examples come to mind. Recent and frequently encountered items are more available.
- **Mechanism:** Hypotheses near recently studied entities are easier to retrieve, so they get chosen more often. This is not because they are more promising.
- **In discovery:** New protein–protein interaction (PPI) discoveries cluster at small graph distances from recent ones ("bias of locality"). Well-studied genes crowd out "dark genes," and fads such as graphene draw effort.
- **Collection:**
  - [Singer et al.](<../computational-scientific-discovery/papers/Singer et al — On biases of attention in scientifi 30ad9854f5884c0e9fb5929d6234be82.md>): "scientists' attention to recent findings." This is inferred from database traces, not observed in scientists.
  - [Hope et al.](<../computational-scientific-discovery/papers/Hope et al — A Computational Inflection for Scient 0e09b88b233b4f229210c8e32859691e.md>)
  - [Pun et al.](../computational-scientific-discovery/papers/pun_target-identification-and-assessment-in-the-era-of-ai.md)
  - [Morris](<../computational-scientific-discovery/papers/Morris — Scientists' Perspectives on the Potential 8e076be900d442babe88dc014144dc49.md>)
- **Grounding:** Mapped. The notes call it "attentional bias" or "bias of locality" and do not name availability.

## C. Search strategy

### L6. Information foraging
- **Theory:** Pirolli & Card (1999). People forage for information the way animals forage for food. They follow *information scent*, meaning cues of relevance, and stay within familiar patches until the rate of return drops.
- **Mechanism:** Distant domains give weak scent and high cost for sensemaking. The patches a person already knows score highest on both counts, so exploration stays local.
- **In discovery:** Researchers end up in filter bubbles, show "aversion to information from novel domains," and pay attention to people like themselves.
- **Collection:**
  - [Hope et al.](<../computational-scientific-discovery/papers/Hope et al — A Computational Inflection for Scient 0e09b88b233b4f229210c8e32859691e.md>): "aversion to information from novel domains, homophily"
  - [Portenoy et al.](<../computational-scientific-discovery/papers/Portenoy et al — Bursting scientific filter bubble ac2a248e0e124dddb7bc2604243305ab.md>)
  - [Kang et al.](<../computational-scientific-discovery/papers/Kang et al — ComLittee Literature Discovery with P 9a5792decf384a3e8981fa2c7f3848e8.md>)
- **Grounding:** Mapped. No note cites Pirolli & Card, although Grolemund & Wickham's sensemaking loop comes from the same tradition.

### L7. Effort–accuracy tradeoff (the adaptive decision maker)
- **Theory:** Payne, Bettman & Johnson (1993). People pick decision strategies by trading cognitive and practical effort against accuracy, and they often settle for low-effort ones.
- **Mechanism:** The cost of an option is immediate and certain, while its informational value is abstract. So the cost dominates the choice.
- **In discovery:** Measurements get taken "in areas that are easy to access rather than those that might theoretically yield the most information." Experiment choice drives cost, but it is rarely optimized.
- **Collection:**
  - [Morris](<../computational-scientific-discovery/papers/Morris — Scientists' Perspectives on the Potential 8e076be900d442babe88dc014144dc49.md>)
  - [King et al.](<../computational-scientific-discovery/papers/King et al — Functional genomic hypothesis generat 01ce3eac5c0245c9a65ee21e74ad7051.md>)
- **Grounding:** Mapped.

## D. Hypothesis testing and evidence evaluation

### L8. Positive test strategy (confirmation bias in testing)
- **Theory:** Wason (1960); Klayman & Ha (1987); Nickerson (1998). People test cases they expect to be instances of their hypothesis. When confirmation is likely anyway, such tests carry little information.
- **Mechanism:** Checking whether a hypothesis *predicts* an outcome is easier than working out what would *falsify* it. Klayman & Ha show this is a reasonable default that fails in predictable conditions.
- **In discovery:** Researchers design experiments that can only confirm. Klahr & Dunbar found scientists and non-scientists did not differ on this.
- **Collection:**
  - [Klahr & Dunbar](<../computational-scientific-discovery/papers/Klahr & Dunbar — Dual Space Search During Scientif ab068a86252640bca9a4045f9f78b8f6.md>): cites Klayman & Ha
  - [Joolingen](<../computational-scientific-discovery/papers/Joolingen — An Extended Dual Search Space Model of 0e3b643e3d374b7c80fa4f05b0355e83.md>)
  - [Gil](<../computational-scientific-discovery/papers/Gil — Thoughtful artificial intelligence Forging a 305d6e6e02d4435d8a703a1292c0d18a.md>)
  - [Hope et al.](<../computational-scientific-discovery/papers/Hope et al — A Computational Inflection for Scient 0e09b88b233b4f229210c8e32859691e.md>)
  - [Carrillo et al.](../computational-scientific-discovery/papers/carrillo_a-workflow-for-human-centered-machine-assisted-hypothesis-generation.md)
  - [Dunbar](../computational-scientific-discovery/papers/dunbar_concept-discovery-in-a-scientific-domain.md)
- **Grounding:** Named. This is the best-supported limitation in the collection.

### L9. Single-hypothesis focus (pseudodiagnosticity)
- **Theory:** Doherty et al. (1979); Mynatt, Doherty & Dragan (1993). People represent and test one hypothesis at a time. They ask how likely the evidence is under that hypothesis, not how likely it is under the alternatives.
- **Mechanism:** Holding competing hypotheses and weighing evidence against each exceeds working-memory limits (L1). As a result, the alternatives are never represented.
- **In discovery:** This is "hypothesis myopia": fixating on evidence for one hypothesis and failing to consider other explanations. The remedy is to state competing hypotheses explicitly and design discriminating experiments.
- **Collection:**
  - [Nuzzo](<../computational-scientific-discovery/papers/Nuzzo — How scientists fool themselves—and how the 7bb2fcdb24a744d78185ba5e1af9d6ac.md>)
  - [Klahr & Dunbar](<../computational-scientific-discovery/papers/Klahr & Dunbar — Dual Space Search During Scientif ab068a86252640bca9a4045f9f78b8f6.md>): "propose a single hypothesis"
  - [Josephson](../computational-scientific-discovery/papers/josephson_abductive-inference.md): a good abduction must beat the alternatives. This is the normative counterpart.
- **Grounding:** Named as a phenomenon ("hypothesis myopia"). The theory label is mine.

### L10. Motivated reasoning / disconfirmation bias
- **Theory:** Lord, Ross & Lepper (1979); Kunda (1990); Edwards & Smith (1996). Evidence against a preferred conclusion gets longer, harsher scrutiny than evidence for it.
- **Mechanism:** Directional goals bias which memories and rules get used to evaluate evidence, while the evaluation still feels objective.
- **In discovery:** This is "asymmetric attention": expected results get a free pass, and counterintuitive ones get checked hard. The remedy is blind data analysis.
- **Collection:**
  - [Nuzzo](<../computational-scientific-discovery/papers/Nuzzo — How scientists fool themselves—and how the 7bb2fcdb24a744d78185ba5e1af9d6ac.md>): "sometimes known as disconfirmation bias"
  - [D'Agostino McGowan et al.](<../computational-scientific-discovery/papers/D’Agostino McGowan, Peng, and Hicks — Design Princ 2324422fa6be409eb0257b3fbd49d5e7.md>): the "Skeptical" principle as a countermeasure
- **Grounding:** Named.

### L11. Hindsight bias
- **Theory:** Fischhoff (1975). Once people know an outcome, it seems more predictable than it was, and their memory of prior expectations shifts toward it.
- **Mechanism:** Knowing the outcome is folded automatically into how the situation is understood. The earlier, uncertain state cannot be recovered.
- **In discovery:** This produces "just-so storytelling." Post-hoc explanations fit any result, and hypotheses get quietly revised to match the data.
- **Collection:** [Nuzzo](<../computational-scientific-discovery/papers/Nuzzo — How scientists fool themselves—and how the 7bb2fcdb24a744d78185ba5e1af9d6ac.md>)
- **Grounding:** Mapped. Nuzzo describes the behavior, and the hindsight-bias label is mine.

## E. Attention and goals

### L12. Goal shielding (goal-directed selective attention)
- **Theory:** Shah, Friedman & Kruglanski (2002). An active goal inhibits competing goals and makes goal-relevant features salient.
- **Mechanism:** While a confirmation goal is unmet, it takes over attention. Features that would diagnose a different mechanism are registered but not analyzed.
- **In discovery:** In Dunbar's study, participants saw that results were discrepant but did not examine why. When the task let them satisfy the first goal, about twice as many found the unexpected mechanism.
- **Collection:** [Dunbar](../computational-scientific-discovery/papers/dunbar_concept-discovery-in-a-scientific-domain.md). This is the only controlled manipulation in the collection.
- **Grounding:** Named, with a caveat. Dunbar's own term is goal *blocking*. The note adds "goal shielding" as a modern interpretation that the study did not measure.

### L13. Responses to anomalous data
- **Theory:** Chinn & Brewer (1993). People faced with contradicting data usually protect their theory. They ignore the data, reject it, exclude it as out of scope, hold it in abeyance, reinterpret it, or make a peripheral change. Changing the theory itself is the least likely response.
- **Mechanism:** The theory being defended is entrenched, and there is no alternative theory available to explain the anomaly.
- **In discovery:** An anomaly does not explain itself. It gets treated as a failed confirmation, not as a clue. Kuhn's anomaly-driven view assumes someone does the work of explaining it.
- **Collection:**
  - [Dunbar](../computational-scientific-discovery/papers/dunbar_concept-discovery-in-a-scientific-domain.md)
  - [Stanford SEP](<../computational-scientific-discovery/papers/Stanford Philosophy Department — Scientific Discov 090a5c887f904fa88888bfd4abe635f0.md>): Kuhn
- **Grounding:** Mapped. Chinn & Brewer are not cited in the collection.

## F. Fixation and set

### L14. Einstellung effect (mental set)
- **Theory:** Luchins (1942); Bilalić, McLeod & Gobet (2008). A familiar solution method comes to mind first and blocks a better one. Bilalić et al. show experts are especially susceptible.
- **Mechanism:** The first schema that is activated guides attention toward itself, so the better alternative is never looked at.
- **In discovery:** Scientists keep "a method that they know well even if newer better methods become available." They get stuck on "specific directions and perspectives."
- **Collection:**
  - [Gil, *Thoughtful AI*](<../computational-scientific-discovery/papers/Gil — Thoughtful artificial intelligence Forging a 305d6e6e02d4435d8a703a1292c0d18a.md>): calls it "status quo or conservation bias"
  - [Gil, *Will AI write papers*](<../computational-scientific-discovery/papers/Gil — Will AI write scientific papers in the futur 619386014dac4c7698b744addadd2596.md>): proteogenomics papers use only one search method
  - [Hope et al.](<../computational-scientific-discovery/papers/Hope et al — A Computational Inflection for Scient 0e09b88b233b4f229210c8e32859691e.md>)
- **Grounding:** Named as a phenomenon. Gil labels it with the decision-theory term *status quo bias* (Samuelson & Zeckhauser, 1988). For habitual method choice, Einstellung is the closer cognitive account.

### L15. Functional fixedness
- **Theory:** Duncker (1945). People have trouble using an object or concept in a role other than its familiar one.
- **Mechanism:** Knowing an item's usual function suppresses other ways of representing it.
- **In discovery:** Mechanisms from other domains don't get seen as applicable. This is why tools expose scientists to unfamiliar purpose–mechanism facets.
- **Collection:** [Radensky et al.](../computational-scientific-discovery/papers/radensky_sideator-human-llm-compound-system-for-scientific-ideation-through-facet-recombination-and-novelty-evaluation.md), which cites Duncker
- **Grounding:** Named.

### L16. Design fixation
- **Theory:** Jansson & Smith (1991); Purcell & Gero (1996). Examples a person has seen constrain what they generate next, even when told to avoid copying them.
- **Mechanism:** An example primes its own features, and new ideas conform to them.
- **In discovery:** Ideation stays close to the papers someone has already read. This is a risk for any tool that shows examples first.
- **Collection:** [Radensky et al.](../computational-scientific-discovery/papers/radensky_sideator-human-llm-compound-system-for-scientific-ideation-through-facet-recombination-and-novelty-evaluation.md), which cites Purcell & Gero
- **Grounding:** Named.

### L17. Representational change impasse
- **Theory:** Ohlsson (1992); Knoblich et al. (1999). When the initial representation makes the solution unreachable, the solver hits an impasse. Progress requires relaxing constraints or re-encoding the problem, which people do not do spontaneously.
- **Mechanism:** The first representation defines which operators seem available. Search inside it cannot reach the answer.
- **In discovery:** Dunbar's participants treated the mechanism as "activation." The answer, "inhibition of inhibition," required re-encoding the same evidence under a different causal relation.
- **Collection:**
  - [Dunbar](../computational-scientific-discovery/papers/dunbar_concept-discovery-in-a-scientific-domain.md): the note calls it "fixation on the current representation"
  - [Klahr & Simon](<../computational-scientific-discovery/papers/Klahr & Simon - Studies of Scientific Discovery Co 371e92e0bdaa45dc85dad99547ddbaea.md>) and [Schunn & Klahr](<../computational-scientific-discovery/papers/Schunn & Klahr — A 4-space model of scientific dis 0538c08e8bfb41bab1df880d1e147022.md>): representation space
- **Grounding:** Mapped.

### L18. Schema-driven interpretation
- **Theory:** Bartlett (1932); Rumelhart (1980). Perception and comprehension are top-down. Prior schemas fill in what a representation means.
- **Mechanism:** An unfamiliar notation gets read through the conventions the person already knows.
- **In discovery:** Biologists read edges in a model diagram as material flow, not causal influence, and so misread the model.
- **Collection:** [Bridewell et al.](<../computational-scientific-discovery/papers/Bridewell et al — An interactive environment for t 1340b2facd2980a7aa04ce7b51337f2c.md>)
- **Grounding:** Mapped. This rests on a single observation.

## G. Working with automation and AI

### L19. Automation bias
- **Theory:** Mosier & Skitka (1996); Parasuraman & Manzey (2010). People use automated output as a shortcut for their own judgment. That leads to errors of commission (following wrong advice) and omission (missing what the automation missed).
- **Mechanism:** Monitoring takes effort (L7), and automation looks authoritative. Checking drops off, most of all outside the person's own expertise.
- **In discovery:** People "cognitively disengage when interacting with more sophisticated AI." They over-trust tools they cannot evaluate, and they run analyses "without fully understanding the methods."
- **Collection:**
  - [Carrillo et al.](../computational-scientific-discovery/papers/carrillo_a-workflow-for-human-centered-machine-assisted-hypothesis-generation.md)
  - [Messeri & Crockett](../computational-scientific-discovery/papers/messeri_artificial-intelligence-and-illusions-of-understanding-in-scientific-research.md)
  - [Nuzzo](<../computational-scientific-discovery/papers/Nuzzo — How scientists fool themselves—and how the 7bb2fcdb24a744d78185ba5e1af9d6ac.md>)
  - [Liu et al., PersonaFlow](../computational-scientific-discovery/papers/liu_personaflow-designing-llm-simulated-expert-perspectives-for-enhanced-research-ideation.md): the paper claims to mitigate over-reliance, but the note judges that claim unsupported
- **Grounding:** Named as the phenomenon (over-reliance, disengagement). The automation-bias literature is not cited.

### L20. Illusion of explanatory depth
- **Theory:** Rozenblit & Keil (2002). People believe they understand causal mechanisms much better than they can explain them.
- **Mechanism:** Being familiar with something, or being able to predict or operate it, is mistaken for knowing how it works.
- **In discovery:** An accurate AI prediction or explanation feels like one's own causal understanding.
- **Collection:** [Messeri & Crockett](../computational-scientific-discovery/papers/messeri_artificial-intelligence-and-illusions-of-understanding-in-scientific-research.md), which cites it by name
- **Grounding:** Named.

### L21. Omission neglect
- **Theory:** Fischhoff, Slovic & Lichtenstein (1978), the fault-tree studies. Kahneman (2011) calls the same idea "what you see is all there is." People underweight possibilities that are missing from a display.
- **Mechanism:** Judgment works on the information present. Missing branches don't trigger any sense that something is incomplete.
- **In discovery:** This is Messeri & Crockett's "illusion of exploratory breadth": the hypotheses an AI can generate are taken to be the whole space.
- **Collection:** [Messeri & Crockett](../computational-scientific-discovery/papers/messeri_artificial-intelligence-and-illusions-of-understanding-in-scientific-research.md)
- **Grounding:** Mapped. Messeri & Crockett coin their own term, and the grounding in omission neglect is mine.

### L22. Naïve realism / bias blind spot
- **Theory:** Ross & Ward (1996); Pronin, Lin & Ross (2002). People take their own perception as objective and see bias in others more readily than in themselves.
- **Mechanism:** Standpoints can't be seen from inside. A tool that shares the user's standpoint looks neutral.
- **In discovery:** This is Messeri & Crockett's "illusion of objectivity": AI is imagined to have no standpoint, or to represent all of them.
- **Collection:** [Messeri & Crockett](../computational-scientific-discovery/papers/messeri_artificial-intelligence-and-illusions-of-understanding-in-scientific-research.md)
- **Grounding:** Mapped.

## H. Externalizing knowledge

### L23. Curse of knowledge
- **Theory:** Camerer, Loewenstein & Weber (1989). Once people know something, they cannot simulate not knowing it, so they underestimate what others need to be told.
- **Mechanism:** Knowledge a person has cannot be switched off when modeling someone else's knowledge.
- **In discovery:** Researchers under-report method details, which hurts reproducibility. Papers also omit how hypotheses were generated.
- **Collection:**
  - [Gil](<../computational-scientific-discovery/papers/Gil — Thoughtful artificial intelligence Forging a 305d6e6e02d4435d8a703a1292c0d18a.md>)
  - [Zhou et al.](../computational-scientific-discovery/papers/zhou_hypothesis-generation-with-large-langauge-models.md)
  - [D'Agostino McGowan et al., analyst–audience alignment](<../computational-scientific-discovery/papers/D’Agostino McGowan, Peng, and Hicks — Evaluating t 91a2c4ac5aec4bb98352b784e6af61a3.md>)
- **Grounding:** Mapped. Publication norms are an alternative explanation.

### L24. Knowledge compilation (proceduralization)
- **Theory:** Anderson (1982), ACT. With practice, declarative knowledge is compiled into procedures that run automatically and are no longer open to verbal report.
- **Mechanism:** Expert skill becomes tacit, so experts cannot say what they do.
- **In discovery:** Contributory and interactional expertise are "tacit, codified by learning-by-doing … rarely documented." Tacit context "only humans hold" cannot be routed or shared.
- **Collection:**
  - [Love et al.](../computational-scientific-discovery/papers/love_interpersonal-relationship-drive-successful-team-science.md)
  - [Choudhury et al.](../computational-scientific-discovery/papers/choudhury_networked-intelligence-active-shared-context-graphs-for-human-ai-team-science.md)
- **Grounding:** Mapped.

---

## Observations

1. **Grounding is thin.** 13 of the 24 theories are named in the collection, but only these papers cite a primary psychology source:
   - Klahr & Dunbar, which cites Klayman & Ha
   - Radensky et al., which cites Duncker and Purcell & Gero
   - Messeri & Crockett, which cites Rozenblit & Keil

   Most AI and system papers state the limitation as motivation and do not cite a source for it.
2. **Direct evidence in scientists is rare.** Klahr & Dunbar (L4, L8) and Dunbar (L12, L13, L17) are the only studies that observe reasoning under controlled conditions. Singer et al. (L5) infers bias from database traces, and Morris (L7) is an interview study.
3. **The limitations interact.** Capacity limits (L1) make it hard to track more than one hypothesis (L9), which feeds the positive test strategy (L8). An unmet goal (L12) combined with a fixed representation (L17) makes it likely an anomaly gets dismissed (L13). A tool aimed at only one of these may leave the others in place.
4. **Some rows are my own labels.** Every "Mapped" row is my theoretical label for a phenomenon the notes describe. These rows need checking before anyone cites them. The weakest fits are L11 (Nuzzo describes the behavior only), L18 (a single observation), and L23 (publication norms compete as an explanation).
