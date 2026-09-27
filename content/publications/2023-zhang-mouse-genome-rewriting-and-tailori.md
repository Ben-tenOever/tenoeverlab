---
id: "2023-zhang-mouse-genome-rewriting-and-tailori"
slug: "2023-zhang-mouse-genome-rewriting-and-tailori"
source_pdf: "Zhang_et_al_Nature2023.pdf"
title: "Mouse genome rewriting and tailoring of three important disease loci"
authors: ["Weimin Zhang", "Ilona Golynker", "Ran Brosh", "Alvaro Fajardo", "Yinan Zhu", "Aleksandra M. Wudzinska", "Raquel Ordoñez", "André M. Ribeiro-dos-Santos", "Lucia Carrau", "Payal Damani-Yokota", "Stephen T. Yeung", "Camille Khairallah", "Antonio Vela Gartner", "Noor Chalhoub", "Emily Huang", "Hannah J. Ashe", "Kamal M. Khanna", "Matthew T. Maurano", "Sang Yong Kim", "Benjamin R. tenOever", "Jef D. Boeke"]
first_author: "Weimin Zhang"
senior_authors: ["Jef D. Boeke"]
corresponding_authors: ["Jef D. Boeke"]
tenoever_position: 20
tenoever_role: "middle"
year: 2023
journal: "Nature"
volume: "623"
issue: "7986"
pages: "423-431"
doi: "10.1038/s41586-023-06675-4"
pmid: "37914927"
pmcid: "PMC10632133"
publication_type: "primary research"
declared_conflicts: null
contribution_character: "collaborative"
research_areas: [pandemic-host-response, programmable-virology]
themes: [synthetic-virology-as-method, models-for-pandemic-virology]
pathogens: ["SARS-CoV-2"]
viral_families: ["Coronaviridae"]
biological_systems: ["mouse embryonic stem cells", "genetically engineered mouse models", "K18-hACE2 mouse", "golden hamster", "mouse lung", "mouse trachea", "mouse testis", "mouse small intestine", "yeast assembly vector"]
host_species: ["mouse", "human", "golden hamster", "yeast"]
technologies: ["mSwAP-In genome writing", "CRISPR-Cas9 assisted homologous recombination", "yeast assembly of large DNA", "bacterial artificial chromosomes", "tetraploid blastocyst complementation", "capture sequencing", "ATAC-seq", "CUT&RUN", "RNA sequencing", "unique molecular identifier amplicon sequencing", "plaque assay", "immunohistochemistry", "ELISA"]
key_concepts: ["mammalian genome writing", "genomic humanization", "non-coding regulatory elements", "iterative genome rewriting", "biallelic engineering", "synonymous recoding", "alternative splicing", "animal models of COVID-19", "ACE2 receptor", "TMPRSS2", "p53 mutational hotspots"]
keywords: ["mSwAP-In", "GREAT-GEMM", "genome writing", "humanized ACE2 mouse", "TMPRSS2 humanization", "SARS-CoV-2 mouse model", "K18-hACE2", "synthetic Trp53", "mouse embryonic stem cells", "tetraploid complementation"]
---

## Citation

Zhang W, Golynker I, Brosh R, Fajardo A, Zhu Y, Wudzinska AM, Ordoñez R, Ribeiro-dos-Santos AM, Carrau L, Damani-Yokota P, Yeung ST, Khairallah C, Vela Gartner A, Chalhoub N, Huang E, Ashe HJ, Khanna KM, Maurano MT, Kim SY, tenOever BR, Boeke JD. Mouse genome rewriting and tailoring of three important disease loci. Nature. 2023. Volume 623, issue 7986, pages 423-431.

DOI 10.1038/s41586-023-06675-4. PMID 37914927. PMCID PMC10632133.

## One-sentence contribution

An iterative, scarless and biallelic method for overwriting large mammalian genomic segments in mouse embryonic stem cells, used to build a recoded Trp53 locus and mice carrying the human ACE2 and TMPRSS2 loci in place of their mouse counterparts.

## Executive summary

