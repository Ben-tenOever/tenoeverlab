---
id: 2014-backes-the-mammalian-response-to-virus-in
slug: 2014-backes-the-mammalian-response-to-virus-in
source_pdf: Backes_et_al_CellReports2014.pdf
title: The Mammalian Response to Virus Infection Is Independent of Small RNA Silencing
authors: ["Simone Backes", "Ryan A. Langlois", "Sonja Schmid", "Andrew Varble", "Jaehee V. Shim", "David Sachs", "Benjamin R. tenOever"]
first_author: Simone Backes
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Benjamin R. tenOever"]
tenoever_position: 7
tenoever_role: senior
year: 2014
journal: Cell Reports
volume: "8"
issue: "1"
pages: "114-125"
doi: 10.1016/j.celrep.2014.05.038
pmid: "24953656"
pmcid: PMC4096324
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [small-rna-antiviral-defense]
themes: [does-mammalian-antiviral-rnai-exist]
pathogens: [vesicular stomatitis virus, influenza A virus, Sindbis virus, Borna disease virus, vaccinia virus]
viral_families: [Rhabdoviridae, Orthomyxoviridae, Togaviridae, Bornaviridae, Poxviridae]
biological_systems: [murine embryonic fibroblasts, Dicer-deficient fibroblasts, BHK cells, RAW macrophage cells, bone marrow derived macrophages, C6 glial cells, mouse lung, mouse spleen, Ifnar1 and Il28r double knockout mice]
host_species: [mouse, hamster]
technologies: [recombinant VSV reverse genetics, small RNA deep sequencing, mRNA sequencing, small RNA Northern blotting, quantitative RT-PCR, plaque assay, siRNA transfection, microRNA target site insertion]
key_concepts: [antiviral RNA interference, interferon response, virus-derived small RNAs, RISC, VP55 poly(A) polymerase, microRNA targetome, interferon-stimulated genes, Dicer independence, small RNA tailing and degradation, evolutionary divergence of antiviral strategies]
keywords: [RNAi, interferon, vesicular stomatitis virus, VP55, NS1, microRNA, Dicer, small RNA sequencing, antiviral defense, mammalian]
---

## Citation

Backes S, Langlois RA, Schmid S, Varble A, Shim JV, Sachs D, tenOever BR. The Mammalian Response to Virus Infection Is Independent of Small RNA Silencing. Cell Reports. 2014. Volume 8, Issue 1, pages 114-125.

DOI 10.1016/j.celrep.2014.05.038. PMID 24953656. PMCID PMC4096324.

## One-sentence contribution

Engineering vesicular stomatitis virus to eliminate RISC-loaded small RNAs attenuates rather than enhances replication in mice, and confers no replication advantage even when interferon signaling is removed, arguing that small RNA silencing does not contribute to mammalian antiviral defense.

## Executive summary

Plants, arthropods and nematodes defend against viruses using RNA interference, in which double-stranded viral RNA is processed into small interfering RNAs that guide cleavage of viral transcripts. Mammals detect the same double-stranded RNA but respond through interferon induction instead. Whether mammals also retain a functional antiviral RNA interference arm has been contested, and reports of virus-derived small RNAs in infected mammalian cells, together with observations that several viral double-stranded RNA binding proteins suppress silencing in heterologous systems, had kept the question open.

The study tests the question with a gain-of-function design. Rather than removing silencing components from the host, which also perturbs other biology, the authors give the virus the ability to remove small RNAs. Vaccinia virus VP55, a poly(A) polymerase previously shown by this group to tail and destroy RISC-associated small RNAs, was inserted into vesicular stomatitis virus, and a parallel virus carrying influenza A virus NS1 was built to blunt interferon induction for comparison.

If small RNAs contributed meaningfully to antiviral defense, the small RNA destroying virus should gain fitness. It did not. It replicated like the control virus in fibroblasts and in primary macrophages, and in wild-type mice it was attenuated by about a log, which transcriptome profiling attributes to derepression of interferon-stimulated transcripts normally held down by microRNAs. In mice lacking both type I and type III interferon receptors, all three viruses reached comparable titers.

## Scientific context

