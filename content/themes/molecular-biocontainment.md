---
id: molecular-biocontainment
area: programmable-virology
name: "Molecular Biocontainment"
question: "Can a transmissible virus be made safe to study without changing the biology being studied?"
publications:
  - 2013-langlois-microrna-based-strategy-to-mitigat
  - 2009-perez-microrna-mediated-species-specific
---

## The scientific problem

Demonstrations that a small number of hemagglutinin substitutions can confer airborne transmission of H5N1 influenza A virus between ferrets prompted a broad argument about whether such experiments should be performed, including a voluntary moratorium. Langlois 2013 takes that argument as its starting point. The existing safeguard was physical, containment at enhanced biosafety level 3.

The requirement that makes an additional layer hard is that it must not alter the phenotype under study. An attenuated virus is safe and useless, because transmission between ferrets is the property the experiment exists to measure. What is needed is a virus that behaves normally in the experimental animal and is crippled in the species of concern, which means the safety device has to be conditional on host identity rather than on viral fitness.

## What this laboratory contributed

The contribution is the recognition that the uneven distribution of microRNAs across species is a usable specification, and that a host-conditional kill switch can therefore be written into a viral genome.

Perez 2009 established the principle without framing it as biocontainment. Target sites for miR-93, present in mouse and human and absent from chicken, placed in the influenza nucleoprotein open reading frame gave a virus attenuated by more than two logs in mice while replicating to normal titres in embryonated eggs. The purpose there was vaccine manufacture, but the structure of the solution is identical. A microRNA expression difference between two hosts becomes a difference in whether the virus can replicate.

Langlois 2013 restates that structure with the ferret and the human in place of the egg and the mouse. Small RNA deep sequencing of human A549 lung cells, primary ferret lung and MDCK cells identified candidates abundant in human cells and scarce in the two carnivore-derived sources. Northern blotting contradicted the sequencing for one candidate, miR-193b, which proved substantially expressed in ferret lung, and the paper reports that discrepancy directly and treats the blot as the arbiter. miR-192 survived, being detectable in murine lung and robustly expressed in human bronchial, alveolar and primary nasal epithelium.

Two design decisions carry the safety argument. Target sites were placed in the hemagglutinin segment rather than in nucleoprotein or NS1, specifically so that the segment carrying the transmission-determining protein cannot be separated from the safety element by reassortment. And they were placed downstream of the hemagglutinin stop codon in a duplicated 5-prime packaging region, which leaves both the protein and the packaging signal unaltered. Mice given the targeted H5 construct showed no morbidity or mortality even at ten times the lethal dose of the parental virus, while an H3N2 version infected, replicated and transmitted in ferrets by direct and by respiratory contact indistinguishably from controls.

## How the work evolved

Between the two papers the same mechanism is repurposed rather than improved, with one substantive engineering change. Perez 2009 had to accept three amino acid substitutions in nucleoprotein, one of which cost about twenty percent of polymerase reconstitution activity and left the control virus mildly attenuated in vivo. Langlois 2013 avoids coding changes entirely by duplicating a packaging signal to create untranslated space. That change is what makes biocontainment compatible with the requirement that the virus behave normally.

The theme does not resolve escape, and both papers are bounded the same way. Perez 2009 recovered no revertants over ten serial passages in A549 cells or from more than twenty five clones per in vivo cohort. Langlois 2013 recovered none from seventeen plaques from mouse lung at day five and none after ferret transmission. These bound escape frequency loosely rather than excluding escape, and the paper's own statement that the results demonstrate the safety of the platform goes beyond what the sampling establishes. The ferret arm in particular applies no selective pressure for escape, since ferrets lack the targeting microRNA. Silencing was demonstrated only in the most favourable configuration, four fully complementary sites, with no titration of site number or mismatch tolerance.

Two further boundaries are worth naming. The human evidence is entirely cell lines and primary cells, so restriction in an infected person is an inference. And the two animal arms use different viruses, a low-pathogenicity H5 construct with the polybasic cleavage site removed for the mouse work and a seasonal H3N2 strain for the ferret transmission, so no single virus was shown to be both restricted in human cells and transmissible as an H5N1.

The proposals in Langlois 2013 that the approach generalises to Ebola virus, SARS coronavirus and henipaviruses, and that targeting multiple segments or multiple microRNAs would further reduce escape, are stated as prospects. Neither is tested there, and neither is taken up elsewhere in this corpus, so this line was demonstrated for influenza and was not developed into a general biosafety platform. tenOever 2019 records the design as one entry in a taxonomy of genetic overrides rather than as a programme that continued.

## Supporting publications

Perez 2009 is lab-led. Langlois 2013 is co-led, with three corresponding authors, and the ferret transmission work sits with the Perez and García-Sastre groups.

## Connections

Both papers are also the foundation of the microrna-mediated-viral-attenuation theme, where the same constructs are treated as attenuation chemistry rather than as safety devices. The related argument that a virus carrying an encoded hairpin is itself attenuated, and therefore that a screening platform built this way cannot enhance a natural pathogen, appears in Varble 2013 and Benitez 2015 in the in-vivo-screening-through-fitness theme. tenOever 2019 places microRNA targeting alongside drug-dependent degron shutoff, developed by another laboratory, as the two classes of genetic override described for influenza.

## Publications referenced
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2009-perez-microrna-mediated-species-specific
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2019-tenoever-synthetic-virology-building-viruse
