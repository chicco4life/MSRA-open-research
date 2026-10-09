# Contributing

Everything published here appears on [msralab.com/research](https://msralab.com/research/) automatically, usually within about five minutes. No one needs to touch the website.

## Add a research project

1. Create a folder named `YYYY-MM-short-name`, for example `2026-11-rabbit-gut-health`.
   On GitHub: **Add file → Create new file**, and type `2026-11-rabbit-gut-health/README.md` as the name (typing the `/` creates the folder).
2. Paste the report template below into `README.md` and write the report.
3. Add `sources/sources.csv` in the same folder, one line per source, numbered as in the report.
   Copy the header line from an existing project's `sources.csv`. Wrap any value that contains a comma in double quotes.
4. Add `sources/README.md`: the same studies as a readable table with PubMed and free-full-text links (copy an existing project's file as a starting point).
5. Add a row for the project to the **Projects** table in the main [README](README.md).
6. Click **Commit changes**.

### Report template (`README.md`)

```markdown
---
title: "Your title"
date: 2026-11-02
summary: "One or two sentences shown in the list of projects."
authors: "MSRA Research"
species: [Rabbits]       # any of: Reptiles, Rabbits, Parrots, Cats, Dogs, Birds, Other
---

# Your title

*The same one or two sentences as the summary.*

[Sources used in this project](sources/)

Opening paragraph.

## A section

Text with a citation [1] and another [2].

## Where the evidence stops

Which species the evidence comes from, whether it tested an ingredient or a finished product, and what is still unknown.

## References

1. Surname A, Surname B, et al. 2025. Title of the paper. *Journal*. [PubMed 12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/) · [Free full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/)
2. Surname C. 2024. Title. *Journal*. [DOI 10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
```

## House rules

- Cite every factual claim with a numbered reference that has a PMID or DOI, and list it in `sources/sources.csv`.
- Say which species a study was done in, and whether it tested an ingredient or a finished product.
- If evidence is missing, write "not found". Never fill a gap with a guess.
- Write reports in English.
- No product promises. Reports inform; they are not veterinary advice.

## Suggest something without editing

[Open an issue](https://github.com/chicco4life/MSRA-Open-Research/issues/new) with the study, the project idea, or the correction.
