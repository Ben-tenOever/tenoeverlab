---
id: in-vivo-screening-through-fitness
area: programmable-virology
name: "In Vivo Genetic Screening Through Viral Fitness"
question: "Can natural selection inside an infected animal be used as the readout of a genetic screen?"
publications:
  - 2013-varble-an-in-vivo-rnai-screening-approach
  - 2015-benitez-in-vivo-rnai-screening-identifies-
  - 2018-han-genome-wide-crispr-cas9-screen-ide
  - 2021-daniloski-identification-of-required-host-fa
---

## The scientific problem

Loss-of-function screens for host factors affecting virus replication had converged on a common format by the time this work began, and on a common set of compromises with it. Varble 2013 and Benitez 2015 both state them. The screen requires cultured cells, usually transformed, so one cell type stands in for an infected tissue, and the output is a surrogate, a reporter or a surface stain or a single-cycle measurement, rather than the replicative success of the virus itself. Han 2018 adds the empirical consequence, noting that at least nine genome-wide influenza screens had been published and that meta-analyses found little overlap between them beyond the vacuolar ATPase subunits.

The proposal that defines this theme is that a natural infection already generates a population from which the host response selects, and that a library of otherwise identical viruses differing only by an encoded perturbation mimics that process with a readable genotype. If a perturbation relieves host restriction, the virus carrying it replicates better and rises in the population, so selection is the assay and viral fitness is the readout.

## What this laboratory contributed

Varble 2013 implements the idea. Sindbis virus was chosen because it is attenuated, mouse-adapted, cytoplasmic and carries a duplicated subgenomic promoter, and because the laboratory had already shown it processes artificial microRNAs accurately. Roughly 10,000 viruses, each encoding a designed guide substituted into the murine miR-124-2 backbone, were passaged through mice by footpad injection with recovery from spleen, and hairpin abundance was read by deep sequencing after each forty eight hour passage.

Two controls make the result interpretable and are the durable methodological contribution. A matched library of 22 nucleotide barcodes, which confer no advantage, quantifies how much apparent reproducibility a bottlenecked in vivo passage generates on its own. Across four independent screens only 0.5 percent of barcoded viruses were shared by two sets and none by three or more, while hairpin-bearing viruses showed a sixteenfold enrichment for appearing in two or more sets. And recloning surviving hairpins into a fresh genome between passages removes hitchhiking mutations. The two most reproducible hits targeted Zfx and Mga, transcription factors previously associated with self-renewal, and loss of either reduced interferon beta induction and components of interferon signalling and raised titres by one to one and a half logs. The authors propose that these are transcriptional maintenance factors rather than antiviral effectors.

Benitez 2015 changes the source of the selective pressure and thereby the class of question. Rather than using a naturally attenuated virus, influenza A virus was attenuated by mutating NS1 so that it can no longer block pattern detection, which costs roughly three logs of replication. Because the attenuation is imposed by the host response, silencing a gene that contributes to that response restores fitness directly. Two viruses targeting Ifih1, which encodes MDA5, were enriched more than fiftyfold in all four screens, one rising from 0.26 percent of input to between 26 and 31 percent of output.

The follow-up is what makes the platform credible. The advantage disappeared in Ifih1 knockout mice, was absent in canine cells where a mouse-specific hairpin cannot act, and was not attributable to the unintended strand's near-perfect match to Setd7. And the biological result revises something treated as settled. Two prior studies had concluded that influenza detection is exclusively through RIG-I, on the basis of interferon beta induction. Benitez 2015 agrees on that point, since interferon beta induction was abolished only by loss of RIG-I, and shows that MDA5 is nonetheless required for full induction of Irf7, OAS isoforms, Ifit1, Stat1 and Isg15, in a manner that depends genetically on RNase L. An interferon-induction readout can miss a sensor's contribution. The proposal that MDA5 detects RNase L cleavage products is offered in that discussion and not tested.

## How the work evolved

Between 2013 and 2015 the platform gains specificity and loses breadth. Varble 2013 used roughly 10,000 hairpins against a whole transcriptome and returned a small number of reproducible hits, several of them broad transcriptional regulators. Benitez 2015 used one hundred genes chosen for induction by infection and low baseline expression, and returned a dominant and mechanistically tractable winner. The narrowing was deliberate, and the cost is stated directly. The screen cannot speak to constitutively abundant restriction factors, which the paper demonstrates with RIG-I itself, whose high basal level in lung is offered as the reason a RIG-I-targeting virus did not dominate. Absence from the enrichment list is therefore not evidence of no antiviral role.

The limitations sections of both papers are unusually substantive and are part of what the theme contributed. Selection is cell-autonomous, so the screen cannot report on factors acting in uninfected bystanders. The value of a hairpin changes over time, since silencing a sensor is worth little once interferon has been induced. A target protein with a half-life longer than the viral life cycle shows no benefit when its transcript is silenced. Target assignment for enriched hairpins in Varble 2013 is computational. Both papers address biosafety the same way, arguing that encoding a hairpin is itself attenuating, so selection operates only within a population already crippled.

Two papers in this theme are not in vivo fitness screens and should not be read as continuations of the platform. Han 2018 is a survival-based genome-wide CRISPR knockout screen in an immortalised human lung line, led by the Manicassamy laboratory with this laboratory represented by one author and no contributions statement to apportion roles. Daniloski 2021 is a genome-scale CRISPR knockout screen in ACE2-expressing A549 cells, co-led, with the screening platform and analysis from the Sanjana laboratory and the virological work including all biosafety level 3 infections from this laboratory. Both use survival of lethal infection as the selection, the same underlying logic of fitness as readout, and both are in cell culture rather than in an animal, which is the constraint the 2013 and 2015 platform was built to escape.

What links all four is convergence rather than lineage. Han 2018 recovered SLC35A1 and the sialic acid pathway as an entry requirement, and also capicua, a transcriptional repressor whose loss raises the antiviral set point and restricts viruses from four families. Daniloski 2021 recovered endosomal machinery, a shared cholesterol biosynthesis signature across six hits, and intracellular sequestration of ACE2 upon RAB7A loss. That two libraries of very different design both returned regulators of cell-intrinsic immunity alongside replication machinery is noted in the Han 2018 record as synthesis visible when the papers are read together, and neither paper claims it.

## Supporting publications

Varble 2013 and Benitez 2015 are lab-led and are the platform papers. Daniloski 2021 is co-led. Han 2018 is collaborative and led elsewhere.

## Connections

The engineering this theme depends on comes from Varble 2010 and the explicit screening proposal from the discussion of Langlois 2012 in Molecular Therapy, both in the rna-vectors-for-delivery theme. The MDA5 result belongs jointly to the sensing-aberrant-rna theme, the capicua result to homeostatic-repression-of-isgs, and the SARS-CoV-2 dependency map to host-factors-and-druggable-signaling in the pandemic-host-response area. The barcode library used here as a drift control is the same design later used to measure transmission bottlenecks in the viral-populations-evolution area.

## Publications referenced
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2021-daniloski-identification-of-required-host-fa
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
