---
name: latex-build
description: >-
  Use when the user wants a LaTeX or Overleaf manuscript, thesis or Beamer deck created from a venue template, compiled, debugged, converted from Word, or checked before submission.
---
# LaTeX build

Own recipe for building and debugging LaTeX documents. Notes: `resources/latex-build/README.md`.

## Setup (once, ask before installing)
`sudo apt-get install -y latexmk texlive-latex-extra texlive-publishers texlive-bibtex-extra biber texlive-lang-european texlive-science` (Turkish hyphenation is in `texlive-lang-european`). Check with `latexmk -v`. For Word conversion add `pandoc`.

## Workflow
1. **Template.** Get the venue's official class from the author guidelines or CTAN (IEEEtran, acmart, llncs, elsarticle, svjour3) or the institute thesis template. Never alter class files; changes go in the preamble.
2. **Structure.** `main.tex`, `sections/*.tex` via `\input`, `figures/`, `refs.bib`. For a thesis: front matter (özet, abstract, teşekkür), chapters, appendices, CV per the institute rules.
3. **Turkish.** pdfLaTeX: `\usepackage[T1]{fontenc}`, `\usepackage[utf8]{inputenc}`, `\usepackage[turkish]{babel}` (add `shorthands=:!` if `=` causes trouble). LuaLaTeX or XeLaTeX with `fontspec` when the template allows. Use `biblatex` plus `biber` for UTF-8 references; for `bibtex` styles escape characters (`{\c{s}}`, `{\u{g}}`, `{\i}`).
4. **Compile.** `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` (or `-lualatex`). Read `main.log` from the first error, not the last. Common fixes: undefined control sequence (missing package), `Missing $ inserted` (math character in text, for example `_`), overfull hbox (rephrase or `\sloppy` locally), undefined citations (run biber, check key), float placement.
5. **Overleaf.** Zip the project folder for upload; or pull/push via Overleaf Git only with the user's own token entered by the user.
6. **Word to LaTeX.** `pandoc in.docx -o out.tex --extract-media=figures`, then move the body into the template; fix tables and equations by hand.
7. **Pre-submission check.** Page limit and margins untouched; anonymisation for double-blind (author block, acknowledgements, self-citations in third person, PDF metadata via `\hypersetup{pdfauthor={}}`); all fonts embedded (`pdffonts main.pdf`); no `??` references; figures vector or at least 300 dpi; bibliography cleaned with `bib-hygiene`; IEEE PDF eXpress if required.
8. **Diff for revisions.** `latexdiff old.tex new.tex > diff.tex` for `reviewer-response-tracker`.

## Rules
- Keep the user's source untouched; work in `./work/latex/<project>/`.
- Report the exact command and the first error line when a build fails.
