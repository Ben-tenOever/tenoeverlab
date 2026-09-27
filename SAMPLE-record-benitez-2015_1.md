---
id: 2015-benitez-engineered-mammalian-rnai-can-elic
slug: 2015-benitez-engineered-mammalian-rnai-can-elic
source_pdf: Benitez_et_al_CellReports2015a.pdf
title: Engineered Mammalian RNAi Can Elicit Antiviral Protection that Negates the Requirement for the Interferon Response
authors: ["Asiel Arturo Benitez", "Laura Adrienne Spanko", "Mehdi Bouhaddou", "David Sachs", "Benjamin Robert tenOever"]
first_author: Asiel Arturo Benitez
senior_authors: ["Benjamin Robert tenOever"]
corresponding_authors: ["Benjamin Robert tenOever"]
tenoever_position: 5
tenoever_role: senior
year: 2015
journal: Cell Reports
volume: "13"
issue: "7"
pages: "1456-1466"
doi: 10.1016/j.celrep.2015.10.020
pmid: "26549455"
pmcid: PMC4654977
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [small-rna-antiviral-defense, viral-populations-evolution]
themes: [reconstructing-antiviral-rnai, recombination-and-escape]
pathogens: [influenza A virus]
viral_families: [Orthomyxoviridae]
biological_systems: [MDCK cells, MDCK cells expressing miR-124, A549 cells, HEK293T cells, NoDice Dicer-deficient cells, murine embryonic fibroblasts, Irf3 and Irf7 double knockout fibroblasts, embryonated chicken eggs, C57BL/6 mice, Ifnar1 knockout mice]
host_species: [human, mouse, dog, chicken]
technologies: [influenza reverse genetics, microRNA target site insertion, virus-encoded artificial microRNA, luciferase reporter assay, small RNA Northern blotting, multicycle growth curves, plaque assay, mRNA sequencing, flow cytometry, lung histology]
key_concepts: [antiviral RNA interference, type I interferon system, engineered RNAi, self-targeting virus, escape mutants, target complementarity threshold, species-specific microRNA attenuation, NS1 and small RNA silencing, evolution of antiviral strategies, live attenuated vaccine design]
keywords: [RNAi, influenza A virus, interferon, miR-124, microRNA targeting, attenuation, escape mutants, Dicer, Ifnar1, evolution]
---

## Citation

Benitez AA, Spanko LA, Bouhaddou M, Sachs D, tenOever BR. Engineered Mammalian RNAi Can Elicit Antiviral Protection that Negates the Requirement for the Interferon Response. Cell Reports. 2015. Volume 13, Issue 7, pages 1456-1466.

DOI 10.1016/j.celrep.2015.10.020. PMID 26549455. PMCID PMC4654977. RNA sequencing data under GEO accession GSE73698.

Asiel Arturo Benitez and Laura Adrienne Spanko are designated co-first authors in the paper's author block.

## One-sentence contribution

Recreating a small RNA antiviral response in mice, using either host microRNAs repurposed as virus-specific guides or a virus-encoded artificial small interfering RNA, attenuates influenza A virus by more than five logs and prevents disease without any requirement for type I interferon signaling.

## Executive summary

Prokaryotes use CRISPR and plants, arthropods and nematodes use RNA interference to mount pathogen-specific nucleic acid defenses. Chordates retain most of the small RNA machinery but respond to viruses instead through the type I interferon system, a protein-based defense that is not tailored to the incoming pathogen. Why that substitution occurred is unknown, and one possible explanation is that a small RNA defense simply would not work well in a mammalian cell.

This study tests that explanation by building the missing response rather than by looking for it. Complementary target sites for cell-restricted or species-restricted host microRNAs were inserted into influenza A virus, converting endogenous microRNAs into virus-specific guides, and separately a virus was engineered to encode its own small interfering RNA directed against one of its own segments.

Silencing required roughly 16 nucleotides of contiguous complementarity, and attenuation in cells reached several logs. Serial passage and mixed-culture passage failed to yield escape mutants that had altered the target site. When escape did occur in self-targeting viruses, it always came from deleting the hairpin that produced the guide rather than from mutating the target. A virus carrying five distinct mammalian microRNA target sites could still be grown in eggs but produced no detectable plaques or nucleoprotein in mammalian cells, caused no morbidity in mice up to 25,000 plaque-forming units, and was equally harmless in mice lacking the type I interferon receptor.

## Scientific context

