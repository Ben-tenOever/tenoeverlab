---
id: reconstructing-antiviral-rnai
area: small-rna-antiviral-defense
name: Reconstructing Antiviral RNA Interference
question: If the system is absent, can it be rebuilt, and what happens when it is?
publications:
  - 2015-benitez-engineered-mammalian-rnai-can-elic
  - 2018-aguado-homologous-recombination-is-an-int
  - 2023-uhl-adar1-biology-can-hinder-effective
---

## The scientific problem

Having concluded that mammals do not use small RNA silencing against viruses, the laboratory faced the question of why. One available explanation is that such a defence would not work in a mammalian cell, so the substitution by interferon was forced. That explanation is testable, but not by looking for the missing system. It requires building one and measuring how well it protects. A second problem follows once the system is built. Viruses that face natural RNA interference in plants and invertebrates almost all encode suppressors of it, which makes their intrinsic capacity to evade the defence impossible to compare. Vertebrate viruses have no reason to carry such a suppressor, so a reconstructed pressure applied in vertebrate cells gives a uniform selective condition across unrelated families.

## What this laboratory contributed

Benitez 2015 built the response two ways. Perfectly complementary target sites for cell-restricted or species-restricted host microRNAs were inserted into influenza A virus, which converts endogenous microRNAs into virus-specific guides present before infection begins. Separately the virus was engineered to encode its own small interfering RNA against its nucleoprotein segment, which places guide production downstream of infection and closer to the kinetics of a genuine response. Reporter calibration fixed the requirement at roughly 16 nucleotides of contiguous complementarity. A virus carrying five distinct mammalian microRNA target sites grew in embryonated eggs but produced no plaques and no detectable nucleoprotein in mammalian cells, and caused no morbidity in mice at 250, 2,500 or 25,000 plaque-forming units. In mice lacking the type I interferon receptor it was equally harmless at 25,000 plaque-forming units, a dose the authors note is more than 2,500 times the lethal dose 50 in that background. That is the result that matters for the evolutionary question, because protection there cannot be attributed to interferon. The conclusion is a possibility claim, that chordates could have used RNA interference in place of interferon, and the authors are explicit that the paper does not explain why they did not.

Two further findings from the same study bear on escape. Attenuation of the self-targeting virus was lost in Dicer-deficient cells, so it runs through the small RNA machinery. And across several independent designs, including one with a single target site, escape variants always disabled guide production rather than altering the target. Why the target was never mutated is not established by these experiments.

Aguado 2018 turned the reconstructed pressure into a comparative assay. A cassette of perfectly complementary sites for five ubiquitous host microRNAs, paired with a reverse-orientation cassette of identical sequence as control, was placed in an essential transcript of six viruses from four families, and applied in wild-type fibroblasts against RNase III deficient fibroblasts as the silencing-off condition. A genome-wide CRISPR screen selecting for loss of silencing recovered Drosha, Dicer, DGCR8, Argonaute 2, XPO5, TP53 and miR-21, and no interferon genes, which is the evidence that the pressure is silencing activity alone. Sendai virus and influenza A virus, both negative-strand, fell by more than five logs and were undetectable by passage four, while Sindbis virus, a Semliki Forest virus chimera and poliovirus were suppressed initially and then recovered through precise excision of the cassette. The causal test is a single polymerase substitution. A poliovirus carrying D79H, previously characterised as blocking homologous recombination, could not excise the cassette and became undetectable, which makes template switching rather than polarity itself the escape requirement. The structural explanation for why negative-strand genomes recombine poorly, that they are encapsidated and less accessible for template jumping, is cited reasoning rather than a result of this study, and the broader claim that poor recombination explains the lower representation of negative-strand viruses across the tree of life is flagged as speculation by the authors.

Uhl 2023 followed the loose end. If negative-sense RNA viruses exist in hosts with functional antiviral RNA interference, some route out must exist. Holding infections without passage, so that rare events are not diluted away, and reading escape as fluorescence in 96-well format, a five-target Sendai virus escaped at six to eight days in roughly 8 percent of wells. The signature was neither excision nor scattered point mutation but dense A to G changes confined to the target sites. Knockout of ADAR1 in a STAT1 deficient background abolished escape in all 96 wells and adenoviral reconstitution restored it. Escape occurred also when the cassette was moved to the phosphoprotein gene, where editing appeared on the antigenome rather than the genome, and in canine and mouse cells, so the phenotype is not specific to human ADAR1.

## How the work evolved

The arc within this theme is a hypothesis narrowed by its own results. Benitez 2015 established that the reconstructed defence works and works without interferon, which removed the simplest explanation for the historical substitution. Aguado 2018 then asked what the defence selects for and found an escape route, recombination, available to some virus classes and not others. Uhl 2023 found the missing route for the classes that could not recombine, and it is not a viral adaptation at all. A host enzyme relieves the selective pressure as a side effect of what it does to double-stranded RNA. That reframing is the most distinctive finding in the theme.

Two boundaries stated by the authors should travel with the conclusions. The reconstructed system departs from endogenous RNA interference in that the guides are present before the virus arrives, or are encoded by the virus, rather than generated by host recognition of viral double-stranded RNA, and the targets are concentrated at one internal site rather than dispersed and regenerating. Benitez 2015 quantifies the first departure, since guides supplied only six hours before infection failed to attenuate. And Uhl 2023 reports that a five-target influenza A virus under the same regime showed neither editing nor escape, with replication site and genome packaging offered as possible reasons and neither resolved, so the ADAR1 route does not generalise across negative-strand families as tested.

## Supporting publications

All three papers are also assigned to the viral populations and evolution area under recombination and escape from selective pressure, where the same experiments are read as statements about viral population dynamics rather than about the silencing pathway.

## Connections

The premise of this theme is the negative result of Backes 2014 in the theme on whether mammalian antiviral RNA interference exists, and the pair is a two-part statement that mammals do not use small RNA silencing against viruses and that they could have. The ADAR1 finding in Uhl 2023 supplies a second and independent incompatibility argument alongside the polymerase argument of tenOever 2016 in the evolutionary theme. The engineering itself belongs to the programmable virology area, where microRNA target insertion serves attenuation and biocontainment rather than an evolutionary question.

## Publications referenced

- 2015-benitez-engineered-mammalian-rnai-can-elic
- 2018-aguado-homologous-recombination-is-an-int
- 2023-uhl-adar1-biology-can-hinder-effective
- 2014-backes-the-mammalian-response-to-virus-in
- 2016-tenoever-the-evolution-of-antiviral-defense
