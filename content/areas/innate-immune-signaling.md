---
id: innate-immune-signaling
name: Innate Immune Signaling and the Interferon Response
question: What determines which genes the interferon system turns on, how strongly, and for how long?
themes:
  - ikk-kinases-and-irf-activation
  - transcription-factor-selectivity
  - homeostatic-repression-of-isgs
  - interferon-and-cell-identity
  - sensing-aberrant-rna
  - calibration-of-interferon-in-vivo
publications:
  - 2003-sharma-triggering-the-interferon-antivira
  - 2007-tenoever-multiple-functions-of-the-ikk-rela
  - 2010-schmid-transcription-factor-redundancy-en
  - 2011-ng-i-b-kinase-ikk-regulates-the-balan
  - 2012-langlois-hematopoietic-specific-targeting-o
  - 2014-heaton-long-term-survival-of-influenza-vi
  - 2014-schmid-mitogen-activated-protein-kinase-m
  - 2015-benitez-in-vivo-rnai-screening-identifies-
  - 2016-tenoever-the-evolution-of-antiviral-defense
  - 2018-han-genome-wide-crispr-cas9-screen-ide
  - 2019-eggenberger-type-i-interferon-response-impairs
  - 2020-blanco-melo-imbalanced-host-response-to-sars-c
  - 2021-hoagland-leveraging-the-antiviral-type-i-in
  - 2021-nilsson-payant-reduced-nucleoprotein-availability
  - 2021-nilsson-payant-the-nf-b-transcriptional-footprint
  - 2023-carrau-delayed-engagement-of-host-defense
  - 2023-paget-stress-granules-are-shock-absorber
  - 2025-manivasagam-transcriptional-repressor-capicua-
---

## In one paragraph

When a cell detects a virus replicating inside it, it switches on genes that make itself inhospitable to the virus and alerts neighbouring cells to do the same. The signalling protein at the centre of that alert is interferon. For decades this was described as a switch, in which detection leads to interferon production, production leads to signalling, and signalling turns on a few hundred so-called interferon-stimulated genes. The work collected in this area treats that description as too coarse to be useful. Different infections turn on different subsets of those genes, some can be induced without any interferon at all, a repressor sits on their promoters holding them quiet when nothing is wrong, some cell types cannot run the program without damaging themselves, and in a whole animal the response often appears in organs the virus barely reaches. Running through all of it is a question about proportion rather than presence. A response too small lets the virus establish itself, and a response too large or too late damages the tissue it was meant to protect, so the interesting biology lies in how magnitude, composition and timing are set.

## The defining scientific question

What determines which genes the interferon system turns on, how strongly, and for how long.

Stated that way the question separates into parts the corpus addresses with different tools. Composition is a question about transcription factors and the DNA elements they read. Magnitude is a question about what the cell detects and what dampens detection once it has begun. Duration and location are questions only an animal can answer, since they depend on which compartment produces the signal, how fast it arrives relative to replication, and whether it persists after the virus is gone.

## Origins

This line of work begins before the independent laboratory existed, in two training-period publications, and the honest account says so plainly.

Sharma 2003 comes from doctoral training in the Hiscott laboratory at the Lady Davis Institute and McGill University, with John Hiscott and Rongtuan Lin as corresponding authors and tenOever second of three authors marked as contributing equally. It assigned the activity then known only as the virus-activated kinase to two named enzymes, IKKepsilon and TBK1, showed that they phosphorylate the C-terminal regulatory cluster of IRF-3 and IRF-7, and separated an interferon regulatory factor arm from a nuclear factor kappa B arm inside the IKK family.

tenOever 2007 was carried out with the Maniatis laboratory at Harvard together with the García-Sastre laboratory at Mount Sinai, with tenOever as first author and Tom Maniatis as corresponding author. It is where the question organising this area first appears in recognisable form. Mice lacking IKKepsilon made normal interferon beta yet failed to induce roughly a third of interferon-stimulated genes, the defect persisted when interferon was supplied from outside the cell, and the responsible substrate was STAT1 Ser708. From that point the interferon-stimulated gene set is no longer a single readout but a structured output whose composition is set by kinases, transcription factor complexes and promoter architecture.

