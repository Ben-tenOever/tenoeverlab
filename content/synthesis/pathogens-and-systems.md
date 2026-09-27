---
id: pathogens-and-systems
name: "Pathogens and Experimental Systems"
question: "Which agents, hosts and tissues does this corpus actually work in, and where does a finding made in one get tested in another?"
kind: cross-cutting synthesis
---

## The shape of the corpus

Across the 63 records, 43 distinct pathogens are named and assigned to 20 virus families. Two families dominate. Orthomyxoviridae appears in 42 records and Coronaviridae in 20. Rhabdoviridae follows with 14, then Togaviridae with 9, Paramyxoviridae with 8, Picornaviridae with 7 and Flaviviridae with 5. Poxviridae, Pneumoviridae, Adenoviridae, Herpesviridae, Retroviridae, Filoviridae, Arenaviridae, Bornaviridae, Dicistroviridae, Nodaviridae, Tombusviridae, Hepadnaviridae and Parvoviridae each appear once or twice. The canonical terms and the surface forms that map to them are recorded in the [controlled vocabulary](controlled-vocabulary.md) and in `data/vocabulary.json`.

The distribution understates how broad the testing is, because many of the single-appearance viruses appear inside panels assembled to ask whether a finding generalises. That pattern, a result obtained in one agent and then put to a second, is the most informative organising principle available for this corpus and is treated separately below.

## Influenza A virus

Influenza A virus is the resident system, present in 42 records, and it occupies three different roles.

As an object of study it carries the genome regulation work. Perez 2010 and Perez 2012 on small viral RNAs and the transcription to replication switch, Chua 2013 on suboptimal splicing of segment 8 as a timer, Nilsson-Payant 2021 in the Journal of Virology on nucleoprotein supply, Nilsson-Payant 2022 on ANP32A, and Oishi 2023 on the conserved kink-turn element in segment 8 all take the virus itself as the question.

As a chassis it carries most of the engineering. Perez 2009, Langlois 2012 in PNAS, Langlois 2013, Schmid 2014 in the Journal of Virology, Benitez 2015 in Cell Reports and Benitez 2015 in the in vivo screening paper all build on influenza reverse genetics.

As a comparator it supplies the benchmark against which the pandemic work is read. Blanco-Melo 2020 positions SARS-CoV-2 against influenza A virus in matched cells, Frere 2022 and Serafini 2023 use influenza as the benchmark virus for post-acute changes in hamsters, Oishi 2022 in the Journal of Virology runs the two viruses against each other in coinfection, and Hoagland 2021 treats both.

Named strains in the records include A/Puerto Rico/8/34, A/WSN/33, A/California/04/2009, an H3N2 isolate, and H5N1 A/Vietnam/1203/04. Langlois 2013 and Varble 2014 are the records where strain identity carries the argument, since both concern transmission phenotypes.

## Coronaviruses, and the SARS-CoV against SARS-CoV-2 distinction

Two different viruses sit behind the coronavirus work and should not be conflated.

SARS-CoV, the 2003 agent, appears in two records. Morales 2017 is the substantive one, and it is led by the Enjuanes and Sola laboratory in Madrid with the tenOever contribution given as reagents, conceptual advice and manuscript writing. That study works in mouse lung infected with the mouse-adapted MA15 strain and with an attenuated envelope-deleted derivative. Its claim about conservation in the human Urbani strain and in SARS-related bat viruses is a sequence comparison, not a demonstration in human virus. SARS-CoV also appears in Blanco-Melo 2020, where the record and the paper's own limitations state that the SARS-CoV-1 and MERS-CoV data were taken from a previously published dataset rather than generated alongside.

SARS-CoV-2 appears in 19 records, all from 2020 onward. Isolate USA-WA1/2020 is named in Hoagland 2021, Horiuchi 2021 and Carrau 2023, and the B.1.351 beta variant is the rechallenge virus in Horiuchi 2021. Two seasonal coronaviruses appear once each, human coronavirus 229E in Yaron 2022 as the second genus for the SRPK finding, and human coronavirus OC43 in Zazhytska 2022.

## Authentic virus against pseudotyped entry reporters

Four records use pseudotyped particles, and each is explicit about what that reports.

