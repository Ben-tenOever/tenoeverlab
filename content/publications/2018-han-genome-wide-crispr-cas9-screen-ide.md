---
id: 2018-han-genome-wide-crispr-cas9-screen-ide
slug: 2018-han-genome-wide-crispr-cas9-screen-ide
source_pdf: Han_et_al_CellReports2018.pdf
title: Genome-wide CRISPR/Cas9 Screen Identifies Host Factors Essential for Influenza Virus Replication
authors: ["Julianna Han", "Jasmine T. Perez", "Cindy Chen", "Yan Li", "Asiel Benitez", "Matheswaran Kandasamy", "Yoontae Lee", "Jorge Andrade", "Benjamin tenOever", "Balaji Manicassamy"]
first_author: Julianna Han
senior_authors: ["Balaji Manicassamy"]
corresponding_authors: ["Balaji Manicassamy"]
tenoever_position: 9
tenoever_role: middle
year: 2018
journal: Cell Reports
volume: "23"
issue: "2"
pages: "596-607"
doi: 10.1016/j.celrep.2018.03.045
pmid: "29642015"
pmcid: PMC5939577
publication_type: methods/resource
declared_conflicts: null
contribution_character: collaborative
research_areas: [innate-immune-signaling, programmable-virology]
themes: [homeostatic-repression-of-isgs, in-vivo-screening-through-fitness]
pathogens: [influenza A virus, vesicular stomatitis virus, Zika virus, encephalomyocarditis virus]
viral_families: [Orthomyxoviridae, Rhabdoviridae, Flaviviridae, Picornaviridae]
biological_systems: [A549 cells, Cas9-expressing A549 clonal line, CRISPR knockout clonal lines]
host_species: [human]
technologies: [genome-wide CRISPR knockout screening, GeCKO library, lentiviral transduction, MAGeCK analysis, deep sequencing, beta-lactamase virus-like particle entry assay, lectin staining, flow cytometry, luciferase promoter reporter assay, quantitative RT-PCR, cDNA complementation]
key_concepts: [host factor discovery, positive selection survival screen, sialic acid biosynthesis, CMP-sialic acid transport, viral receptor expression, cell-intrinsic immunity, transcriptional repression of interferon-stimulated genes, capicua and ATXN1 corepressor, pan-proviral versus virus-specific factors]
keywords: [CRISPR screen, GeCKO, influenza A virus, SLC35A1, capicua, CIC, JAK2, PIAS3, sialic acid, H5N1]
---

## Citation

Han J, Perez JT, Chen C, Li Y, Benitez A, Kandasamy M, Lee Y, Andrade J, tenOever B, Manicassamy B. Genome-wide CRISPR/Cas9 Screen Identifies Host Factors Essential for Influenza Virus Replication. Cell Reports. 2018. Volume 23, issue 2, pages 596-607.

DOI 10.1016/j.celrep.2018.03.045. PMID 29642015. PMCID PMC5939577.

## One-sentence contribution

A survival-based genome-wide CRISPR knockout screen in human lung epithelial cells selected with an avian H5N1 isolate recovers sialic acid biosynthesis and transport as the dominant requirement for influenza entry, with the CMP-sialic acid transporter SLC35A1 as the top hit, and identifies the transcriptional repressor capicua as a negative regulator of cell-intrinsic immunity.

## Executive summary

