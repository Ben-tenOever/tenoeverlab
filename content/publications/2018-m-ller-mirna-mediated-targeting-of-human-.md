---
id: 2018-m-ller-mirna-mediated-targeting-of-human-
slug: 2018-m-ller-mirna-mediated-targeting-of-human-
source_pdf: Moller_et_al_PNAS2018.pdf
title: miRNA-mediated targeting of human cytomegalovirus reveals biological host and viral targets of IE2
authors: ["Rasmus Møller", "Toni M. Schwarz", "Vanessa M. Noriega", "Maryline Panis", "David Sachs", "Domenico Tortorella", "Benjamin R. tenOever"]
first_author: Rasmus Møller
senior_authors: ["Domenico Tortorella", "Benjamin R. tenOever"]
corresponding_authors: ["Domenico Tortorella", "Benjamin R. tenOever"]
tenoever_position: 7
tenoever_role: senior
year: 2018
journal: Proceedings of the National Academy of Sciences
volume: "115"
issue: "5"
pages: "1069-1074"
doi: 10.1073/pnas.1719036115
pmid: "29339472"
pmcid: PMC5798380
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [programmable-virology]
themes: [cell-type-restriction-as-a-tool]
pathogens: ["human cytomegalovirus"]
viral_families: ["Herpesviridae"]
biological_systems: ["MRC-5 fibroblasts", "THP-1-derived macrophages", "miR-122-expressing MRC-5 fibroblasts", "miR-142-expressing MRC-5 fibroblasts", "TB40/E bacterial artificial chromosome"]
host_species: ["human"]
technologies: ["galK one-step BAC recombineering", "microRNA target site insertion", "lentiviral microRNA transduction", "small RNA Northern blot", "RNA sequencing", "differential expression analysis with DESeq2", "gene ontology enrichment analysis", "multicycle growth curves", "plaque and TCID50 titration", "quantitative RT-PCR"]
key_concepts: ["cell-type-specific conditional knockdown", "hematopoietic-specific microRNA targeting", "immediate early gene circuitry", "IE2 autorepression through the cis-repression sequence", "essential gene function in myeloid cells", "herpesvirus latency models", "viral transcriptional cascade", "host transcriptome remodelling", "engineered viral vectors"]
keywords: ["human cytomegalovirus", "IE2", "IE1", "miR-142", "myeloid cells", "macrophages", "recombineering", "conditional knockout", "latency", "microRNA targeting"]
---

## Citation

Møller R, Schwarz TM, Noriega VM, Panis M, Sachs D, Tortorella D, tenOever BR. miRNA-mediated targeting of human cytomegalovirus reveals biological host and viral targets of IE2. Proceedings of the National Academy of Sciences. 2018. Volume 115, issue 5, pages 1069-1074.

DOI 10.1073/pnas.1719036115. PMID 29339472. PMCID PMC5798380.

## One-sentence contribution

A one-step recombineering strategy that inserts hematopoietic-specific miR-142 target sites into the untranslated region of the human cytomegalovirus IE2 transcript permits virus rescue in fibroblasts while silencing IE2 selectively in myeloid cells, revealing that IE2 loss raises rather than abolishes replication in macrophages.

## Executive summary

Human cytomegalovirus persists in a large fraction of the human population and causes serious disease in neonates and immunocompromised people, yet the biology of its latent phase in myeloid cells remains poorly defined. A central technical obstacle is that viral mutants must be rescued in fibroblasts, which means genes essential for acute fibroblast infection cannot be deleted even when their function in myeloid lineages is the question of interest. The authors address this by making the silencing conditional on cell lineage rather than on temperature or a small molecule. Four perfectly complementary target sites for the hematopoietic-restricted microRNA miR-142 were inserted into the noncoding 3 prime untranslated region of IE2 in the TB40/E bacterial artificial chromosome using a single galK-based recombination step with loxP-flanked selection. Because fibroblasts lack miR-142, the recombinant virus grew normally during rescue and in multicycle growth curves. In THP-1-derived macrophages, IE2 protein was silenced, derepression of the cis-repression sequence produced a large excess of IE1, and virus titres were sustained at levels roughly two to three logs above the untargeted control, which declined over ten days. RNA sequencing showed that IE2 loss reshaped both the viral and the host transcriptome in a cell-type-dependent way, with more than 750 host genes differentially expressed in macrophages against roughly fifty in miR-142-expressing fibroblasts. The work supplies a general method for lineage-restricted study of essential herpesvirus genes.

