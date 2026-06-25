<!-- source: https://ieeexplore.ieee.org/document/8812011/ -->

# Choi et al.: Visual (dis)Confirmation

## One Sentence
A 2019 system paper introducing a visual analytics tool that lets users frame hypotheses in natural language and automatically generates visualizations to validate or refute those expectations against data.

## More Sentences
Visual (dis)Confirmation addresses the mismatch between current VA tools (optimized for exploration) and the confirmatory phase of scientific analysis. Users articulate data expectations as natural-language hypotheses; the system selects relevant data features and generates confirming or disconfirming visualizations. The tool operationalizes the idea from Concept-Driven VA (CHI 2019) into an automated pipeline.

## Key Points

### Automated Hypothesis-to-Visualization Pipeline
The system converts natural-language hypothesis statements into feature selections and visualization types, bridging the user's mental model and the data.

### Confirmatory vs. Exploratory Distinction
> "Visualization tools notably lack capabilities that would allow users to visually and incrementally test the fit of their conceptual models and provisional hypotheses against the data."

### Support for Incremental Testing
The "incremental" framing maps directly onto iterative hypothesis evaluation in SDDS: users refine hypotheses as partial confirmations or disconfirmations accumulate.

## Other Notes
Published at IV 2019 (International Conference on Information Visualisation), IEEE. Authors: Kwon Choi, Nirmal Kumar Raveendranath, Jared Westerfield, Khairi Reda. Paper is a systems/design contribution complementing the user study in Concept-Driven VA. [abstract only — full paper behind IEEE paywall]

## Take-Away
Directly implements a hypothesis validation interface; the closest existing HCI system to what the SDDS "evaluate evidence" phase requires in an interactive setting.
