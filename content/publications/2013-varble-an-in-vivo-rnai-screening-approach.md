---
id: 2013-varble-an-in-vivo-rnai-screening-approach
slug: 2013-varble-an-in-vivo-rnai-screening-approach
source_pdf: Varble_et_al_CHM2013.pdf
title: An In Vivo RNAi Screening Approach to Identify Host Determinants of Virus Replication
authors: ["Andrew Varble", "Asiel A. Benitez", "Sonja Schmid", "David Sachs", "Jaehee V. Shim", "Ruth Rodriguez-Barrueco", "Maryline Panis", "Marshall Crumiller", "Jose M. Silva", "Ravi Sachidanandam", "Benjamin R. tenOever"]
first_author: Andrew Varble
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Benjamin R. tenOever"]
tenoever_position: 11
tenoever_role: senior
year: 2013
journal: Cell Host & Microbe
volume: "14"
issue: "3"
pages: "346-356"
doi: 10.1016/j.chom.2013.08.007
pmid: "24034620"
pmcid: null
publication_type: methods/resource
declared_conflicts: null
contribution_character: lab-led
research_areas: [programmable-virology]
themes: [in-vivo-screening-through-fitness]
pathogens: [Sindbis virus, influenza A virus]
viral_families: [Togaviridae, Orthomyxoviridae]
biological_systems: [murine embryonic fibroblasts, A549 cells, BHK-21 cells, Hepa 1.6 cells, Vero cells, Zfx conditional knockout primary fibroblasts, Dicer conditional knockout fibroblasts, mouse spleen]
host_species: [mouse, human, hamster]
technologies: [artificial microRNA libraries, alphavirus reverse genetics, in vivo serial passage selection, small RNA deep sequencing, barcoded virus libraries, messenger RNA sequencing, small RNA Northern blotting, multicycle growth curves]
key_concepts: [in vivo RNA interference screening, virus-delivered artificial microRNAs, natural selection as screen readout, host restriction factors, interferon-stimulated genes, RIG-I sensing of alphavirus, transcriptional maintenance of antiviral capacity, barcode control for drift]
keywords: [Sindbis virus, artificial microRNA, RNAi screen, Zfx, Mga, RIG-I, interferon, host factors]
---

## Citation

Varble A, Benitez AA, Schmid S, Sachs D, Shim JV, Rodriguez-Barrueco R, Panis M, Crumiller M, Silva JM, Sachidanandam R, tenOever BR. An In Vivo RNAi Screening Approach to Identify Host Determinants of Virus Replication. Cell Host & Microbe. 2013. Volume 14, issue 3, pages 346-356.

DOI 10.1016/j.chom.2013.08.007. PMID 24034620.

## One-sentence contribution

Replication-competent Sindbis viruses, each encoding an artificial microRNA against one murine open reading frame, turn viral fitness in infected mice into a selection-based screen for host restriction factors, identifying the transcription factors Zfx and Mga as maintainers of antiviral capacity.

## Executive summary

RNA interference screens for host factors affecting virus replication had used cultured, usually transformed, cells with indirect readouts such as reporter activity or surface staining, which restricts them to one cell type and to a nonphysiological infection. This study replaces exogenous delivery of small interfering RNAs with delivery by the pathogen itself. An attenuated mouse-adapted Sindbis virus was configured to express an artificial microRNA on the murine miR-124-2 backbone, and a library of approximately 10,000 such viruses, each silencing one open reading frame, was passaged through mice with recovery from spleen. Because a hairpin that relieves restriction increases the fitness of the virus carrying it, selection itself becomes the readout and viral titer rather than a surrogate is the output. A matched library of 22 nucleotide barcodes, which confer no advantage, controls for drift, and recloning surviving hairpins into a fresh genome between passages removes hitchhiking mutations. Across four parallel screens, hairpins were shared by two or more sets 16-fold more often than barcodes, and enriched hairpins targeted interferon-stimulated genes, homeostatic genes and general transcription factors. Two hairpins recovered in three or more sets targeted Zfx and Mga. Independent silencing, a Zfx conditional knockout and transcriptome profiling showed that loss of either factor reduced interferon beta induction, STAT1, RIG-I and IKK beta, and raised viral titers by about one to one and a half logs. The authors propose that viral fitness may depend on antagonizing broad cellular programs as much as specific antiviral effectors.

## Scientific context

