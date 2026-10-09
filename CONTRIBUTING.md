# Contributing

Everything published here appears on [msralab.com/research](https://msralab.com/research/) automatically, usually within about five minutes. No one needs to touch the website.

## Add a research project

Every project folder has the same shape:

```
2026-11-short-name/
├── README.md        overview for GitHub visitors: summary, key findings, links to the report and sources
├── report.md        the full report, which msralab.com displays
└── sources/
    ├── README.md    every study cited, with PubMed and free-full-text links
    └── sources.csv  the same list as a table, numbered as in the report
```

1. Create a folder named `YYYY-MM-short-name`, for example `2026-11-guinea-pig-vitamin-c`.
   On GitHub: **Add file → Create new file**, and type `2026-11-guinea-pig-vitamin-c/report.md` as the name (typing the `/` creates the folder).
2. Write the report in `report.md` using the template below. Reports are written in English.
3. Add `sources/sources.csv`, one line per source, numbered as in the report.
   Copy the header line from an existing project. Wrap any value that contains a comma in double quotes.
4. Add `sources/README.md` (copy an existing one): the same studies as a readable table, and a link to the report on msralab.com.
5. Add the folder's `README.md` (copy an existing one and change the title, summary, key findings, counts and links).
   The report's address on the website is `https://msralab.com/research/project/?p=<folder name>`.
6. Add a row to the **Projects** table in the main [README](README.md), then run `python3 tools/make_charts.py` to redraw the charts.
7. Commit.

### Report template (`report.md`)

```markdown
---
title: "Your title: what the evidence supports"
label: "Short name for charts"
date: 2026-11-02
summary: "One or two sentences shown on the website's project cards."
authors: "MSRA Research"
species: [Rabbits]       # any of: Reptiles, Rabbits, Parrots, Cats, Dogs, Birds, Other
---

# Your title: what the evidence supports

*The same one or two sentences as the summary.*

## Key findings

- One finding per line, with its citation [1].

## The question

## How we researched it

## …sections on the evidence…

## What the evidence does not show

## What this means for owners

## References

1. Surname A, Surname B, et al. 2025. Title of the paper. *Journal*. [PubMed 12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/) · [Free full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/)
2. Surname C. 2024. Title. *Journal*. [DOI 10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
```

## House rules

- Cite every factual claim with a numbered reference that has a PubMed ID or DOI, and list it in `sources/sources.csv`.
- Say which species a study was done in, and whether it tested an ingredient, a diet or a finished product.
- Report null and negative results as clearly as positive ones.
- If evidence is missing, write that it was not found. Never fill a gap with a guess.
- No brand or company names, and no product promises. Reports inform; they are not veterinary advice.
- Link to studies; do not upload copies of papers.

## Suggest something without editing

[Open an issue](https://github.com/chicco4life/MSRA-Open-Research/issues/new) with the study, the project idea, or the correction.