Influenza A virus emerges repeatedly from animal reservoirs, seasonal vaccines do not cover zoonotic strains, and drug resistance arises quickly, which has motivated interest in host-directed intervention. Multiple genome-wide screens using interfering RNA, proteomics and insertional mutagenesis had been performed, but meta-analyses found little overlap between them. This study applied a pooled CRISPR knockout library to human lung epithelial cells and selected survivors through repeated lethal infection with a human isolate of a low-pathogenic avian H5N1 virus, which enriches for cells that cannot support the virus rather than scoring a reporter. Two selection regimes were run, one with minimal expansion between rounds and one allowing expansion, and their overlap was used to prioritise candidates. Guide RNAs targeting sialic acid biosynthesis, nucleotide sugar transport, glycan processing and GPI anchor synthesis were enriched, along with vacuolar ATPase subunits that previous screens had also found. Eleven candidates were knocked out individually and seven taken to clonal lines. The top hit, SLC35A1, proved essential for surface sialic acid, hemagglutinin binding and viral entry, and its loss did not affect vesicular stomatitis virus. Capicua, a DNA-binding transcriptional repressor not previously connected to antiviral immunity, restricted influenza together with three unrelated viruses when deleted, raised baseline and infection-induced antiviral gene expression, and repressed interferon-stimulated gene promoters when expressed with its corepressor.

## Scientific context

Host-directed antiviral strategies require knowing which cellular genes influenza depends on, and by 2018 at least nine genome-wide screens had addressed that question using small interfering RNA, proteomic and insertional mutagenesis approaches. The paper notes that these efforts converged on relatively few common hits, most consistently members of the vacuolar ATPase family, and that meta-analyses found little overlap otherwise, which the authors attribute to differences in virus strain, time point and functional readout. CRISPR/Cas9 had recently made genome-scale gene disruption feasible in mammalian cells, and pooled knockout libraries had begun to be applied to virus-host questions in other systems. The rationale given for adding another screen is that a different perturbation modality with a different readout should both surface new factors and independently test previously reported ones. Separately, capicua was known as a conserved DNA-binding transcriptional repressor acting with the corepressor ATXN1 or its paralogue, implicated in cancer, neuropathology and autoimmunity, with one prior report of elevated proinflammatory cytokines in mice deficient for its long isoform, but it had not been connected to cell-intrinsic antiviral immunity.

## Central question

Which human genes are required for influenza A virus replication in lung epithelial cells, as revealed by a positive selection screen in which cells lacking a required factor survive lethal infection.

## Experimental strategy

The design rests on survival as the selective pressure, which is what distinguishes it from reporter-based or knockdown-based screens and biases the output towards factors acting early. A clonal Cas9-expressing A549 line was transduced with a pooled library of 65,383 guide RNAs against 19,050 protein-coding genes and 1,864 microRNA precursors at low multiplicity so that most cells carry one guide, and puromycin selection for fourteen days both established the library and removed cells whose disrupted gene is required for viability, so that hits are not simply essential genes. Library composition was verified by sequencing before selection. Two selection schemes were then run in parallel, a stringent one with five consecutive rounds of lethal infection and minimal expansion, and a less stringent sequential one in duplicate that allows expansion between rounds and permits sgRNA representation to be tracked round by round. Running both allows the intersection to be used as the prioritised candidate set, which partly compensates for the replicate divergence that stringent selection produces. Candidate ranking used MAGeCK. Validation moved from polyclonal knockout pools to clonal lines with sequenced target sites, because incomplete disruption in pools understates effects. Specificity was addressed on three axes, across influenza subtypes including H1N1 and H3N2, against an unrelated virus to separate influenza-specific from broadly proviral factors, and by cDNA complementation to exclude off-target explanations. Mechanism was then assigned by stage, using synchronised high multiplicity infection to test single-cycle competence, beta-lactamase virus-like particles bearing either influenza glycoproteins or the vesicular stomatitis virus glycoprotein to isolate entry and fusion, strand-specific quantitative RT-PCR at three and six hours to separate primary transcription from genome replication, and antiviral gene expression under mock and infected conditions.

## Key findings

