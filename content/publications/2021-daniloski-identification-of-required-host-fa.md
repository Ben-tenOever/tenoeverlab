---
id: 2021-daniloski-identification-of-required-host-fa
slug: 2021-daniloski-identification-of-required-host-fa
source_pdf: Daniloski_et_al_Cell2021.pdf
title: Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells
authors: ["Zharko Daniloski", "Tristan X. Jordan", "Hans-Hermann Wessels", "Daisy A. Hoagland", "Silva Kasela", "Mateusz Legut", "Silas Maniatis", "Eleni P. Mimitou", "Lu Lu", "Evan Geller", "Oded Danziger", "Brad R. Rosenberg", "Hemali Phatnani", "Peter Smibert", "Tuuli Lappalainen", "Benjamin R. tenOever", "Neville E. Sanjana"]
first_author: Zharko Daniloski
senior_authors: ["Benjamin R. tenOever", "Neville E. Sanjana"]
corresponding_authors: ["Benjamin R. tenOever", "Neville E. Sanjana"]
tenoever_position: 16
tenoever_role: senior
year: 2021
journal: Cell
volume: "184"
issue: "1"
pages: 92-105.e16
doi: 10.1016/j.cell.2020.10.030
pmid: "33147445"
pmcid: PMC7584921
publication_type: primary research
declared_conflicts: null
contribution_character: co-led
research_areas: [pandemic-host-response, programmable-virology]
themes: [in-vivo-screening-through-fitness, host-factors-and-druggable-signaling]
pathogens: [SARS-CoV-2]
viral_families: [Coronaviridae]
biological_systems: [A549-ACE2 cells, Huh7.5-ACE2 cells, Caco-2 cells, Calu-3 cells, Vero E6 cells]
host_species: [human]
technologies: [genome-scale CRISPR-Cas9 knockout screening, GeCKOv2 library, amplicon sequencing, robust rank aggregation, ECCITE-seq single-cell CRISPR screening, RNA interference, small-molecule inhibitor panels, flow cytometry, immunofluorescence microscopy, bulk RNA sequencing, cholesterol quantification, plaque assay, quantitative RT-PCR]
key_concepts: [host dependency factors, forward genetic screening, endosomal trafficking, vacuolar ATPase, Retromer complex, Commander complex, ARP2 and ARP3 complex, class 3 PI3K, cholesterol biosynthesis, ACE2 surface availability, druggable target identification]
keywords: [SARS-CoV-2, CRISPR screen, host factors, RAB7A, PIK3C3, ATP6AP1, NPC1, CCDC22, cholesterol, ACE2, amlodipine, COVID-19 therapeutics]
---

## Citation

Daniloski Z, Jordan TX, Wessels HH, Hoagland DA, Kasela S, Legut M, Maniatis S, Mimitou EP, Lu L, Geller E, Danziger O, Rosenberg BR, Phatnani H, Smibert P, Lappalainen T, tenOever BR, Sanjana NE. Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. Cell. 2021. Volume 184, issue 1, pages 92-105.e16.

DOI 10.1016/j.cell.2020.10.030. PMID 33147445. PMCID PMC7584921.

## One-sentence contribution

A genome-scale CRISPR loss-of-function screen in ACE2-expressing human alveolar epithelial cells ranks every protein-coding gene by the effect of its loss on SARS-CoV-2 infection, converging on endosomal machinery, and links several top hits to increased cholesterol biosynthesis and, for RAB7A, to intracellular sequestration of ACE2.

## Executive summary