Vertebrate detection of RNA virus infection proceeds through pattern recognition receptors such as RIG-I and MDA5, recruitment of MAVS at the mitochondrion, activation of NF-kB and interferon regulatory factors, assembly of the interferon beta enhanceosome, and induction of hundreds of interferon-stimulated genes. Many of the host factors in this network, and many proviral factors, had been found by high-throughput RNA interference screens against influenza A virus, dengue virus, hepatitis C virus, West Nile virus and human immunodeficiency virus. Those screens share two constraints. They require cell culture, typically a transformed line, and they measure virus output indirectly. Efforts to move to physiological settings had begun to use genetic variation among outbred mice correlated with susceptibility.

In parallel, several groups including this laboratory had shown that RNA viruses of either polarity and of either replication compartment can be engineered to produce functional microRNAs, even though no RNA virus lacking a DNA intermediate has been found in nature to encode a canonical one. The paper brings these two lines together, using virus-encoded artificial microRNAs as the delivery vehicle for a genome-scale silencing library inside a living host.

## Central question

Can a replication-competent RNA virus that delivers its own silencing reagent be used so that natural selection on virus fitness during infection of an animal identifies the host factors that restrict replication.

## Experimental strategy

The logic is that a natural infection generates quasispecies from which the host response selects, and that a library of otherwise identical viruses differing only in an encoded hairpin mimics that process with a defined, readable genotype. Sindbis virus was chosen because it is an attenuated, mouse-adapted, cytoplasmically replicating alphavirus with a duplicated subgenomic promoter into which sequence can be grafted, and because the laboratory had already shown that it processes artificial microRNAs accurately. Hairpins were built by substituting designed 21 nucleotide guides into the murine miR-124-2 backbone, drawing on an existing miR-30 based whole-genome library for the large screens.

Three screens were run in sequence. A small in vitro screen against a subset of interferon-stimulated genes, with two hairpins per open reading frame, tested whether silencing a restriction factor is enough to be selected. A roughly 4,000 hairpin library passaged through mice by footpad injection with recovery from spleen established the timing of enrichment and, through a genetic reset in which surviving hairpins were recloned into the parental genome, established that enrichment tracks the hairpin rather than unrelated mutations. The full screen used approximately 10,000 hairpins in four independent quadruplicate passage series alongside a matched barcode library, with deep sequencing of the amplified hairpin or barcode region after each 48 hour passage. The barcode arm is the control that distinguishes selection from bottleneck-driven drift, and reproducibility across independent sets is the statistic. Hits were then removed from the viral context entirely and tested with independent small interfering RNAs, with overexpression, with a conditional knockout, and with messenger RNA sequencing, so that no conclusion about a host factor depends on the screening vector.

## Key findings

1. Sindbis virus expressing a designed anti-GFP artificial microRNA processed the hairpin accurately at every time point tested and silenced GFP protein during infection, with four of five designed hairpins effective and two producing complete knockdown (Figures 1B and 1C and Figure S1C).
2. In vitro passage of a virus library targeting interferon-stimulated genes positively selected viruses silencing IKK beta and RIG-I (Figure S2A). RIG-I involvement was confirmed outside the virus library, since an independent small interfering RNA enhanced replication and Ddx58 deficient fibroblasts supported more than a log more virus (Figures S2B to S2D). A purpose-built virus silencing RIG-I reduced RIG-I protein and grew about an order of magnitude better than a matched control virus, and this advantage was lost in Dicer-deficient cells, tying the phenotype to microRNA production rather than to the insert (Figures 2B, 2C, S2F and S2G).
3. In mice, deep sequencing of the roughly 4,000 hairpin library showed clear enrichment of particular hairpins by the third passage, and approximately 75 percent of library amiRNAs were processed as predicted (Figure 3A and Figure S3). A genetic reset between passages three and four preserved the population dynamic, which the authors take as evidence that fitness gains track hairpin identity rather than hitchhiking mutations. A recombinant virus carrying the single most enriched hairpin, predicted to target the interferon-stimulated gene USP32, reached titers about one log above control in mouse spleen (Figures 3B and 3C).
4. Across four independent screens with the approximately 10,000 hairpin library, only 0.5 percent of barcoded viruses were shared by two sets and none by three or more, whereas hairpin-bearing viruses showed a 16-fold enrichment for appearing in two or more sets and some appeared in three or more (Figures 4A to 4D and Table S2). Reproducibility therefore exceeds what drift in the barcode arm produces.
5. Enriched hairpins targeted known interferon-stimulated genes annotated as virus response genes, and the only other functional categories enriched more than fivefold by passage three were cellular homeostasis and general transcription (Figure 5A and Table S3). Candidate hairpins found in at least two sets were verified for processing and silencing, and all but one gave a significant titer increase when the target was silenced with an independent small interfering RNA (Figures S4A to S4J).
6. The two hairpins recovered in three or more independent screens target Zfx and Mga, transcription factors previously implicated in self-renewal rather than in antiviral defense.
7. An independent small interfering RNA against Mga raised Sindbis titers by about an order of magnitude, overexpression of Mga reduced replication, and Mga knockdown lowered RIG-I and STAT1 during infection. The effect was not virus specific, being reproduced with an attenuated influenza A virus, with double-stranded RNA, and with type I interferon treatment (Figures 5B and 5C and Figure S5).
8. Primary fibroblasts from Zfx conditional knockout mice supported about 1.5 logs more virus after Cre delivery, with a marked reduction in interferon-stimulated genes and loss of STAT1 (Figures 5D and 5E).
9. Loss of either factor reduced virus-induced Ifnb and Stat1 transcription, but the point of interruption differed. Interferon-driven upregulation of Stat1 was compromised only by Mga knockdown, whereas NF-kB activity after TNF alpha treatment was affected by Zfx and not by Mga (Figures 6A to 6D). Messenger RNA sequencing showed broad loss of the machinery for interferon induction and signaling, with Zfx loss reducing IKK beta and Mga knockdown reducing Irf9, Stat2, Ifnar1, Ifnar2 and Irf7 (Figures 6E and 6F and Table S4).