1. The library was established at roughly 140-fold coverage with 62,659 guides recovered, and 4.2 percent of guides lost during selection, which the authors read as removal of a non-viable population (Figures S1A and S1B).
2. In the sequential screen, guide representation was unchanged after one round and robustly enriched from round two onwards, so selection of a less permissive population requires two rounds of lethal infection (Figure 1B). Replicates correlated at 0.92 at round one and 0.25 or below thereafter, meaning the two replicates diverged at the same point enrichment began, though a common enriched set was still recovered (Figures S1D and S1E).
3. MAGeCK identified 798 enriched genes at round two and 501 at round five. Genes covered by two or more independent guides fell from 161 to 16 across those rounds, which the authors interpret as stringent selection favouring individual guides rather than genes (Figure 1C). The preliminary consecutive screen gave 119 positively selected genes with SLC35A1 ranked first and represented by all three of its guides.
4. Comparison with nine published influenza screens found 33 of 453 round five hits in common, with vacuolar ATPase subunits recovered as in six prior screens, leaving more than 400 genes not previously reported (Figure 1D, Table S2). Pathway analysis returned proton transport and vacuolar acidification alongside N-acetylneuraminate metabolism, GPI anchor biosynthesis, COPII coating, autophagy and JAK-STAT and MAPK signalling (Figure 1E).
5. Of eleven candidates taken forward from the 63 genes shared between screens, eight polyclonal knockouts reduced H5N1 titre by more than 60 percent, and clonal knockouts gave roughly five logs of reduction for SLC35A1 and capicua and more than 80 percent for the rest (Figures 2B and 2C). The gap between polyclonal and clonal results indicates that complete disruption was needed to see the full effect.
6. Across strains, SLC35A1 loss cost more than five logs and capicua loss more than three logs for H1N1 and H3N2 (Figure 2C). Vesicular stomatitis virus was unaffected in SLC35A1 and PIGN knockouts but reduced by more than two logs in capicua knockouts, which the authors use to classify SLC35A1 and PIGN as influenza-specific and capicua, JAK2, PIAS3, C2CD4C and TRIM23 as broadly proviral. PIAS3 showed strain specificity, affecting H1N1 and H5N1 but not H3N2.
7. Virus-like particle assays placed SLC35A1 at entry or fusion, with only 3.6 percent of knockout cells positive for influenza particles, and implicated PIAS3 more modestly at 25 percent, while particles bearing the vesicular stomatitis virus glycoprotein entered all lines normally (Figure 3B).
8. Capicua knockouts took up normal levels of input genomic RNA but showed more than 90 percent reduction in primary nucleoprotein transcription at three hours and about 80 percent reduction in both genomic RNA and messenger RNA at six hours, placing the block between fusion and primary transcription (Figure 3C).
9. SLC35A1 knockouts lost binding of lectins specific for both 2-3 and 2-6 linked sialic acid and failed to bind recombinant H5 hemagglutinin (Figures 4B to 4D). Complementation with SLC35A1 cDNA restored influenza replication without affecting vesicular stomatitis virus, and overexpression in wild-type cells did not increase replication (Figure 4G, Figure S4B).
10. Chemical inhibition of downstream sialyltransferases with a CMP-sialic acid analogue restricted H1N1 and H3N2 but left H5N1 unchanged despite near-complete loss of lectin binding (Figures 4E and 4F). The authors do not resolve this discrepancy.
11. Capicua knockouts made with an independent guide reproduced the phenotype, showed reduced ATXN1L protein and elevated expression of the known capicua-regulated gene ETV4, and restricted H5N1, H1N1, H3N2, vesicular stomatitis virus, Zika virus and encephalomyocarditis virus (Figure 5A, Figures S5B and S5C). Antiviral gene expression was elevated under both mock and infected conditions by RT-PCR and immunoblot (Figures 5B to 5D).
12. Co-expression of capicua with ATXN1 reduced RIG-I-stimulated IFIT1 reporter activity by up to 50 percent and MxA reporter activity by about 40 percent, more than either protein alone (Figure 5E).
13. Capicua protein declined between forty and sixty minutes after H1N1 infection and its messenger RNA fell by about half by sixteen hours (Figures 5F and 5G). The authors present this as consistent with capicua being downregulated to permit antiviral gene induction, and speculate about MAPK-dependent degradation and about viral usurpation of the COP9 signalosome, both explicitly as speculation.

