---
id: 2019-munoz-moreno-viral-fitness-landscapes-in-divers
slug: 2019-munoz-moreno-viral-fitness-landscapes-in-divers
source_pdf: Munoz-Moreno_et_al_CellReports2019.pdf
title: Viral Fitness Landscapes in Diverse Host Species Reveal Multiple Evolutionary Lines for the NS1 Gene of Influenza A Viruses
authors: ["Raquel Muñoz-Moreno", "Carles Martínez-Romero", "Daniel Blanco-Melo", "Christian V. Forst", "Raffael Nachbagauer", "Asiel Arturo Benitez", "Ignacio Mena", "Sadaf Aslam", "Vinod Balasubramaniam", "Ilseob Lee", "Maryline Panis", "Juan Ayllón", "David Sachs", "Man-Seong Park", "Florian Krammer", "Benjamin R. tenOever", "Adolfo García-Sastre"]
first_author: Raquel Muñoz-Moreno
senior_authors: ["Adolfo García-Sastre"]
corresponding_authors: ["Adolfo García-Sastre"]
tenoever_position: 16
tenoever_role: middle
year: 2019
journal: Cell Reports
volume: "29"
issue: "12"
pages: 3997-4009.e5
doi: 10.1016/j.celrep.2019.11.070
pmid: "31851929"
pmcid: PMC7010214
publication_type: primary research
declared_conflicts: null
contribution_character: collaborative
research_areas: [influenza-genome-regulation, viral-populations-evolution]
themes: [ns1-and-interferon-antagonism, fitness-landscapes]
pathogens: [influenza A virus]
viral_families: [Orthomyxoviridae]
biological_systems: [MDCK cells, A549 cells, HEK293T cells, embryonated chicken eggs, C57BL/6 mouse lung, Stat1 deficient mice, Rag1 deficient mice]
host_species: [mouse, chicken, dog, human]
technologies: [influenza reverse genetics, barcoded virus library, split NS segment design, Illumina deep sequencing, phylogenetic analysis, multidimensional scaling, network and medoid clustering analysis, plaque assay]
key_concepts: [viral fitness landscape, NS1 protein, host tropism, allele A and allele B NS segments, interferon antagonism, within-population competition, convergent and divergent evolution, barcoded library competition assay, STAT1 dependent selection]
keywords: [influenza A virus, NS1, host range, viral fitness, barcoded library, deep sequencing, allele B, type I interferon, STAT1, pandemic risk assessment]
---

## Citation

Muñoz-Moreno R, Martínez-Romero C, Blanco-Melo D, Forst CV, Nachbagauer R, Benitez AA, Mena I, Aslam S, Balasubramaniam V, Lee I, Panis M, Ayllón J, Sachs D, Park MS, Krammer F, tenOever BR, García-Sastre A. Viral Fitness Landscapes in Diverse Host Species Reveal Multiple Evolutionary Lines for the NS1 Gene of Influenza A Viruses. Cell Reports. 2019. Volume 29, issue 12, pages 3997-4009.e5.

DOI 10.1016/j.celrep.2019.11.070. PMID 31851929. PMCID PMC7010214.

## One-sentence contribution

A library of 107 barcoded influenza A viruses differing only in their NS1 sequence, competed in dog cells, human cells, chicken eggs and mice, resolves NS1-driven fitness as a set of divergent and partly convergent evolutionary trajectories rather than a single ordered adaptation gradient.

## Executive summary

The influenza A virus NS1 protein antagonises the type I interferon response through many distinct mechanisms, several of which are strain and host specific. Because NS1 sequences are phylogenetically diverse and because host interaction partners differ between species, NS1 is a plausible determinant of which hosts a given influenza strain can replicate in, but previous work assessed NS1 function mostly one virus at a time. This study places 56 natural NS1 sequences, spanning both allele A and allele B and spanning human, avian, swine, equine, canine, camel and marine mammal isolates from 1954 to 2013, into a common A/Puerto Rico/8/1934 backbone using a split NS segment that separates the NS1 and NEP reading frames and carries a neutral 22-nucleotide barcode. Most sequences were represented by two independently barcoded viruses. The pooled library was used to infect MDCK cells, A549 cells, embryonated chicken eggs and mice, and relative barcode abundance after replication was compared with the input. Fitness varied widely across the library and varied by host. Viruses carrying allele B NS1 were overrepresented in every substrate tested, human H3N2 NS1 viruses were underrepresented everywhere except in human A549 cells, and network analysis identified groups of viruses with similar fitness but substantially different NS1 sequence. Infection of Stat1 deficient mice removed the advantage of several groups, while Rag1 deficiency did not change the profile.

