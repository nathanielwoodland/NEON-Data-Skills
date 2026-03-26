"""
Generate simple section index pages for R, Python, and Other at build time.
Runs via mkdocs-gen-files — no manual updates needed when tutorials are added.
"""
import mkdocs_gen_files

SECTIONS = {
    "R": "R-based tutorials for working with NEON ecological data.",
    "Python": "Python-based tutorials for working with NEON ecological data.",
    "Other": "Concept introductions, tools, and supplementary resources.",
}

for section, description in SECTIONS.items():
    with mkdocs_gen_files.open(f"{section}/index.md", "w") as f:
        f.write(f"# {section} Tutorials\n\n{description}\n")