Han 2018 uses a beta-lactamase virus-like particle assay to separate entry from later steps in the influenza screen. Yang 2020 screens eight human pluripotent stem cell derivatives for entry with a vesicular stomatitis virus particle bearing SARS-CoV-2 Spike, then confirms positives with authentic SARS-CoV-2. The record notes two boundaries the authors state, that most permissiveness calls at the screening stage rest on a particle that reports entry only in a vesicular stomatitis virus context, and that the in vivo kidney capsule xenograft used pseudo-entry virus rather than authentic virus. Daniloski 2021 in eLife isolates the Spike D614G substitution using EGFP lentiviral pseudotypes and then reproduces the result with replication-competent virus through a trans-complementation assay, and the concordance between the two is itself part of the argument. Si 2021 runs a staged design set by containment, using spike-pseudotyped luciferase particles at biosafety level 2 for entry inhibition, then native virus in cells, then hamsters. That record records the authors' own caveat, that the chip data on SARS-CoV-2 speak to prophylaxis against initial infection rather than to therapy, because the pseudoparticles do not replicate.

Everything else in the SARS-CoV-2 corpus uses authentic virus.

## Other negative-sense RNA viruses

Vesicular stomatitis virus appears in 15 records and is used in three ways, as an interferon-sensitive readout virus in Sharma 2003 and Schmid 2014 in the Journal of Biological Chemistry, as an engineering chassis in Langlois 2012 in Molecular Therapy and Backes 2014, and as a panel member in Aguado 2018, Nilsson-Payant 2021, Paget 2023 and Manivasagam 2025.

Sendai virus appears in seven records, most often as a strong interferon inducer. Uhl 2023 uses it as the engineered chassis for the ADAR1 work, on the grounds that a nonsegmented negative-sense virus cannot recombine its way out of a targeted cassette. Measles virus, human parainfluenza virus 3, respiratory syncytial virus, Ebola virus and Lassa virus appear in panels. Borna disease virus appears once, in Backes 2014. Infectious salmon anemia virus appears once, in Oishi 2023, where it extends an orthomyxovirus splicing result to a fish pathogen.

## Positive-sense RNA viruses

Sindbis virus appears in nine records and is the workhorse of the small RNA work, chosen because it is cytoplasmic and tolerant of insertions. It carries the noncanonical biogenesis results of Shapiro 2010 and Shapiro 2012, the in vivo screening library of Varble 2013, and the Drosha restriction work of Shapiro 2014. Semliki Forest virus and Ross River virus appear once each in panels.

Among flaviviruses, dengue virus is the subject of Pham 2012, where the engineered tropism restriction demonstrates that dissemination requires replication in cells of haematopoietic origin. Zika virus, West Nile virus, Langat virus and hepatitis C virus appear in panels or in review.

Among picornaviruses, poliovirus appears in three records and coxsackievirus B3 in McCune 2020, a study led by another laboratory. Encephalomyocarditis virus appears in four, including Cullen 2013, where its behaviour in stem cells against somatic cells is used to argue that cell state rather than viral countermeasure explains the difference in small interfering RNA production.

Two non-animal viruses appear in Aguado 2017, Drosophila C virus and turnip crinkle virus, in service of the claim that the antiviral activity of RNase III proteins is a property of the protein fold rather than of one kingdom.

## DNA viruses and reverse-transcribing viruses

Vaccinia virus and Amsacta moorei entomopoxvirus appear in Backes 2012 as the source of the poly(A) polymerase that degrades host microRNAs, and vaccinia recurs in Backes 2014 and Aguado 2015. Human cytomegalovirus is the subject of Møller 2018. Adenovirus appears mostly as a delivery vector rather than as a pathogen. Human immunodeficiency virus 1 and bovine leukaemia virus appear in review and commentary. Hepatitis B virus and human parvovirus B19 appear only in Guzman-Solis 2021, a collaborative ancient DNA study working from archaeological dental remains, which stands apart from the rest of the corpus in both material and question.

## Where a finding was made in one pathogen and tested in another

This is the pattern that repays attention, and there are at least eight clear instances.

MicroRNA target site insertion was established in influenza A virus by Perez 2009, carried to dengue virus by Pham 2012, and to a herpesvirus genome by Møller 2018. Aguado 2018 then applied one targeted cassette as a common selective pressure across Sendai virus, influenza A virus, Sindbis virus, Semliki Forest virus, poliovirus and vesicular stomatitis virus, and found that escape by excision tracks genome polarity and recombination capacity, a proposition then tested directly with a single polymerase substitution.

