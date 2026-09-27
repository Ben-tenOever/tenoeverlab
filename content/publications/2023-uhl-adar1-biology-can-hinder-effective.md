---
id: 2023-uhl-adar1-biology-can-hinder-effective
slug: 2023-uhl-adar1-biology-can-hinder-effective
source_pdf: Uhl_et_al_JVI2023.pdf
title: ADAR1 Biology Can Hinder Effective Antiviral RNA Interference
authors: ["Skyler Uhl", "Chanyong Jang", "Justin J. Frere", "Tristan X. Jordan", "Anne E. Simon", "Benjamin R. tenOever"]
first_author: Skyler Uhl
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Benjamin R. tenOever"]
tenoever_position: 6
tenoever_role: senior
year: 2023
journal: Journal of Virology
volume: "97"
issue: "4"
pages: e00245-23
doi: 10.1128/jvi.00245-23
pmid: "37017521"
pmcid: PMC10134826
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [small-rna-antiviral-defense, viral-populations-evolution]
themes: [reconstructing-antiviral-rnai, recombination-and-escape]
pathogens: [Sendai virus, influenza A virus]
viral_families: [Paramyxoviridae, Orthomyxoviridae]
biological_systems: [A549 cells, STAT1 knockout A549 cells, ADAR1 knockout A549 cells, MDCK cells, mouse embryonic fibroblasts, NoDice HEK293T cells, BSRT7 cells, Nicotiana benthamiana]
host_species: [human, mouse, canine, hamster, Nicotiana benthamiana]
technologies: [paramyxovirus reverse genetics, microRNA target site engineering, CRISPR knockout, RNA sequencing, amplicon sequencing, high-content microscopy, flow cytometry, adenoviral reconstitution, agroinfiltration, phylogenetic analysis]
key_concepts: [antiviral RNA interference, adenosine to inosine RNA editing, ADAR1 p110 and p150 isoforms, viral escape from silencing, hypermutation, negative-sense RNA virus constraints, ribonucleoprotein protection of genomes, viral suppressors of RNA silencing, incompatibility of ADAR1 and RNAi]
keywords: [ADAR1, RNA editing, Sendai virus, RNA interference, microRNA targeting, viral escape, Nicotiana benthamiana, interferon]
---

## Citation

Uhl S, Jang C, Frere JJ, Jordan TX, Simon AE, tenOever BR. ADAR1 Biology Can Hinder Effective Antiviral RNA Interference. Journal of Virology. 2023. Volume 97, issue 4, article e00245-23.

DOI 10.1128/jvi.00245-23. PMID 37017521. PMCID PMC10134826.

## One-sentence contribution

Escape of a microRNA-targeted Sendai virus from engineered antiviral RNA interference comes not from the virus but from host ADAR1, whose adenosine to inosine editing destroys the target sites, and human ADAR1 also suppresses endogenous silencing in a plant.

## Executive summary

Mammalian cells can be made to mount something close to antiviral RNA interference by embedding perfectly complementary microRNA target sites in an essential viral gene, which converts endogenous microRNAs into cleaving guides through Argonaute 2. Earlier work from this laboratory had shown that positive-sense RNA viruses escape this pressure by homologous recombination while negative-sense viruses do not, apparently lacking a route out. Here a recombinant Sendai virus carrying five microRNA target sites in the 3' untranslated region of the nucleoprotein gene was held under sustained infection rather than serial passage, and escape appeared at six to eight days in roughly 8 percent of wells. Sequencing of escape variants showed neither deletion of the cassette nor random point mutation but a dense pattern of A to G changes confined to the target sites, the signature of adenosine deaminase acting on RNA. Knockout of ADAR1 in a STAT1 deficient background abolished escape in all 96 wells, and adenoviral reconstitution of ADAR1 restored it. Escape also occurred when the cassette was moved to the phosphoprotein gene, where editing appeared on the antigenome rather than the genome. Across a phylogenetic sampling, ADAR1 orthologs were found in species with interferon or interferon-like defenses and absent from those with well-characterized antiviral RNA interference, and expressing human ADAR1 in Nicotiana benthamiana suppressed silencing of a green fluorescent protein reporter.

## Scientific context

Eukaryotic antiviral defenses against RNA fall broadly into two designs, an RNA-based one in which host nucleases are guided by small RNAs derived from the pathogen, found in plants, insects and nematodes, and a protein-based one in which pattern recognition receptors detect pathogen-associated molecular patterns and induce interferon and interferon-stimulated genes, used by vertebrates. Both are triggered by double-stranded RNA. Whether mammals also retain functional antiviral RNA interference has been reported by several groups and remains contested.

