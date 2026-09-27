---
id: influenza-genome-regulation
name: Influenza Genome Regulation and Replication
question: How does influenza A virus control the order and amount of its own gene expression?
themes:
  - small-viral-rnas
  - splicing-and-temporal-control
  - polymerase-nucleoprotein-host-factors
  - ns1-and-interferon-antagonism
publications:
  - 2010-perez-influenza-a-virus-generated-small-
  - 2012-perez-a-small-rna-enhancer-of-viral-poly
  - 2013-chua-influenza-a-virus-utilizes-subopti
  - 2017-morales-sars-cov-encoded-small-rnas-contri
  - 2019-munoz-moreno-viral-fitness-landscapes-in-divers
  - 2021-nilsson-payant-reduced-nucleoprotein-availability
  - 2022-nilsson-payant-the-host-factor-anp32a-is-required
  - 2023-oishi-archaeal-kink-turn-binding-protein
---

## In one paragraph

Influenza A virus has eight segments, comparable promoters on all of them, ten major proteins and no transcription factors. It nevertheless has to order nuclear entry, genome replication, nuclear export and assembly, and it has to keep eight segments in balance so that complete genomes can be packaged. The work in this area asks how that scheduling is achieved, and the answer it assembles is that the virus regulates itself through the timing and the amount of products it already makes for other reasons rather than through dedicated regulatory proteins. A family of small viral RNAs derived from the conserved segment ends loads into the polymerase and shifts it toward genome synthesis (Perez 2010, Perez 2012). A deliberately inefficient splice site on segment 8 paces the accumulation of the nuclear export protein, so that export begins only after replication has proceeded, and correcting the splice site cripples the virus (Chua 2013). The availability of nucleoprotein determines whether the polymerase makes full-length genomes or short immunostimulatory fragments (Nilsson-Payant 2021). Two of the eight publications, both led by other laboratories, extend the area outward rather than deepening this argument, one to a host cofactor requirement (Nilsson-Payant 2022) and one to the sequence diversity of the interferon antagonist NS1 (Munoz-Moreno 2019), and one carries the small viral RNA concept to a coronavirus where it does something different (Morales 2017).

## The defining scientific question

How does influenza A virus control the order and amount of its own gene expression. The question is sharpened by two structural facts about the virus. The first is that one heterotrimeric polymerase performs two incompatible reactions on the same templates, primer-dependent messenger RNA synthesis that requires the enzyme to stay bound in cis to the 5 prime template end, and primer-independent genome synthesis that requires it to read through that same end. Perez 2010 states the paradox directly and notes that the models then available did not reconcile it. The second is that the virus cannot delay a protein by transcribing its segment later, because all eight promoters are comparable, which is the premise Chua 2013 works from. Both facts push the answer toward regulation by product amount and product timing rather than by dedicated switches.

## Origins

The area begins in small RNA sequencing rather than in classical influenza genetics. Perez 2010 deep sequenced the sub-40 nucleotide RNA fraction of infected lung epithelial cells and found a discrete species, svRNA, of 22 to 27 nucleotides matching the 5 prime terminus of each of the eight segments, distributed as a hotspot rather than as breakdown product, made across subtypes and across human, canine, murine and avian systems, and not induced by an unrelated virus or by interferon. The methods and the framing came from the laboratory's parallel interest in small RNA biology, which is why the discovery route was sequencing rather than mutagenesis. The consequence for this area is that the first candidate regulator it identified was an RNA that the virus produces as a byproduct of copying its own genome, which set the pattern the rest of the area follows.

## Major findings

Small viral RNA is templated from the complementary RNA intermediate, stays nuclear, is largely excluded from virions, and binds the polymerase through the PB1 and PA heterodimer with the basic residue R566 of PA most important (Perez 2012). Synthetic svRNA promotes full-length genome synthesis in a cell-free reaction with purified trimer even when its 3 prime hydroxyl is blocked, so the effect is not priming, and the first 13 nucleotides suffice (Perez 2012). Locked nucleic acid inhibition against one segment depletes that segment's genomic RNA while sparing messenger and complementary RNA and the other segments (Perez 2010), and a recombinant virus unable to make svRNA from the neuraminidase segment loses genome synthesis for that segment alone (Perez 2012).

The segment 8 splice site is a timer. Silencing NS1 by more than ninety percent barely affects replication or interferon-regulated gene induction in cell lines, primary cells or mice, whereas lowering the nuclear export protein by a 2A recoding arrangement or by small interfering RNA costs titre, and raising it by an extra gene copy or by optimising the splice site costs about two logs in culture and nearly abolishes replication in mice (Chua 2013). Nucleoprotein reaches the cytoplasm as early as five hours with the splice-optimised virus and is delayed when the export protein is scarce (Chua 2013). A decade later an archaeal kink-turn binding protein, L7Ae, was found to eliminate both spliced orthomyxovirus products while the unspliced ones accumulate, with no measurable effect on host splicing, sensitivity mapping to the 3 prime splice acceptor region of segments 7 and 8, and no true escape after twenty passages under selection (Oishi 2023).

Nucleoprotein availability sets the character of what the polymerase makes. Degrading nucleoprotein messenger RNA without touching genomic RNA abolishes full-length replication while strongly inducing interferon-stimulated genes, because the polymerase then accumulates mini-viral RNA and other aberrant products that are sensed through RIG-I and MAVS, a relationship reproduced by titrating nucleoprotein against fixed polymerase in a reconstituted complex containing no NS1 (Nilsson-Payant 2021). The same pairing of lost replication with interferon induction held across seven negative-sense viruses in six families and failed for the SARS-CoV-2 nucleocapsid, and a nucleoprotein-directed drug induced interferon where a polymerase-directed drug did not (Nilsson-Payant 2021).