In plants, arthropods and nematodes, double-stranded RNA is recognized as a pathogen-associated molecular pattern and processed by Dicer-family RNase III nucleases into virus-derived small interfering RNAs that load into RISC and direct cleavage of complementary viral RNA. Viruses of these hosts have accordingly evolved suppressors of that pathway. Mammalian cells detect the same structures but convert detection into a transcriptional program, inducing type I and type III interferons and hundreds of interferon-stimulated genes, and mammalian viruses have evolved antagonists of that program.

The paper states that whether RNA interference is also a component of the mammalian response remains controversial. Arguments in favor include the conservation of the machinery and of microRNAs, the fact that several viral double-stranded RNA binding proteins that antagonize mammalian sensing also disrupt silencing in plants and flies, and an earlier report from this group identifying a genuine poxvirus inhibitor of small RNAs. Arguments against include that an influenza A virus lacking its double-stranded RNA antagonist regains full virulence in interferon-deficient mice, and that microRNA target sites can be inserted into a wide range of viruses to attenuate them, implying those viruses never evolved countermeasures against silencing.

Deep sequencing intensified rather than settled the debate. Virus-derived small RNAs are detectable in infected mammalian cells, but the paper notes they persist in the absence of Dicer and may be byproducts of interferon-stimulated genes such as RNase L. The paper identifies two recent reports, on a mutant nodavirus in stem cells and immortalized fibroblasts, as the studies that gave the idea of mammalian RNA interference renewed traction, and notes that both used multifunctional viral antagonists whose effects on the host response are not limited to small RNAs.

## Central question

Does small RNA silencing make a physiological contribution to the mammalian cellular response to virus infection, and if any contribution exists, is it masked by the interferon system?

## Experimental strategy

The central design choice is to perturb small RNA function from inside the virus rather than from the host genome. Removing Dicer or Argonaute from a cell changes microRNA-dependent gene regulation broadly and alters the starting state of the cell before infection begins. Encoding a small RNA destroying enzyme in the viral genome instead confines the perturbation to infected cells and to the window of infection, and it poses the question in the form evolution would pose it, namely whether a virus that can destroy host small RNAs gains fitness.

The enzyme is vaccinia virus VP55, which this group had previously shown adds non-templated adenosines specifically to RISC-associated small RNAs and triggers their degradation. A stabilized and more active variant identified by mutagenesis was used. Vesicular stomatitis virus was chosen as the vehicle because it is a vaccine strain highly sensitive to both interferon and to RNA interference in arthropod and nematode systems, so it should register any protective silencing that exists.

The comparison virus encoding influenza A virus NS1, a RIG-I antagonist, is the positive control for the logic of the experiment. It shows what a genuine gain in fitness from disabling a real antiviral system looks like in the same virus backbone and the same animals. A matched control virus carrying an RNA insert of comparable size with no open reading frame controls for the insertion.

Before that, the study characterizes the small RNA landscape across four virus families to ask whether any of these infections generates small RNAs with the size distribution and Dicer dependence expected of genuine RNA interference, and tests whether vesicular stomatitis virus encodes its own silencing suppressor, since a virus already able to block silencing would be uninformative.

Finally, the interferon receptor double knockout animals address the redundancy objection directly. If small RNA silencing were a secondary layer whose contribution is hidden behind interferon, then removing interferon should expose it, and destroying small RNAs should then help the virus.

## Key findings

1. Small RNA deep sequencing of cells infected with Borna disease virus, influenza A virus, Sindbis virus and vesicular stomatitis virus recovered reads mapping across each viral genome, at 0.04, 18.4, 24.1 and 0.05 percent of total small RNA reads respectively (Figure 1A). Only vesicular stomatitis virus showed a size preference, peaking at 22 nucleotides with enrichment at the genome ends (Figure 1A, Figure 1B). The two most abundant of these were detectable by Northern blot and were unchanged in Dicer-deficient cells (Figure 1C, Figure 1D). The observation is Dicer independence. The interpretation is that these species are not products of canonical RNA interference, and the authors use the size distribution as a reason to select this virus as the most demanding test case.