Two prior results from this laboratory set up the experiment. Benitez and colleagues had shown that inserting perfectly complementary microRNA target sites into a virus recreates something functionally equivalent to antiviral RNA interference in mammalian cells and can substitute for the interferon system. A later comparative study applied that same pressure across diverse RNA viruses and found that positive-sense viruses escape by homologous recombination, through polymerase template switching that removes the cassette, while negative-sense viruses showed no escape, consistent with their general inability to recombine. Because negative-sense RNA viruses nevertheless exist in hosts with functional antiviral RNA interference, the authors reasoned that some route to escape must exist, and asked whether more time or weaker pressure would reveal it.

## Central question

Given that negative-sense RNA viruses cannot remove a microRNA targeting cassette by recombination, can they escape RNA interference pressure at all, and if so by what route.

## Experimental strategy

The system imposes a defined, uniform silencing pressure whose escape can be read at single-well resolution. A green fluorescent protein expressing recombinant Sendai virus carries five distinct microRNA target sites in the 3' untranslated region of the nucleoprotein gene, so that endogenous microRNAs of epithelial cells direct Argonaute 2 cleavage of the positive-sense antigenome and nucleoprotein messenger RNA. Two controls define the axes. A construct with the same sequence in reverse complement orientation places the sites on the genome, which is inaccessible inside the ribonucleoprotein, and so reports the cost of the insert without the silencing. A single target site construct lowers the pressure, which separates escape that requires one change from escape that would require five.

Two design choices matter for what was found. Sustained infection replaces serial passage, so that rare escape events are not diluted away by transfer, and readout is by fluorescence in 96-well format, which turns escape frequency into a countable quantity. Genetics then tests causality rather than correlation. ADAR1 is knocked out in a STAT1 deficient background, necessary because losing ADAR1 in interferon-competent cells triggers interferon and cell death, and the phenotype is restored by adenoviral reconstitution so that clonal and off-target explanations are addressed.

Moving the cassette from nucleoprotein to phosphoprotein separates two confounded variables, since silencing nucleoprotein exposes the genome and triggers innate sensing while silencing phosphoprotein attenuates comparably without that exposure. Finally, the question is taken outside mammals in two directions, by phylogenetic survey of the ADAR family against the defense system each species uses, and by expressing human ADAR1 in a plant that has endogenous RNA silencing and no ADARs, with a known viral suppressor as the positive control.

## Key findings

1. Under serial passage, the five target virus was undetectable while the reverse control produced uniform fluorescence, reproducing prior work, and the single target virus produced scattered fluorescent cells (Figure S1A).
2. Under sustained infection without passaging, the single target virus reached control levels of replication by six days, and the five target virus became fluorescent at six days and clearly positive by eight days, escaping in roughly 8 percent of individual wells. Flow cytometry and nucleoprotein immunoblotting agreed with the imaging (Figures 1B, 1C, 1D and S1C).
3. Escape of the single target virus was by point mutation. Around 75 percent of reads at the miR-21 site carried an A to U change in the seed region, with three shared U to C transitions at 5 to 10 percent, two of them in the seed. No elevated mutation frequency was seen in the surrounding region (Figures 2B and S2A).
4. Escape of the five target virus involved neither deletion of the cassette nor scattered point mutation, which is what recombination-based escape would have produced. Instead there were dense U to C transitions in the positive sense, corresponding to A to G changes in the genome, within each target site (Figures 2C and S2B).
5. Amplicon sequencing over time detected low-frequency edits by two days that became dominant by four and eight days, indicating that edited genomes outcompete unedited ones rather than arising late (Figures 2D and S2B).
6. Escape persisted in STAT1 knockout cells with the same editing signature, was observed in none of 96 wells when ADAR1 was additionally knocked out, and was restored when ADAR1 was reconstituted by adenovector, which expressed both the p110 and p150 isoforms (Figures 3A to 3D and S3C).
7. Moving the cassette to the phosphoprotein gene gave comparable attenuation, more than a hundredfold reduction in viral RNA relative to control, but without the strong interferon-stimulated gene response seen with nucleoprotein targeting, consistent with the genome remaining protected (Figures 4B and 4C).
8. The phosphoprotein-targeted virus also escaped, from four days, at lower frequency than the nucleoprotein-targeted virus, and with the same A to G signature. The editing was on the antigenome rather than the genome, and the pattern was more heterogeneous, not always disrupting all five sites, which the authors read as indicating that low levels of phosphoprotein may suffice for limited replication (Figures 4D, 4E, S4A to S4C).
9. Escape with the same editing signature occurred in canine MDCK cells and in mouse embryonic fibroblasts, so the phenotype is not specific to human ADAR1. Escape mutants from these cells carried fewer edits across the cassette, which the authors attribute to the absence of some cognate microRNAs, noting that MDCK cells lack miR-192 and miR-31 (Figures 5B to 5D and S5).
10. Across the species sampled, adenosine deaminases acting on transfer RNA were universal, while the ADAR1 ortholog was present in species with a known interferon or interferon-like system and absent from those with well-characterized antiviral RNA interference. The authors describe this analysis as limited in scope and note it agrees with more extensive published analyses from other groups (Figure 5A).
11. Agroinfiltration of human ADAR1 into Nicotiana benthamiana alongside a green fluorescent protein plasmid increased reporter expression, with p110 more effective than p150, against the tomato bushy stunt virus P19 suppressor as positive control. The authors argue that the differential effect among P19, p110 and p150 rules out simple competition for translational machinery (Figure 5E and S5E).

