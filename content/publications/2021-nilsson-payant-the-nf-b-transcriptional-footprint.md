---
id: 2021-nilsson-payant-the-nf-b-transcriptional-footprint
slug: 2021-nilsson-payant-the-nf-b-transcriptional-footprint
source_pdf: Nilsson-Payant_et_al_JVI2021a.pdf
title: The NF-κB Transcriptional Footprint Is Essential for SARS-CoV-2 Replication
authors: ["Benjamin E. Nilsson-Payant", "Skyler Uhl", "Adrien Grimont", "Ashley S. Doane", "Phillip Cohen", "Roosheel S. Patel", "Christina A. Higgins", "Joshua A. Acklin", "Yaron Bram", "Vasuretha Chandar", "Daniel Blanco-Melo", "Maryline Panis", "Jean K. Lim", "Olivier Elemento", "Robert E. Schwartz", "Brad R. Rosenberg", "Rohit Chandwani", "Benjamin R. tenOever"]
first_author: Benjamin E. Nilsson-Payant
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Rohit Chandwani", "Benjamin R. tenOever"]
tenoever_position: 18
tenoever_role: senior
year: 2021
journal: Journal of Virology
volume: "95"
issue: "23"
pages: e01257-21
doi: 10.1128/jvi.01257-21
pmid: "34523966"
pmcid: PMC8577386
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [innate-immune-signaling, pandemic-host-response]
themes: [calibration-of-interferon-in-vivo, imbalanced-host-response]
pathogens: [SARS-CoV-2]
viral_families: [Coronaviridae]
biological_systems: [A549-ACE2 cells, HeLa-ACE2 cells, RELA knockout HeLa-ACE2 cells, Vero E6 cells]
host_species: [human]
technologies: [bulk RNA sequencing, single-cell RNA sequencing, ATAC sequencing, transcription factor motif accessibility analysis, small interfering RNA silencing, chimeric VPR transcriptional activators, small-molecule inhibitor dose response, multiplexed ELISA, quantitative RT-PCR, immunofluorescence microscopy, western blotting]
key_concepts: [NF-κB signalling, type I interferon antagonism, imbalanced host response, proviral host dependency, enhancer remodelling, chromatin accessibility, infected versus bystander cells, proinflammatory cytokine induction, transcription factor motif enrichment]
keywords: [SARS-CoV-2, NF-κB, RelA, p65, NF-κB1, p50, type I interferon, ATAC-seq, single-cell RNA-seq, BAY11-7082, MG115, A549-ACE2, COVID-19 inflammation]
---

## Citation

Nilsson-Payant BE, Uhl S, Grimont A, Doane AS, Cohen P, Patel RS, Higgins CA, Acklin JA, Bram Y, Chandar V, Blanco-Melo D, Panis M, Lim JK, Elemento O, Schwartz RE, Rosenberg BR, Chandwani R, tenOever BR. The NF-κB Transcriptional Footprint Is Essential for SARS-CoV-2 Replication. Journal of Virology. 2021. Volume 95, issue 23, article e01257-21.

DOI 10.1128/jvi.01257-21. PMID 34523966. PMCID PMC8577386.

## One-sentence contribution

SARS-CoV-2 infection of human lung epithelial cells engages NF-κB at chromatin, transcriptional, protein and post-translational levels without engaging the type I interferon transcription factors, and loss of p65 or p50 abolishes viral replication in a manner rescued by reconstituting RelA transcriptional activity.

## Executive summary

COVID-19 is characterised by a blunted type I interferon response alongside vigorous cytokine production, an imbalance that had been documented but not explained. Working in clonal A549 lung epithelial cells engineered to express ACE2, the authors mapped the early transcriptional response to SARS-CoV-2 at high temporal resolution and found that the dominant signature from 9 hours after infection onward was tumour necrosis factor alpha signalling through NF-κB, with no significant type I interferon signature and, at the protein level, no phosphorylation of STAT1 or IRF3. Single-cell sequencing separated infected from bystander cells and placed the NF-κB signature predominantly in the infected population. Chromatin accessibility profiling showed that infection opens regions enriched for REL, RELA and NFKB1 motifs and not for IRF3 or IRF7 motifs, with the largest changes occurring at distal regulatory elements rather than promoters. Silencing RelA reduced viral nucleocapsid protein and silencing NF-κB1 abolished it, and infection of RELA knockout cells was rescued by a chimeric RelA DNA-binding domain fused to a VPR transcriptional activator. Four small molecules targeting different steps of NF-κB activation reduced infection. The authors conclude that the inflammatory profile of SARS-CoV-2 infection reflects a viral requirement for NF-κB-driven transcription rather than a failure of viral antagonism.