2. Inserting four perfectly complementary miR-142 target sites into the 3-prime untranslated region of the L polymerase message reduced titers by two logs in miR-142-expressing RAW macrophage cells, while all viruses grew comparably in cells lacking the microRNA (Figure 2B, Figure 2C, Figure S1). A virus carrying a primary miR-124 hairpin produced mature microRNA during infection (Figure 2D). The observation is that both the silencing arm and the hairpin processing arm operate normally during infection, so the virus does not encode a suppressor and RISC function is intact at least early in infection.

3. Vesicular stomatitis virus encoding VP55 expressed the protein robustly and tailed and degraded exogenously expressed miR-124 while leaving viral leader RNA and U6 intact (Figure 3B, Figure 3C). Transfected unmodified small interfering RNA against the nucleoprotein silenced the control virus but not the VP55 virus (Figure 3D), and sequencing of miR-146b from infected cells showed 82.1 percent of reads carrying non-templated adenosines (Figure 3E). The tool works as intended.

4. In Dicer-deficient cells, the VP55 virus and the control virus produced equivalent viral protein and reached comparable titers near 1 times 10 to the eighth plaque-forming units per milliliter (Figure 4A, Figure 4B), establishing that the insert itself carries no cost. In Dicer-expressing wild-type fibroblasts the two viruses were again indistinguishable in protein and titer (Figure 4C, Figure 4D) and at earlier time points (Figure S3). The observation is no fitness gain from eliminating small RNAs in cell culture.

5. In primary bone marrow derived macrophages the two viruses replicated comparably (Figure 5A) despite a pronounced loss of miR-142, miR-146, miR-155 and miR-93 with U6 unaffected (Figure 5B), so the absence of a phenotype is not explained by failure of the enzyme in primary cells.

6. Messenger RNA sequencing of infected macrophages found that the transcripts most affected by VP55 expression were predominantly canonical interferon-stimulated genes, including guanylate-binding proteins, cytokines, and components of sensing and signaling machinery, with independent confirmation by quantitative PCR for a subset (Figure 5C, Figure 5D, Table S2). Only two genes were higher in the control infection. The observation is a directional shift. The authors interpret it as consistent with microRNAs acting as negative regulators and with a prior report that microRNAs suppress basal antiviral transcript levels, and they explicitly caution that the data do not indicate specific targeting of this gene class, only that interferon-stimulated gene changes are the most prominent in the context of infection.

7. Intranasal infection of mice produced virus-derived small RNAs resembling those from fibroblasts but at levels the authors describe as vanishingly rare (Figure 6A, Table S3), and lung tissue from three animals showed significant loss of miR-146 with the VP55 virus (Figure 6B), confirming the enzyme works in vivo.

8. In wild-type fibroblasts the NS1-encoding virus showed dramatic loss of interferon beta induction while the control and VP55 viruses induced it robustly, with the VP55 virus modestly higher (Figure 6C). In wild-type mice, interferon beta induction inversely tracked titer. The NS1 virus exceeded control by more than a log in lung and spleen, and the VP55 virus was reduced by about a log, with reported p values of 0.0041, 0.0015 and 0.0365 for the indicated comparisons (Figure 6D).

9. In mice lacking both type I and type III interferon receptors, all three viruses reached comparable titers in lung and spleen with no significant differences (Figure 6E). The authors read this as showing that the NS1 advantage in wild-type animals was entirely attributable to muting interferon, that the VP55 attenuation was attributable to an enhanced interferon response, and that destroying small RNAs confers no benefit even with interferon removed.

## Mechanistic model

The study does not establish a mechanism for an antiviral activity, because its conclusion is that the activity is not present under the conditions tested. What it does propose a mechanism for is the direction of the phenotype it observed.

The model is that host microRNAs act as negative regulators that hold antiviral transcripts, including many interferon-stimulated genes, below their maximum in the infected cell. Destroying those microRNAs relieves that repression, raises the antiviral transcriptional output, and therefore attenuates the virus. On this reading the VP55 virus is attenuated not because small RNAs were protecting it, but because small RNAs were dampening the system that was. The evidence for the derepression step is the transcriptome comparison and the quantitative PCR confirmation, together with the modest rise in interferon beta induction in fibroblasts and the loss of the phenotype in interferon receptor knockout animals.

