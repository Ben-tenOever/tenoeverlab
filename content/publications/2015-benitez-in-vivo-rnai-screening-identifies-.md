---
id: 2015-benitez-in-vivo-rnai-screening-identifies-
slug: 2015-benitez-in-vivo-rnai-screening-identifies-
source_pdf: Benitez_et_al_CellReports2015b.pdf
title: In Vivo RNAi Screening Identifies MDA5 as a Significant Contributor to the Cellular Defense against Influenza A Virus
authors: ["Asiel A. Benitez", "Maryline Panis", "Jia Xue", "Andrew Varble", "Jaehee V. Shim", "Amy L. Frick", "Carolina B. López", "David Sachs", "Benjamin R. tenOever"]
first_author: Asiel A. Benitez
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Benjamin R. tenOever"]
tenoever_position: 9
tenoever_role: senior
year: 2015
journal: Cell Reports
volume: "11"
issue: "11"
pages: "1714-1726"
doi: 10.1016/j.celrep.2015.05.032
pmid: "26074083"
pmcid: PMC4586153
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [innate-immune-signaling, programmable-virology]
themes: [sensing-aberrant-rna, in-vivo-screening-through-fitness]
pathogens: ["influenza A virus"]
viral_families: ["Orthomyxoviridae"]
biological_systems: ["A549 cells", "mouse embryonic fibroblasts", "MDCK cells", "HEK293 and 293T cells", "NoDice 293T cells", "mouse lung"]
host_species: ["mouse", "human", "dog"]
technologies: ["influenza A virus reverse genetics", "artificial microRNA library", "in vivo RNAi screening", "small RNA sequencing", "messenger RNA sequencing", "quantitative PCR", "plaque assay", "gene knockout mice", "small interfering RNA transfection"]
key_concepts: ["pattern recognition receptor", "RIG-I-like receptor", "MDA5", "RIG-I", "NS1 antagonist", "interferon-stimulated gene amplification", "OAS and RNase L system", "fitness-based genetic selection", "virus-encoded small interfering RNA", "self-targeting virus"]
keywords: ["influenza A virus", "MDA5", "Ifih1", "RIG-I", "RNAi screen", "artificial microRNA", "interferon", "NS1", "in vivo screening", "OAS"]
---

## Citation

Benitez AA, Panis M, Xue J, Varble A, Shim JV, Frick AL, López CB, Sachs D, tenOever BR. In Vivo RNAi Screening Identifies MDA5 as a Significant Contributor to the Cellular Defense against Influenza A Virus. *Cell Reports* 2015, volume 11, issue 11, pages 1714-1726.

DOI 10.1016/j.celrep.2015.05.032. PMID 26074083. PMCID PMC4586153.

## One-sentence contribution

An attenuated influenza A virus engineered to deliver individual artificial small interfering RNAs enables a fitness-based loss-of-function screen inside an infected mouse, and that screen identifies MDA5 as a contributor to the antiviral response to influenza A virus despite the established role of RIG-I as the sensor that induces interferon beta.

## Executive summary

Loss-of-function screens for host restriction factors have almost all been performed in transformed cell lines and read out indirectly. This work builds a screening platform in which the readout is virus fitness inside an animal. Influenza A virus was attenuated by mutating NS1 so that it can no longer block pathogen pattern detection, and segment eight was modified to carry an artificial microRNA cassette. Each virus in the resulting library is identical at the protein level but encodes a different mouse-specific small interfering RNA against one of one hundred host genes induced by infection. Because the virus is attenuated by the host antiviral response, a virus that silences a gene contributing to that response should gain replicative advantage and rise in the population. The pooled library was given to mice, and after four days the virus populations in lung were sequenced. Viruses targeting the gene Ifih1, which encodes MDA5, were enriched more than fiftyfold in every one of four screens, with one strain rising from about a quarter of a percent of input to roughly a third of output. Follow-up work confirmed the advantage is lost in mice lacking MDA5, that the advantage is not due to an off-target hit on Setd7, and that MDA5 loss does not impair interferon beta induction but does mute induction of a subset of interferon-stimulated genes including OAS isoforms, in a manner linked to RNase L. Silencing MDA5 in human A549 cells reproduced the increased replication and the reduced antiviral gene induction.

## Scientific context