Noncanonical cytoplasmic microRNA biogenesis was found with an alphavirus in Shapiro 2010 and Shapiro 2012, demonstrated in a negative-sense cytoplasmic virus and in animals in Langlois 2012 in Molecular Therapy, and shown in a nuclear RNA virus in Varble 2010.

The antiviral activity of Drosha, found with Sindbis virus and vesicular stomatitis virus in Shapiro 2014, was generalised in Aguado 2017 from bacteria through yeast to a urochordate and tested against alphaviruses, a flavivirus, influenza A virus, Sendai virus, an insect dicistrovirus and a plant tombusvirus, in human cells, Drosophila cells, zebrafish embryos and Arabidopsis protoplasts.

Small viral RNA was described in influenza A virus by Perez 2010 and Perez 2012 and then looked for in a coronavirus by Morales 2017. Reading the two together gives a contrast rather than a continuity, since the influenza species come from noncoding segment ends and act on the viral life cycle while the SARS-CoV species come from coding regions and act on host pathology.

The coupling between nucleoprotein scarcity and host recognition, established for influenza A virus in Nilsson-Payant 2021, held across Sendai virus, human parainfluenza virus 3, measles virus, respiratory syncytial virus, vesicular stomatitis virus, Ebola virus and Lassa virus, and failed for the SARS-CoV-2 nucleocapsid. The failure is the informative part, because it sets a boundary on the principle.

Occlusion of orthomyxovirus splicing by the archaeal protein L7Ae, shown for influenza A virus in Oishi 2023, extended to influenza B virus and to infectious salmon anemia virus, which converts a feature described for one virus into a family-level property.

Capicua, found as a repressor in an influenza screen by Han 2018, was tested in Manivasagam 2025, a collaborative study, against respiratory syncytial virus, human parainfluenza virus 3, Sendai virus, encephalomyocarditis virus, Zika virus and vesicular stomatitis virus, which makes the axis virus-nonspecific.

The tension between ADAR1 and effective antiviral RNA interference, inferred from mammalian work in Uhl 2023, was tested by moving the mammalian enzyme into a plant with a functioning endogenous silencing system, Nicotiana benthamiana, which is the most direct test of that proposition available in the corpus.

## Host species

Human material appears in 57 records and mouse in 39. Golden hamster is credited in 18, but that count needs a caveat that the vocabulary file records. In the earlier small RNA papers the host annotation "hamster" denotes BHK-21 baby hamster kidney cells rather than the animal, and the hamster as an animal model enters the corpus only with Hoagland 2021 and the records that follow it. Dog appears in 13 records and is almost always MDCK cells. Chicken appears in nine, as embryonated eggs and as DF-1 fibroblasts. African green monkey appears in five and is Vero or Vero E6. Ferret appears in four, in Langlois 2013, Varble 2014, Blanco-Melo 2020 and the tenOever 2019 review. Guinea pig appears once, in Varble 2014.

Beyond vertebrates the corpus reaches Drosophila melanogaster in four records, and once each to zebrafish, Arabidopsis thaliana, Nicotiana benthamiana, a lepidopteran insect cell line, mosquito cells, yeast, bacteria and archaea. Most of these are in the two evolutionary papers, tenOever 2016 and Aguado 2017.

## Cell and tissue systems

The 240 system strings collapse to 197 canonical entries, and the concentration is narrow at the top. The HEK293 and HEK293T family appears in 25 records once its spellings are merged, mouse embryonic fibroblasts in 22, A549 cells in 21, MDCK in 18, BHK-21 in 12 and Vero E6 in 11.

The distinctive asset is not any single line but the genetic panel of fibroblasts and 293T derivatives assembled for the small RNA work, lacking Dicer, Drosha, DGCR8, Argonaute, the interferon alpha receptor, IRF3 and IRF7 together, STAT1, MAP3K8 or Zfx. Shapiro 2010, Shapiro 2012, Shapiro 2014, Aguado 2017, Aguado 2018 and Uhl 2023 all depend on it, and the NoDice HEK293T background recurs through Aguado 2015, Benitez 2015 and Nilsson-Payant 2021.