The negative claim is bounded by what a negative result can support, and the authors say so, writing that it is difficult to prove the absence of a biological activity and framing their result as a strong argument rather than a proof. The design does establish that eliminating RISC-loaded small RNAs gives this virus no replication advantage in fibroblasts, in Dicer-deficient cells, in primary macrophages, in wild-type mice, or in mice with both interferon systems removed. The interpretation that no functional antiviral RNA interference system is available to act on this virus in these settings follows from that, and is the authors' conclusion.

The authors additionally offer several supporting arguments that are reasoning rather than new data. They note that microRNAs pair only partially with targets and so would repress too weakly and too slowly to matter during an acute infection given typical protein half-lives, that mammalian viruses have not evolved suppressors of silencing whereas many can be attenuated by inserted microRNA target sites, that expressing an RNA-dependent RNA polymerase in mammalian cells is itself sufficient to induce type I interferon, and that mammals do not use the 2-prime-O-methylation chemistry that extends small RNA half-life in flies and plants outside of Piwi-interacting RNAs in stem and germ cells. These are category 2 and category 4 material and are presented in the discussion as such.

## Conceptual or technical advance

The work reframes a contested question as a fitness experiment. Instead of asking whether small RNAs derived from viral genomes can be detected, which deep sequencing had already answered affirmatively without settling anything, it asks whether a virus armed with the ability to destroy host small RNAs does better. That reframing is transferable to other proposed antiviral pathways.

The VSV-VP55 virus is itself a reusable reagent, and the authors say so, noting that it allowed the microRNA targetome to be mapped in infected cells from an in vivo infection and suggesting the same enzyme could be added to more inert vectors such as lentivirus or adenovirus for comparable studies.

The conclusion also has a practical consequence the authors draw out. If mammalian viruses do not contend with small RNA silencing, then the small RNA pathway remains available as an engineering handle, for controlling viral tropism, for building attenuated vaccines, for layered biocontainment, and for using RNA viruses as vehicles to deliver small interfering RNAs.

## Relationship to the broader research program

This paper is the conceptual pivot between two strands of the laboratory's work. One strand established that host small RNA pathways can be recruited to control viruses, through microRNA target site insertion to restrict tropism in influenza A virus and in dengue virus and through engineered viral synthesis of microRNAs. The other strand asked what those pathways are actually doing during infection. The immediate predecessor is the identification of VP55 as a poxvirus degrader of RISC-associated microRNAs, which supplied both the reagent used here and part of the argument that motivated the question.

Read together with the dengue and influenza targeting papers from the same group, the picture is coherent and is category 3 synthesis. Those studies depend on RISC functioning during infection, and this study reports directly that it does, while concluding that the virus gains nothing from shutting it down. The corpus records for those papers would be needed to support this as a formal cross-paper claim.

The finding that microRNAs restrain baseline antiviral transcript levels also connects to the laboratory's recurring interest in how the magnitude of the interferon response is set, and the microRNA targetome generated here is a resource pointed in that direction.

## Related publications

- Backes, Shapiro, Sabin, Pham, Reyes, Moss, Cherry and tenOever 2012, Cell Host and Microbe, degradation of host microRNAs by poxvirus poly(A) polymerase. Relationship predecessor and methodological foundation. Source of VP55 and of the finding that terminal RNA methylation protects small RNAs from tailing, which dictated the unmodified small interfering RNA chemistry used here.
- Langlois, Shapiro, Pham and tenOever 2012, Molecular Therapy, in vivo delivery of cytoplasmic RNA virus-derived microRNAs. Relationship methodological foundation. Source of the VSV construct expressing miR-124.
- Langlois, Varble, Chua, Garcia-Sastre and tenOever 2012, Proceedings of the National Academy of Sciences, hematopoietic-specific targeting of influenza A virus. Relationship predecessor. Part of the body of engineered microRNA targeting work cited as evidence that mammalian viruses lack silencing countermeasures, and source of small RNA amplification methods used here.
- Pham, Langlois and tenOever 2012, PLoS Pathogens, replication in cells of hematopoietic origin is necessary for dengue virus dissemination. Relationship predecessor. Cited among the engineered targeting studies that motivate the argument.
- Cullen, Cherry and tenOever 2013, Cell Host and Microbe, on whether RNA interference is a physiologically relevant innate antiviral response in mammals. Relationship review or synthesis. The review framing of the debate that this study addresses experimentally.
- Li and colleagues 2013 and Maillard and colleagues 2013, on virus-derived small interfering RNAs against a mutant nodavirus and against encephalomyocarditis virus. Relationship predecessors from other laboratories whose claims this study is designed to test, and whose limitations the discussion addresses directly.
- Seo and colleagues 2013, on microRNA suppression of basal antiviral transcripts. Relationship conceptual extension from another laboratory. The transcriptome result here is presented as being in agreement with it.