## Scientific context

The antiviral response is described in the paper as two coordinated strategies, direct restriction through type I interferon and interferon-stimulated genes, and recruitment of immune cells through chemokines. Induction of type I interferon requires concurrent activation of interferon regulatory factors, notably IRF3 and IRF7, together with NF-κB members RelA and p50, while NF-κB alone is sufficient for a large part of the proinflammatory cytokine and chemokine programme. NF-κB differs from the IRFs in that it is activated indirectly, through phosphorylation and degradation of an inhibitor, and in that many cellular stresses beyond pattern recognition receptor engagement can trigger it.

Against that background, SARS-CoV-2 had been reported by the same laboratory and others to inhibit type I interferon signalling selectively while allowing chemokine production to proceed. Many SARS-CoV-2 gene products had been implicated in suppressing the interferon response. What was unresolved is why the cytokine arm remains so active when the virus is evidently capable of dampening host transcriptional responses, and whether that activity is simply an escape from viral control or serves the virus.

## Central question

What is the molecular basis of the imbalanced host response to SARS-CoV-2, in which strong cytokine production coexists with a blunted type I interferon response, and does the transcription factor responsible for the cytokine arm serve the virus rather than the host.

## Experimental strategy

The design moves from description to dependency in three steps, each addressing a limitation of the step before.

Descriptive transcriptomics at high temporal resolution in a clonal ACE2-expressing A549 line establishes the timing and composition of the host response and relates it to viral RNA accumulation, viral protein and double-stranded RNA production. Running the kinetics at several multiplicities of infection, and then repeating at a high multiplicity to synchronise the population, separates responses arising in infected cells from those arising in uninfected bystanders, a confound the authors note explicitly when comparing the two datasets.

Single-cell sequencing then resolves that confound directly, using viral transcript content to classify cells as infected or bystander so the NF-κB signature can be assigned to one population or the other. Chromatin accessibility profiling adds an orthogonal layer, because transcription factor motif enrichment among newly accessible sites reports which factors are acting, independent of the downstream gene expression readout, and distinguishes promoter from distal enhancer remodelling.

Perturbation then tests necessity. Silencing RelA and NF-κB1 separately asks whether either subunit is required, with silencing of the viral nucleocapsid transcript as a positive control for the assay. Because silencing and knockout can have pleiotropic effects, the rescue experiment is the critical control, using a chimeric factor comprising the RelA DNA-binding domain fused to the VPR activator to restore transcription from RelA-accessible enhancers in RELA knockout cells. Parallel IRF3-VPR and GFP-VPR constructs serve as specificity controls and, in the IRF3 case, as a check that driving the alternative arm is restrictive rather than permissive. Finally, four chemically distinct inhibitors acting at different steps of the pathway test whether the dependency is pharmacologically accessible, with paired viability measurement to separate antiviral effect from cytotoxicity.

## Key findings

1. The host transcriptional response tracks viral load and trails it. Differential expression began at 8 hours after infection at a multiplicity of 1 and by 16 hours was robust at all multiplicities, plateauing at 36 hours (Figure 1A), correlating with viral read fraction (Figure 1B) and with nucleocapsid and spike protein (Figure 1C). At high multiplicity the response began between 6 and 9 hours and trailed peak viral replication by roughly 3 hours (Figure 1D and 1E), corroborated by quantitative RT-PCR for subgenomic nucleocapsid and genomic envelope RNA (Figure 1F). Double-stranded RNA was readily detected by immunofluorescence (Figure 1H).

2. The dominant early signature is NF-κB and not interferon. Gene set enrichment identified tumour necrosis factor alpha signalling via NF-κB as the most upregulated set from 9 hours onward (Figure 2A), with induction of CXCL8, CXCL10, CXCL11, CCL20, IL1A and IL6 (Figure 2B and 2C). Only a small subset of interferon-related genes rose, and only at the latest time point (Figure 2D). Quantitative RT-PCR showed NFKBIA induction without MX1 induction (Figure 2E). At the protein level, MX1 was absent and neither STAT1 nor IRF3 was phosphorylated, while IκBα and RelA were phosphorylated (Figure 2F). Secretion of CXCL1, CXCL2, CXCL8, CCL2, CCL20 and IL-6 was confirmed by ELISA (Figure 2G).