The paper sets out the comparative picture. Prokaryotes use CRISPR to guide a Cas nuclease with a pathogen-specific RNA template. Many eukaryotes use RNA interference, in which a Dicer-family RNase III enzyme processes viral RNA into 21 to 24 nucleotide small interfering RNAs that load into an Argonaute-containing RISC. Chordates retain much of that machinery, yet antiviral use of it appears limited to plants, arthropods and nematodes, and chordates rely instead on type I interferon.

Chordates do run a small RNA defense against transposable elements through PIWI-interacting RNAs, but that is confined to germ cells. The paper notes that some results support a small RNA antiviral response in pluripotent cells while evidence from differentiated cells is lacking, and that removing Dicer from mammalian fibroblasts does not change replication of most viruses. It further notes evidence that the two systems may be incompatible, citing observations that stem cells process double-stranded RNA without making interferon while differentiated cells do the reverse, that the interferon response shuts down RISC, and that expressing an antiviral Dicer induces interferon.

On timing, the paper cites data from chickens placing the emergence of the interferon system before the divergence of mammals and birds around 350 million years ago, supported by interferon induction in fish, which would place it before the recombination-based adaptive immune system of jawed vertebrates. The stated gap is that the basis for why chordates apparently abandoned RNA interference in favor of interferon remains unknown.

## Central question

Is there something about mammalian cells that prevents a small RNA antiviral defense from working, or could chordates have used RNA interference in place of the type I interferon system with comparable protective effect?

## Experimental strategy

The strategy is reconstruction rather than ablation. Instead of asking whether an endogenous mammalian RNA interference response exists, the study builds a functionally equivalent one and measures how well it protects, including in animals where the interferon arm has been removed.

Two independent routes into that state are used, which matters because each has a different failure mode. The first repurposes host microRNAs by inserting perfectly complementary target sites into the virus, so the guide is present in the cell before infection begins. The second has the virus encode an artificial hairpin that produces a small interfering RNA against one of its own segments, which places guide production downstream of infection and therefore under kinetics closer to a genuine RNA interference response.

Before building viruses, the silencing requirement is calibrated with a luciferase reporter carrying miR-124 target sites of graded complementarity, which fixes the threshold and lets the viral constructs be built with either full complementarity or the minimum that still silences. Building both, and building two-site and four-site versions, sets up a selection experiment in which escape should be easiest for the weakest and least redundant design.

Cell systems are chosen so that single variables differ. A canine kidney line and the same line expressing miR-124 differ only in the presence of one microRNA. Dicer-deficient cells test whether attenuation depends on the small RNA machinery. Fibroblasts lacking interferon regulatory factors 3 and 7 remove the transcriptional arm of innate sensing so that silencing can be measured without it, and a virus encoding an RNA-binding mutant of NS1 tests the claim that NS1 antagonizes silencing.

For the animal work, target sites were selected for microRNAs abundant in human and mouse lung but low in embryonated eggs, so the virus can still be propagated for stock production while being silenced in the host. Mice lacking the type I interferon receptor are the decisive comparison, since protection there cannot be attributed to interferon.

## Key findings

1. In a luciferase reporter, a single 20 nucleotide fully complementary miR-124 site silenced more than 80 percent of activity, sites of 14 nucleotides or fewer gave no repression, and sites of 15, 16 and 17 nucleotides gave a graded relationship between pairing length and silencing (Figure 1A). Two sites were no better than one in this readout (Figure 1B). The threshold for silencing is therefore near 16 nucleotides of contiguous complementarity.

2. Influenza A virus carrying a scrambled insert in the nucleoprotein 3-prime untranslated region replicated indistinguishably from wild-type virus, reaching 10 to the seventh through 10 to the eighth plaque-forming units per milliliter with robust nucleoprotein (Figure S1A, Figure S1B), so the insertion itself is not the source of any phenotype.

3. All targeted viruses replicated normally in canine kidney cells but dropped to between 10 squared and 10 to the fourth plaque-forming units per milliliter with no detectable nucleoprotein in the miR-124-expressing derivative (Figure 1C, Figure 1D). Attenuation increased with target site number but did not differ significantly between full complementarity and 16 contiguous bases.

4. Roughly ten passages in miR-124-expressing cells yielded no recoverable virus, reported as data not shown. Passage in a mixed culture at about three untargeted cells to one targeted cell also produced no escape mutants and instead led to selective death of the permissive cells and to a population dominated by microRNA-expressing cells by 72 hours (Figure 1E).

5. A self-targeting virus expressing a small interfering RNA against the nucleoprotein open reading frame from the NS segment produced the guide during infection (Figure 2B) and was strongly attenuated in wild-type cells but not in Dicer-deficient cells (Figure 2C), giving more than a tenfold loss within 48 hours in cells and in animals (Figure 2D, Figure 2E, Figure S2A). The Dicer dependence establishes that attenuation runs through the small RNA machinery.