## Mechanistic model

This study does not establish a mechanism by which Zfx or Mga acts, and the authors say as much. They report that the two factors are required to maintain a transcriptome capable of mounting an antiviral response, and their proposal is that these are indirect determinants, transcriptional maintenance factors whose loss degrades the network rather than antiviral effectors themselves. The epistasis experiments constrain where each one acts. Mga is needed for interferon-driven induction of Stat1, placing its requirement within or upstream of the response to type I interferon, while Zfx is needed for NF-kB activity after TNF alpha, placing its requirement in a distinct arm. Both reduce IKK beta or the interferon signaling components measured. No direct binding, occupancy or target gene assignment is performed here, and the connection to the self-renewal transcriptional module comes from cited work on Zfx and Myc occupancy rather than from data in this paper.

The authors also flag a timing problem they cannot resolve. It is unclear how silencing either factor within a single round of an acute infection provides enough time to remodel the host transcriptome, and they speculate that at least one critical factor must fall within the first six to eight hours, possibly a component of interferon signaling or a potent interferon-stimulated gene. That is explicitly speculation.

The broader reading offered, that pathogenicity may be defined by the capacity to antagonize broad cellular programs rather than specific antiviral factors, is an interpretation of the screen's output distribution. The authors note that it is consistent with how oncolytic virus selectivity is understood, since transformation compromises the same signaling networks.

## Conceptual or technical advance

The screen inverts the usual arrangement. Instead of perturbing cells and then measuring a proxy for infection, the perturbation rides inside the pathogen and the measurement is the pathogen's own replicative success in a living animal, read out by sequencing. That removes the transformed cell line, removes the single cell type, removes the surrogate readout, and allows any cell the virus enters to contribute. It also brings a control that cell culture screens do not usually need, the matched barcode library, which quantifies how much apparent reproducibility a bottlenecked in vivo passage generates on its own.

The platform is portable in a defined way. The authors point out that the same library, with a different inoculation route or a different tissue for recovery, would select for different biology, for example factors involved in crossing the blood-brain barrier if an alphavirus were recovered from brain, and that the approach should extend to questions of tropism, transmission and persistence. They also address biosafety directly, arguing that the approach cannot enhance a natural pathogen because encoding a hairpin is itself attenuating, so selection operates only within a population of equally attenuated viruses.

## Relationship to the broader research program

This paper converts a capability into an instrument. The engineering it depends on, that an RNA virus can be built to produce a functional small RNA without losing replication, comes from the laboratory's earlier work, and the specific proposal to deliver a library of artificial microRNAs from a virus so that evolutionary selection identifies restriction factors was stated in the discussion of the 2012 Molecular Therapy paper. The alphavirus vector and the evidence that Sindbis processes artificial microRNAs come from the laboratory's Sindbis work with Shapiro and colleagues.

Category 3 synthesis. Placed beside Varble and colleagues in 2010 and Langlois and colleagues in 2012, this paper completes a three-step arc from demonstrating that RNA viruses can make microRNAs, to delivering them in animals, to using them as a selectable genetic tool. The recurring interest in the interface between RNA viruses and the host small RNA machinery, and in why RNA viruses do not naturally exploit it, is treated conceptually in the laboratory's later perspective writing, where the attenuating cost of encoding a hairpin is one of the arguments.