Early in the COVID-19 pandemic the set of human genes known to be required for SARS-CoV-2 infection was limited to a handful, chiefly ACE2 and cathepsin L, while proteomic interaction maps had proposed hundreds of virus-host contacts without establishing which mattered for infection. This study applies pooled genome-scale CRISPR knockout screening to the problem, using the GeCKOv2 library across 19,050 genes in A549 lung epithelial cells engineered to express ACE2, then selecting for survival of SARS-CoV-2 infection at two multiplicities. Guide enrichment analysis placed ACE2 and cathepsin L among the top hits, supporting the readout, and the remaining top-ranked genes fell into coherent complexes dominated by endosomal biology, including thirteen vacuolar ATPase subunits, four Retromer members, four Commander members, four ARP2 and ARP3 complex members and three class 3 PI3K pathway genes. Thirty top genes were retested individually with fresh guides, by small interfering RNA, in a second cell line, and against a panel of 26 small molecules, with PIK3C3 inhibitors among the most effective. Single-cell CRISPR profiling of the top hits found that six of them, all in the endosomal entry pathway, share upregulation of cholesterol biosynthesis when lost, and cellular cholesterol rose accordingly. Amlodipine, which raises intracellular cholesterol, reduced infection. RAB7A loss reduced ACE2 at the cell surface and accumulated it in EEA1-positive vesicles, an effect reproduced in Caco-2 and Calu-3 cells expressing endogenous ACE2.

## Scientific context

At the time of writing, remdesivir was the only approved antiviral and roughly thirty vaccines were in trials. Compound screens had been run against SARS-CoV-2, and affinity purification and proximity labelling proteomics had mapped hundreds of high-confidence virus-host protein interactions, but interaction is not requirement, and the paper states the gap plainly. There were no genome-wide studies directly identifying human genes required for viral infection, and knowledge of essential host genes was limited to ACE2 and cathepsin L. The known entry biology framed the expected answer space. Spike binds ACE2, is proteolytically activated by host proteases including furin, TMPRSS2 and cathepsin L in either the secretory pathway or the target cell during entry, and fusion then releases viral RNA into the cytoplasm. Whether the genes that matter beyond these steps would be lung specific, or broadly expressed, was also open.

## Central question

Which human genes are required for SARS-CoV-2 infection of human lung epithelial cells, and by what cellular mechanisms does loss of the top-ranked genes confer resistance.

## Experimental strategy

The screen exploits the fact that SARS-CoV-2 kills A549-ACE2 cells, turning survival into a selection. Cells transduced at low multiplicity with an all-in-one Cas9 and guide vector receive on average one guide, so a surviving cell can be attributed to a single gene knockout, and guide abundance measured by amplicon sequencing before and after infection reports which knockouts confer resistance. Running the selection at two multiplicities, 0.01 and 0.3, tests whether hits depend on viral dose. Three independent enrichment statistics were applied to the same data to check that the gene ranking is not an artefact of one method.

Because pooled screens carry false positives, the validation strategy was deliberately multi-modal. Thirty genes from the top 200 were retested in arrayed format with three guides per gene that were absent from the screening library, which controls for guide-specific off-target effects. Small interfering RNA knockdown provides a perturbation that does not cut DNA. Repeating a subset in a human liver line tests cell type dependence. A panel of 26 inhibitors against nine druggable hits tests whether the dependency is chemically accessible, with remdesivir as a positive control and paired viability measurement to distinguish antiviral effect from toxicity, and combining the top PIK3C3 inhibitors with PIK3C3 knockout tests on-target specificity by asking whether the drug still works when its target is gone.

To ask why loss of these genes protects rather than only that it does, the authors coupled a minipool of the same guides to ECCITE-seq, which reads out guide identity, transcriptome and surface protein in single cells. Doing this in a pooled rather than arrayed format puts all perturbations through the same handling, so a shared transcriptional signature across different knockouts is unlikely to reflect batch structure. Finally, flow cytometry and immunofluorescence for ACE2 across the perturbed panel test whether any hit acts by controlling receptor availability, with Caco-2 and Calu-3 cells included so the conclusion is not confined to cells overexpressing ACE2.

## Key findings

1. The screen recovers known entry factors. ACE2 ranked 8th in the low multiplicity screen and 12th in the high multiplicity screen, and cathepsin L was also among the top scoring genes (Table S1). Library representation was maintained through selection, and substantial guide dropout followed infection as expected (Figure S1A, Figures 1C and 1D).

