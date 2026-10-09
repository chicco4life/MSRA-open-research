# Contributing

Everything published here appears on [msralab.com/research](https://msralab.com/research/) automatically, usually within about five minutes. No one needs to touch the website.

## Add a research note

1. Open the [`notes/`](notes/) folder → **Add file** → **Create new file**.
2. Name it `YYYY-MM-DD-short-title.md`, for example `2026-11-02-rabbit-gut-notes.md` (lowercase, hyphens, no spaces).
   For a Chinese version use the same name ending in `.zh.md`.
3. Paste the template below and fill it in.
4. Click **Commit changes**.

```markdown
---
title: "Your title"
date: 2026-11-02
summary: "One or two sentences shown in the list of notes."
authors: "MSRA Research"
lang: en                 # en or zh
species: [Rabbits]       # any of: Reptiles, Rabbits, Parrots, Cats, Dogs, Birds, Other
translation:             # optional: file name of the other-language version
---

Opening paragraph.

## A section

Text with a citation [1] and another [2].

## References

1. Surname A, Surname B, et al. Title of the paper. *Journal*, 2025. [PMID 12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/) · [Free full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/)
2. Surname C. Title. *Journal*, 2024. [DOI 10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
```

### House rules

- Cite every factual claim with a numbered reference that has a PMID or DOI.
- Say which species a study was done in, and whether it tested an ingredient or a finished product.
- If evidence is missing, write "not found". Never fill a gap with a guess.
- No product promises. Notes inform; they are not veterinary advice.

## Add a study to the library

Edit [`library/studies.csv`](library/studies.csv) and add one line. Column meanings are in [`library/README.md`](library/README.md).
Wrap any value that contains a comma in double quotes.

## Suggest something without editing

[Open an issue](https://github.com/chicco4life/msra/issues/new) with the study, the note, or the correction.