Neither paper belongs to the independent program, and neither is evidence of its work. What carries forward are the habits, namely influenza A virus infection in a defined host genetic background as the assay for an innate pathway, transcriptional profiling as the readout, and an interferon-stimulated gene set treated as divisible. Blanco-Melo 2020 still cites Sharma 2003 for TBK1.

## Major findings

Much of the antiviral transcriptome does not require interferon. Schmid 2010, lab-led, showed that mice lacking both interferon receptors still induce a large block of interferon-stimulated genes after NS1-deficient influenza A virus infection, that IRF7 and ISGF3 read overlapping but distinguishable elements, and that activating IRF7 in interferon-unresponsive cells reproduces about 80 percent of that set.

Kinases allocate shared transcription factor subunits. Ng 2011, co-led with the Maniatis laboratory, placed STAT1 Ser708 in the homodimer interface and showed that phosphorylation there blocks the GAF homodimer while leaving the ISGF3 partnership intact, biasing a limiting STAT1 pool toward the type I response. Schmid 2014, lab-led, found the same logic among the interferon regulatory factors, where the IRF7-induced kinase MAP3K8 drives phosphorylation in the IRF3 hinge and redirects it into IRF3 and IRF7 heterodimers.

Interferon-stimulated gene promoters are actively repressed rather than merely unoccupied, a finding belonging to the Manicassamy laboratory. Han 2018 and Manivasagam 2025, both collaborative, identified capicua in a survival-based CRISPR screen and then showed the capicua and ATXN1L complex acting at an eight-nucleotide motif, with basal signalling requiring MAVS and virus entry destroying the complex within forty minutes through EGFR-MAPK signalling.

The response is not compatible with every cell state. Eggenberger 2019, lab-led, forced the program into pluripotent stem cells with a constitutively active IRF7 and found roughly 2,000 genes still differentially expressed five days later alongside compromised germ layer differentiation, with KLF4 the most potent repressor among the reprogramming factors.

Less virus can mean more interferon. Nilsson-Payant 2021 on nucleoprotein availability, lab-led, found that blocking full-length replication increases production of short mini-viral RNAs that RIG-I detects, across six negative-sense families but not for SARS-CoV-2 nucleocapsid, and Benitez 2015, lab-led, had shown that MDA5 contributes through amplification rather than through interferon beta induction. Detection also has to be buffered, and Paget 2023, collaborative and led by the Hur laboratory, showed that stress granules restrain double-stranded RNA sensing, with cells unable to form them dying by MAVS-dependent, interferon-independent apoptosis.

In an animal, response and replication are separable in space and time. Langlois 2012, lab-led, silenced influenza only in hematopoietic cells and found that compartment accounts for much of the lung interferon response while being dispensable for CD8 T cell priming, and Heaton 2014, co-led with the Palese laboratory, found surviving infected club cells that remain inflammatory after clearance. Blanco-Melo 2020, lab-led, defined the SARS-CoV-2 response as low interferon with strong interferon-independent chemokine induction, and Nilsson-Payant 2021 on the nuclear factor kappa B footprint, lab-led, showed the virus requires that transcription to replicate. Hoagland 2021 and Carrau 2023, both lab-led, established in golden hamsters that inflammation appears in organs the virus barely reaches, that circulating airway-derived interferon accounts for it and restricts where the virus establishes, and that intranasal interferon lowers virus, pathology and transmission.

## How the work evolved

The trajectory runs from biochemistry to promoters to animals. The training-period work and the papers following it are reductionist, using reconstituted kinase assays, mobility shift assays and reporter constructs to ask which factor acts where. That phase closes around 2014, after which the primary instrument becomes sequencing of host and viral reads from the same libraries, applied to sorted populations, whole tissues and eventually nine organs at once. The object of study changes with it, from a pathway to a response measured as a whole, positioned comparatively and then intervened upon.

Some threads did not become programs. The structural questions left open by Ng 2011 and Schmid 2014 were not returned to. Interferon and cell identity rests on one experimental paper and one Perspective, with no follow-up on pluripotency. Homeostatic repression is a seven-year gap between a screen hit and its characterisation, and both papers belong to another laboratory. The reading that one design principle, a kinase acting at a dimer interface to allocate a shared subunit, appears in both the STAT and IRF systems is synthesis across those two papers and is asserted by neither. One internal correction is worth recording, since Hoagland 2021 proposed disseminated viral RNA as the cause of distal inflammation and Carrau 2023 from the same laboratory reported instead for interferon made in the lung and carried in the blood.