2. Approximately 1,000 genes reached significance by robust rank aggregation (Figure S1B), three enrichment methods largely agreed (Figure S1C), and 27 of the top 50 genes were shared between the two multiplicities (Figure 1F), which the authors read as indicating that several host dependencies function independently of viral dose.

3. Top hits cluster into coherent complexes centred on endosomal biology, including 13 vacuolar ATPase proton pump subunits, four Retromer members, four Commander members, four ARP2 and ARP3 complex members, three class 3 PI3K pathway genes, ER to Golgi trafficking genes and two transcriptional modulators (Figures 2 and 3A). Gene set enrichment identified endosome processing, transport and acidification categories as significant (Figure 3B).

4. Nearly all top hits are broadly expressed across 12 human tissues in GTEx, with ACE2 the exception in showing tissue-restricted expression enriched in testis, small intestine, kidney and heart (Figure 3C). The authors interpret the breadth as implying that these mechanisms may operate independent of cell or tissue type, which is an inference from expression rather than a tested claim.

5. Twenty-two of the top 50 low multiplicity genes had been reported as direct interactors with SARS-CoV-2 proteins in published proteomics, a significant enrichment over random gene sets (Figure 3D). ATP6AP1 interacts with nsp6, ATP6V1A with the membrane protein and RAB7A with nsp7.

6. Comparison with prior screens for Zika virus and pandemic H1N1 influenza showed greater similarity in enriched gene ontology categories between SARS-CoV-2 and Zika virus, with vacuolar ATPase subunits enriched in all three (Figure 3E, Figure S2E).

7. Arrayed validation confirmed the hits. All 30 Cas9-perturbed lines showed reduced infected cell percentage, up to tenfold, at 36 hours after infection (Figures 4A and 4B), with a significant negative correlation between arrayed infection percentage and screen fold change (Figure 4C). Viral load was reduced across a full growth curve at 5, 10, 24 and 48 hours (Figure S3B). All eight genes tested in Huh7.5-ACE2 cells reduced infection (Figure S3C), and small interfering RNA knockdown reproduced the effect (Figure S3D).

8. Seven of 26 inhibitors reduced viral load more than 100-fold, four of them targeting PIK3C3 (Figure 4E). Autophinib and ALLN exceeded 1000-fold. Combining PIK3C3 inhibitors with PIK3C3 knockout indicated that Compound-19, PIK-III and autophinib act on target while SAR405 gave greater inhibition in knockout cells, which the authors read as possible off-target activity. Panobinostat and pracinostat reduced viability by more than half, so their apparent antiviral readouts were flagged as unreliable (Figure 4F).

9. Six endosomal entry pathway genes share a transcriptional response when lost. Single-cell profiling across 18,853 singly perturbed cells found that loss of ATP6AP1, ATP6V1A, CCDC22, NPC1, PIK3C3 or RAB7A upregulated lipid and cholesterol homeostasis pathways (Figures 5B, 5C and S5B), and measured cholesterol rose by 10 to 50 percent depending on the perturbation (Figure 5D). The authors note that only 11 of 30 target genes produced a detectable transcriptomic shift, and suggest the remainder produce subtler changes.

10. Raising cholesterol pharmacologically reduces infection. Amlodipine increased cholesterol in A549-ACE2 cells and reduced infection by quantitative RT-PCR, plaque assay and viral read fraction, with modest impact on viability, and its transcriptional profile resembled the CRISPR perturbations with cholesterol biosynthesis as the top upregulated pathway (Figures S5C to S5I). The interpretation offered, that these perturbations counteract virus-mediated suppression of cholesterol synthesis, draws on the authors' separate work and is presented as a possibility rather than as demonstrated here.