Mouse models often fail to reproduce human disease because the sequences that set where and when a gene is expressed, and how its transcripts are spliced, lie in non-coding regions that conventional transgenesis leaves behind. Overwriting a whole locus, regulatory sequence included, requires delivering DNA on a scale that existing methods handle poorly, and existing methods are generally not designed for repeated rounds. The authors describe mSwAP-In, adapted from a yeast genome rewriting strategy, in which two interchangeable marker cassettes carrying a fluorescent marker, a positive selection marker and a negative selection marker are alternated so that each incoming payload both selects for itself and selects against the preceding cassette. Payloads are assembled in yeast, delivered with CRISPR-Cas9, and integrated by homologous recombination in mouse embryonic stem cells. The method was applied to three loci. A synonymously recoded Trp53 with CG dinucleotides removed from five mutational hotspot codons retained p53 transactivation, growth arrest and apoptosis, and accumulated fewer hotspot mutations over thirty eight passages. Mouse Ace2 was replaced with either a 116 kilobase or a 180 kilobase human ACE2 locus, and the resulting mice reproduced human tissue expression, alternative splicing and chromatin accessibility patterns. These mice were susceptible to SARS-CoV-2 but survived infection without weight loss, unlike K18-hACE2 mice, which all died. Finally, mouse Tmprss2 was replaced biallelically with human TMPRSS2 in the ACE2 line, yielding double humanized animals.

## Scientific context

Whole genome synthesis had been achieved for Escherichia coli, Mycoplasma and Saccharomyces cerevisiae, but mammalian genome synthesis remained out of reach because of genome size and complexity, so an intermediate goal is overwriting a full locus including its regulatory content. Combining assembly of DNA above one hundred kilobases with site specific recombinases had proved efficient for large scale mammalian modification, and the Big-IN method had largely solved the problem of scars left by earlier delivery approaches, but current methods were not generally designed for iterative delivery, which caps the total size that can be written. On the modeling side, ENCODE and genome wide association studies had established the importance of non-coding regulatory elements, making full genomic humanization preferable to transgenesis, in which a human coding sequence driven by a heterologous promoter gives non-physiological expression. Human bacterial artificial chromosome transgenes preserve full gene sequences but usually integrate randomly, producing position effects. In situ humanization of mouse immunoglobulin loci had been demonstrated, but with low per integration efficiency. For COVID-19 specifically, mice are naturally resistant because of coding differences in Ace2, mouse adapted viral strains change the virus being studied, and the K18-hACE2 transgenic model is uniformly lethal, which does not match human disease, lacks human regulatory elements around ACE2, may miss human specific splice isoforms, and retains an intact endogenous Ace2.

## Central question

Can large native mammalian genomic segments be overwritten efficiently, scarlessly, iteratively and biallelically in mouse embryonic stem cells that retain full developmental potential, and does replacing an entire mouse locus with its human counterpart, regulatory sequence included, produce an animal whose expression, splicing and disease phenotype are more human-like than a transgenic model?

## Experimental strategy

The method is built around a swap that is forced in both directions. Two marker cassettes each carry a fluorescent reporter, a positive selection marker and a negative selection marker, and a universal guide RNA target derived from GFP sits in front of each so that Cas9 cuts them specifically. One cassette is placed at a safe position adjacent to the target region. Each payload, assembled in yeast with roughly two kilobase homology arms and the alternate cassette, is co-delivered with guide RNAs that cut the universal target and the distal boundary of the region to be overwritten, and correct integrants are selected for the incoming cassette and against the outgoing one, which removes off target integrations. Alternating the two cassettes allows the process to repeat indefinitely, and the last cassette can be removed to leave a scarless product. Endogenous Hprt1 was deleted beforehand so that an HPRT1 minigene could be used as a selection marker later. The authors then chose three targets that test different demands. Trp53 tests whether a synthetically recoded mouse gene works and whether iterative writing is possible, using three downstream payloads of forty, seventy five and one hundred fifteen kilobases and orthogonal 28 base pair PCRTag watermarks to distinguish synthetic from native sequence. ACE2 tests whether entirely non homologous human DNA can replace a mouse locus, with two payload lengths chosen from DNase hypersensitivity and H3K27 acetylation to ask what the extra sequence contributes. TMPRSS2 tests serial and biallelic writing in an already engineered line. Mice were derived by blastocyst injection and by tetraploid complementation, which requires full pluripotency and therefore also tests whether repeated engineering damages the cells. Verification combined genotyping, copy number quantitative PCR, capture sequencing and a bamintersect analysis that detects reads spanning two references to find off target junctions.