For SARS-CoV-2 the permissive systems are engineered or selected. A549 cells expressing ACE2 appear in nine records, and Blanco-Melo 2020 flags the adenoviral route of ACE2 delivery as an artificial arrangement that introduces a second virus. Calu-3, Caco-2, Huh7.5-ACE2 and HeLa-ACE2 fill out the panel used in Daniloski 2021 in Cell, Daniloski 2021 in eLife and Nilsson-Payant 2021 on NF-kB.

Primary and differentiated human systems enter mainly with the pandemic work. Primary human bronchial epithelial cells appear in Blanco-Melo 2020, Bouhaddou 2020 and Si 2021, airway basal stem cells at an air liquid interface in Si 2021, pluripotent stem cell derivatives and organoids in Yang 2020, and ocular surface cultures with a whole-eye differentiation model in Eriksen 2021.

Human clinical and post-mortem material appears in seven records and is always used as a point of contact rather than as the primary system. Post-mortem lung in Blanco-Melo 2020 and Yang 2020, COVID-19 cadaver lung in Oishi 2022 in Cell Reports, olfactory epithelium and bulb in Frere 2022 and Zazhytska 2022, ocular surface tissue in Eriksen 2021, patient serum in Blanco-Melo 2020, and archaeological dental remains in Guzman-Solis 2021.

## Publications referenced
- 2003-sharma-triggering-the-interferon-antivira
- 2009-perez-microrna-mediated-species-specific
- 2010-perez-influenza-a-virus-generated-small-
- 2010-shapiro-noncanonical-cytoplasmic-processin
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2012-backes-degradation-of-host-micrornas-by-p
- 2012-langlois-hematopoietic-specific-targeting-o
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
- 2012-perez-a-small-rna-enhancer-of-viral-poly
- 2012-pham-replication-in-cells-of-hematopoie
- 2012-shapiro-evidence-for-a-cytoplasmic-micropr
- 2013-chua-influenza-a-virus-utilizes-subopti
- 2013-cullen-is-rna-interference-a-physiologica
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2014-backes-the-mammalian-response-to-virus-in
- 2014-schmid-a-versatile-rna-vector-for-deliver
- 2014-schmid-mitogen-activated-protein-kinase-m
- 2014-shapiro-drosha-as-an-interferon-independen
- 2014-varble-influenza-a-virus-transmission-bot
- 2015-aguado-microrna-function-is-limited-to-cy
- 2015-benitez-engineered-mammalian-rnai-can-elic
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2016-tenoever-the-evolution-of-antiviral-defense
- 2017-aguado-rnase-iii-nucleases-from-diverse-k
- 2017-morales-sars-cov-encoded-small-rnas-contri
- 2018-aguado-homologous-recombination-is-an-int
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2018-m-ller-mirna-mediated-targeting-of-human-
- 2019-tenoever-synthetic-virology-building-viruse
- 2020-blanco-melo-imbalanced-host-response-to-sars-c
- 2020-bouhaddou-the-global-phosphorylation-landsca
- 2020-mccune-rapid-dissemination-and-monopoliza
- 2020-yang-a-human-pluripotent-stem-cell-base
- 2021-daniloski-identification-of-required-host-fa
- 2021-daniloski-the-spike-d614g-mutation-increases
- 2021-eriksen-sars-cov-2-infects-human-adult-don
- 2021-guzman-solis-ancient-viral-genomes-reveal-intro
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2021-horiuchi-immune-memory-from-sars-cov-2-infe
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2021-nilsson-payant-the-nf-b-transcriptional-footprint
- 2021-si-a-human-airway-on-a-chip-for-the-r
- 2022-frere-sars-cov-2-infection-in-hamsters-a
- 2022-nilsson-payant-the-host-factor-anp32a-is-required
- 2022-oishi-a-diminished-immune-response-under
- 2022-oishi-the-host-response-to-influenza-a-v
- 2022-yaron-host-protein-kinases-required-for-
- 2022-zazhytska-non-cell-autonomous-disruption-of-
- 2023-carrau-delayed-engagement-of-host-defense
- 2023-oishi-archaeal-kink-turn-binding-protein
- 2023-paget-stress-granules-are-shock-absorber
- 2023-serafini-sars-cov-2-airway-infection-result
- 2023-uhl-adar1-biology-can-hinder-effective
- 2025-manivasagam-transcriptional-repressor-capicua-
