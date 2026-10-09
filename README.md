# MSRA Open Research

**MSRA stands for Mystical Species Research Academy.** We are an AI-powered deep research lab for animal health and nutrition. This repository is our open knowledge base: every research project we run, published in full with every source behind it, for anyone to read, check and reuse.

**Website:** [msralab.com](https://msralab.com) · **Research on the website:** [msralab.com/research](https://msralab.com/research/)

## What we do

We research nutrition and health for every species, especially the exotic pets that science and the pet industry tend to overlook: reptiles, rabbits and small mammals, parrots and other birds, and the less-studied needs of cats. We believe every species and every condition deserves the same standard of care.

## Our goals

- **Make the evidence findable.** Bring together what is actually known about the health of overlooked species, in one place, in plain language.
- **Be honest about its limits.** Say which species a study was done in, whether it tested an ingredient or a finished product, and where no evidence exists.
- **Publish everything.** Each project comes with its full report and every source it used. Corrections stay visible in the history.
- **Turn research into care.** We use what we learn to build dedicated, species-specific products, and we show the evidence for each one.

## How we do it

1. **Start from real problems.** We read what owners describe in reviews, forums and vet threads, and rank problems by how deep the need is and how poorly it is served.
2. **AI-powered research, human judgement.** Our research system searches and cross-checks the peer-reviewed literature at a scale a traditional team cannot. Our team reviews every claim before it is published.
3. **Safety first.** For any ingredient, toxicity in the target species is checked before efficacy.
4. **Every claim has a source.** Each reference carries a PubMed ID or DOI. Where we find no evidence, we write "not found" rather than fill the gap.
5. **Lab-tested.** Our in-house research facility tests raw materials and finished products for identity, potency, contaminants and stability.

## Projects

| Project | Published | Species |
|---|---|---|
| [How we researched our first six products](2026-10-first-six-products/) · [中文](2026-10-first-six-products/README.zh.md) | 2026-10-09 | Reptiles, rabbits, parrots, cats |

## How this repository is organised

Each folder is one research project. Every project has the same shape:

```
2026-10-first-six-products/
├── README.md          the research report
├── README.zh.md       the report in Chinese (when available)
└── sources/
    ├── sources.csv    every source the report cites, numbered as in the report
    └── README.md      what each column means
```

Open a project folder to read its report. Open `sources/sources.csv` to see its sources as a searchable table, with links to PubMed and to free full text where it exists.

## Use and cite

Our reports and source lists are licensed under [CC BY 4.0](LICENSE): share and adapt them freely, with credit.

> MSRA Open Research (2026). *How we researched our first six products.* https://github.com/chicco4life/MSRA-Open-Research

The studies we list belong to their authors and publishers. We link to them; we do not host copies.

## Contribute

- **Suggest a study or a correction:** [open an issue](https://github.com/chicco4life/MSRA-Open-Research/issues/new).
- **Add a project:** see [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

These reports summarise published research for information. They are not veterinary advice; talk to a vet about your animal.

---

### 中文简介

MSRA（Mystical Species Research Academy，神奇物种研究院）是一家 AI 驱动的深度研究机构，专注动物健康与营养。我们研究每一个物种的营养与健康，尤其是被科学与宠物行业忽视的异宠。本仓库是我们的开放知识库：每个文件夹是一个研究项目，包含完整的研究报告和全部参考文献，任何人都可以阅读、核查和引用。官网：[msralab.com](https://msralab.com)
