<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Morris et al.: Position: Levels of AGI for Operationalizing Progress on the Path to AGI

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

**Table 1. Levels of AGI, exemplified with current AI systems**

| Performance Level | Narrow (task-specific) | General (metacognitive tasks, incl. learning new skills) |
|---|---|---|
| Level 0: No AI | Calculator software; compiler | Human-in-the-loop computing, e.g., Amazon Mechanical Turk |
| Level 1: Emerging (equal to or somewhat better than an unskilled human) | GOFAI (Good Old-Fashioned AI); simple rule-based systems, e.g., SHRDLU | ChatGPT, Bard, Llama 2, Gemini |
| Level 2: Competent (at least 50th percentile of skilled adults) | Toxicity detectors, e.g., Jigsaw; Smart Speakers, e.g., Siri, Alexa, Google Assistant; VQA systems, e.g., PaLI; Watson; SOTA LLMs for a subset of tasks, e.g., short essay writing, simple coding | Not yet achieved |
| Level 3: Expert (at least 90th percentile of skilled adults) | Grammarly; generative image models, e.g., Imagen, DALL-E 2 | Not yet achieved |
| Level 4: Virtuoso (at least 99th percentile of skilled adults) | Deep Blue, AlphaGo | Not yet achieved |
| Level 5: Superhuman (outperforms 100% of humans) | AlphaFold, AlphaZero, Stockfish | Artificial Superintelligence (ASI) — not yet achieved |

## Key Points
<!-- the most important things in this paper -->

### The process-capability spectrum of defining AGI
Amongst various definitions of AGI, some lean towards a process-oriented approach (e.g., reasoning like human brain) whereas others are capability-oriented (e.g., human-level performance in cognitive tasks).

This paper argues that AGI should be defined by capability not process.

### AGI principles

1. Focus on Capabilities, not Processes
(See the point above)

2. Focus on Generality *and* Performance
AGI should achieve both the ability to perform general tasks with a high performance

3. Focus on Cognitive and Metacognitive, but not Physical, Tasks
- The paper equates metacognition as learning
- This principle's exclusion of physical tasks makes sense from a scoping point of view but doesn't intelligence also comes from interacting with the physical world?

4. Focus on Potential, not Deployment
> ... systems that are *capable* of achieving a certain level of performance (e.g., against a given benchmark) may not match this level *in practice* when deployed

- Just because AGI *can* do something doesn't mean it will succeed in that thing in the real world.
- The paper gives the example of image generation: the model has the potential to generate high-quality images but it doesn't mean it can help real-world users (e.g., illustrators) create high-quality images.
- **I believe this gap is pretty much why HCI exists even AI models hold the promises of automation without humans in the loop**

5. Focus on Ecological Validity
> ... the importance of choosing tasks that align with real-world (i.e., ecologically valid) tasks that people value ...

6. Focus on the Path to AGI, not a Single Endpoint
> Much as the adoption of a standard set of Levels of Driving Automation allowed for clear discussions of policy and progress relating to autonomous vehicles ...

## Other Notes
<!-- other things, not so important, but good to know -->

### The theory of "evolution of technology" might disagree with---
> The concept of AGI is related to a prediction about progress in AI, namely. that is is toward greater generality, approaching and exceeding human generality.

### Historical, original framing of AGI
> ... in a 1997 article about military technologies by Mark Gubrud, which defined AGI as "AI systems that rival or surpass the human brain in complexity and speed, that can acquire, manipulate and reason with general knowledge, and that are usable in essentially any phase of industrial or military operations where a human intelligence would otherwise be needed."

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### Is brain-based process needed for AGI?
> ... the success of transformer-based architecture whose performance is not reliant on human-like learning suggests that strict brain-based processes and benchmarks are not inherently necessary for AGI ...

Yes, with an important distinction. A transformer is an artificial neural network, so it inherits a *loose* analogy to the brain: many simple units exchange weighted signals and jointly encode information. But its “neurons” are mathematical abstractions, not models of the low-level operation of biological neurons. Transformer self-attention uses global vector and matrix operations, and the network is ordinarily trained with backpropagation—neither closely matches the anatomy, signaling, or learning mechanisms of a human brain. Thus, it is reasonable to call a transformer brain-*inspired*, but not a brain-based process in the stronger biological or cognitive sense used here.

The paper's conclusion should still be read as suggestive rather than conclusive. The success of transformers shows that substantial cognitive capabilities do not require faithfully reproducing human learning, but current transformers do not establish that no brain-like process will be necessary for full AGI.

### is AGI development too detached from physical, robotic tasks?
Is this intentional?
The paper thinks it's fine to exclude physical tasks.

### The pre-assumption that AGI should aim to surpass humans
The levels are measured by---
> percentiles (of humans that AGI can beat) ... in reference to a sample of adults who possess the relevant skill

But why not consider an alternative view---AGI might not surpass humans but it does what humans categorically would not do.