## Key findings

1. mSwAP-In rewrote the Trp53 locus efficiently. After delivering the recoded synTrp53 payload, 87.1 percent of colonies had switched cassettes, and of thirty eight genotype verified clones, twenty six carried recoded codons on one allele and three carried only recoded synTrp53 (Figures 2b and 2c). Capture sequencing confirmed hemizygosity in those three, and bamintersect detected no off target junctions in six sequenced clones, with yeast assembly vector backbone integration in one.

2. Recoding did not impair p53 function. Doxorubicin treated synTrp53 cells upregulated Mdm2, Pmaip1 and Cdkn1a comparably to wild type, showed similar global stress responses by transcript profiling, and underwent growth arrest and apoptosis (Figures 2d to 2f). Trp53 expression was thirty to forty percent lower in synTrp53 cells, which the authors relate to prior observations linking gene body methylation to higher expression.

3. Recoding reduced hotspot mutation accumulation. After thirty eight passages, C to T and G to A mutations were frequent at wild type Trp53 hotspot codons but not at recoded synTrp53 hotspot codons, with no significant differences at other codons (Figure 2g and Extended Data Figure 3c).

4. Iterative writing worked at increasing payload size. Forty, seventy five and one hundred fifteen kilobase downstream payloads all integrated with efficiency above fifty percent by genotyping, although total drug resistant colony number fell as payload length rose (Figures 2i, 2j and Extended Data Figure 4c). Final marker cassette removal was 47.6 percent efficient with a repair template and 36.4 percent without, and complete when using piggyBac (Figure 2k).

5. Mouse Ace2 was replaced with human ACE2. Payloads of 116 and 180 kilobases were assembled from human bacterial artificial chromosomes and integrated at 61.5 percent and 60.8 percent efficiency by genotyping, with overall success rates after full sequence quality control of 15.4 percent and 22.8 percent (Figures 3d to 3f).

6. Engineered cells retained developmental potential. Thirty one of forty five pups from blastocyst injection showed coat colour chimerism, several chimeric males gave complete germline transmission, and tetraploid complementation gave birth rates of 14 percent and 22.9 percent for the two payloads (Figure 4a and Supplementary Table 2).

7. Expression followed human rather than mouse patterns in several respects. ACE2 mRNA was abundant in small intestine and kidney with moderate levels in testis and colon. ACE2 was readily detected in testis, where mouse Ace2 is not expressed, and lung ACE2 was lower than mouse Ace2 in wild type lung, both consistent with human against mouse transcriptome comparisons (Figure 4b and Extended Data Figure 6b). Immunohistochemistry showed ACE2 in Sertoli cells, spermatogonia and spermatocytes in humanized testis, against only a subset of spermatozoa in wild type (Figure 4c).

8. The longer payload changed expression levels. ACE2 expression in the 180 kilobase model was roughly one hundred fold higher in brain, three to five fold higher in lung and liver, and two to three fold lower in small intestine and colon than in the 116 kilobase model, which the authors read as regulatory function residing in the additional 64 kilobases (Extended Data Figure 6c).

9. Human specific splicing and chromatin accessibility were recapitulated. The interferon stimulated dACE2 isoform was detected in lung, kidney, small intestine and colon, and the long transcript variant 3 in small intestine, kidney, brain and testis (Figures 4d and 4e). ATAC-seq peaks in humanized small intestinal cells overlapped extensively with an ENCODE human small intestine DNase-seq track (Figure 4f).

10. ACE2 mice were susceptible to SARS-CoV-2 but developed milder disease. At three days after intranasal challenge, viral RNA was undetectable in wild type lungs, high in K18-hACE2 lungs, and moderate in ACE2 mouse lungs at the higher inoculum, with plaque assay agreeing (Figures 5a and 5b). ACE2 mice expressed roughly seventy fold less ACE2 in lung than K18-hACE2 mice. Infected ACE2 lungs mounted a moderate type I and type III interferon response overlapping that of K18-hACE2 lungs and not that of wild type (Figures 5c and 5d). dACE2 transcript rose on infection, matching reports in humans (Figure 5e and Extended Data Figure 8a).