11. RAB7A loss relocates ACE2. Surface ACE2 measured by flow cytometry was significantly reduced in RAB7A knockout A549-ACE2 cells (Figures 6A and 6B), with Rab7a depletion confirmed by western blot. Immunofluorescence showed ACE2 accumulating in vesicle-like structures in about 35 percent of RAB7A knockout cells compared with predominantly membrane localisation in controls (Figures 6C and 6D), and these vesicles colocalised often with EEA1 and less often with LysoTracker (Figure 6E). The effect held in Caco-2 and Calu-3 cells expressing endogenous ACE2 (Figures 6F to 6I).

## Mechanistic model

The study is a dependency map first and a mechanism study second, and it does not establish a single mechanism for the class of hits it identifies. The authors state in their own limitations section that the precise mechanism by which changes in cholesterol disrupt viral infection remains to be elucidated.

What the data constrain is the following. A large fraction of the genes whose loss confers resistance operate in endosomal maturation, acidification, sorting and recycling, which is consistent with a virus that depends on endosomal entry and cathepsin L cleavage. Within that class, six genes converge on a shared downstream consequence, elevated cholesterol biosynthesis, and an independent pharmacological route to the same elevation also reduces infection, which makes cholesterol a plausible common effector rather than an incidental correlate. The authors propose that these perturbations counter a virus-driven suppression of cholesterol synthesis reported in their separate work, and they note precedents for lipid composition affecting virion maturation and infectivity in hepatitis C and influenza A. Neither the causal ordering between cholesterol change and infection block, nor the step of the viral life cycle affected, is established here.

For RAB7A the data support a more specific model. Loss of Rab7a reduces ACE2 at the plasma membrane and accumulates it in early endosomal compartments, which would limit viral attachment. The authors note that this cannot be the whole story, because Rab7a interacts with nsp7 and nsp7 is not present in the incoming virion, implying an additional post-entry role, and they point to RAB7A being the top performer in arrayed validation and showing both altered cholesterol and ACE2 sequestration as consistent with more than one contributing pathway. That multiplicity is offered as a possibility, not demonstrated.

## Conceptual or technical advance

The screen converts the question of which host genes matter for SARS-CoV-2 from a list of candidates into a genome-scale quantitative ranking with an effect size for every protein-coding gene, which is the resource the paper positions as its main output. Coupling a minipool of validated guides to single-cell transcriptomic and surface protein readout makes it possible to ask not only which genes are required but whether mechanistically distinct knockouts converge on a shared cellular state, and that is how the cholesterol link was found rather than assumed. The authors also frame a methodological argument, that starting from forward genetics and moving to inhibitors yields therapeutic candidates whose mechanism of action is known from the outset, in contrast to compound-first screening where mechanism must be reconstructed afterwards.

## Relationship to the broader research program

The virological work, including all BSL3 infections, sits with the tenOever laboratory while the screening platform and analysis sit with the Sanjana laboratory, and the two are joint corresponding authors with Sanjana as lead contact. The A549-ACE2 line used throughout, made by Danziger and Rosenberg, is the same engineered system used across the tenOever laboratory's SARS-CoV-2 work. The cholesterol connection draws on Hoagland and colleagues from the same collaboration network, which reported that SARS-CoV-2 downregulates cholesterol synthesis and that compounds raising it are antiviral.

Category 3 synthesis. Comparison of this screen with the laboratory's transcriptional and epigenetic work on SARS-CoV-2 would bear on whether host dependencies and host response pathways overlap, and the paper's own comparison with Zika virus and influenza screens raises the question of shared versus virus-specific dependency architecture. Both are cross-paper questions and neither is settled by this study alone.

## Related publications