## Scientific context

NS1 is encoded on segment 8 alongside NEP and is a major contributor to influenza A virus pathogenicity. The paper summarises the known repertoire of NS1 activities, including sequestration of double-stranded RNA away from OAS, RIG-I like receptors, PKR and MDA5, direct inhibition of RIG-I and PKR, and interference with host messenger RNA maturation and nuclear export through CPSF30. Several of these activities are strain specific, and not every influenza strain retains all of them, which the authors attribute to functional redundancy. Host interaction partners of NS1 are not identically conserved across species, which opens the possibility that a given NS1 supports replication better in some host species than in others. NS segments fall into two gene pools, allele A and allele B, with sequence identity above ninety percent within a pool and around sixty percent between pools. Allele B is largely avian in origin, and work by Turnbull and colleagues in 2016 had reported that allele B segment 8 does not impose mammalian host restriction, although the individual contributions of NS1 and NEP were not separated in that study. The unresolved question the paper sets up is how NS1 evolution has distributed function across this sequence space and what that implies for host preference.

## Central question

How has the influenza A virus NS1 gene evolved across its phylogenetic lineages with respect to host tropism, and does phylogenetic relatedness among NS1 sequences predict comparable replicative fitness in a given host.

## Experimental strategy

The design converts a question about sequence space into a competition experiment readable by sequencing. Holding the entire viral genome constant except NS1 isolates the contribution of that one protein, and pooling all the viruses into a single inoculum means every variant experiences the same host environment and the same inoculating conditions, which removes the between-experiment variability that limits one-virus-at-a-time comparisons. A modified NS segment separates the NS1 and NEP reading frames so that NS1 can be replaced without altering NEP, which is what allows the fitness readout to be attributed to NS1 rather than to segment 8 as a whole. A neutral 22-nucleotide barcode in the intervening non-coding region gives each virus an identity readable by amplicon sequencing, and representing most NS1 sequences with two distinct barcodes provides an internal control for barcode-specific amplification bias and for rescue-associated variability.

Sequence selection was structured rather than opportunistic, drawing on sequence feature variant type annotation as well as on phylogenetic distance, host, country and year, so that the library samples the observed NS1 sequence space rather than a convenience set. Four host substrates spanning three species plus two cell lines of different species and tissue origin allow host dependence to be separated from intrinsic replicative capacity. Validation layers were built in around the core competition. A four-virus pilot including an RNA-binding-deficient NS1 mutant established that the barcode readout tracks expected fitness. Single-virus infections of three library members tested whether library behaviour is reproduced outside competition. Repeating three of those viruses in an A/Vietnam/1203/04 HALo backbone, phylogenetically distant from H1N1, tested whether the observed differences depend on the rest of the viral genome. Finally, running the library in Stat1 deficient and Rag1 deficient mice partitions the selective pressure between interferon signalling and adaptive immunity.

## Key findings

1. The barcoded library reports fitness as intended. In a four-virus pilot, barcode reads for the RNA-binding-deficient PR8-R38A/K41A NS1 virus fell sharply relative to input and A/Udorn/1972 NS1 fell to a lesser extent, while wild-type PR8 NS1 rose and A/Shanghai/02/2013 NS1 followed (Figure S1C). Profiles were similar at 50 and 100 plaque-forming units per virus, and 100 was used thereafter.

2. Viruses carrying phylogenetically related NS1 behaved similarly across MDCK cells, eggs and mouse lung, and duplicate-barcoded versions of the same NS1 gave concordant abundances (Figure 2A). Two independently prepared libraries gave highly correlated profiles in mouse lung and MDCK cells at 48 hours (Data S1).

3. Fitness is host dependent in a manner specific to NS1 clade. Avian H5N1 NS1 viruses replicated poorly in mouse lung relative to MDCK supernatant and allantoic fluid, human H3N2 NS1 viruses were underrepresented in all three, and NS1 from non-human mammalian H3N8 isolates was overrepresented in MDCK supernatant and allantoic fluid (Figure 2A).

4. Allele B NS1 viruses were overrepresented in every substrate tested, including mouse lung, MDCK cells, allantoic fluid and human A549 cells (Figures 2A, 4B, 4D, 4F, and S2). The authors read this as evidence that allele B NS1, despite avian origin, supports efficient replication across a range of hosts, and note that their split NS design attributes this to NS1 specifically rather than to segment 8 as a whole.

