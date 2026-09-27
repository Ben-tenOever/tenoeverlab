---
id: technologies-and-platforms
name: "Technologies and Platforms"
question: "What does this laboratory build, what does it borrow, and what became possible as a result?"
kind: cross-cutting synthesis
---

## How to read this document

The 63 publication records carry a `technologies` field written independently for each paper, and the 338 distinct strings in those fields have been collapsed into 145 canonical methods, recorded with their surface forms in the [controlled vocabulary](controlled-vocabulary.md) and in `data/vocabulary.json`. What follows groups those methods into families and says, for the ones that matter, what they are, what they made possible, and which papers used them.

A distinction runs through the whole account. Some methods this laboratory built, and several of those were built because a question could not otherwise be asked. Others it adopted, often at scale and often early. Where a platform belongs to a collaborating group, that is stated. The records carry a `contribution_character` field, and the values `collaborative`, `co-led` and `training period` are honoured here.

## Viral engineering

Reverse genetics is the substrate for almost everything else. Twenty-seven records use it, across influenza A virus, Sindbis virus, vesicular stomatitis virus, Sendai virus, dengue virus and poxviruses. On its own it is a standard capability. What distinguishes the work is the set of payloads designed to sit inside it.

**MicroRNA target site insertion** is the method most identified with this laboratory and appears in twelve records. Perez 2009 placed tandem sites for a microRNA inside the nucleoprotein open reading frame of influenza A virus rather than in an untranslated region, which the record notes was forced by influenza messenger RNA architecture and which had the secondary effect of coupling escape to an amino acid cost. Because microRNA expression differs between species and between lineages, one engineered segment yields a virus that grows in eggs and is attenuated in mice. The same cassette then did four further jobs. Langlois 2012 in PNAS restricted influenza replication out of the haematopoietic compartment and read the consequences for interferon induction and CD8 T cell priming. Pham 2012 did the equivalent for dengue virus and showed that dissemination requires replication in cells of haematopoietic origin. Langlois 2013 in Nature Biotechnology, a co-led study, moved the sites into the haemagglutinin segment by duplicating the packaging signal, so that a gain-of-function transmission experiment carries its own containment. Møller 2018 applied it to a herpesvirus genome through BAC recombineering, which decoupled the cell type in which human cytomegalovirus must be grown from the cell type in which an essential gene is to be studied. Nilsson-Payant 2021 in the Journal of Virology used it differently again, to lower nucleoprotein supply during genuine infection without altering the template the polymerase copies.

**Virus-encoded artificial microRNAs** run the same machinery in the opposite direction. Varble 2010 showed that a nuclear RNA virus can carry a primary microRNA hairpin in a spliced transcript, which removed the standing objection that excising a hairpin would destroy the genome. Langlois 2012 in Molecular Therapy extended this to cytoplasmic viruses and to animals. Schmid 2014 in the Journal of Virology turned the arrangement into a delivery vector, and the enabling step there was a complementing MDCK line supplying both haemagglutinin and nucleoprotein, which allowed production of a vector whose own essential nucleoprotein is silenced in the target cell. The associated design features, a **split NS segment 8** with an engineered intergenic insertion site, **2A peptide recoding**, and **replication-incompetent single-cycle vectors**, recur in Chua 2013, Munoz-Moreno 2019 and the tenOever 2019 review.

**Barcoded virus libraries** appear in five records and serve two different purposes. Varble 2014 used a neutral barcode library in replication-competent influenza A virus to make founder population size directly measurable, and the matched library control quantifies how much apparent structure a bottlenecked passage generates on its own. Munoz-Moreno 2019, a collaborative study, used a barcoded library of natural NS1 sequences in one isogenic backbone to build a fitness landscape across hosts. McCune 2020 is led by another laboratory and pairs a barcoded coxsackievirus B3 library with a neutral red replication label, which separates arrival at a site from replication at it.

**Cre-LoxP lineage tracing** from an engineered virus, in Heaton 2014, converts a transient infection into a permanent heritable mark, and pairing it with an inducible diphtheria toxin receptor turns the same label into an ablation experiment. The tenOever 2019 review treats this as the general case, that engineering can convert a virus into a reagent for a host question.

## Small RNA methods

Seventeen records use **small RNA deep sequencing** and fourteen use **small RNA northern blot**, and in this corpus the two are used together because the sequencing is treated as a discovery step and the blot as the claim. Perez 2010 identified svRNA in the sub-40 nucleotide fraction and then supported it with pan-specific and segment-specific probes, primer extension and synthetic 5 prime triphosphorylated mimetics. The same pairing carries the noncanonical biogenesis work of Shapiro 2010 and Shapiro 2012 and the negative results of Backes 2014.

