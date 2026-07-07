<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Swanson et al.: An interactive system for finding complementary literatures

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->
> ... interactive software and database search strategies that facilitate the discovery of previously unknown cross specialty information of scientific interest.

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### A key and profound observation
> An important problem in the growth of knowledge is brought to light by the following type of literature structure: one set of articles (AB) reports an interesting association between variables A and B, a different set of articles (BC) reports a relationship between B and C, but nothing at all has been published concerning a relationship between A and C, ...

![Figure 1: A and C are non-overlapping literatures linked through intermediate B literatures](../_assets/swanson_an-interactive-system-for-finding-complementary-literatures-figure-1.png)

### Definition of "complementary"
> The two sets are complementary if together they can reveal new useful information that cannot be inferred from either set alone.

### A real example of the A-B-C approach
> Articles on Raynaud's disease (C) and articles on eicosapentaenoic acid (A) when considered together were suggestive that Raynaud patients might benefit from dietary fish oils rich in eicosapentaenoic acid. One B-linkage, for example, was: dietary eicosapentaenoic acid can decrease blood viscosity (B); abnormally high blood viscosity has been reported in patients with Raynaud's disease.

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

<!-- AGENT, questions for you -->
### What else can we learn from this article besides the key A-B-C approach?

The paper is also a design argument for *interactive* discovery systems. Swanson and Smalheiser explicitly avoid full automation: the software creates suggestive juxtapositions of titles and terms, but the scientist supplies background knowledge, plausibility judgments, and final hypothesis formation.

Another important lesson is that discovery depends heavily on filtering and ranking, not just search. Their system uses stoplists, frequency comparisons, probabilistic filters, category restrictions, and human editing to keep the combinatorial explosion manageable.

The paper also treats "undiscovered public knowledge" as a social/communication failure, not merely an information retrieval problem. The relevant facts can all be public, but if they live in noninteracting specialties, no one is in a position to combine them.

Finally, the output is meant to be a heuristic guide to reading. ARROWSMITH does not prove the A-C relation; it produces organized title displays and B-term pathways that tell the user where to look for plausible mechanistic arguments.

### What if there is more than one degree of separation? (e.g., A-B1-B2-C)

The paper's implemented model is one intermediate layer: A-B-C. A longer chain such as A-B1-B2-C is a natural generalization, but it would amplify exactly the problem the authors are fighting: too many paths, many of them semantically weak or biologically irrelevant.

A practical multi-hop version would need stronger constraints at each step: typed relations rather than only shared title words, evidence scoring for each edge, novelty checks against direct A-C literature, and probably an interactive workflow where the user approves promising intermediates before expanding them. In other words, the spirit carries over, but naive multi-hop expansion would quickly become noise.

### Verify the interpretation of how the paper implemented the A-B-C approach

Procedure I does **not** identify many A and C literature sets symmetrically. It starts with one user-chosen source literature C, usually a disease or problem area, represented by a MEDLINE title-word search. From titles in C, the system extracts candidate B terms, filters them, searches those B terms in MEDLINE under chosen category restrictions, extracts candidate A terms from the resulting titles, and ranks A candidates by the number of different B pathways linking them to C.

So the rough shape is:

`C -> candidate B terms -> candidate A terms -> ranked A-candidate list`

The user then chooses a plausible A from that ranked list. In the migraine example, C is migraine and Procedure I helps surface magnesium as a promising A.

Procedure II starts after A and C have already been selected. It forms a broader B-list of words and short phrases shared by the A-title file and C-title file, edits/filter this B-list, and produces a title display organized by B term. The purpose is to help the user inspect paired A-side and C-side titles for possible complementary arguments.

So the rough shape is:

`selected A + selected C -> shared B terms/phrases -> organized title display -> candidate A-B-C arguments`

Therefore, the interpretation should be closer to: Procedure I proposes and ranks possible A literatures for a fixed C; Procedure II explores the B-linkages between one selected A and one selected C. It is not primarily a loop over all `(Ai, Cj)` pairs.