6. Sequencing plaque-purified escape variants from self-targeting viruses recovered only guide-side mutations. The nucleoprotein-directed virus escaped through a large deletion in the artificial hairpin that abolished guide production and restored wild-type replication (Figure 2E, Figure 2F, Figure 2G). The 16-nucleotide four-site design escaped through six dispersed deletions in the hairpin (Figure 3B, Figure 3C, Figure 3D) and the 20-nucleotide four-site design by excising the hairpin entirely (Figure 3E, Figure 3F). The authors report they were unable to identify any virus that had mutated the target site itself, even with only a single site present.

7. A timing experiment transfecting guide-expressing plasmids at 3, 6, 12 or 24 hours before infection found attenuation only when transfection preceded infection by 12 hours or more (Figure S2C), with guides visible by Northern blot by 12 hours post-transfection (Figure S2B). From comparison with a loading control the authors estimate 100 to 1,000 copies per cell and infer that a cell would need to accumulate that many guides within the first 6 hours of infection for targeting to succeed. The copy number figure is an estimate calibrated against published quantification of other microRNAs, not a direct measurement.

8. In wild-type and Irf3 and Irf7 double knockout fibroblasts, comparing self-targeting viruses encoding wild-type NS1 with those encoding an RNA-binding mutant of NS1 showed that NS1 functionality had minimal impact on the extent of attenuation once the interferon regulatory factor arm was removed, with a 20-fold to 50-fold titer loss in a single cycle in knockout cells and a 50-fold to 100-fold loss when both silencing and an intact interferon system were present (Figure 3G, Figure 3H). The authors interpret the larger loss with both systems as the two pathways complementing one another, and interpret the small NS1-dependent difference as more likely reflecting defective interfering particles arising without functional NS1 than direct antagonism of silencing.

9. A virus carrying five distinct target sites for miR-93, miR-192, miR-21, miR-31 and miR-29b in the nucleoprotein transcript grew in eggs to roughly 2 times 10 to the fifth egg infectious dose 50 per milliliter against 6 times 10 to the fifth for control (Figure 4A), yet produced no plaques, no hemagglutination activity and no detectable nucleoprotein in mammalian cells (Figure 4B, Figure 4C, Figure S4C). Titer in eggs had to be estimated by egg infectious dose because the targeted virus could not be plaqued at all.

10. In C57BL/6 mice, 250 plaque-forming units of control virus, five times the reported lethal dose 50 of 50 plaque-forming units, caused severe weight loss and complete mortality, while the targeted virus caused no morbidity or mortality at 250, 2,500 or 25,000 plaque-forming units (Figure 5A). Lung histology at 2 and 9 days showed no inflammation or damage with the targeted virus against severe bronchiolar epithelial lesions and perivascular and alveolar edema with untargeted virus (Figure 5B).

11. In Ifnar1 knockout mice the targeted virus caused no morbidity or mortality even at 25,000 plaque-forming units, a dose the authors note is more than 2,500 times the lethal dose 50 in that background, with no detectable viral messenger RNA at day 2 (Figure 5C, Figure S5A) and attenuation confirmed by plaque assay at days 2 and 9 (Figure S5B, Figure S5C). This is the central result, since protection here cannot be attributed to interferon.

12. Transcriptome profiling showed robust interferon-stimulated gene induction with untargeted virus, for example Mx1 induced more than 40-fold against 2-fold for the targeted strain, and Ifit1, Oas1b, Oas2 and Isg15 induced around 10-fold against baseline for the targeted strain (Figure 6A, Table S1). By day 9 elevated antiviral and chemokine transcripts persisted with untargeted virus and were absent with the targeted strain. In Ifnar1 knockout mice the overall response was muted and differences between cohorts were less pronounced for genes such as Ifit1 (Figure 6B, Table S2), which the authors attribute to direct induction by interferon regulatory factors 3 and 7 independent of interferon feedback. Quantitative PCR for the matrix gene found untargeted virus not fully cleared by day 9 in either background while the targeted virus was at background (Figure S6A, Figure S6B).

## Mechanistic model

The mechanism at the level of the engineered response is direct. Guide small RNAs, whether supplied as host microRNAs repurposed by inserting complementary sites or produced by the virus itself, load into RISC and cleave or silence the targeted viral transcript, and this requires Dicer, as shown by the loss of self-targeting attenuation in Dicer-deficient cells. Silencing requires approximately 16 nucleotides of contiguous pairing.