- Daniloski and colleagues, 2021, eLife, companion. The same first author and the same two corresponding laboratories, using the related A549-ACE2 and Caco-2 systems, on the Spike D614G substitution.
- Hoagland and colleagues, 2020, companion. Cited here as the independent survey of more than 20,000 candidate treatments that identified induction of cholesterol biosynthesis as a mechanism of viral inhibition, and as the source of the claim that SARS-CoV-2 downregulates cholesterol synthesis.
- Gordon and colleagues, 2020, predecessor. The SARS-CoV-2 protein interaction map against which top-ranked screen hits were cross-referenced.
- Zhu and colleagues, 2020, companion. An independent genome-scale CRISPR screen in ACE2-overexpressing A549 cells with a different library, reported here as giving substantially overlapping top-ranked genes.
- Wei and colleagues, 2020, and Heaton and colleagues, 2020, companion. Contemporaneous loss-of-function screens for SARS-CoV-2 host factors, with the African green monkey cell screen of Wei and colleagues overlapping only at ACE2 and cathepsin L.
- Sanjana and colleagues, 2014, methodological foundation. Source of the GeCKOv2 library used for the screen.
- Mimitou and colleagues, 2019, methodological foundation. Source of the ECCITE-seq method used for the single-cell CRISPR readout.

## Limitations and boundaries

The authors provide their own limitations section and it is followed here. The screen was performed in A549 cells overexpressing ACE2, so transcriptional regulators of endogenous ACE2 would not be recovered, and A549 is a lung adenocarcinoma line rather than primary airway tissue. Tissue-specific host factors relevant to the other organs affected in COVID-19 are not addressed. The mechanism by which increased cholesterol blocks infection is not established. Integration with human genetic variants associated with COVID-19 risk is proposed as future work rather than performed.

Beyond the authors' list, the selection is survival-based, so the screen reports resistance to virus-induced death rather than blockade of any defined step, and genes whose loss is itself lethal or strongly deleterious cannot score. Guide dropout after infection was substantial, which reduces effective library complexity in the selected population. Validation of protein loss by western blot was performed for a subset of genes only, and knockout lines are polyclonal, so residual protein is expected, a point the authors raise specifically in interpreting the PIK3C3 inhibitor specificity test. Inhibitors were tested at a single concentration of 10 micromolar with viability assessed at 36 hours, and two compounds were excluded on viability grounds. Only 11 of 30 perturbations produced detectable transcriptomic shifts in the single-cell data, so the cholesterol signature is established for a subset rather than for all validated hits. Comparison with the monkey cell screen of Wei and colleagues overlapped only at two genes, which the authors attribute to technical or biological differences without resolving which. All work uses a single early isolate, USA-WA1/2020, and there is no animal model or primary tissue component.

## Audience summaries

### 25 words

Switching off each human gene in turn showed which ones SARS-CoV-2 needs. Most were endosome trafficking genes, and losing several of them raised cholesterol and blocked infection.

### 75 words

To find the human genes SARS-CoV-2 depends on, every protein-coding gene was disabled in turn across a pool of lung cells, which were then infected and sequenced to see which knockouts survived. Known entry factors appeared near the top, alongside whole complexes that move and acidify endosomes. Disabling six of these genes raised cellular cholesterol, and a drug that raises cholesterol also blocked infection. Losing RAB7A trapped the ACE2 receptor inside cells instead of at the surface.

### 150 words

A GeCKOv2 genome-scale CRISPR knockout screen in ACE2-expressing A549 cells, selected by survival of SARS-CoV-2 infection at two multiplicities, ranked all 19,050 targeted genes. ACE2 and cathepsin L scored highly, and the remaining top hits formed coherent endosomal complexes including thirteen vacuolar ATPase subunits, Retromer, Commander, ARP2 and ARP3, and class 3 PI3K components. Thirty hits were confirmed with independent guides, small interfering RNA, a second cell line, and inhibitors, with PIK3C3 antagonists among the most potent. Pooled single-cell CRISPR profiling showed that loss of ATP6AP1, ATP6V1A, CCDC22, NPC1, PIK3C3 or RAB7A converges on upregulated cholesterol biosynthesis, with measured cholesterol rising 10 to 50 percent, and amlodipine reproduced both the cholesterol increase and the antiviral effect. RAB7A loss reduced surface ACE2 and accumulated it in EEA1-positive vesicles in A549, Caco-2 and Calu-3 cells. How cholesterol blocks infection was not determined, and the work is confined to transformed human cell lines.
