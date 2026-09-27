---
id: models-for-pandemic-virology
area: pandemic-host-response
name: Models for Pandemic Virology
question: What experimental system gives an answer that transfers to a human being?
publications:
  - 2021-si-a-human-airway-on-a-chip-for-the-r
  - 2023-zhang-mouse-genome-rewriting-and-tailori
  - 2020-yang-a-human-pluripotent-stem-cell-base
  - 2021-hoagland-leveraging-the-antiviral-type-i-in
---

## The scientific problem

Every claim in this area depends on a model, and in early 2020 the available ones were poor in specific, diagnosable ways. African green monkey cells are not human. The human lines in wide use are cancer derived, carry mutations, and in some cases have known defects in innate sensing, which matters because interferon competence is selected against during continuous passage. Neither cell lines nor conventionally cultured primary airway cells form the mucociliary pseudostratified epithelium of the living airway, and organoids do not permit an air liquid interface, epithelial to endothelial cross-talk or recruitment of circulating immune cells. Drugs are applied statically in all of them, so the exposure a patient experiences after oral dosing is absent. Mice are naturally resistant because of coding differences in Ace2, mouse-adapted strains change the virus being studied, and the K18-hACE2 transgenic is uniformly lethal, lacks human regulatory elements around ACE2 and retains an intact endogenous Ace2.

The question is therefore not which model is best but which question each model can answer, and what a result inherits from the system that produced it.

## What this laboratory contributed

Hoagland 2021 carries `lab-led` and is the laboratory's own model-building contribution. Golden hamsters were chosen because an unmodified clinical isolate replicates and causes progressive lower respiratory pathology without host genetic modification. The decisive technical step was making interferon biology legible in the species, since Ifnb1 was unannotated in the hamster genome. A de novo assembly identified a candidate transcript, which was cloned and shown to induce interferon-stimulated genes in hamster but not human cells. Route and dose were then characterised deliberately, with intranasal, ocular, contact and fomite exposure compared and inoculum varied over four orders of magnitude. The resulting longitudinal multi-tissue atlas is what most of the area's animal work was built on.

Yang 2020 carries `collaborative` and was led by the Chen, Evans and Schwartz groups, with the tenOever laboratory supplying the authentic virus infections and the comparison against human lung autopsy material. Its model contribution is a genetically matched panel of non-transformed human cell types and organoids in which tropism questions can be asked side by side, which produced a result a cancer line panel could not, namely a systematic mismatch between receptor expression and permissiveness across lineages.

Si 2021 carries `collaborative` and was conceived and led at the Wyss Institute, with the tenOever laboratory contributing the hamster model and the native virus efficacy testing in vivo. Its argument is about model fidelity rather than any one drug. Validation preceded application, with a perfused bronchial chip reproducing strain-dependent influenza virulence ranking, the dissociation between viral load and inflammatory output seen with H5N1, endothelial disruption without endothelial infection, neutrophil adhesion and transmigration under flow, and both the efficacy and the two-day treatment window of oseltamivir. Only then were drugs dosed at published human maximum plasma concentrations, and the filtering that followed separated candidates which failed on chip and had also failed in trials from candidates which worked on chip and then worked in hamsters.

Zhang 2023 carries `collaborative` and was conceptualized and led by Zhang and Boeke, with Golynker, Fajardo and Carrau performing the infections in high containment and tenOever participating in design and revision. The method overwrites large genomic segments iteratively, scarlessly and biallelically in mouse embryonic stem cells that retain full developmental potential. Mouse Ace2 was replaced with a 116 or 180 kilobase human ACE2 locus, regulatory content included, and the animals reproduced human tissue expression patterns, human-specific splice isoforms including the interferon-stimulated dACE2 variant, and human chromatin accessibility patterns. They were susceptible to unmodified SARS-CoV-2 and survived without weight loss while all K18-hACE2 animals died, and they mounted a spike-reactive antibody response. Human TMPRSS2 was then written biallelically into the same line, and the laboratory's hamster model served as the benchmark.