## Mechanistic model

The causal chain from ADAR1 to escape is established by genetics, since knockout abolishes escape and reconstitution restores it, and by the editing signature itself. What is not established, and the authors say so directly, is how ADAR1 comes to edit these particular sequences. They state that the dynamics of how this editing occurs remain somewhat uncertain and that distinguishing a direct from an indirect role for microRNAs will be difficult, because the escape frequency is too low for biochemistry and there are few other ways to impose this degree of attenuation while also generating double-stranded RNA.

Two models are laid out. In the indirect model, ADAR1 acts on double-stranded RNA formed between genome and antigenome, or on cleaved viral messenger RNA, or on a highly complementary species such as a defective viral genome, with editing more active in the nucleoprotein-targeted virus because silencing nucleoprotein exposes the genome. In the direct model, the RISC recruits ADAR1, for which there is published evidence of an ADAR1 interaction with Dicer from another group, and editing then occurs at or opposite the bound sites.

The data cut both ways and the authors present them that way. Editing of the nucleoprotein-targeted virus is on the genome, which microRNAs do not bind, which argues against direct recruitment, while editing of the phosphoprotein-targeted virus is on the antigenome, which does conform to the direct model. The observation that escape mutants from MDCK cells, which lack two of the five cognate microRNAs, carry edits at fewer sites is offered as tempting to speculate in favor of a direct role, since genome and antigenome duplex formation should produce editing across the whole cassette regardless of which microRNAs are present. The authors propose as one possibility that RISC engagement of the nascent messenger RNA recruits ADAR1 to the aligned genomic template, which would reconcile the two observations, but this is put forward as a possible mechanism and not demonstrated.

The evolutionary claim is correlative. The distribution of ADAR1 across species with interferon-like versus RNA interference-based defense, together with the plant experiment, is presented as evidence that ADAR1 is disruptive to RNA silencing and as a possible explanation for its absence where that defense is essential. The authors note that many explanations exist for gene loss and that if RNA interference does function antivirally in some mammalian cells then how ADAR1 operates there is unclear, raising the possibility that it negatively regulates both systems in a context-dependent way as reported for Caenorhabditis elegans ADARs by another group.

## Conceptual or technical advance

The result reframes what escape from antiviral RNA interference can mean. Escape here is not a viral adaptation at all. The virus acquires no antagonist and performs no recombination, and the selective pressure is relieved by a host enzyme acting on the virus in a way that happens to destroy the guide binding sites. That makes a host editing enzyme, rather than a virally encoded suppressor, the relevant actor, and it explains why negative-sense viruses that cannot recombine are nonetheless not trapped.

It also supplies a functional argument that connects two literatures. If ADAR1 activity degrades the sequence fidelity that perfect complementarity requires, then ADAR1 and effective antiviral RNA interference are in tension, which offers a reason for the observed phylogenetic anticorrelation between them and connects to the broader question of why vertebrates use interferon rather than small RNA defense. The plant experiment is the most direct test of that tension available here, since it introduces the mammalian enzyme into a functioning endogenous silencing system.

Practically, the finding matters for any attempt to build microRNA-based antiviral control or microRNA-based attenuation into a vector, since it identifies a host-driven route by which such designs erode over time.

## Relationship to the broader research program

This paper continues a line running through the laboratory's work on whether mammals can be made to use RNA-based antiviral defense and what happens when that pressure is applied. Benitez and colleagues established that engineered microRNA targeting can substitute for interferon, and the immediately preceding comparative study established the difference between positive-sense and negative-sense viruses under that pressure. The recombinant Sendai virus constructs and the five target cassette come from that prior work.

Category 3 synthesis. Read with the laboratory's 2016 Perspective, which argued that chordates lost RNA interference because systemic small RNA defense is incompatible with interferon biology, this study supplies a second and different incompatibility, at the level of a single interferon-associated enzyme rather than at the level of the pathway. The two arguments are independent and are not claimed together in either paper, but together they make the loss of antiviral RNA interference in vertebrates look overdetermined. The interest in ribonucleoprotein protection of negative-strand genomes from small RNA targeting also connects back to the laboratory's early observation that influenza genomic RNA is not accessible to RISC.