5. Human A549 cells were the only substrate in which human H3N2 NS1 viruses were not underrepresented (Figure S2), which the authors interpret as specific adaptation of human H3N2 NS1 to human cells. Human H1N1 NS1 did not show the same pattern. The authors state in the discussion that their design cannot separate species origin of a cell line from its tissue origin or passage history.

6. Sequence distance and fitness distance are not proportional. Network analysis in mouse lung, MDCK cells and eggs identified clusters of viruses with similar fitness profiles but significantly different NS1 amino acid sequence (Figure 2B to 2D). The authors read this as possible convergent evolution of some NS1 subsets toward host-specific factors.

7. Library ranking is reproduced outside competition, but only in one substrate. Single-virus infection with A/Moscow/2/2007, A/Tasmania/277/2007 or A/Udorn/1972 NS1 recombinants showed no statistically significant replication differences in eggs or MDCK cells, while mouse lung replication matched the library ranking and correlated with differences in morbidity and mortality (Figure 3B to 3E). The authors propose that eggs and MDCK cells offer effectively unlimited replicative resource, so differences emerge only under competition.

8. The observed differences are driven by host rather than by the rest of the viral genome. The same three NS1 sequences in an A/Vietnam/1203/04 HALo H5N1 backbone reproduced the direction of the differences seen in the PR8 library, with differences in eggs and MDCK cells more apparent than in the PR8 context (Figure S3).

9. Selection acts largely through innate immune signalling. Infection of Stat1 deficient mice flattened differences within the library relative to wild-type mice, and the enrichment of allele B NS1 viruses was lost in the absence of STAT1 although those viruses still outperformed the rest of the library (Figures 5 and S5A). H7N9, H9N2 and H10N4 NS1 viruses also gained fitness in Stat1 deficient mice. Human H3N2 NS1 viruses remained underrepresented even without STAT1, which the authors interpret as an NS1-regulated restriction that is independent of interferon. Rag1 deficiency, which removes adaptive immunity, did not alter the library profile (Figures S5B and S6).

10. Fitness trajectories over time fall into distinct patterns. Medoid-based clustering of barcode profiles from days 2 to 5 in wild-type mice grouped phylogenetically related viruses together, with human H3N2 NS1 viruses declining over time and a heterogeneous cluster containing avian H7N9, H9N2, H10N7 and H10N4 NS1 grouping with pandemic H1N1 NS1 viruses and increasing over time (Figure 6A, Data S2). Among the fittest viruses two distinct dynamics were seen, with allele B NS1 viruses high from early on and A/Shanghai/02/2013 and A/Chicken/Rizhao/651/2013 NS1 viruses rising sharply after day 3 to reach comparable levels by day 5 (Figure 6B). The authors propose that this second group confers enhanced fitness under the high inflammatory conditions that develop in mice after day 3, which is offered as a proposal rather than as a demonstrated mechanism.

## Mechanistic model

The study does not establish a molecular mechanism for any of the fitness differences it measures. It is a phenotypic mapping exercise, and the authors are explicit that the appropriate next step is protein interaction work.

What the data do constrain is the level at which selection operates. Because only NS1 varies across the library and because the phenotype is preserved when three representative NS1 sequences are moved into a distantly related H5N1 backbone, the differences are attributable to NS1 rather than to segment 8 as a whole or to interaction with a particular genome constellation. Because the STAT1 deficiency collapses much of the spread but does not eliminate the underrepresentation of human H3N2 NS1, the selective pressure is partly but not entirely interferon signalling, and the authors conclude that an NS1-regulated host factor independent of interferon restricts those viruses in murine lung. Because Rag1 deficiency has no effect at these timescales, adaptive immunity is not the relevant filter.

The interpretive framework the authors propose is that NS1 tropism differences reflect adaptation to particular host factors among the many known NS1 interactors, with NS1 proteins that engage highly conserved partners such as CPSF30 being permissive across hosts and NS1 variants that instead target more sequence-divergent partners becoming host specialised. They offer TRIM25 as an example of such a divergent target. This is presented as a proposal consistent with the fitness data, and the authors caution in the same passage that focusing on a single domain or a set of amino acid changes may not be the right way to explain the phenotypes they observed.

## Conceptual or technical advance

Placing natural sequence variation of a single viral gene into an isogenic backbone and competing the whole set in one inoculum converts a comparative virology question into a quantitative one, and the split NS segment makes that possible for segment 8 by decoupling NS1 from NEP. The result is a fitness landscape for NS1 across several hosts rather than a ranking of a few strains, and it shows that phylogenetic proximity is a poor predictor of shared phenotype in this gene. Practically, the authors present the approach as a way to flag influenza strains whose NS1 supports broad host tropism, which bears on pandemic risk assessment, and note that the same barcoded-library strategy generalises to other viral genes and other viruses with high sequence diversity.