## How the work evolved

The four studies form an argument about fitness for purpose rather than a progression. A model is chosen so that the response of interest can be seen at all, and each system here is built to make one thing visible. The hamster makes the longitudinal systemic host response visible. The stem cell panel makes lineage-by-lineage permissiveness visible at constant genetic background. The chip makes clinically relevant drug exposure and immune cell recruitment visible. The humanized mouse makes human regulatory and splicing control of an entry factor visible, and supplies a survivable infection in which longer term consequences can be studied, which a uniformly lethal transgenic cannot.

What each system cannot do is equally part of the contribution. The chip work with SARS-CoV-2 used spike-pseudotyped particles throughout, which report entry only and do not replicate, so those data speak to prophylaxis against initial infection rather than therapy, and the authors state that native virus on chip awaits higher containment. Drug absorption into the device and protein binding were not quantified, so delivered concentrations are unknown. The stem cell panel screened permissiveness with a vesicular stomatitis virus particle bearing Spike, used that same reporter rather than authentic virus for its in vivo kidney capsule experiment in an immunodeficient host, contains no immune component, and rests on developmentally immature derivatives. In the hamster, annotation remains incomplete, Ifnb1 was newly assigned by the authors, transcriptomics are bulk so cell type attributions are inferences from marker genes, and young animals that clear the virus and survive represent neither age nor lethal disease. In the humanized mouse, whether the milder disease follows from the roughly seventyfold lower lung ACE2 expression, from the absence of a keratin 18 driven pattern, from human regulatory control or from some combination is unresolved, the two payload lengths differ in both size and expression, each humanized locus reflects one human haplotype, group sizes were four or five per arm, a sex difference in lung viral RNA is unexplained, the hamster comparison rests on a single experiment, and humanizing two entry factors leaves the rest of the animal a mouse.

## Supporting publications

- **2021-hoagland-leveraging-the-antiviral-type-i-in.** Establishes the golden hamster as a system in which interferon biology can be read, with annotated Ifnb1, characterised routes and doses, and a longitudinal multi-tissue atlas.
- **2020-yang-a-human-pluripotent-stem-cell-base.** Led by the Chen, Evans and Schwartz groups. Supplies a genetically matched panel of human cell types and adult organoids for side-by-side tropism comparison.
- **2021-si-a-human-airway-on-a-chip-for-the-r.** Led at the Wyss Institute. Shows that a perfused airway chip dosed at clinically achievable concentrations discriminates among repurposing candidates where static assays do not.
- **2023-zhang-mouse-genome-rewriting-and-tailori.** Led by Zhang and Boeke. Replaces whole mouse loci with their human counterparts including regulatory content, giving a survivable ACE2-humanized COVID-19 mouse benchmarked against the hamster.

## Connections

The hamster platform underwrites interferon as intervention, post-acute sequelae and immunity, age and reinfection, and the specific finding that made the humanized mouse interesting, a survivable infection in an immunocompetent animal, is the same property that made the hamster usable for persistence and memory questions. Si 2021 belongs equally to host factors and druggable signaling, since its output was a drug candidate, and Yang 2020 belongs equally to tropism and permissive tissues, since its output was a permissiveness map. The genome writing method in Zhang 2023 also connects outward to programmable virology in the corpus, where engineering a genome to answer a question rather than to express a product is the recurring approach.

## Publications referenced
- 2021-si-a-human-airway-on-a-chip-for-the-r
- 2023-zhang-mouse-genome-rewriting-and-tailori
- 2020-yang-a-human-pluripotent-stem-cell-base
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2023-carrau-delayed-engagement-of-host-defense
- 2022-frere-sars-cov-2-infection-in-hamsters-a
- 2021-horiuchi-immune-memory-from-sars-cov-2-infe