## Scientific context

Herpesvirus genetics depends on bacterial artificial chromosomes or temperature-sensitive mutants, systems that permit rescue only in particular cells or at particular temperatures. This constrains what can be asked about genes that are essential during acute fibroblast infection but may serve different roles in the myeloid compartment where cytomegalovirus establishes latency. Existing conditional approaches require additional stimuli such as small compounds or temperature shifts and are described by the authors as laborious. On the biology side, IE1 and IE2 arise from a shared major immediate early promoter and enhancer and share the first three exons. IE2 had been characterised as both a transactivator of early and late genes and an autorepressor that binds the 14 base pair cis-repression sequence as a dimer, damping transcription from the promoter and thereby limiting both IE1 and itself. IE1 was known to be dispensable for replication while IE2 was considered essential, a conclusion drawn from fibroblast studies. The function of these proteins in shaping viral and cellular gene expression during infection of myeloid cells had not been characterised. Recent work from other groups had implicated valosin-containing protein as required for IE2 function and had shown IE2 to have a broad transcriptional footprint on viral genes, and had reported UL144 as a gene whose expression rises in the absence of IE2.

## Central question

Can a lineage-restricted cellular microRNA be used to silence an essential cytomegalovirus gene only in the cells where its function is in question, and if so, what does selective loss of IE2 do to viral replication, to the viral transcriptional cascade, and to the host transcriptome in myeloid cells as opposed to fibroblasts?

## Experimental strategy

The strategy converts a genetic problem into a post-transcriptional one. Rather than deleting or mutating the IE2 open reading frame, four perfect miR-142 target sites were placed in the noncoding 3 prime untranslated region of IE2 in the TB40/E clone, so the coding capacity of the gene is untouched and silencing is imposed only where miR-142 is present. Recombineering was simplified to a single step by combining a galK positive selection marker with flanking loxP sites, allowing Cre excision during virus rescue and removing the need for a counterselection round. The cellular logic rests on the restriction of miR-142 to the hematopoietic lineage, which the authors confirmed by small RNA Northern blot against ubiquitous miR-93 in MRC-5 fibroblasts and THP-1-derived macrophages, including during infection. Two comparisons were then run in parallel. Untargeted and targeted viruses were compared in fibroblasts, where the targeted virus should behave as wild type, and in macrophages, where IE2 should be silenced. To separate effects of IE2 loss from effects of cell type, the authors built fibroblast populations transduced to express either miR-142 or the hepatocyte-specific miR-122, giving a fibroblast background in which IE2 could be silenced and a matched control in which it could not. Readouts combined immunoblotting for IE1 and IE2, multicycle growth curves, and RNA sequencing of both viral and host transcripts at nine days post-infection with differential expression called by DESeq2.

## Key findings

1. Insertion of the four miR-142 target sites plus loxP-flanked galK into the IE2 3 prime untranslated region by one round of homologous recombination produced the targeted virus TB40/E142T, and multicycle growth curves in fibroblasts showed no discernible difference from the untargeted control, with peak titres near 1 times 10 to the sixth plaque-forming units per millilitre (Figure 1A and Results).

2. Small RNA Northern blot confirmed that miR-142 is absent from MRC-5 fibroblasts and abundant in THP-1-derived macrophages, that miR-93 is present in both, and that infection did not alter either profile after two days (Figure 1B).

3. At twenty-four hours post-infection, IE1 and IE2 protein levels were comparable between the control and targeted viruses in fibroblasts, while in macrophages IE2 was silenced and IE1 was strongly overproduced (Figure 1C). The authors attribute the IE1 excess to relief of IE2-mediated repression at the cis-repression element, which follows from established IE2 autorepression but is not separately tested here.

4. RNA sequencing of infected macrophages at twenty-four hours showed IE1-specific exon 4 reads six times higher with miR-142 targeting, representing 1.2 percent of the cytomegalovirus transcriptome against 0.2 percent for the control, with IE2 reads inversely affected, and at this early time point only IE1 and IE2 expression was changed (Figure 1D and Figure S1).

5. Across twenty-four, forty-eight and seventy-two hours, fibroblasts showed no difference in IE1 or IE2 between the two viruses, while macrophages showed sustained loss of IE2 and elevated IE1 that remained detectable at seventy-two hours when IE1 was undetectable in control infections (Figures 2A and 2B).