## Relationship to the broader research program

The barcoded influenza library used here descends directly from the method developed in Varble and colleagues in 2014, a tenOever laboratory paper on transmission bottlenecks, and the barcode design, the split NS segment and the sequencing analysis parameters are all cited to that work. The tenOever contribution to the present study sits in that methodological lineage and in supervision. The authors of the contributions statement list tenOever under supervision and under writing review and editing, and the corresponding author and lead contact is García-Sastre, so the work is led by another laboratory with the tenOever laboratory supplying one component.

Category 3 synthesis. The corpus contains other work using barcoded or otherwise individually trackable influenza populations to read selection within a host, including Varble and colleagues in 2014 on transmission bottlenecks. Reading this paper together with those would allow a statement about how within-host population composition is shaped by route, host and gene identity, but that comparison requires those records and is not established here.

## Related publications

- Varble and colleagues, 2014, methodological foundation. The barcoded NS segment design, the barcode generation strategy and the sequencing analysis pipeline used here are taken from that tenOever laboratory study of influenza transmission bottlenecks.
- Benitez and colleagues, 2015, predecessor. Cited here for in vivo RNAi screening identifying MDA5 as a contributor to cellular defence against influenza A virus, work from the tenOever laboratory that bears on the innate sensing pathways NS1 antagonises.
- Turnbull and colleagues, 2016, predecessor. Cited as the report that allele B segment 8 does not restrict mammalian host range, a claim this study revisits at the level of NS1 alone.
- Noronha and colleagues, 2012, methodological foundation. The sequence feature variant type framework used to structure NS1 sequence selection for the library.

## Limitations and boundaries

All viruses share a single genetic backbone, A/Puerto Rico/8/1934, with a partial check in an A/Vietnam/1203/04 HALo backbone for three NS1 sequences only, so the generality of the fitness ranking across the full diversity of influenza genome constellations is untested. Fitness is measured as relative barcode abundance under competition, which is not the same quantity as replicative capacity in isolation, and indeed single-virus infections reproduced the library ranking only in mouse lung and not in eggs or MDCK cells. The authors state explicitly that they cannot distinguish fitness effects arising from the species origin of a substrate from those arising from tissue origin or passage history, using the MDCK and A549 comparison as the example. Host coverage is limited to mouse, chicken embryo, and two cell lines, with no ferret, swine or primary human airway model, and human data come only from an adenocarcinoma cell line. The main competition readout is taken at 48 hours, with time course data in wild-type mice extending only to day 5. Five of the 56 NS1 sequences are represented by a single barcode rather than two, and 107 of 112 intended viruses were rescued. Duplicate-barcode measurements identified as significantly different at a threshold of 0.13 were treated as outliers and excluded from cluster analysis. The study measures fitness phenotype only and does not test any of the candidate molecular explanations the discussion offers, including the CPSF30 and TRIM25 proposals. Weight loss and mortality data are reported for a small selection of viruses rather than across the library.

## Audience summaries

### 25 words

Influenza NS1 genes were swapped into one identical virus backbone and competed across hosts. Closely related NS1 sequences often behaved very differently, and avian allele B NS1 performed well everywhere.

### 75 words

The influenza NS1 protein blocks host antiviral responses, and different influenza strains carry very different NS1 sequences. Fifty-six natural NS1 sequences were placed into an otherwise identical virus, each tagged with a genetic barcode, and the whole pool was grown in dog cells, human cells, chicken eggs and mice. Sequencing revealed which versions thrived in which host. Relatedness on the family tree did not reliably predict shared behaviour, and avian allele B versions replicated well in every host tested.

### 150 words

A pooled library of 107 barcoded influenza A viruses, identical apart from a natural NS1 sequence carried on a split NS segment that leaves NEP unchanged, was used to compete 56 NS1 variants against one another in MDCK cells, A549 cells, embryonated chicken eggs and mice. Relative barcode abundance after replication defined an NS1 fitness landscape for each host. Allele B NS1, largely of avian origin, was overrepresented in every substrate. Human H3N2 NS1 was underrepresented everywhere except in human A549 cells. Network analysis found clusters sharing fitness profiles despite substantial amino acid divergence, indicating that phylogenetic position predicts phenotype poorly for this gene. Loss of STAT1 collapsed much of the spread, while loss of RAG1 did not, placing the selective pressure in early innate immune signalling, though human H3N2 NS1 remained restricted in murine lung even without STAT1. No molecular mechanism for the individual fitness differences is established.
