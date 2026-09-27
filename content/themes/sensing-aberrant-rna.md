---
id: sensing-aberrant-rna
area: innate-immune-signaling
name: Sensing Aberrant RNA and Restraining the Response
question: What exactly does the cell detect during infection, and what keeps detection proportionate?
publications:
  - 2021-nilsson-payant-reduced-nucleoprotein-availability
  - 2023-paget-stress-granules-are-shock-absorber
  - 2015-benitez-in-vivo-rnai-screening-identifies-
---

## The scientific problem

Saying that RIG-I-like receptors detect viral RNA leaves two questions open. The first is which RNA species is the ligand during a real infection, since a replicating virus produces genomes, antigenomes, messenger RNAs, small viral RNAs and a range of truncated products, and the receptors do not see all of them equally. The second is what sets the ceiling. Double-stranded RNA sensing converges on MAVS and drives interferon, chemokine and pro-apoptotic programs, and cells also encounter host-derived double-stranded RNA continuously, so a system tuned only for sensitivity would kill its host. Both questions matter practically, because the amount of interferon a cell makes is not a simple function of how much virus is present.

## What this laboratory contributed

Two of the three publications are `lab-led`, Benitez 2015 and Nilsson-Payant 2021, both with tenOever as senior and corresponding author. Paget 2023 is `collaborative` and was led by the Hur laboratory at Harvard, with Sun Hur as lead contact and sole corresponding author, and the contributions statement records the tenOever role as provision of reagents. That discovery is not this program's.

Benitez 2015 addressed the ligand question indirectly, by asking which host genes actually restrict influenza A virus in an animal. An influenza A virus attenuated by a three-residue substitution in NS1 was engineered so that segment eight carries an artificial microRNA, giving a library in which each virus silences one of a hundred mouse antiviral genes and in which restoring fitness is the readout, because the host response is what imposes the attenuation. Viruses targeting Ifih1, encoding MDA5, were enriched more than fiftyfold in four independent screens, one rising from 0.26 percent of input to roughly a third of output. The advantage disappeared in Ifih1 knockout mice, was not attributable to an off-target match to Setd7, and was reproduced by conventional silencing in human A549 cells. The result does not overturn RIG-I as the sensor for interferon beta induction, which the paper confirms. What MDA5 was required for was full induction of a subset of downstream genes including Irf7, Oas2, Oas3, Ifit1, Stat1 and Isg15, and the effect on Oas2 required RNase L. The authors propose that MDA5 may detect aberrant RNA generated during the response itself, including RNase L cleavage products, and state plainly that no ligand was identified. The lesson is methodological as much as biological, since an interferon-induction readout can miss a sensor's contribution entirely.

Nilsson-Payant 2021 attacked the ligand question directly. Recombinant influenza A and Sendai viruses carry microRNA target sites downstream of the nucleoprotein open reading frame, so nucleoprotein messenger RNA is degraded while genomic RNA is untouched, separating protein supply from genome supply during a genuine infection. Silencing nucleoprotein abolished detectable viral protein and full-length replication yet produced a strongly elevated interferon response relative to the viral material present. Sequencing showed terminal read enrichment and increased noncanonical junctions, and Northern blotting against the conserved 5 prime promoter showed accumulation of mini-viral RNA appearing by three hours and tracking with interferon beta induction. Titrating nucleoprotein against fixed polymerase in a reconstituted complex reproduced the inverse relationship between full-length product and mini-viral RNA, and reporter cells lacking RIG-I or MAVS lost the response while MDA5-deficient cells did not. The mechanism follows from nucleoprotein acting as an elongation factor. When it is scarce the polymerase can initiate but cannot copy long templates, so short 5 prime triphosphate products below the length threshold are preferentially made under exactly the conditions that block replication. Knockdown across seven negative-sense viruses spanning six families gave the same pairing, while SARS-CoV-2 nucleocapsid knockdown reduced replication without inducing IFIT1, and nucleozin induced IFIT1 where the polymerase inhibitor baloxavir marboxil did not. The authors state that how much of the response is driven by mini-viral RNA rather than by longer defective genomes is unresolved, and that their junction-read counts substantially undercount defective genomes.

Paget 2023 supplies the restraint side. Stress granules had been proposed as signalling platforms for RIG-I-like receptors, on the basis of receptor concentration inside them. Using three genetically distinct routes to granule deficiency, deletion of G3BP1 with G3BP2, of UBAP2L, or of PKR, the study found the opposite. All three backgrounds showed stronger signalling to a defined 162 base pair 5 prime triphosphate double-stranded RNA at the level of transcriptome, cytokine messenger RNA and protein, IRF3 activation and MAVS signalling potential measured cell-free, with PKR and the OAS-RNase L arm also hyperactive. Granule-deficient cells underwent caspase-dependent apoptosis largely rescued by deleting MAVS but not IRF3 and relieved by blocking tumour necrosis factor alpha. Restoring granules in PKR-deficient cells with thapsigargin or starvation suppressed signalling, which ties the effect to granules rather than to the route that makes them, and the protection extended to endogenous double-stranded RNA accumulating after ADAR1 knockdown. The molecular mechanism is not established, and the authors say so.

## How the work evolved

The three papers do not form a single line. Benitez 2015 asks which sensors matter and finds one whose contribution lies downstream of induction. Nilsson-Payant 2021 asks what the sensed species is and identifies a control point, nucleoprotein availability, where replication competence and immune invisibility are coupled so tightly that any perturbation trades one against the other. Paget 2023, from another laboratory, asks what stops detection running away and finds a condensate acting as a buffer. Read together, which is synthesis, the area's account of detection shifts from receptor identity toward the quantity and quality of aberrant RNA produced and the machinery that dampens the response to it.

## Supporting publications

- **2015-benitez-in-vivo-rnai-screening-identifies-.** Uses viral fitness inside an animal as the selection signal and shows that MDA5 contributes to influenza defence through amplification of the response rather than through interferon beta induction.
- **2021-nilsson-payant-reduced-nucleoprotein-availability.** Shows that limiting nucleoprotein blocks full-length replication while generating short RIG-I agonists, so less virus produces more interferon, across six negative-sense virus families.
- **2023-paget-stress-granules-are-shock-absorber.** Collaborative work led by the Hur laboratory showing that stress granules restrain rather than promote double-stranded RNA sensing and prevent MAVS-dependent apoptosis.

## Connections

Nilsson-Payant 2021 is shared with influenza genome regulation, where nucleoprotein and polymerase stoichiometry is the subject rather than the instrument, and it depends on earlier laboratory work characterising influenza small viral RNAs. The microRNA target site insertion used there and the artificial microRNA cassette used in Benitez 2015 both come from the engineering line catalogued under programmable virology, which is what makes conditional removal of a viral protein during infection possible at all. Benitez 2015 interprets the loss of Irf7 induction using the framework of Schmid 2010 under transcription factor selectivity. Paget 2023 addresses endogenous double-stranded RNA through condensate buffering where Manivasagam 2025 under homeostatic repression addresses the same tonic signal transcriptionally, and its ADAR1 experiments touch editing biology that recurs in work on viral populations and evolution.

## Publications referenced
- 2010-schmid-transcription-factor-redundancy-en
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2023-paget-stress-granules-are-shock-absorber
- 2025-manivasagam-transcriptional-repressor-capicua-