The study does not establish a mechanism for the evolutionary question it raises, and the authors treat that question as open. What the data establish is a possibility claim, that a small RNA response can protect a mammal from a lethal virus challenge with no contribution from type I interferon signaling, and therefore that the historical substitution cannot be explained by the mammalian cell being unable to support such a defense. The authors state this as the conclusion, that chordates could have used RNA interference in place of interferon.

An additional mechanistic reading concerns where selection acts. Escape arose only by destroying guide production, never by altering the target, across several independent designs including one with a single target site. The authors interpret this as reflecting the strength of the selective pressure and the difficulty of escaping a guide that is present before infection begins. The explanation for why the target was never mutated is not established by these experiments, and alternative explanations, such as functional constraint on the targeted coding sequence or on the inserted untranslated region, are not separately excluded here.

The discussion offers several hypotheses for why mammals use interferon, and these are explicitly speculative. They include that error-prone RNA viruses escape small RNA targeting readily and may have driven the emergence of a more general system, that DNA viruses including poxviruses, adenoviruses and herpesviruses do encode antagonists of small RNA pathways and one such ancient pathogen might have disabled an RNA interference response, that chordates lack the RNA-dependent RNA polymerase needed to amplify guides and lack the Dicer gene family expansion seen in plants, and that a non-viral pathogen such as an ancient protozoan or bacterium might have demanded a more general response. The authors write that such evolutionary questions are near impossible to address.

On NS1, the paper reports that it does not find NS1 to be an effective inhibitor of small RNA silencing, notes the small residual difference between wild-type and mutant NS1 genotypes, and attributes that difference more plausibly to defective interfering particles than to antagonism. That is an interpretation.

## Conceptual or technical advance

The work converts an evolutionary question into a testable protection experiment, and the result narrows the space of explanations. Because a reconstructed small RNA defense fully protected animals with no functional type I interferon receptor, the hypothesis that mammals abandoned RNA interference because it could not work in their cells is no longer available in that simple form.

Practically, the study produces an influenza strain that can be propagated in eggs at usable titers while being undetectable by plaque assay, protein expression or transcript level in mammalian cells, and that causes no disease at 25,000 plaque-forming units even without interferon signaling. The consistent failure of target-site escape across designs, contrasted with the ready guide-side escape of self-targeting viruses, bears directly on how attenuated strains and biocontainment layers built on microRNA targeting should be designed.

The calibration work is also reusable. The complementarity threshold near 16 nucleotides, and the estimate that a guide must reach roughly 100 to 1,000 copies per cell within the first six hours of infection to be effective, give quantitative design parameters for anyone building such systems.

## Relationship to the broader research program

This paper is the counterpart to the laboratory's own negative result. The earlier study by Backes and colleagues concluded that the mammalian response to virus infection is independent of small RNA silencing, and it is cited here in exactly that role. Taken together, the pair makes a two-part statement, that mammals do not use small RNA silencing against viruses and that they could have. Placing the two side by side is category 3 synthesis, and the corpus record for the earlier paper supports it.

The study also draws on and extends the laboratory's long-running engineering line, which includes microRNA-mediated species-specific attenuation of influenza A virus, hematopoietic-specific targeting of influenza, microRNA-based mitigation of gain-of-function influenza risk, engineered RNA viral synthesis of microRNAs, and the dengue tropism work. The self-targeting design here, in which the virus encodes a guide against its own genome, is a further step in that line.

Benitez and colleagues 2015 in the same journal, on in vivo RNA interference screening identifying MDA5 as a contributor to influenza defense, is cited here by the same first author and supports the statement that microRNA insertion does not inherently alter influenza biology.

## Related publications

- Backes, Langlois, Schmid, Varble, Shim, Sachs and tenOever 2014, Cell Reports, the mammalian response to virus infection is independent of small RNA silencing. Relationship predecessor. Cited for the conclusion that the dominant intrinsic mammalian response is interferon based, and the direct conceptual complement to this study.
- Varble and colleagues 2010, engineered RNA viral synthesis of microRNAs. Relationship methodological foundation. Source of the modified NS segment used for the self-targeting and guide-expressing viruses, and of the estimate of guide production kinetics during infection.
- Perez and colleagues 2009, Nature Biotechnology, microRNA-mediated species-specific attenuation of influenza A virus. Relationship predecessor. Source of target site designs and of the small RNA sequencing that identified microRNAs differentially expressed between eggs and mammalian lung.
- Langlois, Varble, Chua, Garcia-Sastre and tenOever 2012, Proceedings of the National Academy of Sciences, hematopoietic-specific targeting of influenza A virus. Relationship methodological foundation. Source of the approach to inserting target sites as an artificial 3-prime untranslated region of nucleoprotein.
- Langlois and colleagues 2013, Nature Biotechnology, microRNA-based strategy to mitigate the risk of gain-of-function influenza studies. Relationship predecessor and application. Source of miR-93 and miR-192 target designs.
- Pham, Langlois and tenOever 2012, PLoS Pathogens, replication in cells of hematopoietic origin is necessary for dengue virus dissemination. Relationship predecessor. Cited in the discussion as a case where virus escape occurred by excision.
- Benitez, Panis, Xue, Varble, Shim, Frick, Lopez, Sachs and tenOever 2015, Cell Reports, in vivo RNA interference screening identifies MDA5 as a contributor to cellular defense against influenza A virus. Relationship companion. Cited to support that microRNA insertion does not inherently perturb influenza biology.
- Bogerd, Whisnant, Kennedy, Flores and Cullen 2014, RNA, derivation of Dicer- and microRNA-deficient human cells. Relationship methodological foundation from another laboratory. Source of the NoDice cells.
- Varble and colleagues 2013. Relationship methodological foundation. Source of the control target sequence used for the five-site control virus.

