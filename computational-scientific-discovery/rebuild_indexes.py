#!/usr/bin/env python3
"""Validate paper metadata and rebuild the collection's Markdown indexes."""

from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
PAPERS = ROOT / "papers"
INDEXES = ROOT / "indexes"

DEFINITIONS = {
    "activities": {
        "problem-formulation": "Selecting, constructing, or reframing research questions and goals.",
        "literature-discovery": "Finding, connecting, or synthesizing relevant prior knowledge.",
        "data-representation": "Choosing the objects, variables, formats, or visualizations through which data are understood.",
        "hypothesis-generation": "Proposing, revising, or prioritizing explanations, relationships, models, or discovery candidates.",
        "experiment-design": "Choosing experimental paradigms, interventions, measurements, controls, or parameter settings.",
        "experiment-execution": "Carrying out physical or computational experiments and simulations.",
        "data-analysis": "Transforming, exploring, or modeling data to extract patterns and results.",
        "evidence-evaluation": "Assessing support, validity, novelty, plausibility, or competing claims and candidates.",
        "communication": "Writing, reviewing, explaining, or otherwise sharing research outputs.",
        "collaboration": "Coordinating people, agents, expertise, artifacts, or shared understanding.",
        "workflow-orchestration": "Integrating research activities into a managed computational, robotic, or agentic process.",
        "reproducibility": "Supporting provenance, replication, data stewardship, or reuse.",
    },
    "contributions": {
        "theory": "Explanatory or predictive accounts of scientific discovery or behavior.",
        "framework": "Organizing concepts, stages, dimensions, or relationships.",
        "method": "Procedures, algorithms, or analytical techniques.",
        "system": "Implemented interfaces, software systems, agents, or robots.",
        "benchmark": "Tasks, datasets, or metrics intended for systematic comparison.",
        "empirical-study": "Evidence from experiments, observations, interviews, deployments, or user studies.",
        "review": "Syntheses of prior literature or approaches.",
        "perspective": "Arguments, critiques, agendas, or commentaries.",
        "design-guidance": "Principles or recommendations for designing tools and practices.",
    },
    "domains": {
        "general": "Cross-domain scientific discovery.",
        "data-science": "Data science and statistical analysis.",
        "machine-learning": "Machine-learning research.",
        "biology": "Biological science.",
        "biomedicine": "Biomedical research.",
        "drug-discovery": "Drug discovery and development.",
        "climate-science": "Climate science.",
        "ocean-science": "Ocean science.",
        "environmental-science": "Environmental science.",
        "high-energy-physics": "High-energy physics.",
        "nanophotonics": "Nanophotonics.",
        "science-of-science": "Empirical and computational study of science itself.",
        "social-science": "Social science.",
    },
    "scope": {
        "focused": "One or two closely related research activities.",
        "multi-activity": "Several connected activities without the full research loop.",
        "end-to-end": "A near-complete iterative discovery pipeline.",
        "field-level": "Scientific discovery broadly rather than one bounded pipeline.",
    },
}

REQUIRED_FIELDS = ("activities", "contributions", "domains", "scope", "coding_status")
LIST_FIELDS = {"activities", "contributions", "domains"}


def parse_paper(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing YAML front matter")
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"{path}: unclosed YAML front matter") from error

    metadata = {}
    current = None
    for line in lines[1:closing]:
        if line.startswith("  - "):
            if current not in LIST_FIELDS:
                raise ValueError(f"{path}: list item without a recognized field: {line}")
            metadata[current].append(line[4:])
        elif ":" in line:
            key, value = line.split(":", 1)
            current = key.strip()
            metadata[current] = [] if not value.strip() else value.strip()
        elif line.strip():
            raise ValueError(f"{path}: unsupported front matter line: {line}")

    missing = set(REQUIRED_FIELDS) - set(metadata)
    if missing:
        raise ValueError(f"{path}: missing fields: {', '.join(sorted(missing))}")
    if metadata["coding_status"] != "coded":
        raise ValueError(f"{path}: expected coding_status: coded")
    for field in LIST_FIELDS:
        if not metadata[field]:
            raise ValueError(f"{path}: {field} must not be empty")
        unknown = set(metadata[field]) - set(DEFINITIONS[field])
        if unknown:
            raise ValueError(f"{path}: unknown {field}: {', '.join(sorted(unknown))}")
    if metadata["scope"] not in DEFINITIONS["scope"]:
        raise ValueError(f"{path}: unknown scope: {metadata['scope']}")

    title = next((line[2:].strip() for line in lines[closing + 1 :] if line.startswith("# ")), None)
    if not title:
        raise ValueError(f"{path}: missing level-one title")
    return {"path": path, "title": title, **metadata}


def paper_link(paper, from_indexes=False):
    prefix = "../papers/" if from_indexes else "papers/"
    return f"[{paper['title']}]({prefix}{quote(paper['path'].name)})"


def build_grouped_index(papers, field, heading, introduction):
    groups = defaultdict(list)
    for paper in papers:
        values = paper[field] if field in LIST_FIELDS else [paper[field]]
        for value in values:
            groups[value].append(paper)

    lines = [
        f"# {heading}",
        "",
        introduction,
        "",
        "This file is generated by `../rebuild_indexes.py` from paper front matter.",
        "",
    ]
    for value in DEFINITIONS[field]:
        members = sorted(groups[value], key=lambda paper: paper["title"].casefold())
        lines.extend([f"## {value.replace('-', ' ').title()} ({len(members)})", "", DEFINITIONS[field][value], ""])
        lines.extend(f"- {paper_link(paper, from_indexes=True)}" for paper in members)
        lines.append("")
    return "\n".join(lines)


def build_catalog(papers):
    lines = [
        "# All Papers",
        "",
        "Alphabetical catalog generated by `../rebuild_indexes.py` from paper front matter.",
        "",
        "| Paper | Activities | Contributions | Domains | Scope |",
        "| --- | --- | --- | --- | --- |",
    ]
    for paper in sorted(papers, key=lambda item: item["title"].casefold()):
        formatted = {
            field: ", ".join(f"`{value}`" for value in paper[field])
            for field in LIST_FIELDS
        }
        lines.append(
            f"| {paper_link(paper, from_indexes=True)} | {formatted['activities']} | "
            f"{formatted['contributions']} | {formatted['domains']} | `{paper['scope']}` |"
        )
    lines.append("")
    return "\n".join(lines)


def main():
    papers = [parse_paper(path) for path in sorted(PAPERS.glob("*.md"))]
    INDEXES.mkdir(exist_ok=True)
    outputs = {
        "research-activities.md": build_grouped_index(
            papers,
            "activities",
            "Papers by Research Activity",
            "A paper may appear under several activities when it substantively connects them.",
        ),
        "contribution-types.md": build_grouped_index(
            papers,
            "contributions",
            "Papers by Contribution Type",
            "Contribution codes describe what each paper contributes, independently of the research activities it addresses.",
        ),
        "domains.md": build_grouped_index(
            papers,
            "domains",
            "Papers by Domain",
            "Domain codes describe the scientific setting; `general` denotes a cross-domain account.",
        ),
        "scopes.md": build_grouped_index(
            papers,
            "scope",
            "Papers by Scope",
            "Scope distinguishes focused papers from multi-activity, end-to-end, and field-level accounts.",
        ),
        "all-papers.md": build_catalog(papers),
    }
    for filename, content in outputs.items():
        (INDEXES / filename).write_text(content, encoding="utf-8")
    print(f"Validated {len(papers)} papers and rebuilt {len(outputs)} indexes")


if __name__ == "__main__":
    main()