Two reagents built here are worth naming separately. The first is **VP55-mediated ablation of the cellular microRNA pool**. Backes 2012, a co-led study with the Mohr laboratory, established that the poxvirus poly(A) polymerase degrades host microRNAs and that a 3 prime terminal methyl group protects them. Backes 2014 then used a vesicular stomatitis virus armed with VP55 as a fitness experiment, asking not whether virus-derived small RNAs can be detected but whether destroying host small RNAs helps a virus. Aguado 2015 converted the same enzyme into a general tool delivered by adenoviral vector, which removes the microRNA population from terminally differentiated primary cells rapidly and without provoking an antiviral response, and used subtraction to define the stimulus-specific target set.

The second is the **reconstructed antiviral RNAi system**. Benitez 2015 in Cell Reports built slicing-competent silencing out of endogenous vertebrate microRNAs and a target cassette, and showed protection in animals lacking a type I interferon receptor. Aguado 2018 used the same construct as a comparative selective pressure across four virus families, with a reverse-orientation control of identical sequence isolating targeting from insertion burden. Uhl 2023 used it again and found that escape can be supplied by the host, since ADAR1 editing degrades the sequence fidelity that perfect complementarity requires.

Supporting methods in this family include **locked nucleic acid antisense inhibition**, used in Perez 2009, Perez 2010 and Morales 2017, **Argonaute immunoprecipitation**, **post-transcriptional silencing reporter assays**, and genetic panels lacking Drosha, Dicer or Argonaute, which recur across Shapiro 2010, Shapiro 2012, Aguado 2017 and Uhl 2023.

## Functional genomics and screening

**In vivo RNAi screening through viral fitness** inverts the usual screen. Varble 2013 encoded an artificial microRNA library inside Sindbis virus, passaged it in animals and read host gene requirement as the pathogen's own replicative success. Benitez 2015 in Cell Reports applied the same logic to influenza A virus lacking NS1 and recovered MDA5. Both records note the biosafety argument the authors make, that encoding a hairpin is itself attenuating, so selection operates only within an already crippled population.

**Genome-wide CRISPR-Cas9 knockout screening** enters the corpus later and through collaborations. Han 2018, led elsewhere, used a survival-based screen for influenza host factors and recovered the sialic acid biosynthesis and transport pathway as a block. Daniloski 2021 in Cell, co-led with the Sanjana laboratory, screened for SARS-CoV-2 host factors and coupled a validated minipool to **single-cell CRISPR screening with ECCITE-seq**, which is how the cholesterol link was found rather than assumed. Aguado 2018 used a genome-wide screen in a different role, to look for a host contribution to escape.

## Transcriptomics, epigenomics and proteomics

**Bulk RNA sequencing** appears in 32 records and is the single most used readout after quantitative RT-PCR. The corpus shows it deployed in three distinct modes. As comparison, in Blanco-Melo 2020, where one matched panel across six respiratory viruses and four levels of system is what makes the low interferon phenotype interpretable at all. As atlas, in Hoagland 2021, which required identifying and validating the previously unannotated hamster Ifnb1 before the hamster could be read for interferon biology. And as subtraction, in Aguado 2015 and Frere 2022, where a benchmark condition is what separates a virus-specific effect from a general one.

**Single-cell RNA sequencing** appears in four records, and Eriksen 2021 uses it for a purpose bulk work cannot serve, separating what a cell does because it contains virus from what it does because its neighbours do. **ATAC sequencing**, **chromatin immunoprecipitation with CUT&RUN**, and **in situ Hi-C** are each used sparingly and for specific claims, the last in Zazhytska 2022 on neuronal nuclei sorted from human autopsy tissue.

The proteomics in this corpus belongs largely to collaborators. Bouhaddou 2020, from the Krogan collaboration, supplies time-resolved phosphoproteomics converted into inferred kinase activities and then into a ranked compound set. Yaron 2022, with the Cantley laboratory, adds combinatorial peptide substrate specificity profiling and resolves an ambiguous phosphosite cluster into an ordered sequence from measured kinase preferences. Earlier biochemistry in the corpus is more classical, with **in vitro kinase assays** and **electrophoretic mobility shift assays** carrying the IKK and IRF work of Sharma 2003, tenOever 2007, Schmid 2010, Ng 2011 and Schmid 2014 in the Journal of Biological Chemistry. Sharma 2003 and tenOever 2007 fall in the training period and belong to the Hiscott laboratory.

**In vitro reconstitution with purified components** recurs where a cellular result needed to be made mechanistic, in Perez 2012 with purified influenza polymerase, in Aguado 2017 with recombinant RNase III proteins, and in Paget 2023 with a cell-free IRF3 dimerisation assay.

## Animal, organoid and tissue models

The animal work moves from mouse to hamster with the pandemic. Hoagland 2021 established the golden hamster as an interferon-readable model. Horiuchi 2021 then assembled a **hamster immunology toolkit** from cross-reactive antibodies, reporting CXCR3, CXCR5 and Bcl6 as newly usable in the species, along with peptide restimulation, biotinylated antigen probes and a validated adoptive transfer procedure. Oishi 2022 in Cell Reports applies that toolkit across age. Carrau 2023 adds a **serum interferon bioassay** that works without species-specific reagents, together with two independent ways to remove airway priming, one pharmacological and one by route of inoculation.