Detection of influenza A virus in most cells had been assigned to RIG-I, which recognises the exposed triphosphate on the ends of the viral genome segments. Two prior studies had asked directly whether an influenza A virus lacking functional NS1 is detected by MDA5 and had concluded that detection is exclusively through RIG-I, a conclusion that rested on transcriptional induction of Ifnb as the readout. Approaches to defining the antiviral repertoire had relied either on large-scale overexpression screens, which cannot implicate multi-subunit effectors whose single components have no activity alone, or on high-throughput small interfering RNA screens, which the authors note are limited to indirect measures of virus output and are not performed in vivo. The laboratory had previously established that influenza A virus can be engineered to make a functional microRNA and that the miR-124 scaffold tolerates sequence substitution, which supplied the technical basis for turning the virus itself into the delivery vehicle for a small interfering RNA library.

## Central question

Which host factors impose significant restriction on influenza A virus replication during a genuine infection in an animal, and can virus fitness under that restriction be used directly as the selection signal in a loss-of-function screen?

## Experimental strategy

The design turns the screen into a competition. Attenuation is imposed by a three-amino-acid substitution in NS1 that impairs double-stranded RNA binding, which removes the virus's principal means of blocking pattern detection and costs it roughly three logs of replication. The NS1 and NEP open reading frames were split to create an insertion point for a hairpin while preserving small viral RNA and NEP levels, both of which matter to the viral life cycle. Because the attenuation is imposed by the host response, silencing a gene that contributes to that response should restore fitness, making enrichment in the population the direct readout. Hairpins were modelled on mmu-miR-124-2 rather than the more commonly used hsa-miR-30a after a side-by-side comparison favoured the former, and were designed with thermodynamic asymmetry so that the intended strand loads into the silencing complex. All small interfering RNAs were made mouse-specific, which both restricts the screen to the animal and addresses biosafety, since the viruses cannot silence the corresponding human transcripts. Validation of the platform proceeded through a self-targeting virus, in which a virus carrying GFP on segment three and an anti-GFP hairpin on segment eight should attenuate itself, with Dicer-deficient cells serving as the control that the effect is small RNA dependent. Follow-up on the screen hit combined mouse genetics, transcriptome profiling of infected fibroblasts, comparison across single and double sensor knockouts, and conventional small interfering RNA silencing in human cells.

## Key findings

