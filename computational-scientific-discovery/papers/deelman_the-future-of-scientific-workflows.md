---
activities:
  - experiment-execution
  - data-analysis
  - workflow-orchestration
  - reproducibility
contributions:
  - framework
  - review
  - perspective
domains:
  - general
scope: field-level
coding_status: coded
---

<!-- save as: <last-name-of-first-author>_<paper-title>.md -->

# Deelman et al.: The future of scientific workflows

## One Sentence
<!-- summarize the paper in one sentence, ideally with one figure as well -->

## More Sentences
<!-- additional sentences -->

## Key Points
<!-- the most important things in this paper -->

### Definition of "workflow" in the context of scientific discovery
> All science campaigns of sufficient complexity consist of numerous interconnected computational tasks. A *workflow* in this conrtext is the composition of several such computing tasks.

A concrete example (based on target ID in AD) could be
```
Literature Corpus
    ↓
Entity Extraction
    ↓
Knowledge Graph Construction
    ↓
Target Prioritization
    ↓
Report Generation
```

## Other Notes
<!-- other things, not so important, but good to know -->

## Take-Away
<!-- critiques, ideas, actionable things, etc. -->

### On provenance
In the case of target ID---without provenance:
```
Top Target: TREM2
```

With provenance:
```
Input:
  AD GWAS dataset v3

Step 1:
  Variant mapping using Tool A

Step 2:
  Pathway enrichment using Tool B

Step 3:
  Knowledge graph ranking using Tool C

Parameters:
  significance threshold = 0.01

Execution:
  UCLA cluster
  June 15, 2026

Output:
  TREM2 ranked #1
```


### Overall, this paper's implications for HCI
> The second area isi *programming and usability*. The participants found that the lack of support for workflows on HPC platforms impedes adoption of workflow technologies and that programming models, design patterns, the user interface, task communication, and portability are potential areas for improvement. 

Some specific opportunities for HCI involvement:
- Direct manipulation for specifying workflows
    > Today, scientists use Python or shell scripts to specify workflows, or they integrate the workflow directly into their simulation code.

- Abstracting (reusable) patterns of workflows
    > Many scientists build workflows by example; they iteratively construct one workflow using a previous one as a template. ...

    > Research to identify common needs and expression patterns (akin to design patterns in software engineering) in workflows ...

    > The appropriate level of abstraction for workflows is unclear.

- Human in the loop of workflows
    > All models treat workflow tasks as black boxes … and none of them captures details of the execution environment or human interactions.

    > The real-time status of the workflow needs to be accessible to users. A human-in-the-loop is needed in many different types of workflows including exploration and failure recovery.

Given a workflow (e.g., the example above), some HCI-related questions:
* What abstractions should scientists see?  
* How should workflows be represented?  
* How should humans steer workflows?  
* How should workflow patterns be reused?  
* How should provenance be presented and interpreted? 