3. The NF-κB signature is concentrated in infected cells. Single-cell sequencing classified cells by viral transcript content and confirmed the reported loss of host messenger RNA in infected cells (Figure 3A to 3C). Tumour necrosis factor alpha signalling via NF-κB was enriched in both populations but dominated the infected transcriptome (Figure 3D and 3E). The authors read this as indicating that virus replication itself, rather than paracrine signalling, drives the response.

4. Infection remodels chromatin toward NF-κB-responsive elements. Accessibility increased at CXCL2, NFKBIA and TNF loci (Figure 4A), with the largest changes 20 to 200 kilobases from transcription start sites rather than at promoters (Figure 4B). Newly accessible sites corresponded to previously poised enhancers and newly inaccessible sites to previously active enhancers based on A549 ENCODE histone marks (Figure 4C to 4E). The authors interpret this as repression of normally active enhancers alongside activation of normally poised ones.

5. Motif analysis of opening sites showed enrichment for REL, NFKB1 and RELA and not for IRF3 or IRF7 (Figure 4F). The largest accessibility gains corresponded to NF-κB family binding sites and the largest losses to TEAD pathway sites (Figure 4G), and these changes had a corresponding transcriptional impact (Figure 4H). Enrichment for NF-κB associated genes and enhancers, to the exclusion of interferon signatures, was seen in both the expression and accessibility data (Figure 4I to 4L).

6. NF-κB subunits are required for viral protein production. Silencing RelA significantly reduced nucleocapsid protein and silencing NF-κB1 eliminated detectable nucleocapsid, comparable to directly targeting the viral subgenomic nucleocapsid transcript (Figure 5A). Immunofluorescence quantification across eight biological replicates confirmed a significant loss of nucleocapsid-positive cells after silencing NF-κB1, RelA or nucleocapsid (Figure 5B).

7. The requirement is for NF-κB transcriptional output. RELA knockout HeLa-ACE2 cells supported far less viral protein production than wild-type, and this was rescued by transient expression of a RelA DNA-binding domain fused to the VPR activator (Figure 5C). An IRF3-VPR construct instead inhibited replication and induced IFIT1, consistent with known interferon sensitivity of SARS-CoV-2.

8. Pharmacological inhibition of NF-κB reduces infection. BAY11-7082, MG115, parthenolide and p-xyleneselenocyanate each reduced infected cell number, with no or minimal cytotoxicity at low concentrations (Figure 5D). BAY11-7082 and MG115 reduced viral protein and RNA, with near complete loss under MG115 (Figure 5E and 5F), reduced viral read fraction and NF-κB target gene expression including CXCL2, NFKBIA, JUN and JUNB (Figure 5G and 5H), and BAY11-7082 reduced secreted CXCL5, CXCL8, CCL2 and IL-6 (Figure 5I).

## Mechanistic model

The study establishes a requirement but does not establish the mechanism of that requirement, and the authors say so directly. They state that it remains difficult to deconvolute which NF-κB target gene or genes produce the phenotype, and they note that their data do not exclude an IKK-mediated post-translational modification of viral proteins operating alongside the transcriptional requirement.

What the data constrain is the following. Virus replication generates signals sufficient to activate IKK and drive IκBα phosphorylation and NF-κB nuclear translocation, since the signature is concentrated in infected cells and its kinetics depend on viral load. NF-κB engages cognate distal enhancers and drives a cytokine programme, while the IRF arm is not engaged at motif, transcript or protein level. Loss of either p65 or p50 blocks viral protein accumulation, and restoring transcription from RelA-accessible enhancers with a heterologous activator restores replication, which places the requirement at the level of NF-κB-driven gene expression rather than at the level of the NF-κB protein itself performing some non-transcriptional function.

What the data do not constrain is the identity of the required gene or genes, and the specific viral trigger for IKK activation. On the latter the authors offer a proposal rather than a demonstration, suggesting that accumulating pathogen-associated molecular patterns such as viral double-stranded RNA or misfolded proteins induce a cellular stress response that converges on IκBα degradation. They also note that a strong NF-κB response carries costs for the virus by recruiting immunity, so the dependency they describe is presented as explaining why the virus tolerates that cost.

## Conceptual or technical advance