6. At nine days post-infection, RNA sequencing of fibroblasts lacking miR-142 showed no significant viral gene expression changes between the two viruses, whereas macrophages showed extensive remodelling of the viral transcriptome including UL144, IE1, RNA5.0, vIL-10, US29, US30, US31 and US32 (Figures 2C and 2D, Figure S2, Table S1). The authors note that many of these genes lie near putative cis-repression elements and that some may nonetheless be indirect targets of IE2.

7. Replication diverged by cell type. In fibroblasts the two viruses reached comparable peak titres near 10 to the sixth plaque-forming units per millilitre over ten days. In macrophages the control virus declined steadily to as low as 10 plaque-forming units per millilitre while the targeted virus was maintained between 1,000 and 10,000 (Figures 3A and 3B). The abstract states this as a greater than 100-fold increase in titre in myeloid cells.

8. In fibroblasts engineered to express miR-142, the targeted virus reproduced the IE1 and IE2 pattern seen in macrophages, although knockdown was less complete than with endogenous miR-142, while miR-122-expressing fibroblasts showed no effect (Figures 4A and 4B). Cytopathic effect and viral read counts were comparable between the viruses in this system (Table S2).

9. Viral genes lost in the absence of IE2 in both miR-142-expressing fibroblasts and macrophages included IE2 itself, UL24, UL25, UL69, UL71, UL94, UL95, UL97, pp65 and pp71, while vIL-10, US29 and UL145 were induced in the fibroblast setting (Figure 4C, Figure S2C, Tables S1 and S2). RNA5.0 rose sharply in macrophages without significant change in fibroblasts, which the authors read as evidence of cell-specific viral gene function.

10. Host transcriptional consequences were markedly cell-type-dependent. Roughly fifty host genes changed in miR-142-expressing fibroblasts, enriched for cellular metabolism, and included upregulation of the interferon-stimulated gene IFIT2, which the authors suggest may indicate a role for IE2 in damping innate defences as proposed by others. More than 750 host genes changed in macrophages, validated in part by quantitative PCR, with about 20 percent overlap with the fibroblast set, additional enrichment for immune system processes, and loss of genes involved in cell-to-cell communication (Figure 4D, Figures S4 and S5, Tables S3 and S4).

## Mechanistic model

The study does not establish a definitive mechanism for how IE2 controls the genes whose expression changes, and the authors state that many of the macrophage changes are likely not direct consequences of transcriptional repression by the viral product. What the data support is a layered account. Silencing is imposed post-transcriptionally through perfect complementarity between miR-142 and sites in the IE2 untranslated region, so it occurs only where that microRNA is expressed. Loss of IE2 protein removes occupancy of the cis-repression sequence and thereby raises IE1, consistent with the established negative feedback architecture of the major immediate early locus. Elevated IE1 accompanies sustained rather than abolished replication in macrophages, and the authors propose that high IE1 supports continued virus production in this lineage. On why the virus survives at all without a gene deemed essential, the authors offer two non-exclusive readings. Myeloid cells may supply compensatory factors that substitute for IE2 regulatory functions, or the residual near-undetectable IE2 that microRNA targeting cannot eliminate may suffice for an early essential step, since silencing efficiency falls as target abundance falls. The data do not distinguish these. The assignment of individual differentially expressed viral genes to direct IE2 repression is supported only by proximity to putative cis-repression motifs identified by sequence search, which is suggestive rather than demonstrative.

## Conceptual or technical advance

The method decouples the cell type in which a recombinant herpesvirus must be produced from the cell type in which a gene is to be studied, removing the fibroblast bottleneck that had prevented direct interrogation of essential genes in the myeloid compartment. Because the open reading frame is untouched and the trigger is an endogenous lineage-restricted microRNA, no exogenous stimulus, temperature shift, or complementing cell line is required, and the single galK plus loxP recombination step lowers the labour of construction. Conceptually, the work makes visible that essentiality determined in fibroblasts does not transfer to myeloid cells, and it supplies a transcriptome-level map of what IE2 loss does in each lineage. The authors also point to tunable control of gene expression by lineage as relevant to the use of cytomegalovirus as a vaccine vector.

## Relationship to the broader research program