## Mechanistic model

For SLC35A1 the mechanism is well supported and simple. The transporter delivers CMP-sialic acid into the Golgi, its loss removes sialic acid from cell surface glycans in both linkage types, hemagglutinin cannot bind, and the virus does not enter. Loss of entry accounts for the downstream absence of input genome and transcription, complementation restores the phenotype, and an unrelated virus that uses a different receptor is unaffected.

For capicua the study does not establish a mechanism and the paper is careful about this. The data show that capicua loss raises antiviral gene expression at baseline and during infection, restricts four unrelated viruses, and blocks influenza between fusion and primary transcription, and that ectopic capicua with its corepressor suppresses two interferon-stimulated gene promoters under RIG-I stimulation. The authors write that it is possible that capicua suppresses antiviral gene expression through its transcriptional repressor activity, which is the natural reading but is not demonstrated by occupancy at those promoters or by separation of repressor function from the observed phenotype. Whether the antiviral state is the sole cause of the influenza block, and in particular why primary transcription specifically is impaired, is not resolved. The downregulation of capicua during infection is observed, and the routes proposed for it, MAPK-driven degradation and interference through the COP9 signalosome, are labelled by the authors as speculation and left to future work.

For JAK2 and PIAS3 the paper reports discordant observations without resolving them. JAK2 had been implicated in entry in a prior screen, but no entry defect was seen here while genome replication fell, and the authors suggest that raised antiviral gene expression may account for it. PIAS3 shows both an entry defect and increased antiviral gene expression only upon infection, and possible roles in cytoskeletal regulation through SUMOylation and in negative regulation of STAT signalling are offered as untested candidates.

## Conceptual or technical advance

The study shows that a survival-based CRISPR knockout screen returns a different and largely non-overlapping slice of the influenza host factor landscape than the interfering RNA screens that preceded it, recovering the sialic acid biosynthesis, transport and glycan processing pathway as a coherent block rather than as isolated hits. That coherence is itself informative, since it is the pathway rather than any single gene that the screen resolves. The screen also promotes SLC35A1 from a marginal hit in one earlier study to the top-ranked factor with a five log effect, which illustrates how the readout shapes what a screen can see. Independently of influenza, the identification of capicua as a repressor whose loss raises the antiviral set point and restricts viruses from four families opens a line on transcriptional restraint of cell-intrinsic immunity that is not virus specific. The paired stringent and expansion-permitting selection schemes, with their intersection used for prioritisation, are a practical contribution to how such screens can be run given that stringent selection drives replicate divergence.

## Relationship to the broader research program

This is a collaborative paper led by the Manicassamy laboratory at the University of Chicago, with the tenOever laboratory represented by Asiel Benitez in the author list and no author contributions statement in the article to apportion roles further. The point of contact with the tenOever program is the parallel interest in unbiased genetic identification of influenza host factors, and the paper cites the tenOever laboratory's own in vivo RNAi screen that identified MDA5 as a contributor to cellular defence against influenza A virus. Both studies approach the same question with a loss-of-function library and arrive at regulators of cell-intrinsic immunity rather than only at replication machinery, which is a category 3 synthesis visible when the two are read together rather than a claim made in either. The influenza reverse genetics and virology context here also overlaps with the strains and tools used across the corpus.

## Related publications