1. The split NS1 mutant virus induced strongly elevated Ifnb, Ifit1 and Ifit2 relative to wild-type virus, and this elevation was unchanged when the virus also encoded an anti-GFP hairpin, showing that carrying a small RNA cassette does not itself further attenuate the virus (Figure 1A). Replication was inversely proportional to the induced response, and the difference between mutant and wild-type virus was absent in mice lacking a functional type I interferon receptor (Figure 1, B and C).
2. A virus encoding GFP on segment three together with an anti-GFP hairpin on segment eight attenuated itself and lost nucleoprotein and NS1 expression, whereas the matched virus carrying miR-124 did not. The attenuation was abolished in Dicer-deficient 293T cells (Figure 2). This is direct evidence that silencing occurs within the time course of a productive infection, which the authors note was not obvious given a prior report that NS1-deficient virus triggers ribosylation of the silencing complex.
3. Small RNA sequencing of cells infected with the assembled library showed that 83 percent of hairpins produced only the intended strand, 13 percent both strands, 2 percent only the unintended strand and 2 percent no small RNA, and that virus-derived small RNA abundance was comparable to the most abundant endogenous microRNAs (Figure 3A). Direct silencing was verified for more than ten percent of hairpins at the transcript level and for ISG15 at the protein level (Figure 3, B and C).
4. In four independent in vivo screens, both viruses targeting Ifih1 were enriched more than fiftyfold, and one of them rose from 0.26 percent of the input population to between 26 and 31 percent of output (Figure 4A). More than thirty further host factors were enriched more than twenty-fivefold across all four screens, six of them represented by both of their gene-specific hairpins.
5. Three additional screens using sub-libraries of about eighty hairpins each, with both Ifih1 viruses excluded, selected for viruses targeting Ddx58, the nuclear factor kappa B subunits p50 and p65, and the interferon regulatory factors IRF5 and IRF7. The authors present this as evidence that the platform selects genuine antiviral factors rather than one idiosyncratic winner.
6. The selected Ifih1-targeting virus carried no mutations relative to the parent beyond the engineered hairpin stems, showed no replication advantage in canine MDCK cells where the mouse-specific hairpin cannot act, and gave a modest but significant titre increase over the control virus in wild-type mice at 24 and 48 hours (Figure 4B). No significant difference between the two viruses remained in Ifih1 knockout mice (Figure 4C), and viruses carrying no hairpin at all showed elevated titre in Ifih1 knockout mice when NS1 was non-functional (Figure 4D).
7. The unintended strand of the selected hairpin was a near-perfect match to Setd7, but the virus silenced Ifih1 potently and failed to reduce Setd7 at transcript or protein level, and messenger RNA sequencing confirmed no change in Setd7 between conditions. This argues the fitness gain comes from loss of MDA5.
8. In fibroblasts lacking MDA5, Ifnb induction by the NS1 mutant virus was only moderately reduced and was abolished only in cells lacking both MDA5 and RIG-I, while loss of RIG-I alone abolished it (Figure 5, A and B). The paper therefore agrees with the earlier conclusion that RIG-I is the sensor responsible for interferon beta induction by influenza A virus.
9. Despite intact Ifnb induction, loss of MDA5 reduced Irf7 induction by more than twentyfold and reduced induction of Oas2, Ifit1, Stat1 and Isg15 (Figure 5, C through F). The authors interpret this as MDA5 contributing to amplification of the antiviral state downstream of RIG-I-mediated recognition rather than to sensing itself.
10. Depletion of MDA5 reduced Oas2 transcript by about half in wild-type cells but had no effect in RNase L deficient fibroblasts, and silencing RNase L reduced Oas2 only when MDA5 was present (Figure 5, G and H). The authors read this as crosstalk in which MDA5 enhances the antiviral response through the OAS and RNase L system, and they propose in the discussion that MDA5 may detect the RNA by-products of RNase L cleavage. That proposal is not tested here.
11. Messenger RNA sequencing of fibroblasts infected with the MDA5-targeting virus, and independently of MDA5 knockout cells infected with a hairpin-free virus, showed a common set of virus-induced genes reduced without a defect in interferon beta induction (Figure 6).
12. Transfecting a human-directed small interfering RNA against IFIH1 into A549 cells increased replication of the NS1 mutant virus by about one log at every timepoint, an effect absent with wild-type virus, and reduced IFIT1 induction after treatment with viral pattern RNA and interferon beta (Figure 7). The authors take the loss of phenotype with wild-type virus as further support for NS1 interfering with MDA5 function, which is an interpretation and not a direct demonstration.
13. A virus targeting human RIG-I reduced RIG-I levels and gave about a one log replication increase, and immunoblotting of whole lung showed abundant RIG-I with no detectable MDA5 at baseline. The authors offer high basal RIG-I in vivo as the explanation for why RIG-I-targeting viruses did not dominate the screen.

## Mechanistic model

The study does not establish a mechanism by which MDA5 acts, and the authors are explicit that MDA5 is not directly responsible for type I interferon induction during influenza A virus infection. What the data constrain is the placement of the contribution. RIG-I is required for Ifnb induction and MDA5 is not, yet MDA5 is required for the full induction of a defined subset of interferon-stimulated genes including Irf7, Oas2, Oas3, Ifit1, Stat1 and Isg15, and that requirement translates into measurable restriction of virus replication in mouse lung and in human cells. The genetic interaction between MDA5 and RNase L, in which the effect of each on Oas2 depends on the presence of the other, is a correlation between two perturbations rather than a demonstrated biochemical link. The authors propose that MDA5, being both virus-inducible and interferon-inducible, may detect aberrant RNA species generated during the interferon response itself, including RNase L cleavage products, and they cite work from other groups suggesting MDA5 can displace viral proteins that mask double-stranded RNA and can detect caps lacking 2'O-methylation. None of these candidate ligands is tested here. Similarly, the claim that NS1 antagonises MDA5 rests on the observation that phenotypes present with the NS1 mutant virus disappear with wild-type virus.

## Conceptual or technical advance

The platform is the principal advance. By making the pathogen itself the delivery vehicle for the silencing reagent and by using an attenuation that the host response imposes, the screen converts host gene function into viral fitness and can therefore be run inside an animal with selection over twelve viral generations, without a transformed cell line and without an indirect surrogate readout. The demonstration of a self-inactivating virus establishes that silencing is fast enough to matter within one infection cycle. Biologically, the result reopens a question that had been treated as settled, showing that an interferon-induction readout can miss a sensor's contribution, and it makes MDA5's role in the influenza A virus response testable as an amplification function rather than as a sensing function. The authors also note that the approach cannot be used to enhance wild-type virus pathogenesis, since the selection operates only within a population already crippled by loss of NS1.