The paper applies a targeting principle the tenOever laboratory had developed and reviewed previously, namely that inserting perfectly complementary microRNA binding sites into a viral transcript silences it potently without altering coding capacity, and that the tissue restriction of the chosen microRNA sets where silencing occurs. Earlier work in the corpus applied that principle to attenuate RNA viruses in a species- or tissue-restricted manner. Here the same logic is turned from attenuation into a genetics tool and extended from RNA viruses to a large DNA virus manipulated through a bacterial artificial chromosome. The use of miR-142 to confine activity to the hematopoietic lineage and miR-122 as a non-hematopoietic control reflects the same design vocabulary. Marked as category 3 synthesis, the recurring thread across these papers is the use of the host microRNA machinery as a programmable cell-type switch for viral gene expression rather than as an object of study in its own right, a shift from asking what microRNAs do to viruses toward using them to ask what viral genes do.

## Related publications

- tenOever 2013 (Nature Reviews Microbiology), review or synthesis. The author's own review of RNA viruses and the host microRNA machinery, cited here as the basis for the perfect-complementarity silencing approach.
- Perez et al. 2009 and related engineered microRNA-targeting work from the same laboratory, methodological foundation. Establishes microRNA target insertion as a means of restricting virus replication by cell or species, the principle repurposed here as a conditional knockdown.
- Noriega et al. 2014 (Viruses), methodological foundation. Source of the cytomegalovirus BAC electroporation and rescue procedure used here, from the co-senior author's group.
- Lin et al. 2017 (PLoS Pathogens), predecessor. Reported the broad transcriptional footprint of IE2 on viral genes and the response of UL144 to IE2 loss, predictions the present work tested in macrophages.

## Limitations and boundaries

Silencing by microRNA targeting is incomplete by design, and the authors state that residual low-level IE2 cannot be excluded as sufficient for an early essential function, which means the macrophage phenotype is a strong knockdown rather than a null. Spliced IE2 variants would also carry the inserted target sites, and while these products were not detected by immunoblot, the authors say they cannot rule out that part of the phenotype derives from their loss. The myeloid model is THP-1-derived macrophages treated with phorbol ester rather than primary monocytes or a physiological latency system, and the fibroblast model is a single primary line, MRC-5, with cells passaged fewer than twenty times. No animal work, primary hematopoietic progenitors, or latency and reactivation assays are included, so conclusions about latency itself are framed by the authors as prospective rather than demonstrated. Only one viral gene, IE2, and one microRNA, miR-142, were used, so the generality of the approach across genes and lineages is asserted rather than tested. The host and viral transcriptome comparisons rest on a single late time point of nine days at low multiplicity, with the differential expression sets validated only in part by quantitative PCR. Assignment of differentially expressed genes to direct IE2 action is based on proximity to consensus cis-repression motifs found by sequence search. Finally, the greater titres of the targeted virus in macrophages are measured by plaque assay on fibroblasts, so they report production of fibroblast-infectious particles rather than any myeloid-specific outcome.

## Audience summaries

### 25 words

Placing blood-cell-specific microRNA targets in a cytomegalovirus gene lets the virus be grown normally in fibroblasts while the gene is switched off only in macrophages.

### 75 words

Cytomegalovirus mutants must be grown in fibroblasts, which blocks study of genes essential there but interesting elsewhere. Inserting target sites for the blood-lineage microRNA miR-142 into the IE2 transcript silenced IE2 only in macrophages while leaving fibroblast growth intact. Loss of IE2 raised IE1 sharply and sustained virus titres in macrophages instead of abolishing them, and it reshaped both viral and host gene expression far more in macrophages than in fibroblasts.

### 150 words

Human cytomegalovirus genetics is limited by the requirement to rescue recombinant virus in fibroblasts, which precludes deleting genes essential during acute fibroblast infection. Møller and colleagues inserted four perfect target sites for the hematopoietic-restricted microRNA miR-142 into the noncoding 3 prime untranslated region of IE2 in the TB40/E bacterial artificial chromosome using a single galK and loxP recombination step. The resulting virus replicated indistinguishably from control in fibroblasts, which lack miR-142, while in THP-1-derived macrophages IE2 protein was silenced, IE1 rose through relief of cis-repression, and titres were sustained two to three logs above a control that declined over ten days. RNA sequencing showed extensive viral transcriptome remodelling and more than 750 host gene changes in macrophages against roughly fifty in miR-142-expressing fibroblasts. The authors note that residual IE2 may still support an early essential role, so the system represents a strong lineage-restricted knockdown rather than a null.