11. At one hundred thousand plaque forming units, all five K18-hACE2 mice died by day eight after marked weight loss, while all four ACE2 mice survived fourteen days without weight loss and produced spike reactive serum IgG (Figures 5g to 5i). Histopathology showed pneumonia with monocyte infiltration in both, with substantially milder alveolar epithelial lesions in the humanized ACE2 mice (Figure 5f).

12. Tropism outside the lung was limited. No viral RNA or infectious virus was detected in small intestine or kidney. Nucleocapsid protein was present mainly on Leydig cell membranes in testis, and the virus did not enter seminiferous tubules, unlike reports from severe human COVID-19, which the authors attribute tentatively to immune clearance in these immunocompetent animals (Extended Data Figures 8c to 8g).

13. Compared against golden hamsters in a longitudinal infection, ACE2 mice had lower lung viral RNA at five days that declined by fourteen days, while a subset of ACE2 mice showed higher tracheal viral RNA than hamsters, which the authors relate to the limited Ace2 expression in hamster tracheal epithelium (Extended Data Figures 9a to 9c).

14. Serial biallelic writing was demonstrated. An eighty kilobase human TMPRSS2 payload replaced both mouse Tmprss2 alleles in the ACE2 line at thirty to forty percent efficiency, about half the clones carried two TMPRSS2 copies, double humanized mice were obtained by tetraploid complementation, backcrossing gave complete heterozygous transmission, and both TMPRSS2 splice isoforms were detected across tissues (Figures 6c to 6g and Extended Data Figure 11e).

## Mechanistic model

The study does not set out to establish a biological mechanism, and where it touches on mechanism it is careful. For the method, the causal logic is engineered rather than discovered, since alternating positive and negative selection between two cassettes is what enforces on target integration and permits iteration, and this is demonstrated directly by efficiency and sequencing data. For the recoded Trp53, the authors hypothesize that removing CG dinucleotides at mutational hotspots reduces the deamination of 5-methylcytosine and adduct binding that generate C to T changes, and the reduced mutation frequency after thirty eight passages is consistent with that hypothesis without isolating either process. For the phenotype of the humanized ACE2 mice, the data show a correlation between lung ACE2 expression level and disease severity, with roughly seventy fold lower expression than K18-hACE2 and markedly milder outcome, and the authors speculate that faster infection kinetics in the 180 kilobase model follow from its higher ACE2 expression. Whether the milder disease is caused by expression level, by the absence of the keratin 18 driven expression pattern, by the presence of human regulatory control, or by some combination is not resolved by these experiments. The interpretation that the additional 64 kilobases in the longer payload carries regulatory function rests on the expression difference between the two models and no direct element level test.

## Conceptual or technical advance

mSwAP-In makes iterative, scarless, large scale genome writing routine enough in mouse embryonic stem cells that whole loci can be replaced and the cells can still make animals through tetraploid complementation, which the authors argue opens a path toward writing megabase scale synthetic DNA. Because a locus can be replaced together with its regulatory and intronic content, the resulting animals, which the authors call GREAT-GEMMs, allow questions about human specific regulation and splicing to be asked in vivo rather than inferred. The ACE2 model in particular provides a COVID-19 mouse that is infectable with an unmodified virus, survives, mounts a humoral response, and therefore supports study of medium and longer term consequences of infection, which the uniformly lethal K18-hACE2 model cannot. The double humanized ACE2 and TMPRSS2 animal shows that entry pathway components can be humanized together, which is relevant to testing therapies directed at TMPRSS2.

## Relationship to the broader research program

The tenOever contribution to this study is the SARS-CoV-2 side. By the author contributions statement, Golynker, Fajardo and Carrau performed the SARS-CoV-2 infections and mouse tissue collection in the biosafety level 3 facility, tenOever participated in experimental design and in reviewing and editing the manuscript, and the study was conceptualized and led by Zhang and Boeke. The connection to the tenOever laboratory's own program is the question of what constitutes an adequate small animal model for SARS-CoV-2, and the paper cites the laboratory's golden hamster work as the comparator against which the humanized mouse is benchmarked. Category 3 synthesis, visible only when corpus papers are read together, is that the laboratory's recurring position is that model choice determines which parts of the host response can be seen at all, expressed here in the comparison of the humanized ACE2 mouse against both the K18-hACE2 transgenic and the golden hamster. That statement rests on more than this paper alone.