## Relationship to the broader research program

The work rests on a line of engineering from the same laboratory in which RNA viruses are built to express small RNAs, and it extends that line from delivery and species-specific attenuation into forward genetics. Its own reference list cites earlier reports from the group on engineered RNA viral synthesis of microRNAs, on influenza A virus small viral RNAs and the transcription to replication switch, on suboptimal splicing timing of infection, on hematopoietic-specific targeting of influenza A virus, and on transcription factor redundancy in induction of the antiviral state. Setting this screen beside the laboratory's later transcriptional profiling of infected tissue and its work on RNA interference as an antiviral pathway would be category 3 synthesis and is not attempted from this paper alone.

## Related publications

- Varble and colleagues, 2010, methodological foundation. Cited as the origin of engineered RNA viral synthesis of microRNAs and of the modified segment eight cloning site used to build the library.
- Shapiro and colleagues, 2012, and Langlois and colleagues, 2012, predecessor. Cited for the finding that influenza A virus infection does not substantially perturb host microRNA levels, which the discussion uses to argue the approach does not itself impair the antiviral response.
- Chua and colleagues, 2013, predecessor. Cited for the constraints on segment eight engineering and for the potency of NS1 antagonism.
- Schmid and colleagues, 2010, conceptual extension. Cited for interferon-independent induction of antiviral genes downstream of IRF activation, the framework used to interpret the Irf7 result.
- Perez and colleagues, 2010, predecessor. Cited for small viral RNA function on segment eight, a constraint the virus design had to respect.

## Limitations and boundaries

The screen surveys one hundred selected host genes chosen for induction by infection and low baseline expression, so it is not genome-wide and cannot speak to constitutively abundant restriction factors. The authors demonstrate this limitation directly with RIG-I, whose high basal level in lung they offer as the reason a RIG-I-targeting virus did not dominate, which means absence from the enrichment list is not evidence of no antiviral role. Selection depends on silencing efficiency, target protein abundance and protein stability, all of which vary between genes and none of which the enrichment magnitude separates. The whole platform requires a virus lacking functional NS1, so the results describe restriction that operates when the principal viral antagonist is disabled, and the phenotypes in human cells were indeed lost with wild-type virus. Some off-target effects were present in the screen output, and the paper only excludes the specific off-target concern for the winning hairpin. The in vivo work uses one mouse-adapted H1N1 strain in one mouse background over four days, with cell culture work in A549, MDCK and fibroblast lines, so the findings do not extend on their own to other influenza subtypes, to other species or to natural infection doses. The MDA5 effect on replication is modest, roughly one log or less, and the link between MDA5 and the OAS and RNase L system is genetic rather than biochemical. The proposed ligand for MDA5 during influenza A virus infection remains undetermined.

## Audience summaries

### 25 words

Influenza viruses carrying individual silencing RNAs were allowed to compete inside mice, and those disabling MDA5 won, revealing a role for this sensor beyond interferon induction.

### 75 words

Screens for host genes that block a virus are usually done in cell lines. Here an attenuated influenza A virus was engineered to carry one silencing RNA each against a hundred host antiviral genes, then the library was given to mice and the winners sequenced. Viruses silencing MDA5 dominated. MDA5 is not needed to switch on interferon beta during influenza infection, but it is needed for the full induction of downstream antiviral genes.

### 150 words

An influenza A virus attenuated by mutation of its NS1 antagonist was engineered so that segment eight carries an artificial microRNA, yielding a library in which each virus silences one of a hundred mouse antiviral genes. Because host restriction is what attenuates the virus, silencing a genuine restriction factor restores fitness, so enrichment after four days in mouse lung is the readout. Viruses targeting Ifih1, encoding MDA5, were enriched over fiftyfold in four independent screens and one came to dominate. The advantage disappeared in MDA5 knockout mice, was not attributable to an off-target match to Setd7, and was reproduced by conventional silencing in human A549 cells. MDA5 loss left interferon beta induction largely intact, consistent with RIG-I being the sensor, but reduced induction of Irf7, OAS isoforms, Ifit1, Stat1 and Isg15. The effect on Oas2 required RNase L. The ligand MDA5 recognises during infection was not determined.