## Principal publications

- **2003-sharma-triggering-the-interferon-antivira.** Training-period work from the Hiscott laboratory that converted the virus-activated kinase from an operational activity into two named enzymes.
- **2007-tenoever-multiple-functions-of-the-ikk-rela.** Training-period work with the Maniatis laboratory showing that the interferon-stimulated gene set is divisible and set by a kinase acting inside interferon signalling.
- **2010-schmid-transcription-factor-redundancy-en.** Established that much of the antiviral transcriptome is inducible without interferon signalling, with sequence criteria for sorting promoters by the factor that reads them.
- **2011-ng-i-b-kinase-ikk-regulates-the-balan.** Explained a phosphosite as a competitive allocation switch between two interferon complexes sharing one subunit.
- **2012-langlois-hematopoietic-specific-targeting-o.** Made viral tropism an experimental variable and located much of the in vivo interferon response in a numerically minor compartment.
- **2014-schmid-mitogen-activated-protein-kinase-m.** Identified a feedback kinase that changes which IRF dimer forms, scaling the breadth of the response to the persistence of the threat.
- **2014-heaton-long-term-survival-of-influenza-vi.** Showed that some infected airway cells survive and remain inflammatory after clearance.
- **2015-benitez-in-vivo-rnai-screening-identifies-.** Used viral fitness in an animal as a genetic screen and reopened the question of what a sensor contributes when interferon induction is intact.
- **2016-tenoever-the-evolution-of-antiviral-defense.** A single-author Perspective, largely synthesising other laboratories' work, supplying the framework in which two antiviral systems can be mutually incompatible.
- **2018-han-genome-wide-crispr-cas9-screen-ide.** Collaborative screen led by the Manicassamy laboratory that surfaced a transcriptional repressor of cell-intrinsic immunity.
- **2019-eggenberger-type-i-interferon-response-impairs.** Turned the unresponsiveness of pluripotent cells into a manipulation and measured what engaging the program costs.
- **2020-blanco-melo-imbalanced-host-response-to-sars-c.** Provided the comparative reference description of the SARS-CoV-2 host response and separated its interferon and chemokine arms experimentally.
- **2021-nilsson-payant-reduced-nucleoprotein-availability.** Identified nucleoprotein availability as the point where replication competence and immune invisibility are coupled.
- **2021-nilsson-payant-the-nf-b-transcriptional-footprint.** Reframed COVID-19 inflammation as a viral transcriptional dependency, supported by a chimeric activator rescue.
- **2021-hoagland-leveraging-the-antiviral-type-i-in.** Delivered a longitudinal multi-tissue atlas in a permissive animal and moved interferon toward local airway prophylaxis.
- **2023-carrau-delayed-engagement-of-host-defense.** Showed by three independent manipulations that airway-derived circulating interferon primes distal organs and restricts tropism.
- **2023-paget-stress-granules-are-shock-absorber.** Collaborative work led by the Hur laboratory reversing the prevailing reading of stress granules in double-stranded RNA sensing.
- **2025-manivasagam-transcriptional-repressor-capicua-.** Collaborative work placing a repressor at the DNA and identifying how respiratory viruses remove it.

## Connections to other areas

**Small RNA Biology and the Limits of Antiviral Silencing.** The link is the incompatibility argument. tenOever 2016 belongs to both areas, and its claim that chordates could not retain RNA silencing because systemic small RNA defence needs a polymerase whose expression triggers innate immunity is a statement about interferon as much as about silencing. Eggenberger 2019 applies the same argument to a cell state rather than a lineage.

**Programmable Virology.** This area depends on that one for its instruments, since the miR-142 restricted virus of Langlois 2012, the Cre reporter virus of Heaton 2014, the artificial microRNA library of Benitez 2015 and the nucleoprotein targeting cassette of Nilsson-Payant 2021 are engineering results before they are immunology results. Four publications are shared.