## Related publications

- Hoagland et al. 2021, leveraging the antiviral type I interferon system as a first line of defense against SARS-CoV-2 pathogenicity, predecessor. Cited in this paper as the golden hamster model against which the humanized ACE2 mouse is compared, and produced by the tenOever laboratory.
- Brosh et al. 2021, a versatile platform for locus scale genome rewriting and verification, methodological foundation. The Big-IN platform, the acceptor vector, the Capture-seq verification and the bamintersect analysis used here come from this work, and Brosh is a co-author.
- Boeke et al. 2016, the Genome Project-write, conceptual extension. The cancer mutation resistant Trp53 was undertaken to address a challenge set by that project, and Boeke is the senior author of both.
- Ribeiro-dos-Santos et al. 2022, genomic context sensitivity of insulator function, methodological foundation. Source of the unique molecular identifier based amplicon sequencing used to measure hotspot mutation frequencies, with shared authorship.
- Mitchell et al. 2021, de novo assembly and delivery to mouse cells of a 101 kilobase functional human gene, predecessor. Source of the assemblon concept used for the payloads.

## Limitations and boundaries

The genome writing demonstrations are confined to mouse embryonic stem cells, and the authors state that generalization to other mammalian species depends on those species having comparable homologous recombination efficiency. The payloads delivered in the Trp53 iterations were more than ninety nine percent identical to native mouse sequence, which the authors note may itself have contributed to the high efficiency, so efficiencies for non homologous human DNA are the lower figures reported for ACE2. Overall success rates after full sequence quality control were 15.4 and 22.8 percent, well below the raw genotyping efficiencies, and yeast assembly vector backbone integration was observed in one clone. Payload sequences carried single nucleotide polymorphisms present in the parental bacterial artificial chromosomes, so a humanized locus reflects one human haplotype. For the infection work, the authors state that the animals used were relatively young at ten to fifteen weeks and healthy, corresponding to people with mild or minimal COVID-19, and that older or comorbid models would be needed to address severe disease. Group sizes in the infection experiments are small, with four or five mice per arm. Male and female animals differed in lung viral RNA despite equal inoculum and no detected difference in ACE2 expression, which is unexplained. The two ACE2 models differ in both payload length and expression level, so the contribution of the extra sequence cannot be separated from the expression difference it produces. Comparison against the golden hamster rests on a single longitudinal experiment. Finally, humanizing ACE2 and TMPRSS2 does not humanize the rest of the mouse, so immune and physiological responses to infection remain those of a mouse.

## Audience summaries

### 25 words

A genome writing method replaces whole mouse loci with synthetic or human DNA, producing mice carrying the human ACE2 gene that catch SARS-CoV-2 and recover.

### 75 words

Mouse models often miss human disease because regulatory DNA outside the coding sequence is left out. A new method swaps large genomic segments in mouse stem cells repeatedly and without scars, using paired selection markers that alternate with each round. It was used to build a mutation resistant p53 gene and to replace mouse Ace2 with the full human ACE2 locus. Those mice are infectable with SARS-CoV-2 and survive, unlike an existing transgenic model.

### 150 words

mSwAP-In alternates two marker cassettes, each carrying positive and negative selection, so that every payload delivered into mouse embryonic stem cells selects for itself and against its predecessor, permitting iterative, scarless and biallelic overwriting of large genomic segments assembled in yeast. A synonymously recoded Trp53 lacking CG dinucleotides at five mutational hotspots retained transactivation, arrest and apoptosis while accumulating fewer hotspot mutations over passage. Mouse Ace2 was replaced with 116 or 180 kilobase human ACE2 loci, and the resulting animals, derived by tetraploid complementation, reproduced human tissue expression including testicular expression absent in mice, the interferon inducible dACE2 isoform, and human chromatin accessibility. These mice were infectable with SARS-CoV-2, mounted a moderate interferon response and a spike specific antibody response, and survived without weight loss, while all K18-hACE2 controls died. Mouse Tmprss2 was then replaced biallelically with human TMPRSS2 in the same line.