## Limitations and boundaries

The response studied here is engineered, not endogenous. The guides are either host microRNAs already present before infection or a virus-encoded hairpin, and neither is generated by host recognition of viral double-stranded RNA. The study therefore tests whether a small RNA defense can protect a mammal, not whether mammals possess one, and the authors keep that distinction.

The kinetics differ from a genuine RNA interference response in a way the authors themselves raise. Host microRNAs are present before the virus arrives, which imposes selective pressure earlier and more strongly than a response that must first detect the pathogen. The timing experiment quantifies this and shows that guides supplied only 6 hours before infection fail to attenuate.

All of the virology is one virus, influenza A/Puerto Rico/8/34, a segmented negative-sense RNA virus with a nuclear replication cycle. Conclusions about other virus families, and in particular about the DNA viruses the discussion invokes as possible drivers of evolutionary change, are not tested.

The evolutionary conclusion is a possibility claim and cannot be more than that. The discussion offers several competing hypotheses for the emergence of the interferon system and the authors state that answers to such questions are near impossible to address.

Quantitative estimates carry caveats. The guide copy number of 100 to 1,000 per cell is inferred from Northern blot signal compared with a loading control and calibrated against published values for other microRNAs. The titer of the five-site targeted virus in eggs had to be converted from egg infectious dose because the virus would not plaque, so egg and cell titers are not directly comparable.

The absence of target-site escape is bounded by the passage regimes and sequencing depth used. Approximately ten passages in microRNA-expressing cells and one mixed-culture experiment are reported, with escape mutants characterized by plaque purification and sequencing rather than by deep sequencing of the population, so rare variants could be missed. The failure to recover virus after ten passages is reported as data not shown.

The animal work is confined to intranasal infection of C57BL/6 and Ifnar1 knockout mice at 6 to 8 weeks of age, with lungs assessed at days 2 and 9. Mice lacking the type I interferon receptor still have type III interferon and adaptive immunity, so this is a removal of one arm rather than of all antiviral defense, and the study does not test whether the engineered response would suffice in an animal more broadly immunocompromised.

Finally, the claim that the two pathways complement one another rests on comparing fold reductions across cell genotypes in single-cycle assays, which is consistent with additivity but is not a formal test of interaction.

## Audience summaries

### 25 words

Influenza was engineered so host small RNAs silence it. The resulting virus caused no disease in mice, including animals unable to respond to type I interferon.

### 75 words

Plants and insects fight viruses with RNA interference while mammals use interferon, and why the switch happened is unknown. Researchers rebuilt a small RNA defense by inserting microRNA target sites into influenza and by having the virus produce a guide against itself. Attenuation reached more than five logs, escape occurred only by deleting the guide rather than altering the target, and protection in mice was complete even without type I interferon signaling.

### 150 words

Chordates retain the small RNA machinery but defend against viruses through type I interferon rather than RNA interference, and it is unclear whether that reflects an incompatibility with mammalian cells. This study reconstructs a small RNA defense against influenza A virus in two ways, by inserting complementary target sites for cell-restricted or species-restricted host microRNAs and by engineering the virus to encode a small interfering RNA against its own nucleoprotein segment. Silencing required about 16 nucleotides of contiguous complementarity. Self-targeting attenuation was lost in Dicer-deficient cells, and escape variants always disabled guide production rather than altering the target. A virus carrying five mammalian microRNA target sites grew in eggs but was undetectable in mammalian cells and caused no morbidity in mice at 25,000 plaque-forming units, including in animals lacking the type I interferon receptor. The authors conclude that chordates could have used RNA interference in place of interferon.