## Related publications

- Varble and colleagues, 2010, Engineered RNA viral synthesis of microRNAs, cited here. Predecessor and methodological foundation.
- Shapiro and colleagues, 2010 and 2012, on noncanonical cytoplasmic processing of viral microRNAs, cited here and supplying both the Sindbis platform and the observation that virus-mediated amiRNA production causes low level self-targeting. Methodological foundation.
- Langlois and colleagues, 2012, In Vivo Delivery of Cytoplasmic RNA Virus-derived miRNAs, cited here. Predecessor, and the source of the explicit proposal for this kind of screen.
- Silva and colleagues, 2005, the miR-30 based whole-genome library, cited here with Silva as a coauthor of this paper. Methodological foundation.
- Galan-Caridad and colleagues, 2007, the Zfx conditional knockout, cited here and supplying the mice. Methodological foundation.
- Frolova and colleagues, 2002, on Sindbis nsP2 and interferon, cited here and supplying the nsP2 mutant used for in vitro knockdown work. Methodological foundation.
- tenOever, 2016, The Evolution of Antiviral Defense Systems. Review or synthesis, treating conceptually why RNA viruses do not encode microRNAs in nature.

## Limitations and boundaries

The authors devote a section of the discussion to the constraints of the platform, and they are substantial. The output is the emergence of dominant strains, so the screen is biased toward hairpins that confer an advantage cell-autonomously within an infected cell, and it cannot report on factors acting in uninfected bystanders or on paracrine effects. The advantage a hairpin confers changes with time, since silencing a pattern recognition receptor is worth little once interferon has been induced, and the fitness landscape shifts as the composition of the population shifts. Successful production of an artificial microRNA does not guarantee knockdown of the target protein, off-target silencing can confound the assignment of a hairpin to a gene, and a target protein with a half-life longer than the viral life cycle would show no benefit when its transcript is silenced. These together prevent comprehensive coverage of the transcriptome, and the screen returned only a small number of reproducible hits.

Results are specific to what was selected on. All in vivo selection used footpad inoculation of an attenuated mouse-adapted Sindbis virus in C57BL/6 mice with recovery from spleen at 48 hours, so the hits reflect splenic replication in an acute alphavirus infection and not neurotropic disease, other routes, other tissues, other viruses, other mouse genotypes or other species. The authors note that the screen recovered relatively few interferon-stimulated genes, and offer two competing explanations, that Sindbis nsP2 already antagonizes them and so biases the output, or that broadly acting host genes matter more, without resolving which applies. Target assignment for enriched hairpins is computational, based on free energy prediction, so a predicted target such as USP32 for the most enriched hairpin in the small screen is a prediction rather than a validated target. The mechanistic follow-up on Zfx and Mga is largely in cell culture, uses transcript and protein abundance rather than direct transcription factor assays, and does not test whether the in vivo fitness advantage of those hairpins operates through the pathways mapped in vitro. Finally, the connection drawn between the screen output and pathogenicity is an interpretation, since no pathogenesis measurement is reported.

## Audience summaries

### 25 words

Viruses were made to carry their own gene-silencing reagents, so that surviving best in infected mice revealed which host genes had been holding infection back.

### 75 words

Screens for host genes that limit virus infection normally use cultured cells and indirect readouts. Here roughly 10,000 Sindbis viruses, each silencing one mouse gene, were passaged through mice, letting the virus's own replication do the selecting. Barcoded control viruses showed the enrichment was real. Hits included known interferon-stimulated genes and, unexpectedly, the transcription factors Zfx and Mga, whose loss degraded interferon signaling and allowed substantially more virus growth.

### 150 words

Conventional RNA interference screens for virus host factors require transformed cells and surrogate readouts. This work delivers the silencing reagent from inside a replication-competent alphavirus, so that a hairpin relieving host restriction increases the fitness of the virus carrying it and selection during infection of mice becomes the assay. Approximately 10,000 artificial microRNA viruses were passaged by footpad injection with recovery from spleen, alongside a barcode library that controls for drift and with recloning between passages to remove hitchhiking mutations. Hairpins were shared across independent screens 16-fold more often than barcodes. Enriched hairpins targeted interferon-stimulated genes, homeostatic genes and general transcription factors, and the two most reproducible targeted Zfx and Mga. Independent silencing, a conditional knockout and transcriptome sequencing showed that losing either factor collapses parts of the interferon induction and signaling machinery and raises viral titers, with Mga required for interferon-driven Stat1 induction and Zfx for NF-kB activity.