**Influenza Genome Regulation and Replication.** Nilsson-Payant 2021 on nucleoprotein availability sits in both, since nucleoprotein and polymerase stoichiometry is the subject there and the instrument here. NS1 connects the areas throughout, because NS1-deficient viruses are the standard reference for an unantagonised host response in Schmid 2010, Benitez 2015, Eggenberger 2019 and Blanco-Melo 2020.

**Pandemic Host Response and Disease.** Four publications are shared and read for different purposes. Here Blanco-Melo 2020, Nilsson-Payant 2021 on nuclear factor kappa B, Hoagland 2021 and Carrau 2023 are evidence about how a response is calibrated, while there they are evidence about why SARS-CoV-2 produces the disease it does. The post-clearance state of Heaton 2014 anticipates the post-acute sequelae theme.

**Viral Populations, Evolution and Transmission.** The link runs through ADAR1. tenOever 2007 introduced it as an IKKepsilon-dependent effector whose editing of influenza matrix mRNA was measured directly, and Paget 2023 uses ADAR1 knockdown to generate the endogenous double-stranded RNA that granules buffer. The connection is real but thin, and no publication in either area asserts it.

## Current implications

The choice of drug target determines whether an antiviral also engages host defence. Nilsson-Payant 2021 on nucleoprotein availability found that two compounds blocking influenza equally well differ in whether they induce IFIT1, because one pushes the polymerase into making immunostimulatory short products. The proposed bystander priming benefit is an extrapolation from cell culture and is flagged as such.

Interferon is more tractable as a local early intervention than a systemic one. Hoagland 2021 showed that intranasal interferon before or one day after challenge reduces virus, pathology and transmission in hamsters, and that a receptor agonist gives comparable activity, which matters because systemic interferon has been limited by tolerability and trial results. Carrau 2023 supplies the reason the early airway response matters, since it primes every other organ.

Inflammation and replication can be the same target. Nilsson-Payant 2021 on the nuclear factor kappa B footprint predicts that blocking NF-kappa B-driven transcription suppresses both, and four mechanistically distinct inhibitors reduced infection in vitro. The authors note the absence of approved NF-kappa B inhibitors and their own failure to reproduce the effect in a hamster model.

## Open questions

The structural chemistry of allocation is unresolved, since Ng 2011 states that the consequences of Ser708 phosphorylation within ISGF3 are unknown and Schmid 2014 does not establish MAP3K8 as a direct kinase for IRF3 or identify the modified hinge residues.

Occupancy has not been shown for the repressor, since Manivasagam 2025 rests on motif prediction, accessibility change and transfected reporters, the motif is a Drosophila consensus carried by most affected genes, and the ligase connecting ERK activity to degradation is unidentified.

The ligand remains undefined in two places. Benitez 2015 did not determine what MDA5 recognises during influenza infection, and Nilsson-Payant 2021 on nucleoprotein availability leaves the contribution of mini-viral RNA against longer defective genomes unresolved. How granules suppress signalling is likewise unknown, stated as such by the authors of Paget 2023.

Which NF-kappa B target genes SARS-CoV-2 requires was not determined, and whether that dependency holds in vivo remains open. Whether the interferon program is incompatible with pluripotency in a developing organism is untested, since all of Eggenberger 2019 is in vitro with an artificial driving construct. Finally, the compartment arithmetic of Langlois 2012 is unexplained, since its authors could not account for why removing replication from a minor hematopoietic compartment costs so much total lung interferon.

## Publications referenced
- 2003-sharma-triggering-the-interferon-antivira
- 2007-tenoever-multiple-functions-of-the-ikk-rela
- 2010-schmid-transcription-factor-redundancy-en
- 2011-ng-i-b-kinase-ikk-regulates-the-balan
- 2012-langlois-hematopoietic-specific-targeting-o
- 2014-heaton-long-term-survival-of-influenza-vi
- 2014-schmid-mitogen-activated-protein-kinase-m
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2016-tenoever-the-evolution-of-antiviral-defense
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2019-eggenberger-type-i-interferon-response-impairs
- 2020-blanco-melo-imbalanced-host-response-to-sars-c
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2021-nilsson-payant-the-nf-b-transcriptional-footprint
- 2023-carrau-delayed-engagement-of-host-defense
- 2023-paget-stress-granules-are-shock-absorber
- 2025-manivasagam-transcriptional-repressor-capicua-