## Limitations and boundaries

The strongest conclusions rest on one virus in one backbone. Vesicular stomatitis virus was selected because it is highly sensitive to both interferon and, in invertebrate systems, to RNA interference, but a negative result in one rhabdovirus does not exclude a silencing contribution against other viruses, other tissues, or other infection kinetics. The small RNA profiling covers four families, but the functional tests do not.

The conclusion is a negative one, and the authors state plainly that it is difficult to prove the absence of a biological activity and that they regard their result as a strong argument rather than a demonstration of absence.

All in vivo work used intranasal inoculation and examined lung and spleen at 24 hours in wild-type animals and 48 hours in knockout animals, with different inoculum doses between the two, which limits direct quantitative comparison across the two mouse genotypes.

The perturbation is specific to RISC-associated small RNAs. VP55 tails and degrades small RNAs loaded into RISC, so activities of the small RNA machinery that do not proceed through that state, and any small RNA species resistant to tailing, would not be tested by this approach. Relatedly, 2-prime-O-methylated small RNAs are resistant to VP55, which is why unmodified duplexes were used in the silencing control.

Cell culture work relies substantially on immortalized fibroblasts, hamster kidney cells and a macrophage line in addition to primary bone marrow derived macrophages. The competing reports the study addresses proposed that RNA interference operates in undifferentiated stem cells and diminishes as cells become interferon responsive, and stem cells were not examined here.

VP55 is a viral enzyme with its own biology, and expressing it from the virus adds a foreign activity to the infection. The matched no-open-reading-frame control and the equivalence in Dicer-deficient cells address the insertion and the general burden, but they do not exclude effects of the enzyme unrelated to small RNA tailing.

The transcriptome analysis is correlative with respect to the attenuation mechanism. Derepression of interferon-stimulated transcripts is observed and the attenuation disappears in interferon receptor knockout mice, which is consistent, but no experiment restores individual repressed targets to test whether they account for the titer difference.

## Audience summaries

### 25 words

Giving a virus an enzyme that destroys host small RNAs made it grow worse, not better, arguing mammals do not use RNA silencing against viruses.

### 75 words

Plants and insects fight viruses with RNA interference, while mammals use interferon. Whether mammals also retain the RNA silencing defense has been disputed. Researchers armed vesicular stomatitis virus with a poxvirus enzyme that destroys host small RNAs. The armed virus gained no advantage in cells or mice, and was attenuated because losing microRNAs raised antiviral gene expression. Removing interferon signaling in mice erased all differences, indicating no hidden silencing contribution beneath interferon.

### 150 words

Whether mammals retain a functional antiviral RNA interference arm alongside interferon has been contested, with detectable virus-derived small RNAs on one side and the absence of viral silencing suppressors on the other. This study tests the question by arming vesicular stomatitis virus with vaccinia virus VP55, an enzyme that tails and destroys RISC-loaded small RNAs, and comparing it with a virus carrying influenza NS1 to blunt interferon induction. Small RNA profiling across four virus families found viral small RNAs that were, in the one case with an informative size distribution, Dicer independent. The VP55 virus destroyed host microRNAs efficiently yet gained no fitness in Dicer-deficient cells, fibroblasts or primary macrophages, and was attenuated about a log in mice. Transcriptome profiling attributed that attenuation to derepression of interferon-stimulated genes normally held down by microRNAs. In mice lacking type I and type III interferon receptors, all viruses replicated comparably.
