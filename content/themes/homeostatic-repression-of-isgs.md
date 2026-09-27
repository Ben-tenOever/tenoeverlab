---
id: homeostatic-repression-of-isgs
area: innate-immune-signaling
name: Homeostatic Repression of Interferon-Stimulated Genes
question: What holds the antiviral program off when there is no infection?
publications:
  - 2025-manivasagam-transcriptional-repressor-capicua-
  - 2018-han-genome-wide-crispr-cas9-screen-ide
---

## The scientific problem

An antiviral program that is expensive to run and damaging when misdirected has to be held off most of the time. The safeguards described in the literature act almost entirely before transcription, on the sensing and signalling machinery, through suppression of receptor components, post-translational modification, or editing of endogenous double-stranded RNA by ADAR1 so that MDA5 is not engaged. Interferon and interferon-stimulated gene promoters themselves were treated as sitting in a default off state, waiting for an activated interferon regulatory factor or for ISGF3, with FOXO3 repression of the Irf7 promoter as the noted exception.

That account leaves a question unasked. If these loci are unoccupied rather than actively silenced, why is basal expression as low as it is in cells constantly generating host-derived double-stranded RNA. The problem is whether a DNA-binding repressor sets the resting state, and if one does, how it is removed when a virus arrives.

## What this laboratory contributed

Both publications carry the contribution character `collaborative`, and both were led by the Manicassamy laboratory. Han 2018 was published from the University of Chicago with Balaji Manicassamy as corresponding author, with the tenOever laboratory represented by Asiel Benitez in the author list and no contributions statement apportioning roles further. Manivasagam 2025 has Priya Issuree and Balaji Manicassamy as corresponding authors and records the tenOever contribution under investigation alongside Maryline Panis of the same laboratory. The discovery belongs to those groups. What the tenOever program supplies is the adjacent question, pursued independently elsewhere in this area, of which factors set the interferon-stimulated gene program and how much of it can run without interferon signalling.

Han 2018 is where the repressor appears, as a by-product of a screen built for another purpose. A pooled CRISPR knockout library in human lung epithelial cells was put through repeated lethal infection with an avian H5N1 isolate, so that cells missing a required host factor survive. The dominant signal was sialic acid biosynthesis and transport, with the CMP-sialic acid transporter SLC35A1 ranked first and required for surface sialic acid, hemagglutinin binding and entry. Capicua, a conserved HMG-box repressor previously studied in development, cancer and neurodegeneration, came out of the same screen with a different signature. Its loss restricted influenza A virus and also vesicular stomatitis, Zika and encephalomyocarditis viruses, raised antiviral gene expression under both mock and infected conditions, and co-expression with the corepressor ATXN1 suppressed IFIT1 and MxA reporters. Capicua protein fell between forty and sixty minutes after infection. The paper is careful that no mechanism is established, since no promoter occupancy was shown, and the routes proposed for the downregulation are labelled speculation.

Manivasagam 2025 develops that observation into a mechanism. Knockouts of capicua and of its obligate partner ATXN1L in human lung epithelial cells raised interferon and interferon-stimulated gene transcripts under mock conditions and during infection and restricted influenza A virus, reproduced by knockdown in primary human airway basal cells and by conditional knockout in mice. The basal signal required MAVS, which the authors read as tonic RIG-I-like receptor engagement by host-derived ligands. ATAC sequencing showed matching increases in chromatin accessibility, and reporter work with native and mutated CIC binding site motifs, together with a synthetic capicua in which the repressor domain is replaced by VP16 repeats, established motif dependence in both directions. Removal is fast and specific. The complex is degraded by the proteasome within forty minutes of synchronised infection, before genome replication, through EGFR-MAPK signalling, reproduced by recombinant hemagglutinin or by EGF alone and blocked by MEK or ERK inhibition. Capicua knockout mice lost less weight, carried 5 to 50-fold lower lung viral burden and showed smaller areas of inflammation.

## How the work evolved

The line is short and runs in one direction, from an unexplained hit in a 2018 screen to a characterised repressor in 2025, with a seven-year gap and no intervening publications in this corpus. The decisive additions in 2025 are motif dependence, a chromatin-level readout, genetic placement of the basal signal on MAVS, and the degradation mechanism, which converts an observation that capicua levels fall during infection into a receptor-to-proteasome circuit conserved from Drosophila development.

Real limits remain. Direct occupancy of endogenous loci was not measured in either paper, the motif is the Drosophila consensus applied to mammalian genomes and is carried by 93 percent of the differentially accessible genes, so its discriminating power is open to question, and the functional motif evidence comes from transfected reporters rather than native chromatin. No ubiquitin ligase or ERK substrate site is identified, the panel of viruses failing to trigger degradation is small and unexplained, and the mouse deletion is whole-body rather than lung-restricted. Whether chronic loss of this repression is harmful is raised by the authors as a question rather than tested.

## Supporting publications

- **2018-han-genome-wide-crispr-cas9-screen-ide.** A survival-based CRISPR screen for influenza host factors that recovered sialic acid supply as the dominant requirement and, separately, identified capicua as a repressor whose loss raises the antiviral set point across four virus families.
- **2025-manivasagam-transcriptional-repressor-capicua-.** Places a DNA-binding repressor complex on interferon and interferon-stimulated gene loci during homeostasis and shows it is degraded within minutes of respiratory virus entry through EGFR-MAPK signalling.

## Connections

This theme completes the picture drawn from the activating side in transcription factor selectivity. Schmid 2010 showed that output at an interferon-stimulated response element depends on which activators are present and on the element's sequence, and Manivasagam 2025 adds an independent repressive layer acting through a distinct motif, so a promoter's behaviour reflects both which activators are available and whether the repressor has been removed. That combined reading is synthesis and is not drawn in either paper. The MAVS dependence of basal signalling ties the theme to sensing aberrant RNA, where Paget 2023 addresses the same endogenous double-stranded RNA problem through condensate buffering rather than transcriptional silencing. Han 2018 also belongs to programmable virology through its screening design, and cites the laboratory's own in vivo RNAi screen, Benitez 2015, among prior screening efforts.

## Publications referenced
- 2010-schmid-transcription-factor-redundancy-en
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2023-paget-stress-granules-are-shock-absorber
- 2025-manivasagam-transcriptional-repressor-capicua-