Three model platforms in the corpus are built by collaborators and used here. Si 2021, from the Ingber laboratory, is an **organ-on-a-chip** with primary human airway epithelium at an air liquid interface over perfused endothelium. Yang 2020, from the Chen laboratory, is a **directed differentiation platform** giving eight genetically matched human cell types and organoids. Zhang 2023, from the Boeke laboratory, is **mSwAP-In genome writing**, which produced the humanised ACE2 mouse that survives infection with unmodified virus.

One tool is unusual enough to note on its own. Oishi 2023 introduced the archaeal kink-turn binding protein L7Ae as a single heterologous protein that occludes orthomyxovirus splicing without disturbing host splicing, which works across three genera of the family. The record carries a declared conflict, since tenOever is a co-founder of Archean Biologics and an author of a patent covering L7Ae commercialisation.

## Imaging and routine assays

**Plaque assay** appears in 31 records and **quantitative RT-PCR** in 36, and neither is informative about the programme beyond confirming that titre and transcript abundance remain the common currency. **Immunofluorescence and confocal microscopy** appear in 18. Histopathology, immunohistochemistry and RNA in situ hybridisation cluster in the animal work of the pandemic period. Electron microscopy appears once, in Bouhaddou 2020, where it documents the branched filopodia.

## What the method inventory does not show

Two absences are worth recording. Structural biology is almost absent, and both Perez 2012 and Nilsson-Payant 2022 state that no structure of the complex they describe exists in the paper. And the small viral RNA reagents built in Perez 2010 and Perez 2012 did not become a continuing platform, appearing afterwards only as a species observed alongside mini-viral RNA in Nilsson-Payant 2021.

## Publications referenced
- 2003-sharma-triggering-the-interferon-antivira
- 2007-tenoever-multiple-functions-of-the-ikk-rela
- 2009-perez-microrna-mediated-species-specific
- 2010-perez-influenza-a-virus-generated-small-
- 2010-schmid-transcription-factor-redundancy-en
- 2010-shapiro-noncanonical-cytoplasmic-processin
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2011-ng-i-b-kinase-ikk-regulates-the-balan
- 2012-backes-degradation-of-host-micrornas-by-p
- 2012-langlois-hematopoietic-specific-targeting-o
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
- 2012-perez-a-small-rna-enhancer-of-viral-poly
- 2012-pham-replication-in-cells-of-hematopoie
- 2012-shapiro-evidence-for-a-cytoplasmic-micropr
- 2013-chua-influenza-a-virus-utilizes-subopti
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2014-backes-the-mammalian-response-to-virus-in
- 2014-heaton-long-term-survival-of-influenza-vi
- 2014-schmid-a-versatile-rna-vector-for-deliver
- 2014-schmid-mitogen-activated-protein-kinase-m
- 2014-shapiro-drosha-as-an-interferon-independen
- 2014-varble-influenza-a-virus-transmission-bot
- 2015-aguado-microrna-function-is-limited-to-cy
- 2015-benitez-engineered-mammalian-rnai-can-elic
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2017-aguado-rnase-iii-nucleases-from-diverse-k
- 2017-morales-sars-cov-encoded-small-rnas-contri
- 2018-aguado-homologous-recombination-is-an-int
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2018-m-ller-mirna-mediated-targeting-of-human-
- 2019-munoz-moreno-viral-fitness-landscapes-in-divers
- 2019-tenoever-synthetic-virology-building-viruse
- 2020-blanco-melo-imbalanced-host-response-to-sars-c
- 2020-bouhaddou-the-global-phosphorylation-landsca
- 2020-mccune-rapid-dissemination-and-monopoliza
- 2020-yang-a-human-pluripotent-stem-cell-base
- 2021-daniloski-identification-of-required-host-fa
- 2021-eriksen-sars-cov-2-infects-human-adult-don
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2021-horiuchi-immune-memory-from-sars-cov-2-infe
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2021-si-a-human-airway-on-a-chip-for-the-r
- 2022-frere-sars-cov-2-infection-in-hamsters-a
- 2022-nilsson-payant-the-host-factor-anp32a-is-required
- 2022-oishi-a-diminished-immune-response-under
- 2022-yaron-host-protein-kinases-required-for-
- 2022-zazhytska-non-cell-autonomous-disruption-of-
- 2023-carrau-delayed-engagement-of-host-defense
- 2023-oishi-archaeal-kink-turn-binding-protein
- 2023-paget-stress-granules-are-shock-absorber
- 2023-uhl-adar1-biology-can-hinder-effective
- 2023-zhang-mouse-genome-rewriting-and-tailori