## Related publications

- Benitez and colleagues, 2015, Engineered Mammalian RNAi Can Elicit Antiviral Protection that Negates the Requirement for the Interferon Response, cited as reference 37 from the same laboratory. Methodological foundation and predecessor.
- The immediately preceding comparative escape study from this laboratory, cited as reference 38, which established recombination-mediated escape in positive-sense viruses and its absence in negative-sense viruses. Predecessor, and the study this work directly extends.
- The prior study supplying the recombinant Sendai virus genomes and the N5T and N5R stocks, cited as references 43 and 78. Methodological foundation.
- Varble and colleagues, 2010, Engineered RNA viral synthesis of microRNAs. Predecessor from the same laboratory, reporting that negative-sense genomic RNA within the ribonucleoprotein is not accessible to microRNA-directed silencing.
- tenOever, 2016, The Evolution of Antiviral Defense Systems. Review or synthesis from the same author, supplying the evolutionary framing of why vertebrates use interferon rather than RNA interference.
- Work from another group on ADAR1 association with the RISC through Dicer, cited as reference 57, which motivates the direct recruitment model. Conceptual foundation.
- Work from another group on Caenorhabditis elegans ADARs preventing Dicer processing of host transcripts, cited as reference 67. Conceptual foundation for the closing argument.

## Limitations and boundaries

All virological work is in cultured cells, with no animal infection and no test of whether ADAR1-mediated escape occurs in vivo or affects pathogenesis. The central genetics is performed in a STAT1 knockout background, required because ADAR1 loss in interferon-competent cells causes interferon induction and death, so escape and its abolition were established in cells that cannot mount a STAT1-dependent response. The authors verified that escape and editing still occur in STAT1 knockout cells, but the ADAR1 requirement itself was not demonstrated in a fully interferon-competent setting.

The system is an engineered mimic of antiviral RNA interference, and the authors state its two departures from endogenous RNA interference. Endogenous small interfering RNAs require early viral replication to generate substrate, which gives a virus time to antagonize the pathway, and they are biased to the ends of the genome, whereas the microRNA targets used here are internal and act immediately. The authors argue the plant result mitigates concern about where targeting occurs, but the mismatch remains.

Escape is rare, at roughly 8 percent of wells for the nucleoprotein-targeted virus and lower for the phosphoprotein-targeted one, and that rarity is itself a limit, since the authors note it puts biochemical characterization of the editing event out of reach. The mechanism of ADAR1 recruitment is explicitly unresolved, with two models that the data support unevenly, and the inference favoring direct microRNA involvement rests on fewer edits in MDCK cells, which is attributed to a published microRNA profile rather than measured here, with the microRNA profile of mouse embryonic fibroblasts stated to be unknown.

The result does not generalize across RNA viruses. The authors report that they again attempted to generate an escape mutant of a five target recombinant influenza A virus and observed neither editing nor escape, and offer replication site and genome packaging as possible reasons without resolving them. The phylogenetic analysis is described by the authors as limited in scope and is correlative, so it cannot establish that ADAR1 presence and antiviral RNA interference are mutually exclusive by causation. The plant experiment uses a transgene reporter and agroinfiltration rather than virus infection, shows suppression by both isoforms with p110 stronger, which differs from a published report in Drosophila where interference was attributed to p150, and that discrepancy is noted but not explained.

## Audience summaries

### 25 words

A virus put under engineered RNA silencing pressure escaped, but the change came from the host. ADAR1 edited the target sites away, rescuing the virus.

### 75 words

Mammalian cells can be forced to silence a virus by inserting perfectly matched microRNA target sites into an essential viral gene. A Sendai virus under this pressure eventually escaped, not by mutating or deleting the cassette, but because the host enzyme ADAR1 edited adenosines within the target sites. Deleting ADAR1 abolished escape and restoring it brought escape back. Human ADAR1 expressed in a plant also suppressed that plant's own gene silencing.

### 150 words

Negative-sense RNA viruses cannot recombine, and a previous study found they could not escape engineered microRNA-directed silencing, unlike positive-sense viruses. Holding infections without passage rather than serially passaging revealed escape of a five-target Sendai virus at six to eight days in about 8 percent of wells. Sequencing showed no deletion and no random mutation, but dense A to G transitions confined to the target sites. Knocking out ADAR1 in a STAT1 deficient background eliminated escape in all 96 wells, and adenoviral reconstitution restored it. Moving the cassette to the phosphoprotein gene, which attenuates without exposing the genome, also permitted escape, with editing on the antigenome rather than the genome. Whether ADAR1 is recruited by the silencing complex or acts on duplex viral RNA is unresolved. ADAR1 orthologs track with interferon-based defense across species, and human ADAR1 suppressed endogenous silencing in Nicotiana benthamiana.
