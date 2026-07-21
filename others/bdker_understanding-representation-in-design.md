<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Bødker et al.: Understanding Representation in Design

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### What "design" means in this paper
> ... the design of computer applications. Design--in this context--means focusing on the parts of computer systems development that are directed toward the creation of something new.

### What "representation" means in this paper
> "The information gathered needs to be organised and represented, perhaps in a diagrammatic or formal (mathematical) notation. We use the term representation for this process, and for the product"

### Pointing out the very nature of design representations
> Most design representations are intended to hold on to something not yet existing, something under construction ...

### Defining representation from a purpose-oriented point of view
> Representation is mediating the relation between designers and their products, between designers in a team, between the design team and other design teams, and between the design team and the future users of the computer applications.

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### Implications for supporting design exploration

Bødker's most useful move is to treat a representation not as a neutral picture of a design, but as something that *mediates* design activity. It both holds an idea about the future artifact and shapes what designers can notice, discuss, and do next. For tools meant to support exploration across many alternatives, this suggests:

- **Represent alternatives as containers of ideas, not merely finished candidates.** A partial sketch, scenario, mock-up, or prototype can preserve a promising principle without requiring the rest of the design to be resolved. The system should therefore support incomplete and heterogeneous alternatives rather than forcing every option into one fully specified schema.
- **Judge a representation by the work it enables.** The relevant question is not only whether it accurately depicts the eventual artifact, but whether it helps people generate, compare, reinterpret, communicate, or test alternatives. Different exploratory activities may require different representations of the same candidate.
- **Make the representation's framing visible.** Every notation selects, adds, and suppresses information; it is not a transparent mapping of reality. At scale, tools should retain the purpose, perspective, assumptions, source material, and criteria behind each alternative so users can understand why it was represented in a particular way.
- **Keep representations open and mutable during exploration.** Within an active design setting, representations work because people can point to them, reinterpret them, and change them. Prematurely formalizing or standardizing alternatives creates a “closure” that may make comparison easier but can also eliminate ambiguity and possibilities that are productive for ideation.
- **Design explicitly for boundary crossing.** Alternatives must often travel among designers, users, engineers, and managers. A useful representation should be plastic enough for each group to work with yet robust enough to retain a shared identity. When human explanation cannot travel with it, attach portable context—for example, concrete use scenarios, rationale, provenance, and critical situations—rather than relying on abstraction alone.
- **Offer multiple linked views instead of seeking one universal representation.** Bødker exposes a tension: situated, tangible representations support local exploration, while more closed representations support coordination and division of work. A large-space exploration tool can address this by linking lightweight exploratory views to more structured comparison or implementation views while preserving their relationships and history.

The resulting design principle is: **optimize not only the expressiveness of the representation, but its capacity to keep alternatives generative, interpretable, transformable, and communicable in the activity where they are used.** This extends familiar properties such as low fidelity, abstraction, and editability with two additional concerns: *situatedness* (what context makes an alternative meaningful) and *mobility* (what must accompany it when it moves across people or stages of work).