- Benitez and colleagues, 2015, companion in approach, from the tenOever laboratory. An in vivo RNAi screen for influenza host factors that identified MDA5, cited here among the prior genome-wide screening efforts, and the source of the RNase III deficient cell resources used elsewhere in this corpus.
- Shalem and colleagues, 2014, Sanjana and colleagues, 2014, and Wang and colleagues, 2014, methodological foundation, from other laboratories. Supply the GeCKO library and the pooled screening procedure followed here.
- Li and colleagues, 2014, methodological foundation, from another laboratory. The MAGeCK analysis used to rank enriched genes.
- Brass and colleagues, 2009, Hao and colleagues, 2008, Karlas and colleagues, 2010, König and colleagues, 2010, Shapira and colleagues, 2009, Sui and colleagues, 2009, Ward and colleagues, 2012, Su and colleagues, 2013, and Watanabe and colleagues, 2014, predecessor, from other laboratories. The nine prior genome-wide influenza screens against which the hit list is compared, and the source of the earlier and weaker SLC35A1 and JAK2 observations.
- Tscherne and colleagues, 2010, methodological foundation, from another laboratory. Source of the beta-lactamase virus-like particle entry assay.
- Kim and colleagues, 2015, and Jiménez and colleagues, 2012, predecessor, from other laboratories. Establish capicua as a transcriptional repressor acting with ATXN1 and report elevated proinflammatory cytokines in mice lacking its long isoform, the prior observation most consistent with the immune phenotype found here.

## Limitations and boundaries

The two screen replicates diverged sharply once selection took effect, with correlation falling from 0.92 to 0.25 or below, and the number of genes supported by more than one guide fell from 161 at round two to 16 at round five, so most reported hits rest on a single guide RNA and the screen output should be treated as a candidate list rather than a validated gene set. Only eleven of 63 shared candidates were tested individually and seven taken to clonal lines. One of those clonal capicua lines retained a wild-type allele, which the authors report. Off-target risk was assessed computationally by mismatch analysis rather than experimentally for most lines, though complementation was performed for SLC35A1 and JAK2. All work is in one immortalised human lung epithelial cell line with no primary cells, no differentiated airway model and no animal infection, and a survival-based design is acknowledged by the authors to favour factors acting at early steps, so requirements for assembly, egress or spread would not be recovered. The sialyltransferase inhibitor restricted H1N1 and H3N2 but not H5N1 despite loss of detectable lectin binding, an internal inconsistency the paper notes but does not explain. For capicua no promoter occupancy or direct target is shown, the connection between the raised antiviral state and the specific block at primary transcription is not established, and the proposed mechanisms for its downregulation during infection are labelled speculative. The JAK2 entry result conflicts with a prior report and is left unresolved.

## Audience summaries

### 25 words

Deleting genes across the human genome and selecting cells that survive influenza infection pointed to sialic acid supply for viral entry and to capicua for antiviral control.

### 75 words

A pooled CRISPR knockout library in human lung cells was put through repeated lethal infection with an avian H5N1 isolate, so that cells missing a required host gene survive. Guides against sialic acid biosynthesis, transport and glycan processing were most enriched, with the CMP-sialic acid transporter SLC35A1 ranked first and its loss removing the viral receptor. The screen also found capicua, a transcriptional repressor whose loss raises antiviral gene expression and restricts viruses from four families.

### 150 words

Prior genome-wide screens for influenza host factors overlapped poorly with one another, motivating a different perturbation and readout. A genome-scale CRISPR knockout library was established in human lung epithelial cells and subjected to repeated lethal infection with a human isolate of a low-pathogenic avian H5N1 strain, under two selection regimes whose intersection defined the candidate set. Sialic acid biosynthesis, nucleotide sugar transport, glycan processing and GPI anchor synthesis were enriched along with vacuolar ATPase subunits found in earlier screens. The top hit, SLC35A1, was required for surface sialic acid in both linkages, for hemagglutinin binding and for entry, and its loss did not affect vesicular stomatitis virus. Capicua, a DNA-binding transcriptional repressor previously linked to cancer and neuropathology, restricted influenza together with vesicular stomatitis, Zika and encephalomyocarditis viruses when deleted, raised antiviral gene expression, and repressed interferon-stimulated gene promoters with its corepressor. Most hits rest on a single guide RNA.