Two findings sit at the edge of the argument. ANP32A is required for both steps of genome replication and acts on the replicating rather than the encapsidating polymerase, shown by promoter mutations that restrict a minigenome to one step at a time (Nilsson-Payant 2022, led by the te Velthuis laboratory). NS1 fitness across 56 natural sequences in a common backbone is structured by allele and by host, with allele B overrepresented in every substrate and with selection acting largely through STAT1 signalling, and phylogenetic proximity predicts phenotype poorly (Munoz-Moreno 2019, led by the García-Sastre laboratory).

## How the work evolved

Three movements are visible. The first is the svRNA line of 2010 to 2012, which went from an observed species to a binding site and a non-priming mode of action and then stopped. It was not returned to as a dedicated programme, and the proposal that eight svRNA-loaded replicases set segment balance was never tested by direct measurement of polymerase occupancy, nor was a structure of the complex obtained. Its later appearance is incidental, as a band alongside mini-viral RNA on the Northern blots of Nilsson-Payant 2021.

The second is the splicing line, which is the most continuous thread in the area. Chua 2013 established the timer genetically. Oishi 2023 returned to the same step with a heterologous protein, converted a feature described for influenza A virus into a family-level property spanning influenza B virus and a salmon orthomyxovirus, and showed that the virus cannot escape an inhibitor of the step without either truncating NS1 or driving splicing efficiency up at a large fitness cost. The splicing-independent 2A virus built in the Chua work supplies the decisive control in the Oishi work, which is an unusually direct reagent lineage across ten years.

The third is the polymerase and nucleoprotein line of 2021 and 2022, which approaches the same machine from the side of what it lacks. Here the area partly turns outward. Nilsson-Payant 2021 belongs equally to the laboratory's work on innate sensing of aberrant viral RNA, and Nilsson-Payant 2022 belongs to another laboratory's host adaptation programme.

## Principal publications

Perez 2010 and Perez 2012 for small viral RNA, both lab-led. Chua 2013 for the splice site timer and for the finding that most NS1 is dispensable for antagonism, lab-led. Oishi 2023 for the separation of orthomyxovirus splicing from host splicing, lab-led and carrying a declared conflict tied to commercialisation of L7Ae. Nilsson-Payant 2021 for nucleoprotein availability, lab-led. Nilsson-Payant 2022 and Munoz-Moreno 2019 are collaborative and led elsewhere, and Morales 2017 is led by the Enjuanes and Sola group in Madrid with this laboratory contributing reagents, conceptual advice and manuscript writing.

## Connections to other areas

Morales 2017 links this area to small RNA antiviral defence and to coronavirus biology, and the link is a contrast. Influenza svRNAs come from noncoding segment ends and act on the viral life cycle, while the SARS-CoV species come from coding regions and contribute to lung immunopathology without lowering titres. Nilsson-Payant 2021 links to innate immune signalling, where the short products of a nucleoprotein-starved polymerase become the substrate of detection. Munoz-Moreno 2019 links to viral populations and evolution, and its barcoded library descends from the transmission bottleneck method of Varble 2014. Oishi 2023 links to the laboratory's interest in antiviral tools drawn from other domains of life. The recombinant viruses in Chua 2013 and Nilsson-Payant 2021 both use microRNA target site insertion, a technique developed in the laboratory's attenuation work and reused here as conditional genetics.

## Current implications

The area yields three practical positions. Target choice determines whether an antiviral also engages host defences, since nucleozin induced interferon and baloxavir marboxil did not, which the authors offer as a case for nucleoprotein-directed inhibitors and bystander priming, an extrapolation from cell culture (Nilsson-Payant 2021). Orthomyxovirus splicing is a family-wide vulnerability that a single heterologous protein can attack with a high fitness cost to escape (Oishi 2023). And because svRNA sequences derive from conserved noncoding ends, inhibitors against them need not be strain restricted, which Perez 2010 names as a direction rather than demonstrates.

## Open questions

How svRNA is made remains unresolved, and so does whether it causes the transcription to replication switch rather than accompanying it. Whether each segment really has its own svRNA-loaded replicase, and whether that is how segment balance is set, has not been measured directly. The structure that L7Ae engages has not been observed, crosslinking produced no footprint, and whether the effect is direct occlusion or indirect interference is undecided. The step at which mistimed ribonucleoprotein export becomes lethal is not identified, and no experiment restores correct timing to rescue the titre defect. The relative contribution of mini-viral RNA against longer defective genomes to the interferon response is explicitly left open, and why coronavirus nucleocapsid knockdown does not produce the same result is unexplained. Almost all of this work is in cell lines, with animal experiments confined to Chua 2013, Munoz-Moreno 2019 and Morales 2017, so what nucleoprotein scarcity or splice site alteration does in tissue is largely untested. Finally, the unifying idea that the virus regulates itself by timing and stoichiometry is well supported for svRNA, for the splice site and for nucleoprotein, and is not what the NS1 landscape work or the ANP32A work is about, so the area is better described as one strong argument with two adjacent contributions than as four themes making a single case.

## Publications referenced
- 2010-perez-influenza-a-virus-generated-small-
- 2012-perez-a-small-rna-enhancer-of-viral-poly
- 2013-chua-influenza-a-virus-utilizes-subopti
- 2017-morales-sars-cov-encoded-small-rnas-contri
- 2019-munoz-moreno-viral-fitness-landscapes-in-divers
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2022-nilsson-payant-the-host-factor-anp32a-is-required
- 2023-oishi-archaeal-kink-turn-binding-protein
- 2014-varble-influenza-a-virus-transmission-bot
