# Ruomeng Ding CV

- `ruomeng_cv.tex`: main academic CV.
- `publications.bib`: publication entries, including ADE, WAPA, and SpecEval.
- `resume.cls`: shared layout class.
- `resume_visa.tex`: separate visa version; not updated in this revision.

From the repository root, compile with Tectonic (runs BibTeX automatically):

```sh
mkdir -p output/pdf
tectonic Resume_RuomengDing/ruomeng_cv.tex --outdir output/pdf
```

Alternatively, from this folder, run `latexmk ruomeng_cv.tex` with XeLaTeX and BibTeX installed. The included `latexmkrc` selects XeLaTeX.

The CV uses the LaTeX `sourcesanspro` package with semibold headings, matching the original Source Sans Pro font. Tectonic downloads the package and fonts automatically; other TeX installations need this package installed.

The output is `output/pdf/ruomeng_cv.pdf`. The website's existing `files/Resume_RuomengDing.pdf` is not automatically overwritten.
