"""
Generate section index pages for R, Python, and Other at build time.
Runs via mkdocs-gen-files — no manual updates needed when tutorials are added.
"""
import mkdocs_gen_files
from pathlib import Path

DOCS_DIR = Path("tutorials")

SECTIONS = {
    "R": "R-based tutorials for working with NEON ecological data.",
    "Python": "Python-based tutorials for working with NEON ecological data.",
    "Other": "Concept introductions, tools, and supplementary resources.",
}

for section, description in SECTIONS.items():
    section_path = DOCS_DIR / section
    if not section_path.is_dir():
        continue

    subdirs = sorted(
        d for d in section_path.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )

    lines = [
        f"# {section} Tutorials\n\n",
        f"{description}\n\n",
        "## Topics\n\n",
    ]

    for subdir in subdirs:
        display = subdir.name.replace("-", " ").replace("_", " ")
        lines.append(f"- [{display}]({subdir.name}/)\n")

    with mkdocs_gen_files.open(f"{section}/index.md", "w") as f:
        f.writelines(lines)