The work reframes the inflammatory profile of COVID-19 as a consequence of a viral dependency rather than as a failure of viral immune evasion, which makes the cytokine arm and the replication arm two readouts of the same requirement and predicts that blocking one blocks the other. The chimeric transcription factor rescue is the element that makes the claim interpretable, because it separates loss of an NF-κB protein from loss of NF-κB-driven transcription. Practically, the observation that four mechanistically distinct NF-κB inhibitors reduce replication in vitro identifies a host pathway whose targeting would in principle suppress both replication and the inflammatory response at once, while the authors themselves note the absence of FDA-approved NF-κB inhibitors and the pathway's central role in cell survival and proliferation as obstacles.

## Relationship to the broader research program

The study builds directly on the laboratory's earlier characterisation of the imbalanced host response to SARS-CoV-2, cited here as reference 18, which reported suppression of type I interferon alongside preserved chemokine production. The present work supplies a transcription factor level explanation for that pattern. The A549-ACE2 system, the paired RNA sequencing and quantitative RT-PCR readouts and the emphasis on separating infected from bystander responses recur across the laboratory's SARS-CoV-2 work.

Category 3 synthesis. The discussion notes that influenza A virus has also been reported to depend on NF-κB, with the mechanism unclear, which positions this paper within a broader recurring question in the corpus about whether respiratory RNA viruses co-opt inflammatory transcription for their own replication. Establishing that as a cross-paper claim requires the influenza records alongside this one.

## Related publications

- Blanco-Melo and colleagues, 2020, predecessor. Cited here as reference 18 for the imbalanced host response to SARS-CoV-2, the observation this study seeks to explain mechanistically, and as the source of the plaque assay protocol used here.
- Nilsson-Payant and colleagues, companion work on the A549-ACE2 system, methodological foundation. The ACE2-expressing A549 line used throughout is cited to prior description by this group.

## Limitations and boundaries

The mechanistic claim is bounded to transformed human cell lines, principally clonal A549 cells engineered to overexpress ACE2, with the rescue experiment in HeLa cells similarly engineered, and no primary human airway or organoid system is used here. The authors state in the discussion that they were unable to recapitulate the in vivo NF-κB inhibitor effect reported for influenza when they tested SARS-CoV-2 in their hamster model, so the requirement is demonstrated in vitro only. Only one viral isolate is used, USA-WA1/2020, and no variants are tested. The required NF-κB target gene or genes are not identified, and the authors note that an IKK-mediated post-translational effect on viral proteins is not excluded. The trigger for NF-κB activation is proposed rather than shown, and the paper offers no experiment discriminating double-stranded RNA sensing from misfolded protein stress or other stress inputs. The small molecules used are broadly acting rather than NF-κB specific, and MG115 in particular is a proteasome inhibitor with effects well beyond IκBα stability, so the pharmacology supports the genetic result rather than standing alone. Time points are largely 24 hours after infection for the perturbation experiments, which does not address later or persistent infection. Readouts of replication are principally viral protein, viral RNA and infected cell fraction rather than infectious titre.

## Audience summaries

### 25 words

SARS-CoV-2 switches on the inflammatory factor NF-κB rather than the antiviral interferon programme, and the virus needs that NF-κB activity to replicate in human lung cells.

### 75 words

Severe COVID-19 combines weak interferon responses with strong inflammation. In human lung epithelial cells, SARS-CoV-2 infection turned on NF-κB across chromatin, gene expression and protein readouts while leaving interferon transcription factors inactive. Removing either NF-κB subunit stopped the virus making protein, and restoring NF-κB-driven transcription with an engineered activator restored infection. Several drugs targeting the pathway also suppressed the virus. The inflammation therefore appears to reflect something the virus requires, not something it failed to block.

### 150 words

High-resolution kinetics of SARS-CoV-2 infection in ACE2-expressing A549 cells showed a host response beginning between 6 and 9 hours, trailing peak viral RNA by about 3 hours, and dominated by tumour necrosis factor alpha signalling through NF-κB with no significant interferon signature and no STAT1 or IRF3 phosphorylation. Single-cell sequencing placed that signature predominantly in infected rather than bystander cells. ATAC sequencing showed remodelling concentrated at distal regulatory elements, with opening sites enriched for REL, RELA and NFKB1 motifs and not IRF3 or IRF7, and with previously poised enhancers gaining accessibility as previously active ones lost it. Silencing RelA reduced and silencing NF-κB1 eliminated nucleocapsid protein, and infection of RELA knockout cells was rescued by a RelA DNA-binding domain fused to a VPR activator, whereas an equivalent IRF3 construct restricted the virus. Which NF-κB target genes are required was not determined, and the work is in vitro.
