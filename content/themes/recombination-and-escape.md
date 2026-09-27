---
id: recombination-and-escape
area: viral-populations-evolution
name: "Recombination and Escape from Selective Pressure"
question: "What genomic capacity determines whether a virus can escape a given pressure?"
publications:
  - 2018-aguado-homologous-recombination-is-an-int
  - 2023-uhl-adar1-biology-can-hinder-effective
  - 2015-benitez-engineered-mammalian-rnai-can-elic
---

## The scientific problem

Whether a virus survives a defence is usually studied one virus and one defence at a time, and the answer is usually an encoded antagonist. That framing leaves a prior question unasked. Given a pressure that no virus in the comparison has evolved to antagonise, what feature of a replication strategy decides whether escape is available at all? Answering it requires a pressure genuinely identical across viruses that otherwise share nothing, which natural defences cannot supply.

Aguado 2018 states this directly. RNA interference is the dominant antiviral defence in plants and invertebrates, so the capacity to evade it should have shaped which viruses persist in those hosts, but testing that is difficult because most viruses facing RNA interference also encode suppressors of it. Vertebrate cells offer a way around the problem, since a vertebrate virus has no reason to carry such a suppressor, and vertebrates retain the small RNA machinery even though they do not use it antivirally.

## What this laboratory contributed

All three publications in this theme are lab-led with tenOever as senior and corresponding author, and the line runs in a clear order.

Benitez 2015 built the pressure. Inserting perfectly complementary target sites for host microRNAs into influenza A virus converts endogenous microRNAs into virus specific guides, because perfect complementarity licenses Argonaute 2 cleavage rather than the subtle repression that ordinary microRNA pairing produces. That paper fixed the design parameters, finding a silencing threshold near sixteen nucleotides of contiguous complementarity, and it produced a virus carrying five distinct mammalian microRNA target sites that grew in eggs yet gave no plaques and no detectable nucleoprotein in mammalian cells, and caused no morbidity in mice at 25,000 plaque forming units, including in animals lacking the type I interferon receptor.

Benitez 2015 also produced the first escape result, and it is a negative one that set up everything after it. Across several designs, including one with a single target site, escape variants of self targeting viruses always arose by destroying guide production, through deletion or excision of the artificial hairpin, and the authors report being unable to identify any virus that had mutated the target site itself. Alternative explanations for that asymmetry, such as functional constraint on the targeted sequence, were not separately excluded.

Aguado 2018 turned the cassette into a comparative assay. The same five site cassette, paired with a reverse orientation cassette of identical composition as the sequence matched control and read in wild type against the RNase III deficient fibroblasts the laboratory had generated for Aguado 2017, was placed in an essential transcript of six viruses across four families. A genome wide CRISPR screen confirmed that the pressure runs through the microRNA machinery alone, recovering Drosha, Dicer, DGCR8, Argonaute 2, TP53, miR-21 and XPO5, with no interferon genes implicated.

The outcome split by replication strategy. Sendai virus and influenza A virus, both negative sense, lost more than five logs of titre and were cleared. Sindbis virus, a Semliki Forest virus chimera and poliovirus were suppressed at first and then recovered within passages by precise excision of the cassette that left downstream promoter elements intact. Poliovirus escaped despite making all its proteins from one RNA, so a multi transcript genome organisation is not the requirement. The causal test was a single polymerase substitution. Poliovirus carrying D79H, previously characterised as blocking homologous recombination, grew normally without the pressure but could not excise the cassette and was undetectable by passage four. Template switching, rather than polarity as such, is therefore the escape requirement.

Several statements in that discussion are flagged as speculation by the authors, including the proposal that inefficient recombination explains the lower representation of negative strand RNA viruses across the tree of life. The attribution of poor recombination to genomes being encapsidated, and so less accessible to the polymerase, is cited reasoning rather than a result of the study.

## How the work evolved

Uhl 2023 returned to the case Aguado 2018 had left as a dead end, on the argument that negative sense RNA viruses do exist in hosts with functional antiviral RNA interference, so some route out must exist. Two changes to the design revealed one. Sustained infection replaced serial passage, so rare events were not diluted by transfer, and readout in 96 well format turned escape frequency into a countable quantity. A five target Sendai virus then escaped at six to eight days in roughly eight percent of wells.

The escape was not viral. Sequencing found neither deletion of the cassette nor scattered point mutation but dense A to G changes confined to the target sites, the signature of adenosine deaminase acting on RNA. Knockout of ADAR1 in a STAT1 deficient background abolished escape in all 96 wells, and adenoviral reconstitution restored it. The selective pressure is relieved by a host enzyme that happens to destroy the guide binding sites, so escape here is not a viral adaptation at all. Moving the cassette to the phosphoprotein gene, which attenuates comparably without exposing the genome, also permitted escape, with editing on the antigenome rather than the genome.

How ADAR1 comes to edit those particular sequences is unresolved, and the authors say so, laying out a duplex substrate model and a direct RISC recruitment model that their own observations support unevenly. The result also does not generalise, since a five target influenza A virus subjected to the same regime showed neither editing nor escape. The phylogenetic survey associating ADAR1 orthologs with interferon based defence, and the suppression of reporter silencing when human ADAR1 was expressed in Nicotiana benthamiana, are described by the authors as limited in scope and correlative.

## Supporting publications

Benitez 2015 supplies the cassette, the design parameters and the guide side escape asymmetry. Aguado 2018 establishes recombination capacity as the determinant of escape. Uhl 2023 shows that a host editing enzyme provides a second and entirely different route, available to a virus that cannot recombine.

## Connections

All three publications are also filed under the small-rna-antiviral-defense area, in the reconstructing-antiviral-rnai theme, where the engineering line and the evolutionary argument about why vertebrates use interferon are the primary subject. Read with tenOever 2016 on the evolution of antiviral defence systems, Uhl 2023 supplies an incompatibility between ADAR1 and effective small RNA defence at the level of a single enzyme, which is a different argument from the pathway level incompatibility that review advanced. Both connect back to Varble 2010, which reported that negative sense genomic RNA inside the ribonucleoprotein is not accessible to microRNA directed silencing. The practical consequence for microRNA based attenuation, that such designs erode over time by routes differing by virus class, runs through all three.

## Publications referenced
- 2018-aguado-homologous-recombination-is-an-int
- 2023-uhl-adar1-biology-can-hinder-effective
- 2015-benitez-engineered-mammalian-rnai-can-elic
- 2016-tenoever-the-evolution-of-antiviral-defense
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2017-aguado-rnase-iii-nucleases-from-diverse-k
