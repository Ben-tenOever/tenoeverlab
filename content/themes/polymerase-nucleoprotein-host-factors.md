---
id: polymerase-nucleoprotein-host-factors
area: influenza-genome-regulation
name: Polymerase, Nucleoprotein and Host Factors
question: What does the replication machinery require, and what happens when it is short of it?
publications:
  - 2021-nilsson-payant-reduced-nucleoprotein-availability
  - 2022-nilsson-payant-the-host-factor-anp32a-is-required
---

## The scientific problem

The influenza polymerase does not work alone. Nucleoprotein winds the genome into a ribonucleoprotein complex and acts as an elongation factor, dispensable on templates up to about 76 nucleotides and supporting only diminished synthesis up to about 125, which is understood to prioritise viral protein synthesis early and postpone genome replication until there is enough protein to package new material. Nucleoprotein also shields viral RNA from host nucleases, to a degree that varies across families. These two roles had largely been studied separately, and whether nucleoprotein availability governs host detection independently of its role in supporting replication had not been tested. Separately, the host protein ANP32A is essential for influenza genome replication and bridges an RNA-bound polymerase to an RNA-free one in published structures of an influenza C polymerase dimer, and the difference between avian and mammalian ANP32A is sufficient to restrict avian polymerases in mammalian cells. Work with purified protein had led to the proposal that ANP32A is required only for the second step of replication, which does not fit the observation that both nascent species are encapsidated.

## What this laboratory contributed

Nilsson-Payant 2021 is lab-led and turns on separating protein supply from genome supply. Recombinant influenza A and Sendai viruses carry microRNA target sites downstream of the nucleoprotein open reading frame, which degrades nucleoprotein messenger RNA without targeting the genomic RNA that the polymerase copies, with matched nonfunctional-target viruses as the control. Silencing nucleoprotein abolished detectable viral protein and full-length genome replication and yet strongly induced interferon-stimulated genes relative to the viral material present. For Sendai virus the absolute induction was equal or slightly lower than control while viral transcripts fell roughly 300-fold. Sequencing showed reduced coverage with enrichment at segment termini and increased noncanonical junction reads for influenza, and 3 prime terminal enrichment indicating copy-back products for Sendai. Northern blotting against the conserved 5 prime promoter showed accumulation of mini-viral RNA, appearing as early as three hours and tracking with interferon beta induction. Titrating nucleoprotein against fixed polymerase in a reconstituted complex reproduced the inverse relationship between full-length product and mini-viral RNA in a system containing no NS1, and reporter cells placed the response through RIG-I and MAVS rather than MDA5.

The model the data support is that when nucleoprotein is scarce the polymerase can initiate but cannot processively copy full-length templates, so short products that fall below the length at which nucleoprotein is required are preferentially made and amplified under exactly the conditions that prevent replication. Less virus therefore yields more interferon. The relative contribution of mini-viral RNA against longer defective genomes is explicitly left unresolved, and the junction-read counting is acknowledged to undercount substantially. Knockdown of nucleoprotein across seven negative-sense viruses spanning six families gave the same pairing of lost replication with IFIT1 induction, while knockdown of the SARS-CoV-2 nucleocapsid transcript reduced replication without inducing interferon, a contrast the paper does not resolve. Nucleozin, directed at nucleoprotein, induced IFIT1 while the polymerase inhibitor baloxavir marboxil did not, from which the authors propose bystander priming as a property of target choice. That proposal is an extrapolation from two compounds in cell culture.

Nilsson-Payant 2022 is led by the te Velthuis laboratory at Princeton, with the first author based in the tenOever laboratory, and the tenOever contribution is one component of a collaborative study. Its methodological move is to break a coupling that infection cannot break. A G5U change in the 5 prime genomic promoter restricts a minigenome to primary complementary RNA synthesis, while a G2C and C9G pair in the 5 prime complementary promoter blocks further complementary RNA synthesis. An avian-like polymerase was made by a single PB2 K627E substitution, and chicken ANP32A supplied in trans was the rescue arm. Both steps required ANP32A, which removes the single-step model. The requirement was independent of nucleoprotein and of template length on 76, 47 and 30 nucleotide templates, and single-molecule FRET found no effect of the 627 position on promoter binding, which weighs against the competing explanation that avian restriction reflects weaker template binding. Pre-expressing catalytically inactive or active polymerase under actinomycin D showed that encapsidation is unaffected by the 627 identity while replication is, placing the requirement on the actively synthesising polymerase. The bridging mechanism itself is imported from published structural work and is not demonstrated here.

## How the work evolved

The two papers arrive at the same machine from opposite sides. Nilsson-Payant 2021 removes a viral component and reads out what the polymerase does when its elongation factor runs short. Nilsson-Payant 2022 removes the compatible version of a host component and asks where in the two-step reaction the requirement sits. The first turns nucleoprotein into a single control point where replication competence and immune invisibility are coupled, so any perturbation that lowers it trades one for a worse outcome in the other. The second constrains how a host factor must operate functionally and supplies a promoter-mutation approach reusable for other factors and other steps. Neither paper includes animal work, and both are bounded by cell lines, predominantly A549 and HEK-293T, with the mechanistic work in 2022 resting on short truncated minigenome templates that do not reproduce a full-length ribonucleoprotein.

There is a real discontinuity to note. The 2021 paper reads nucleoprotein scarcity as a source of pathogen-associated molecular patterns, which pulls it toward the laboratory's innate sensing work, and its record carries a second research area for that reason. The 2022 paper pursues a host adaptation question in another laboratory's programme. Only the 2021 paper continues the argument this area is built around, that amount and timing rather than dedicated regulators set the behaviour of the influenza replication machinery.

## Supporting publications

Nilsson-Payant 2021 supplies the nucleoprotein availability result and the cross-family survey, lab-led. Nilsson-Payant 2022 supplies the ANP32A placement, collaborative and led elsewhere.

## Connections

The theme meets the small viral RNA work at the Northern blot, where svRNA described by Perez 2010 and Perez 2012 is visible alongside the mini-viral RNA of Nilsson-Payant 2021, two short products of the same polymerase with different consequences. It meets the splicing theme through the shared logic that the amount of a viral product, not its presence, is what regulates the cycle. Outside this area, Nilsson-Payant 2021 belongs equally to the laboratory's work on how the cell recognises aberrant viral RNA, and its recombinant viruses come from the laboratory's practice of inserting microRNA target sites to control individual viral gene products.

## Publications referenced
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2022-nilsson-payant-the-host-factor-anp32a-is-required
- 2010-perez-influenza-a-virus-generated-small-
- 2012-perez-a-small-rna-enhancer-of-viral-poly
