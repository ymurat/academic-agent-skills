---
name: icarus-figures
description: >-
  Use when making reproducible publication-grade data figures (matplotlib) or
  TikZ method/framework figures for a paper.
---
# Icarus figures

Full upstream skill (TAO-QKV/Icarus-Figures, vetted low risk on 2026-10-31): `resources/Icarus-Figures/`.

1. Read `resources/Icarus-Figures/.claude/skills/icarus-figures/SKILL.md` in full and follow it. Read the helper files and example scripts it points to as needed.
2. Work in a copy under `./work/figures/<project>/`, not inside the source folder.
3. Dependencies: numpy and pandas are required. Install matplotlib (`pip install matplotlib`) before the first run if it is missing. TikZ figures need LaTeX, which is not installed; install a minimal TeX Live (`apt-get install texlive-latex-extra texlive-pictures` or similar) only when a TikZ figure is actually needed, or hand the user the `.tex` source.
4. Use only data the user supplied. Never invent or smooth data points; label any placeholder data as example data.
5. Match the target venue's figure rules (column width, font size, vector format, colour-blind safe palette). Check the venue's author guide when it matters.
6. Deliver the figure file plus the script that produced it, so it can be regenerated.
7. Captions and text follow these writing rules: no em dashes, no buzzwords, plain and precise.
