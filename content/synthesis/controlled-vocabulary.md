---
id: controlled-vocabulary
name: "Controlled Vocabulary"
question: "Which surface forms were merged into which canonical terms, and on what grounds?"
kind: reference
---

## What this document is

The 63 publication records carry six descriptive fields written independently by eleven contributors, and the fields are inconsistent. Before the filters on this site or the machine-readable data can be trusted, those strings have to be resolved into a controlled vocabulary. This document records the result and the reasoning, so that a later curator can see why two strings were merged and reverse the decision if it was wrong.

This document and `data/vocabulary.json` were produced from one mapping in a single pass, so the two cannot disagree, and the entries below carry the full mapping in readable form. Every publication list was checked programmatically against the files in `content/publications`, and every canonical term has at least one publication.

## Scale of the problem

| Field | Surface forms | Canonical terms |
| --- | --- | --- |
| technologies | 338 | 145 |
| pathogens | 59 | 43 |
| viral_families | 20 | 20 |
| host_species | 30 | 21 |
| biological_systems | 240 | 197 |
| key_concepts | 542 | 154 |

## Principles applied

Normalisation was not done by lowercasing and deduplicating, because that gets both directions wrong. Genuinely identical things are sometimes spelled very differently, and genuinely different things are sometimes spelled almost the same.

Things merged despite very different spellings. The small RNA blot appears as "small RNA Northern blot", "small RNA northern blot" and "small RNA Northern blotting" and is one method. Bulk transcriptome profiling appears as "RNA sequencing", "bulk RNA sequencing", "bulk mRNA sequencing", "mRNA sequencing", "messenger RNA sequencing", "mRNA deep sequencing" and "ribosomal RNA-depleted total RNA sequencing", and no record uses the variation to mark a distinction. The BHK line appears as "BHK cells", "BHK-21 cells", "BHK21 cells" and "baby hamster kidney cells". Hosts appear as "dog" and "canine" and "canine cells", and as "golden hamster" and "hamster" and "hamster cells".

Things kept apart despite similar spellings. "northern blot" and "small RNA northern blot" are separate entries, because the second denotes a denaturing polyacrylamide system for species under about 40 nucleotides and the two are used for different claims in the same papers. "Vero cells" and "Vero E6 cells" are separate lines. "coimmunoprecipitation", "Argonaute immunoprecipitation" and "RNA immunoprecipitation" are three different experiments. "SARS-CoV" and "SARS-CoV-2" are two different viruses, and the strings "SARS-CoV-1" and "severe acute respiratory syndrome coronavirus" were folded into the former, not the latter. "in vivo RNAi screening" and "genome-wide CRISPR knockout screening" are both forward genetic screens and remain separate, because they differ in delivery, selection and readout.

Strain strings were folded into the species and preserved as aliases, so that "influenza A virus H5N1 A/Vietnam/1203/04" and "SARS-CoV-2 USA-WA1/2020" remain findable without fragmenting the species counts.

Group terms were kept as entries in their own right. "poxviruses", "herpesviruses", "RNA viruses" and "DNA viruses" appear only in review articles, where they denote categories rather than agents, and merging them into a member species would misattribute a claim.

Platform statements were separated from assays. "SOLiD sequencing", "Illumina MiSeq" and "Illumina deep sequencing" name instruments rather than experiments and sit in a single entry for sequencing platforms, leaving the assay entries to describe what was sequenced.

Engineered derivatives were kept distinct from their parents where the genotype is the point of the experiment, so NoDice HEK293T cells, ADAR1 knockout A549 cells and RELA knockout HeLa-ACE2 cells each have their own entry, while variants that differ only in spelling were merged.

## Known ambiguities left in place

Three decisions are judgement calls that a later curator may want to revisit.

The string "luciferase reporter assay" is used in this corpus for two different experiments, a promoter reporter measuring transcriptional induction and a target site reporter measuring post-transcriptional silencing. It is mapped to the promoter reporter entry by default, and several records that use it, notably Perez 2009, use it in the second sense. Where a record spelled the silencing use out, as in "luciferase 3-prime UTR reporter assay" or "reporter-based post-transcriptional silencing assay", it was mapped to the silencing entry instead. The ambiguity cannot be resolved from the frontmatter alone.

The strings "quantitative PCR" and "quantitative RT-PCR" were merged. In every record where the underlying experiment can be identified, the template is RNA and the step is reverse transcription followed by quantitative PCR, so the shorter string appears to be an abbreviation rather than a different assay.

The host annotation "hamster" in the earlier small RNA papers denotes BHK-21 baby hamster kidney cells and not an animal experiment. Merging it with "golden hamster" makes the host count for hamster read higher than the number of studies that used the animal. The animal enters the corpus with Hoagland 2021 and the records that follow it.

## A caution about key concepts

The `key_concepts` field is the least consistent of the six, with 542 surface forms across 63 records and most of them appearing once. Merging there is thematic rather than strictly synonymous, and the resulting 154 entries should be read as a browsing index rather than as an ontology. Grouping "IKK-related kinases", "IKKepsilon", "TBK1" and "virus-activated kinase" into one term is defensible for a filter and wrong for a claim. The alias lists below preserve every original string, so any grouping here can be undone.


## Technologies

145 canonical terms from 338 surface forms. Grouped by family, then ordered by number of publications.

### Animal, organoid and tissue models

**Route-controlled in vivo infection and delivery** (`in-vivo-infection-route`)

Surface forms. "intranasal and intravenous infection of mice", "intranasal delivery", "intranasal infection of hamsters", "intranasal interferon administration", "intranasal mouse infection", "intravenous infection"

Publications. 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-schmid-a-versatile-rna-vector-for-deliver, 2017-morales-sars-cov-encoded-small-rnas-contri, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2023-carrau-delayed-engagement-of-host-defense

**Animal transmission models** (`animal-transmission-model`)

Surface forms. "cohousing transmission model", "ferret transmission study", "hamster challenge and transmission models", "nebulized aerosol exposure"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat, 2014-varble-influenza-a-virus-transmission-bot, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r

**Behavioural and sensory testing** (`behavioural-and-sensory-testing`)

Surface forms. "buried food finding test", "Hargreaves thermal testing", "locomotor beam break assay", "marble burying assay", "von Frey monofilament testing"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a, 2023-serafini-sars-cov-2-airway-infection-result

**Cre-LoxP lineage tracing of infected cells** (`cre-lox-lineage-tracing`)

Surface forms. "Cre-lox lineage tracing", "Cre-LoxP lineage tracing", "tdTomato reporter mice"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2019-tenoever-synthetic-virology-building-viruse

**Directed differentiation of human pluripotent stem cells** (`hpsc-directed-differentiation`)

Surface forms. "directed differentiation of human pluripotent stem cells", "directed trilineage differentiation", "embryoid body cardiomyocyte differentiation", "hPSC ScoreCard assay"

Publications. 2019-eggenberger-type-i-interferon-response-impairs, 2020-yang-a-human-pluripotent-stem-cell-base

**Air-liquid interface culture** (`ali-culture`)

Surface forms. "air-liquid interface culture"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Epithelial barrier permeability measurement** (`barrier-permeability`)

Surface forms. "barrier permeability measurement"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Kidney capsule xenotransplantation** (`xenotransplantation`)

Surface forms. "kidney capsule xenotransplantation"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Organ-on-a-chip microfluidics** (`organ-on-chip`)

Surface forms. "organ-on-a-chip microfluidics"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Organoid culture** (`organoid-culture`)

Surface forms. "organoid culture"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Pharmacokinetic analysis** (`pharmacokinetics`)

Surface forms. "pharmacokinetic analysis"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Pharmacological immunosuppression** (`immunosuppression-treatment`)

Surface forms. "dexamethasone immunosuppression"

Publications. 2023-carrau-delayed-engagement-of-host-defense

**Serum transfer with ultraviolet inactivation** (`serum-transfer`)

Surface forms. "serum transfer with ultraviolet inactivation"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Targeted cell ablation** (`cell-ablation`)

Surface forms. "diphtheria toxin receptor depletion"

Publications. 2014-heaton-long-term-survival-of-influenza-vi

### Functional genomics and screening

**Site-directed and alanine scanning mutagenesis** (`site-directed-mutagenesis`)

Surface forms. "alanine scanning mutagenesis", "site-directed mutagenesis", "site-directed promoter mutagenesis", "site-directed splice site mutagenesis"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-schmid-mitogen-activated-protein-kinase-m, 2021-daniloski-the-spike-d614g-mutation-increases, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-yaron-host-protein-kinases-required-for-, 2023-oishi-archaeal-kink-turn-binding-protein

**Adenoviral vector delivery** (`adenoviral-vector`)

Surface forms. "adenoviral overexpression", "adenoviral reconstitution", "adenoviral vector delivery", "adenoviral vector transduction"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2015-aguado-microrna-function-is-limited-to-cy, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2023-uhl-adar1-biology-can-hinder-effective

**CRISPR-Cas9 knockout cell lines** (`crispr-knockout`)

Surface forms. "CRISPR Cas9 gene disruption", "CRISPR knockout", "CRISPR knockout cell lines", "CRISPR-Cas9 knockout"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Lentiviral transduction** (`lentiviral-transduction`)

Surface forms. "lentiviral microRNA transduction", "lentiviral transduction", "lentiviral vectors"

Publications. 2010-schmid-transcription-factor-redundancy-en, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2018-han-genome-wide-crispr-cas9-screen-ide, 2018-m-ller-mirna-mediated-targeting-of-human-

**Conditional and inducible gene knockout** (`conditional-knockout`)

Surface forms. "conditional gene knockout", "conditional knockout with Cre-expressing adenoviral vectors", "tamoxifen-inducible conditional knockout mouse"

Publications. 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2014-shapiro-drosha-as-an-interferon-independen, 2025-manivasagam-transcriptional-repressor-capicua-

**Genome-wide CRISPR-Cas9 knockout screening** (`genome-wide-crispr-screen`)

Surface forms. "GeCKO library", "GeCKOv2 library", "genome-scale CRISPR-Cas9 knockout screening", "genome-wide CRISPR knockout screening", "MAGeCK analysis", "robust rank aggregation"

Publications. 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2021-daniloski-identification-of-required-host-fa

**In vivo RNAi screening through viral fitness** (`in-vivo-rnai-screen`)

Surface forms. "artificial microRNA libraries", "artificial microRNA library", "in vivo RNAi screening"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2015-benitez-in-vivo-rnai-screening-identifies-, 2019-tenoever-synthetic-virology-building-viruse

**Knockout mouse infection** (`knockout-mice`)

Surface forms. "gene knockout mice", "knockout mouse infection"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2015-benitez-in-vivo-rnai-screening-identifies-

**Doxycycline-inducible lentiviral expression** (`inducible-expression`)

Surface forms. "doxycycline-inducible lentiviral expression", "lentiviral doxycycline-inducible expression"

Publications. 2019-eggenberger-type-i-interferon-response-impairs, 2023-oishi-archaeal-kink-turn-binding-protein

**Engineered transcription factor constructs** (`engineered-tf-constructs`)

Surface forms. "chimeric VPR transcriptional activators", "constitutively active IRF7 truncation"

Publications. 2019-eggenberger-type-i-interferon-response-impairs, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Adeno-associated virus vectors** (`aav-vector`)

Surface forms. "adeno-associated virus vectors"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

**Agroinfiltration of plant tissue** (`agroinfiltration`)

Surface forms. "agroinfiltration"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**cDNA complementation of knockouts** (`genetic-complementation`)

Surface forms. "cDNA complementation"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

**Expression screening of codon-optimised heterologous proteins** (`heterologous-protein-expression-screen`)

Surface forms. "expression screening of codon-optimized proteins"

Publications. 2023-oishi-archaeal-kink-turn-binding-protein

**Head-to-head competition assay** (`competition-assay`)

Surface forms. "in vitro competition assay"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**Single-cell CRISPR screening with ECCITE-seq** (`single-cell-crispr-screen`)

Surface forms. "ECCITE-seq single-cell CRISPR screening"

Publications. 2021-daniloski-identification-of-required-host-fa

**Trans-complementation infection assay** (`trans-complementation-assay`)

Surface forms. "trans-complementation infection assay"

Publications. 2021-daniloski-the-spike-d614g-mutation-increases

### Genome engineering

**Cellular reprogramming to pluripotency** (`cellular-reprogramming`)

Surface forms. "cellular reprogramming with OCT4 SOX2 KLF4 and c-MYC"

Publications. 2019-eggenberger-type-i-interferon-response-impairs

**mSwAP-In iterative genome writing** (`mswap-in-genome-writing`)

Surface forms. "CRISPR-Cas9 assisted homologous recombination", "mSwAP-In genome writing", "yeast assembly of large DNA"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**Tetraploid blastocyst complementation** (`tetraploid-complementation`)

Surface forms. "tetraploid blastocyst complementation"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

### Imaging and histology

**Immunofluorescence and confocal microscopy** (`immunofluorescence-microscopy`)

Surface forms. "confocal immunofluorescence", "immunofluorescence", "immunofluorescence confocal microscopy", "immunofluorescence microscopy", "immunofluorescence microscopy and colocalization analysis"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2018-aguado-homologous-recombination-is-an-int, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-yaron-host-protein-kinases-required-for-, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Histopathology** (`histopathology`)

Surface forms. "haematoxylin and eosin histology", "histology and immunohistochemistry", "histopathology", "lung histology", "lung histopathology scoring"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2015-benitez-engineered-mammalian-rnai-can-elic, 2017-morales-sars-cov-encoded-small-rnas-contri, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-the-host-response-to-influenza-a-v, 2025-manivasagam-transcriptional-repressor-capicua-

**Immunohistochemistry** (`immunohistochemistry`)

Surface forms. "immunohistochemistry"

Publications. 2017-morales-sars-cov-encoded-small-rnas-contri, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-oishi-a-diminished-immune-response-under, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result, 2023-zhang-mouse-genome-rewriting-and-tailori

**RNA in situ hybridisation** (`rna-in-situ-hybridization`)

Surface forms. "RNA in situ hybridization", "RNAscope in situ hybridization"

Publications. 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-serafini-sars-cov-2-airway-infection-result

**Cell viability and cell death assays** (`cell-death-assays`)

Surface forms. "cell viability assay", "Sytox and caspase activity cell death assays", "TUNEL staining"

Publications. 2014-schmid-a-versatile-rna-vector-for-deliver, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2023-paget-stress-granules-are-shock-absorber

**Electron microscopy** (`electron-microscopy`)

Surface forms. "scanning electron microscopy", "transmission electron microscopy"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

**Fluorescent fusion protein localisation** (`fluorescent-fusion-localization`)

Surface forms. "GFP fusion localization"

Publications. 2003-sharma-triggering-the-interferon-antivira

**High-content microscopy** (`high-content-imaging`)

Surface forms. "high-content microscopy"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**Lectin staining of surface glycans** (`lectin-staining`)

Surface forms. "lectin staining"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

### Immunology assays

**Flow cytometry** (`flow-cytometry`)

Surface forms. "flow cytometry", "flow cytometry DNA content analysis", "flow cytometry immune profiling", "flow cytometry with cross-reactive antibodies", "imaging cytometry"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-oishi-a-diminished-immune-response-under, 2023-carrau-delayed-engagement-of-host-defense, 2023-uhl-adar1-biology-can-hinder-effective

**ELISA** (`elisa`)

Surface forms. "anti-RBD ELISA", "ELISA"

Publications. 2009-perez-microrna-mediated-species-specific, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-oishi-a-diminished-immune-response-under, 2023-paget-stress-granules-are-shock-absorber, 2023-zhang-mouse-genome-rewriting-and-tailori

**Multiplexed cytokine measurement** (`multiplex-cytokine-assay`)

Surface forms. "cytokine multiplex assay", "ELISA cytokine profiling", "Luminex cytokine panel", "multiplex bead cytokine array", "multiplexed ELISA"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2015-aguado-microrna-function-is-limited-to-cy, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r

**Cell and nuclei sorting** (`cell-sorting`)

Surface forms. "fluorescence-activated cell sorting", "fluorescence-activated nuclei sorting", "magnetic-activated cell sorting"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2014-heaton-long-term-survival-of-influenza-vi, 2022-zazhytska-non-cell-autonomous-disruption-of-

**Antigen-specific B cell detection** (`antigen-specific-b-cell-detection`)

Surface forms. "antigen-specific B cell staining", "biotinylated antigen B cell probe"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-oishi-a-diminished-immune-response-under

**Dye dilution cell division tracking** (`cell-division-tracking`)

Surface forms. "CellTrace Violet labeling", "CFSE cell division tracking"

Publications. 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2021-horiuchi-immune-memory-from-sars-cov-2-infe

**Plaque reduction neutralisation test** (`neutralization-assay`)

Surface forms. "plaque reduction neutralization test"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-oishi-a-diminished-immune-response-under

**Adoptive cell transfer** (`adoptive-transfer`)

Surface forms. "adoptive cell transfer"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe

**Hemagglutination inhibition assay** (`hemagglutination-inhibition`)

Surface forms. "hemagglutination inhibition assay"

Publications. 2009-perez-microrna-mediated-species-specific

**Interferon bioassay** (`interferon-bioassay`)

Surface forms. "interferon bioassay"

Publications. 2023-carrau-delayed-engagement-of-host-defense

**MHC class I tetramer staining** (`tetramer-staining`)

Surface forms. "MHC class I tetramer staining"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

**MHC epitope prediction** (`epitope-prediction`)

Surface forms. "MHC epitope prediction"

Publications. 2021-daniloski-the-spike-d614g-mutation-increases

**Peptide restimulation of T cells** (`t-cell-restimulation`)

Surface forms. "peptide restimulation assay"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe

**T cell hybridoma antigen presentation assay** (`antigen-presentation-assay`)

Surface forms. "CD8 T cell hybridoma antigen presentation assay"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

### Proteomics and biochemistry

**Luciferase promoter reporter assay** (`luciferase-promoter-reporter`)

Surface forms. "interferon-stimulated response element luciferase reporter", "luciferase promoter reporter assay", "luciferase reporter assay", "luciferase reporter assays", "promoter reporter assays"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2009-perez-microrna-mediated-species-specific, 2010-schmid-transcription-factor-redundancy-en, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2014-schmid-mitogen-activated-protein-kinase-m, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-han-genome-wide-crispr-cas9-screen-ide, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2025-manivasagam-transcriptional-repressor-capicua-

**Immunoblotting** (`immunoblotting`)

Surface forms. "immunoblotting", "western blot", "western blotting"

Publications. 2014-schmid-a-versatile-rna-vector-for-deliver, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2019-eggenberger-type-i-interferon-response-impairs, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Electrophoretic mobility shift assay** (`emsa`)

Surface forms. "electrophoretic mobility shift assay"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2014-schmid-mitogen-activated-protein-kinase-m, 2017-aguado-rnase-iii-nucleases-from-diverse-k

**In vitro reconstitution with purified components** (`in-vitro-reconstitution`)

Surface forms. "cell-free IRF3 dimerization assay", "in vitro minus-strand synthesis assay", "in vitro RNA polymerase assay", "in vitro RNase cleavage assay", "polymerase reconstitution assay", "reconstituted influenza replication complex"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber

**Coimmunoprecipitation** (`co-ip`)

Surface forms. "coimmunoprecipitation", "immunoprecipitation"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2014-schmid-mitogen-activated-protein-kinase-m, 2017-aguado-rnase-iii-nucleases-from-diverse-k

**In vitro kinase assay** (`in-vitro-kinase-assay`)

Surface forms. "in vitro kinase assay", "in vitro kinase assays", "radiolabeled ATP incorporation", "recombinant kinase assay"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2007-tenoever-multiple-functions-of-the-ikk-rela, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2022-yaron-host-protein-kinases-required-for-

**Mass spectrometry proteomics** (`mass-spectrometry-proteomics`)

Surface forms. "mass spectrometry", "mass spectrometry proteomics", "quantitative mass spectrometry", "quantitative mass spectrometry proteomics"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-si-a-human-airway-on-a-chip-for-the-r, 2023-oishi-archaeal-kink-turn-binding-protein

**Minigenome, minireplicon and replicon reporters** (`minigenome-assay`)

Surface forms. "minigenome assay", "minireplicon systems", "Sindbis replicon and luciferase reporters"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2019-tenoever-synthetic-virology-building-viruse, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Radiolabelling and translation measurement** (`translation-measurement`)

Surface forms. "in vivo radiolabeling", "puromycin incorporation translation assay", "radiolabeled amino acid tracing"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m, 2020-mccune-rapid-dissemination-and-monopoliza, 2023-paget-stress-granules-are-shock-absorber

**Phosphoproteomics** (`phosphoproteomics`)

Surface forms. "data-independent acquisition phosphoproteomics", "phosphoproteomics by liquid chromatography mass spectrometry"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca, 2022-yaron-host-protein-kinases-required-for-

**Phosphospecific immunoblotting and phosphatase treatment** (`phospho-immunoblotting`)

Surface forms. "phosphatase treatment", "phosphospecific immunoblotting"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2014-schmid-mitogen-activated-protein-kinase-m

**Subcellular fractionation** (`subcellular-fractionation`)

Surface forms. "subcellular fractionation"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly, 2014-shapiro-drosha-as-an-interferon-independen

**Bio-layer interferometry** (`biolayer-interferometry`)

Surface forms. "bio-layer interferometry"

Publications. 2021-daniloski-the-spike-d614g-mutation-increases

**Cellular cholesterol quantification** (`metabolite-quantification`)

Surface forms. "cholesterol quantification"

Publications. 2021-daniloski-identification-of-required-host-fa

**Chimeric minigene splicing reporters** (`splicing-reporter`)

Surface forms. "chimeric minigene reporters"

Publications. 2023-oishi-archaeal-kink-turn-binding-protein

**Combinatorial peptide substrate specificity profiling** (`kinase-substrate-profiling`)

Surface forms. "combinatorial peptide substrate specificity profiling"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Kinase activity inference** (`kinase-activity-inference`)

Surface forms. "kinase activity inference"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

**Phos-tag gel electrophoresis** (`phos-tag-electrophoresis`)

Surface forms. "Phos-tag gel electrophoresis"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Single-molecule FRET** (`single-molecule-fret`)

Surface forms. "single-molecule FRET"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Size-exclusion chromatography** (`size-exclusion-chromatography`)

Surface forms. "size-exclusion chromatography"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**Transcription and translation inhibitor blocks** (`metabolic-inhibitor-blocks`)

Surface forms. "cycloheximide and actinomycin D blocks"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

### Sequence and population analysis

**Deep sequencing of viral populations** (`viral-population-deep-sequencing`)

Surface forms. "deep sequencing", "deep sequencing of barcodes", "deep sequencing of virus populations", "escape mutant sequencing", "whole-genome consensus sequencing"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2014-varble-influenza-a-virus-transmission-bot, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-tenoever-synthetic-virology-building-viruse, 2020-mccune-rapid-dissemination-and-monopoliza

**Phylogenetic and coalescent analysis** (`phylogenetics`)

Surface forms. "dated coalescent analysis", "maximum likelihood phylogenetics", "phylogenetic analysis", "phylogenetic inference"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2021-guzman-solis-ancient-viral-genomes-reveal-intro, 2023-uhl-adar1-biology-can-hinder-effective

**Amplicon sequencing** (`amplicon-sequencing`)

Surface forms. "amplicon sequencing", "unique molecular identifier amplicon sequencing"

Publications. 2021-daniloski-identification-of-required-host-fa, 2023-uhl-adar1-biology-can-hinder-effective, 2023-zhang-mouse-genome-rewriting-and-tailori

**Short-read sequencing platforms** (`short-read-sequencing-platform`)

Surface forms. "Illumina deep sequencing", "Illumina MiSeq", "SOLiD sequencing"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2014-varble-influenza-a-virus-transmission-bot, 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**Comparative genomics and conservation analysis** (`comparative-sequence-analysis`)

Surface forms. "comparative genomics", "comparative sequence conservation analysis", "evolutionary parsimony analysis"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense, 2022-yaron-host-protein-kinases-required-for-

**Population diversity statistics and simulation** (`population-diversity-statistics`)

Surface forms. "Monte Carlo simulation", "Shannon diversity analysis"

Publications. 2014-varble-influenza-a-virus-transmission-bot, 2020-mccune-rapid-dissemination-and-monopoliza

**Targeted in-solution hybridisation capture** (`targeted-capture`)

Surface forms. "capture sequencing", "targeted in-solution hybridisation capture"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro, 2023-zhang-mouse-genome-rewriting-and-tailori

**Ancient DNA extraction** (`ancient-dna`)

Surface forms. "ancient DNA extraction"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Deamination damage authentication** (`ancient-dna-authentication`)

Surface forms. "deamination damage analysis"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Host genetic ancestry analysis** (`host-ancestry-analysis`)

Surface forms. "ADMIXTURE ancestry analysis", "principal component analysis of ancient genomes"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Radiocarbon dating and strontium isotope analysis** (`archaeometric-dating`)

Surface forms. "radiocarbon dating", "strontium isotope analysis"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Shotgun metagenomic sequencing** (`metagenomic-sequencing`)

Surface forms. "shotgun metagenomic sequencing"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

### Small RNA methods

**Small interfering RNA and short hairpin knockdown** (`sirna-knockdown`)

Surface forms. "RNA interference", "RNA interference knockdown", "short hairpin RNAs", "siRNA knockdown", "siRNA transfection", "small interfering RNA knockdown", "small interfering RNA silencing", "small interfering RNA transfection"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-schmid-transcription-factor-redundancy-en, 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2015-benitez-in-vivo-rnai-screening-identifies-, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-yaron-host-protein-kinases-required-for-, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Small RNA deep sequencing** (`small-rna-seq`)

Surface forms. "small RNA cloning and sequencing", "small RNA deep sequencing", "small RNA sequencing"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri

**Small RNA northern blot** (`small-rna-northern-blot`)

Surface forms. "small RNA Northern blot", "small RNA northern blot", "small RNA Northern blotting"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-shapiro-drosha-as-an-interferon-independen, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-m-ller-mirna-mediated-targeting-of-human-

**Northern blot** (`northern-blot`)

Surface forms. "northern blot", "Northern blot", "Northern blotting"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2021-nilsson-payant-reduced-nucleoprotein-availability

**Post-transcriptional silencing reporter assay** (`silencing-reporter-assay`)

Surface forms. "luciferase 3-prime UTR reporter assay", "luciferase reporter silencing assay", "reporter silencing assay", "reporter-based post-transcriptional silencing assay"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2017-morales-sars-cov-encoded-small-rnas-contri

**Argonaute immunoprecipitation** (`argonaute-ip`)

Surface forms. "Argonaute 2 immunoprecipitation", "argonaute immunoprecipitation", "Argonaute immunoprecipitation"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr

**Locked nucleic acid antisense inhibition** (`lna-antisense-inhibition`)

Surface forms. "locked nucleic acid antagomir inhibition", "locked nucleic acid antimiR inhibition", "locked nucleic acid antisense inhibition"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2017-morales-sars-cov-encoded-small-rnas-contri

**Primer extension** (`primer-extension`)

Surface forms. "primer extension"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**RNA immunoprecipitation** (`rna-immunoprecipitation`)

Surface forms. "RNA immunoprecipitation"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Stem-loop quantitative RT-PCR for small RNAs** (`small-rna-rt-qpcr`)

Surface forms. "small RNA RT-qPCR", "stem-loop quantitative RT-PCR"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-, 2017-morales-sars-cov-encoded-small-rnas-contri

**Synthetic and chemically modified RNA mimetics** (`synthetic-rna-mimetics`)

Surface forms. "synthetic 5-prime triphosphate RNA chemistry", "synthetic modified RNA mimetics"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2012-perez-a-small-rna-enhancer-of-viral-poly

**5 prime RACE** (`five-prime-race`)

Surface forms. "5' RACE"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-

**Genetic panels lacking small RNA machinery** (`rnai-machinery-knockout-cells`)

Surface forms. "Argonaute knockout cells", "Dicer deficient cells"

Publications. 2013-cullen-is-rna-interference-a-physiologica

**Morpholino knockdown** (`morpholino-knockdown`)

Surface forms. "morpholino knockdown"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**SELEX selection of bound RNA** (`selex`)

Surface forms. "SELEX"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**UV crosslinking immunoprecipitation sequencing** (`clip-seq`)

Surface forms. "UV crosslinking immunoprecipitation sequencing"

Publications. 2023-oishi-archaeal-kink-turn-binding-protein

### Transcriptomics and epigenomics

**Bulk RNA sequencing** (`bulk-rna-seq`)

Surface forms. "bulk mRNA sequencing", "bulk RNA sequencing", "messenger RNA sequencing", "mRNA deep sequencing", "mRNA sequencing", "ribosomal RNA-depleted total RNA sequencing", "RNA sequencing"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-m-ller-mirna-mediated-targeting-of-human-, 2019-eggenberger-type-i-interferon-response-impairs, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-serafini-sars-cov-2-airway-infection-result, 2023-uhl-adar1-biology-can-hinder-effective, 2023-zhang-mouse-genome-rewriting-and-tailori, 2025-manivasagam-transcriptional-repressor-capicua-

**Gene ontology and gene set enrichment analysis** (`pathway-enrichment-analysis`)

Surface forms. "gene ontology and gene set enrichment analysis", "gene ontology enrichment", "gene ontology enrichment analysis", "gene set enrichment analysis", "gene set enrichment with Enrichr", "Ingenuity Pathway Analysis"

Publications. 2015-aguado-microrna-function-is-limited-to-cy, 2018-m-ller-mirna-mediated-targeting-of-human-, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-serafini-sars-cov-2-airway-infection-result

**Single-cell RNA sequencing** (`single-cell-rna-seq`)

Surface forms. "single-cell RNA sequencing"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2022-zazhytska-non-cell-autonomous-disruption-of-

**ATAC sequencing** (`atac-seq`)

Surface forms. "ATAC sequencing", "ATAC-seq"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2023-zhang-mouse-genome-rewriting-and-tailori, 2025-manivasagam-transcriptional-repressor-capicua-

**Chromatin immunoprecipitation and CUT&RUN** (`chip`)

Surface forms. "ChIP sequencing", "chromatin immunoprecipitation", "CUT&RUN"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2023-zhang-mouse-genome-rewriting-and-tailori

**Dimensionality reduction and clustering** (`dimensionality-reduction`)

Surface forms. "multidimensional scaling", "network and medoid clustering analysis", "principal component analysis", "sparse principal component analysis"

Publications. 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Cell type deconvolution of bulk transcriptomes** (`deconvolution`)

Surface forms. "cell type deconvolution", "RNA sequencing deconvolution"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a, 2023-serafini-sars-cov-2-airway-infection-result

**Differential expression analysis** (`differential-expression-analysis`)

Surface forms. "differential expression analysis with DESeq2", "differential gene expression analysis"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-, 2022-oishi-the-host-response-to-influenza-a-v

**Expression microarray** (`microarray`)

Surface forms. "Affymetrix microarray"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en

**Promoter motif discovery and enrichment** (`motif-analysis`)

Surface forms. "motif discovery", "motif enrichment analysis"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2025-manivasagam-transcriptional-repressor-capicua-

**Transcription factor activity and motif accessibility inference** (`tf-activity-inference`)

Surface forms. "transcription factor activity inference", "transcription factor motif accessibility analysis"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Cross-dataset meta-analysis** (`meta-analysis`)

Surface forms. "cross-dataset meta-analysis"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**De novo transcriptome assembly** (`de-novo-transcriptome-assembly`)

Surface forms. "de novo transcriptome assembly"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in

**In situ Hi-C and compartment analysis** (`in-situ-hi-c`)

Surface forms. "hidden Markov model compartment analysis", "in situ Hi-C"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Noncanonical splice junction read analysis** (`splice-junction-analysis`)

Surface forms. "noncanonical junction read analysis"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

### Viral engineering

**Reverse genetics and virus rescue** (`reverse-genetics`)

Surface forms. "alphavirus reverse genetics", "bidirectional plasmid reverse genetics", "flavivirus infectious cDNA clone and virus rescue", "in vitro transcription and electroporation", "influenza A virus reverse genetics", "influenza reverse genetics", "paramyxovirus reverse genetics", "recombinant alphavirus engineering", "recombinant poxvirus engineering", "recombinant Sindbis virus", "recombinant viral vectors", "recombinant VSV reverse genetics", "reverse genetics"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-aguado-homologous-recombination-is-an-int, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-uhl-adar1-biology-can-hinder-effective

**MicroRNA target site insertion into viral genomes** (`mirna-target-site-insertion`)

Surface forms. "microRNA target cassette engineering", "microRNA target site attenuation", "microRNA target site engineering", "microRNA target site insertion", "microRNA target site insertion into viral genomes", "microRNA-mediated attenuation"

Publications. 2012-langlois-hematopoietic-specific-targeting-o, 2012-pham-replication-in-cells-of-hematopoie, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-aguado-homologous-recombination-is-an-int, 2018-m-ller-mirna-mediated-targeting-of-human-, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-uhl-adar1-biology-can-hinder-effective

**Barcoded virus libraries** (`barcoded-virus-library`)

Surface forms. "barcoded virus libraries", "barcoded virus library", "genetic barcoding", "RNA barcoding"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2014-varble-influenza-a-virus-transmission-bot, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2020-mccune-rapid-dissemination-and-monopoliza

**Virus-encoded artificial microRNAs** (`artificial-mirna`)

Surface forms. "artificial microRNA expression", "artificial microRNAs", "virus-encoded artificial microRNA"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-benitez-engineered-mammalian-rnai-can-elic, 2019-tenoever-synthetic-virology-building-viruse

**Serial passage and selection** (`serial-passage`)

Surface forms. "in vivo serial passage selection", "serial passage", "serial passage selection"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2018-aguado-homologous-recombination-is-an-int, 2023-oishi-archaeal-kink-turn-binding-protein

**2A peptide recoding of viral segments** (`2a-recoding`)

Surface forms. "2A peptide polycistronic design", "2A ribosome recoding"

Publications. 2013-chua-influenza-a-virus-utilizes-subopti, 2019-tenoever-synthetic-virology-building-viruse

**Bacterial artificial chromosome recombineering** (`bac-recombineering`)

Surface forms. "bacterial artificial chromosomes", "galK one-step BAC recombineering"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-, 2023-zhang-mouse-genome-rewriting-and-tailori

**Replication-incompetent influenza vector** (`single-cycle-influenza-vector`)

Surface forms. "replication-incompetent virus-like vectors"

Publications. 2013-chua-influenza-a-virus-utilizes-subopti, 2014-schmid-a-versatile-rna-vector-for-deliver

**Deep mutational scanning** (`deep-mutational-scanning`)

Surface forms. "deep mutational scanning"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Fluorescent and luciferase reporter viruses** (`reporter-virus`)

Surface forms. "fluorescent and luciferase reporter viruses"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Neutral red light-sensitive virus labeling** (`neutral-red-labeling`)

Surface forms. "neutral red light-sensitive virus labeling"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

**NS1-deleted influenza A virus** (`delns1-virus`)

Surface forms. "influenza A virus lacking NS1"

Publications. 2019-eggenberger-type-i-interferon-response-impairs

**RNA affinity tagging of viral genomes** (`rna-affinity-tagging`)

Surface forms. "RNA affinity tagging"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Small molecule-assisted shutoff of viral proteins** (`degron-shutoff`)

Surface forms. "small molecule-assisted shutoff"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Split NS segment 8 design** (`split-ns-segment`)

Surface forms. "split NS segment design"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**Suppressor-deficient virus mutants** (`vsr-mutant-viruses`)

Surface forms. "viral suppressor mutant viruses"

Publications. 2013-cullen-is-rna-interference-a-physiologica

**Transposon insertional mutagenesis of viral genomes** (`transposon-mutagenesis`)

Surface forms. "transposon insertional mutagenesis"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**VP55-mediated ablation of the cellular microRNA pool** (`vp55-mirna-ablation`)

Surface forms. "VP55 poly(A) polymerase microRNA degradation"

Publications. 2015-aguado-microrna-function-is-limited-to-cy

### Virology assays

**Quantitative RT-PCR** (`rt-qpcr`)

Surface forms. "quantitative PCR", "quantitative RT-PCR", "real-time quantitative RT-PCR", "RT-PCR", "RT-qPCR"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2013-langlois-microrna-based-strategy-to-mitigat, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-schmid-mitogen-activated-protein-kinase-m, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-han-genome-wide-crispr-cas9-screen-ide, 2018-m-ller-mirna-mediated-targeting-of-human-, 2019-eggenberger-type-i-interferon-response-impairs, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2023-carrau-delayed-engagement-of-host-defense, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-serafini-sars-cov-2-airway-infection-result, 2025-manivasagam-transcriptional-repressor-capicua-

**Plaque assay and TCID50 titration** (`plaque-assay`)

Surface forms. "plaque and TCID50 titration", "plaque assay", "TCID50 titration"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2012-langlois-hematopoietic-specific-targeting-o, 2012-pham-replication-in-cells-of-hematopoie, 2013-langlois-microrna-based-strategy-to-mitigat, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-aguado-homologous-recombination-is-an-int, 2018-m-ller-mirna-mediated-targeting-of-human-, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-mccune-rapid-dissemination-and-monopoliza, 2021-daniloski-identification-of-required-host-fa, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2023-carrau-delayed-engagement-of-host-defense, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-serafini-sars-cov-2-airway-infection-result, 2023-zhang-mouse-genome-rewriting-and-tailori

**Multicycle growth curves** (`growth-curve`)

Surface forms. "multicycle growth curve", "multicycle growth curves"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-varble-an-in-vivo-rnai-screening-approach, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-m-ller-mirna-mediated-targeting-of-human-

**Small molecule inhibitor profiling** (`small-molecule-inhibitor-profiling`)

Surface forms. "JAK inhibitor treatment", "pharmacological dose response profiling", "protease inhibition with TPCK", "small molecule kinase inhibition", "small-molecule inhibitor dose response", "small-molecule inhibitor panels"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2022-yaron-host-protein-kinases-required-for-

**Pseudotyped entry reporters** (`pseudotyped-entry-reporter`)

Surface forms. "beta-lactamase virus-like particle entry assay", "lentiviral pseudotyping", "pseudotyped virus entry assay", "vesicular stomatitis virus pseudo-entry virus"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-si-a-human-airway-on-a-chip-for-the-r

**Amplification on permissive cells to detect low-level infectious virus** (`virus-amplification-assay`)

Surface forms. "virus amplification on permissive cells"

Publications. 2023-carrau-delayed-engagement-of-host-defense

## Pathogens

43 canonical terms from 59 surface forms. Grouped by family, then ordered by number of publications.

### Adenoviridae

**Adenovirus** (`adenovirus`)

Surface forms. "adenovirus", "adenovirus type 5"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2015-aguado-microrna-function-is-limited-to-cy

### Arenaviridae

**Lassa virus** (`lassa-virus`)

Surface forms. "Lassa virus"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

### Bornaviridae

**Borna disease virus** (`borna-disease-virus`)

Surface forms. "Borna disease virus"

Publications. 2014-backes-the-mammalian-response-to-virus-in

### Coronaviridae

**SARS-CoV-2** (`sars-cov-2`)

Surface forms. "SARS-CoV-2", "SARS-CoV-2 B.1.351 beta variant", "SARS-CoV-2 USA-WA1/2020"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result, 2023-zhang-mouse-genome-rewriting-and-tailori

**SARS-CoV** (`sars-cov`)

Surface forms. "SARS-CoV", "SARS-CoV-1", "severe acute respiratory syndrome coronavirus"

Publications. 2017-morales-sars-cov-encoded-small-rnas-contri, 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Human coronavirus 229E** (`hcov-229e`)

Surface forms. "human coronavirus 229E"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Human coronavirus OC43** (`hcov-oc43`)

Surface forms. "human coronavirus OC43"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**MERS-CoV** (`mers-cov`)

Surface forms. "MERS-CoV"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

### Dicistroviridae

**Drosophila C virus** (`drosophila-c-virus`)

Surface forms. "Drosophila C virus"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Filoviridae

**Ebola virus** (`ebola-virus`)

Surface forms. "Ebola virus"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2021-nilsson-payant-reduced-nucleoprotein-availability

### Flaviviridae

**Dengue virus** (`dengue-virus`)

Surface forms. "dengue virus", "dengue virus serotype 2"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2013-tenoever-rna-viruses-and-the-host-microrna-

**Zika virus** (`zika-virus`)

Surface forms. "Zika virus"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide, 2025-manivasagam-transcriptional-repressor-capicua-

**Hepatitis C virus** (`hcv`)

Surface forms. "hepatitis C virus"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

**Langat virus** (`langat-virus`)

Surface forms. "Langat virus"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**West Nile virus** (`west-nile-virus`)

Surface forms. "West Nile virus"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

### Hepadnaviridae

**Hepatitis B virus** (`hbv`)

Surface forms. "hepatitis B virus"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

### Herpesviridae

**Herpesviruses as a group** (`herpesviruses`)

Surface forms. "herpesviruses"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

**Human cytomegalovirus** (`hcmv`)

Surface forms. "human cytomegalovirus"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

### Nodaviridae

**Nodamura virus** (`nodamura-virus`)

Surface forms. "nodamura virus"

Publications. 2013-cullen-is-rna-interference-a-physiologica

### Orthomyxoviridae

**Influenza A virus** (`influenza-a-virus`)

Surface forms. "influenza A virus", "influenza A virus H1N1 A/Puerto Rico/8/34", "influenza A virus H1N1 A/Puerto Rico/8/34 NS1 R38A K41A", "influenza A virus H3N2", "influenza A virus H5N1", "influenza A virus H5N1 A/Vietnam/1203/04", "influenza A/California/04/2009", "influenza A/California/04/2009 (H1N1pdm09)", "influenza A/WSN/33"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-oishi-the-host-response-to-influenza-a-v, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-serafini-sars-cov-2-airway-infection-result, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Infectious salmon anemia virus** (`infectious-salmon-anemia-virus`)

Surface forms. "infectious salmon anemia virus"

Publications. 2023-oishi-archaeal-kink-turn-binding-protein

**Influenza B virus** (`influenza-b-virus`)

Surface forms. "influenza B virus"

Publications. 2023-oishi-archaeal-kink-turn-binding-protein

### Paramyxoviridae

**Sendai virus** (`sendai-virus`)

Surface forms. "Sendai virus"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Human parainfluenza virus 3** (`hpiv3`)

Surface forms. "human parainfluenza virus 3", "human parainfluenza virus type 3"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2025-manivasagam-transcriptional-repressor-capicua-

**Measles virus** (`measles-virus`)

Surface forms. "measles virus"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

### Parvoviridae

**Human parvovirus B19** (`parvovirus-b19`)

Surface forms. "human parvovirus B19"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

### Picornaviridae

**Encephalomyocarditis virus** (`emcv`)

Surface forms. "encephalomyocarditis virus"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2018-han-genome-wide-crispr-cas9-screen-ide, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Poliovirus** (`poliovirus`)

Surface forms. "poliovirus"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2018-aguado-homologous-recombination-is-an-int, 2020-mccune-rapid-dissemination-and-monopoliza

**Coxsackievirus B3** (`coxsackievirus-b3`)

Surface forms. "coxsackievirus B3"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

### Pneumoviridae

**Respiratory syncytial virus** (`rsv`)

Surface forms. "human respiratory syncytial virus", "respiratory syncytial virus"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2025-manivasagam-transcriptional-repressor-capicua-

### Poxviridae

**Vaccinia virus** (`vaccinia-virus`)

Surface forms. "vaccinia virus"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2014-backes-the-mammalian-response-to-virus-in, 2015-aguado-microrna-function-is-limited-to-cy

**Amsacta moorei entomopoxvirus** (`amsacta-entomopoxvirus`)

Surface forms. "Amsacta moorei entomopoxvirus"

Publications. 2012-backes-degradation-of-host-micrornas-by-p

**Poxviruses as a group** (`poxviruses`)

Surface forms. "poxviruses"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

### Retroviridae

**Bovine leukaemia virus** (`blv`)

Surface forms. "bovine leukaemia virus"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

**Human immunodeficiency virus 1** (`hiv-1`)

Surface forms. "human immunodeficiency virus 1"

Publications. 2013-cullen-is-rna-interference-a-physiologica

### Rhabdoviridae

**Vesicular stomatitis virus** (`vsv`)

Surface forms. "vesicular stomatitis virus"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-perez-influenza-a-virus-generated-small-, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-si-a-human-airway-on-a-chip-for-the-r, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

### Togaviridae

**Sindbis virus** (`sindbis-virus`)

Surface forms. "Sindbis virus"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int

**Ross River virus** (`ross-river-virus`)

Surface forms. "Ross River virus"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Semliki Forest virus** (`semliki-forest-virus`)

Surface forms. "Semliki Forest virus"

Publications. 2018-aguado-homologous-recombination-is-an-int

### Tombusviridae

**Turnip crinkle virus** (`turnip-crinkle-virus`)

Surface forms. "turnip crinkle virus"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Group

**DNA viruses as a group** (`dna-viruses`)

Surface forms. "DNA viruses"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

**RNA viruses as a group** (`rna-viruses`)

Surface forms. "RNA viruses"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

### Phage

**Bacteriophage** (`bacteriophage`)

Surface forms. "bacteriophage"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

## Viral families

20 canonical terms from 20 surface forms. Grouped by family, then ordered by number of publications.

### Double-stranded DNA

**Poxviridae** (`poxviridae`)

Surface forms. "Poxviridae"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2015-aguado-microrna-function-is-limited-to-cy

**Adenoviridae** (`adenoviridae`)

Surface forms. "Adenoviridae"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2015-aguado-microrna-function-is-limited-to-cy

**Herpesviridae** (`herpesviridae`)

Surface forms. "Herpesviridae"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2018-m-ller-mirna-mediated-targeting-of-human-

### Negative-sense nonsegmented RNA

**Rhabdoviridae** (`rhabdoviridae`)

Surface forms. "Rhabdoviridae"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-perez-influenza-a-virus-generated-small-, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2018-han-genome-wide-crispr-cas9-screen-ide, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-si-a-human-airway-on-a-chip-for-the-r, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Paramyxoviridae** (`paramyxoviridae`)

Surface forms. "Paramyxoviridae"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Pneumoviridae** (`pneumoviridae`)

Surface forms. "Pneumoviridae"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2025-manivasagam-transcriptional-repressor-capicua-

**Filoviridae** (`filoviridae`)

Surface forms. "Filoviridae"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2021-nilsson-payant-reduced-nucleoprotein-availability

**Bornaviridae** (`bornaviridae`)

Surface forms. "Bornaviridae"

Publications. 2014-backes-the-mammalian-response-to-virus-in

### Negative-sense segmented RNA

**Orthomyxoviridae** (`orthomyxoviridae`)

Surface forms. "Orthomyxoviridae"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-oishi-the-host-response-to-influenza-a-v, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-serafini-sars-cov-2-airway-infection-result, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Arenaviridae** (`arenaviridae`)

Surface forms. "Arenaviridae"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

### Positive-sense RNA

**Coronaviridae** (`coronaviridae`)

Surface forms. "Coronaviridae"

Publications. 2017-morales-sars-cov-encoded-small-rnas-contri, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result, 2023-zhang-mouse-genome-rewriting-and-tailori

**Togaviridae** (`togaviridae`)

Surface forms. "Togaviridae"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int

**Picornaviridae** (`picornaviridae`)

Surface forms. "Picornaviridae"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2020-mccune-rapid-dissemination-and-monopoliza, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Flaviviridae** (`flaviviridae`)

Surface forms. "Flaviviridae"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-han-genome-wide-crispr-cas9-screen-ide, 2025-manivasagam-transcriptional-repressor-capicua-

**Dicistroviridae** (`dicistroviridae`)

Surface forms. "Dicistroviridae"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Nodaviridae** (`nodaviridae`)

Surface forms. "Nodaviridae"

Publications. 2013-cullen-is-rna-interference-a-physiologica

**Tombusviridae** (`tombusviridae`)

Surface forms. "Tombusviridae"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Reverse-transcribing

**Retroviridae** (`retroviridae`)

Surface forms. "Retroviridae"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2013-tenoever-rna-viruses-and-the-host-microrna-

**Hepadnaviridae** (`hepadnaviridae`)

Surface forms. "Hepadnaviridae"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

### Single-stranded DNA

**Parvoviridae** (`parvoviridae`)

Surface forms. "Parvoviridae"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

## Host species

21 canonical terms from 30 surface forms. Grouped by family, then ordered by number of publications.

### Archaeon

**Archaea** (`archaea`)

Surface forms. "archaea"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

### Bird

**Chicken** (`chicken`)

Surface forms. "chicken", "chicken embryo"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2022-nilsson-payant-the-host-factor-anp32a-is-required

### Fish

**Zebrafish** (`zebrafish`)

Surface forms. "zebrafish"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Fungus

**Yeast** (`yeast`)

Surface forms. "yeast"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

### Group

**Chordates as a group** (`chordates`)

Surface forms. "chordates"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

### Invertebrate

**Drosophila melanogaster** (`drosophila`)

Surface forms. "Drosophila", "Drosophila melanogaster"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2014-shapiro-drosha-as-an-interferon-independen, 2016-tenoever-the-evolution-of-antiviral-defense, 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Amsacta moorei** (`amsacta-moorei`)

Surface forms. "Amsacta moorei"

Publications. 2012-backes-degradation-of-host-micrornas-by-p

**Insects as a group** (`insect`)

Surface forms. "insect"

Publications. 2013-cullen-is-rna-interference-a-physiologica

**Mosquito** (`mosquito`)

Surface forms. "mosquito"

Publications. 2012-pham-replication-in-cells-of-hematopoie

**Nematode** (`nematode`)

Surface forms. "nematode"

Publications. 2013-cullen-is-rna-interference-a-physiologica

### Mammal

**Human** (`human`)

Surface forms. "human", "human cells"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-pham-replication-in-cells-of-hematopoie, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2014-varble-influenza-a-virus-transmission-bot, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2016-tenoever-the-evolution-of-antiviral-defense, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2018-m-ller-mirna-mediated-targeting-of-human-, 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-mccune-rapid-dissemination-and-monopoliza, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-guzman-solis-ancient-viral-genomes-reveal-intro, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective, 2023-zhang-mouse-genome-rewriting-and-tailori, 2025-manivasagam-transcriptional-repressor-capicua-

**Mouse** (`mouse`)

Surface forms. "mouse"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2014-varble-influenza-a-virus-transmission-bot, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2016-tenoever-the-evolution-of-antiviral-defense, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri, 2018-aguado-homologous-recombination-is-an-int, 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse, 2020-mccune-rapid-dissemination-and-monopoliza, 2020-yang-a-human-pluripotent-stem-cell-base, 2023-serafini-sars-cov-2-airway-infection-result, 2023-uhl-adar1-biology-can-hinder-effective, 2023-zhang-mouse-genome-rewriting-and-tailori, 2025-manivasagam-transcriptional-repressor-capicua-

**Golden hamster** (`golden-hamster`)

Surface forms. "golden hamster", "hamster", "hamster cells"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-cullen-is-rna-interference-a-physiologica, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result, 2023-uhl-adar1-biology-can-hinder-effective, 2023-zhang-mouse-genome-rewriting-and-tailori

**Dog** (`dog`)

Surface forms. "canine", "canine cells", "dog"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-hematopoietic-specific-targeting-o, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-uhl-adar1-biology-can-hinder-effective

**African green monkey** (`african-green-monkey`)

Surface forms. "African green monkey", "African green monkey cells"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2020-bouhaddou-the-global-phosphorylation-landsca, 2022-yaron-host-protein-kinases-required-for-, 2023-carrau-delayed-engagement-of-host-defense, 2023-oishi-archaeal-kink-turn-binding-protein

**Ferret** (`ferret`)

Surface forms. "ferret"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat, 2014-varble-influenza-a-virus-transmission-bot, 2019-tenoever-synthetic-virology-building-viruse, 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Guinea pig** (`guinea-pig`)

Surface forms. "guinea pig"

Publications. 2014-varble-influenza-a-virus-transmission-bot

### Plant

**Plants as a group** (`plants`)

Surface forms. "plant", "plants"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2016-tenoever-the-evolution-of-antiviral-defense

**Arabidopsis thaliana** (`arabidopsis`)

Surface forms. "Arabidopsis thaliana"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Nicotiana benthamiana** (`nicotiana-benthamiana`)

Surface forms. "Nicotiana benthamiana"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

### Prokaryote

**Bacteria** (`bacteria`)

Surface forms. "bacteria"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

## Biological systems

197 canonical terms from 240 surface forms. Grouped by family, then ordered by number of publications.

### Animal or egg system

**Embryonated chicken eggs** (`embryonated-eggs`)

Surface forms. "embryonated chicken eggs"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-heaton-long-term-survival-of-influenza-vi, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2019-tenoever-synthetic-virology-building-viruse

**Golden hamster** (`golden-hamster-animal`)

Surface forms. "golden hamster"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2023-carrau-delayed-engagement-of-host-defense, 2023-zhang-mouse-genome-rewriting-and-tailori

**Laboratory mice** (`mouse-animal`)

Surface forms. "BALB/c mice", "C57BL/6 mice", "C57BL/6 mouse", "mouse", "mouse models", "suckling mice"

Publications. 2009-perez-microrna-mediated-species-specific, 2013-cullen-is-rna-interference-a-physiologica, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2019-tenoever-synthetic-virology-building-viruse

**Ferret** (`ferret-animal`)

Surface forms. "ferret"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat, 2014-varble-influenza-a-virus-transmission-bot, 2019-tenoever-synthetic-virology-building-viruse

**Guinea pig** (`guinea-pig`)

Surface forms. "guinea pig"

Publications. 2014-varble-influenza-a-virus-transmission-bot

**LoxP reporter mice** (`loxp-reporter-mice`)

Surface forms. "LoxP reporter mice"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**SCID-beige mouse xenograft** (`scid-beige-mouse-xenograft`)

Surface forms. "SCID-beige mouse xenograft"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Zebrafish embryos** (`zebrafish-embryos`)

Surface forms. "zebrafish embryos"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Cell-free or reconstituted

**Cell-free in vitro polymerase reactions** (`cell-free-in-vitro-polymerase-reactions`)

Surface forms. "cell-free in vitro polymerase reactions"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly

**Cell-free mitochondrial fraction assay** (`cell-free-mitochondrial-fraction-assay`)

Surface forms. "cell-free mitochondrial fraction assay"

Publications. 2023-paget-stress-granules-are-shock-absorber

**In vitro replicase assays** (`in-vitro-replicase-assays`)

Surface forms. "in vitro replicase assays"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Purified recombinant influenza A virus polymerase** (`purified-recombinant-influenza-a-virus-polymerase`)

Surface forms. "purified recombinant influenza A virus polymerase"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly

**Recombinant protein in vitro kinase reactions** (`recombinant-protein-in-vitro-kinase-reactions`)

Surface forms. "recombinant protein in vitro kinase reactions"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Recombinant purified influenza RNA polymerase** (`recombinant-purified-influenza-rna-polymerase`)

Surface forms. "recombinant purified influenza RNA polymerase"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

### Engineered cell line

**ACE2-expressing A549 cells** (`a549-ace2`)

Surface forms. "A549 cells expressing ACE2", "A549-ACE2 cells", "ACE2-expressing A549 cells"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-

**Huh7.5-ACE2 cells** (`huh7-5-ace2-cells`)

Surface forms. "Huh7.5-ACE2 cells"

Publications. 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases

**A549-Dual reporter cells** (`a549-dual-reporter-cells`)

Surface forms. "A549-Dual reporter cells"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

**Cas9-expressing A549 clonal line** (`cas9-expressing-a549-clonal-line`)

Surface forms. "Cas9-expressing A549 clonal line"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

**Complementing MDCK cells** (`mdck-complementing`)

Surface forms. "HA and NP complementing MDCK cells", "HA-complementing MDCK cells"

Publications. 2014-schmid-a-versatile-rna-vector-for-deliver

**DBT-mACE2 cells** (`dbt-mace2-cells`)

Surface forms. "DBT-mACE2 cells"

Publications. 2017-morales-sars-cov-encoded-small-rnas-contri

**HEK293T cells stably expressing IRF7** (`hek293t-cells-stably-expressing-irf7`)

Surface forms. "HEK293T cells stably expressing IRF7"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m

**HeLa cells expressing E1A** (`hela-cells-expressing-e1a`)

Surface forms. "HeLa cells expressing E1A"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**HeLa-ACE2 cells** (`hela-ace2-cells`)

Surface forms. "HeLa-ACE2 cells"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**K18-hACE2 mouse** (`k18-hace2-mouse`)

Surface forms. "K18-hACE2 mouse"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**MDCK cells expressing miR-124** (`mdck-cells-expressing-mir-124`)

Surface forms. "MDCK cells expressing miR-124"

Publications. 2015-benitez-engineered-mammalian-rnai-can-elic

**MiR-122-expressing MRC-5 fibroblasts** (`mir-122-expressing-mrc-5-fibroblasts`)

Surface forms. "miR-122-expressing MRC-5 fibroblasts"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**MiR-142-expressing MDCK cells** (`mir-142-expressing-mdck-cells`)

Surface forms. "miR-142-expressing MDCK cells"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

**MiR-142-expressing MRC-5 fibroblasts** (`mir-142-expressing-mrc-5-fibroblasts`)

Surface forms. "miR-142-expressing MRC-5 fibroblasts"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

### Engineered knockout line

**Dicer-deficient fibroblasts** (`dicer-deficient-fibroblasts`)

Surface forms. "Dicer conditional knockout fibroblasts", "Dicer knockout fibroblasts", "Dicer-deficient fibroblasts", "Dicer-deficient murine fibroblasts", "Dicer1-deficient fibroblasts"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2018-aguado-homologous-recombination-is-an-int

**NoDice Dicer-deficient HEK293T cells** (`nodice-cells`)

Surface forms. "HEK-293T NoDice cells", "NoDice 293T cells", "NoDice Dicer-deficient cells", "NoDice Dicer-deficient HEK293T cells", "NoDice HEK293T cells"

Publications. 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-uhl-adar1-biology-can-hinder-effective

**Drosha and Dicer double knockout HEK293T cells** (`drosha-dicer-dko-293t`)

Surface forms. "Drosha and Dicer deficient 293T cells", "Drosha and Dicer double knockout HEK293T cells"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri

**Ifnar1 and Il28r double knockout mice** (`ifnar1-and-il28r-double-knockout-mice`)

Surface forms. "Ifnar1 and Il28r double knockout mice"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2014-backes-the-mammalian-response-to-virus-in

**ADAR1 knockout A549 cells** (`adar1-knockout-a549-cells`)

Surface forms. "ADAR1 knockout A549 cells"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**Argonaute knockout fibroblasts** (`argonaute-knockout-fibroblasts`)

Surface forms. "Argonaute knockout fibroblasts"

Publications. 2018-aguado-homologous-recombination-is-an-int

**Conditional knockout fibroblast lines** (`conditional-knockout-fibroblast-lines`)

Surface forms. "conditional knockout fibroblast lines"

Publications. 2012-shapiro-evidence-for-a-cytoplasmic-micropr

**CRISPR knockout clonal lines** (`crispr-knockout-clonal-lines`)

Surface forms. "CRISPR knockout clonal lines"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

**DGCR8-deficient fibroblasts** (`dgcr8-deficient-fibroblasts`)

Surface forms. "DGCR8-deficient fibroblasts"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin

**G3BP1 and G3BP2 knockout cells** (`g3bp1-and-g3bp2-knockout-cells`)

Surface forms. "G3BP1 and G3BP2 knockout cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Ifnar1 knockout mice** (`ifnar1-knockout-mice`)

Surface forms. "Ifnar1 knockout mice"

Publications. 2015-benitez-engineered-mammalian-rnai-can-elic

**Ifnar1-deficient fibroblasts** (`ifnar1-deficient-fibroblasts`)

Surface forms. "Ifnar1-deficient fibroblasts"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin

**Ikbke knockout mice** (`ikbke-knockout-mice`)

Surface forms. "Ikbke knockout mice"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**Ikbke-deficient mice** (`ikbke-deficient-mice`)

Surface forms. "Ikbke-deficient mice"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela

**Irf3 and Irf7 double knockout fibroblasts** (`irf3-and-irf7-double-knockout-fibroblasts`)

Surface forms. "Irf3 and Irf7 double knockout fibroblasts"

Publications. 2015-benitez-engineered-mammalian-rnai-can-elic

**Map3k8 knockout fibroblasts** (`map3k8-knockout-fibroblasts`)

Surface forms. "Map3k8 knockout fibroblasts"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m

**MAVS knockout cells** (`mavs-knockout-cells`)

Surface forms. "MAVS knockout cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**MAVS-deficient A549 cells** (`mavs-deficient-a549-cells`)

Surface forms. "MAVS-deficient A549 cells"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

**MDA5-deficient A549 cells** (`mda5-deficient-a549-cells`)

Surface forms. "MDA5-deficient A549 cells"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

**PKR knockout cells** (`pkr-knockout-cells`)

Surface forms. "PKR knockout cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Rag1 deficient mice** (`rag1-deficient-mice`)

Surface forms. "Rag1 deficient mice"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**RELA knockout HeLa-ACE2 cells** (`rela-knockout-hela-ace2-cells`)

Surface forms. "RELA knockout HeLa-ACE2 cells"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**RIG-I-deficient A549 cells** (`rig-i-deficient-a549-cells`)

Surface forms. "RIG-I-deficient A549 cells"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability

**RNase III deficient fibroblasts** (`rnase-iii-deficient-fibroblasts`)

Surface forms. "RNase III deficient fibroblasts"

Publications. 2018-aguado-homologous-recombination-is-an-int

**RNase L knockout cells** (`rnase-l-knockout-cells`)

Surface forms. "RNase L knockout cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Stat1 deficient mice** (`stat1-deficient-mice`)

Surface forms. "Stat1 deficient mice"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**STAT1 knockout A549 cells** (`stat1-knockout-a549-cells`)

Surface forms. "STAT1 knockout A549 cells"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**Stat1-deficient embryonic fibroblasts** (`stat1-deficient-embryonic-fibroblasts`)

Surface forms. "Stat1-deficient embryonic fibroblasts"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela

**U3A STAT1-deficient cells** (`u3a-stat1-deficient-cells`)

Surface forms. "U3A STAT1-deficient cells"

Publications. 2010-schmid-transcription-factor-redundancy-en

**UBAP2L knockout cells** (`ubap2l-knockout-cells`)

Surface forms. "UBAP2L knockout cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Zfx conditional knockout primary fibroblasts** (`zfx-conditional-knockout-primary-fibroblasts`)

Surface forms. "Zfx conditional knockout primary fibroblasts"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach

### General

**Mammalian cell culture in general** (`mammalian-cell-culture`)

Surface forms. "mammalian cell culture", "mammalian somatic cells"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2016-tenoever-the-evolution-of-antiviral-defense, 2019-tenoever-synthetic-virology-building-viruse

### Human clinical or post-mortem material

**Archaeological human dental remains** (`archaeological-human-dental-remains`)

Surface forms. "archaeological human dental remains"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**COVID-19 lung autopsy tissue** (`covid-19-lung-autopsy-tissue`)

Surface forms. "COVID-19 lung autopsy tissue"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Ferret nasal wash and trachea** (`ferret-nasal-wash-and-trachea`)

Surface forms. "ferret nasal wash and trachea"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Human COVID-19 cadaver lung tissue** (`human-covid-19-cadaver-lung-tissue`)

Surface forms. "human COVID-19 cadaver lung tissue"

Publications. 2022-oishi-a-diminished-immune-response-under

**Human olfactory epithelium autopsy tissue** (`human-olfactory-epithelium-autopsy-tissue`)

Surface forms. "human olfactory epithelium autopsy tissue"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Human serum** (`human-serum`)

Surface forms. "human serum"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Nasal wash** (`nasal-wash`)

Surface forms. "nasal wash"

Publications. 2014-varble-influenza-a-virus-transmission-bot

**Parietal bone** (`parietal-bone`)

Surface forms. "parietal bone"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Peripheral blood mononuclear cells** (`peripheral-blood-mononuclear-cells`)

Surface forms. "peripheral blood mononuclear cells"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe

**Phalanx** (`phalanx`)

Surface forms. "phalanx"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Post-mortem human lung** (`post-mortem-human-lung`)

Surface forms. "post-mortem human lung"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Post-mortem human ocular surface tissue** (`post-mortem-human-ocular-surface-tissue`)

Surface forms. "post-mortem human ocular surface tissue"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

**Post-mortem human olfactory bulb and olfactory epithelium** (`post-mortem-human-olfactory-bulb-and-olfactory-epithelium`)

Surface forms. "post-mortem human olfactory bulb and olfactory epithelium"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

**Stool** (`stool`)

Surface forms. "stool"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

**Tooth enamel** (`tooth-enamel`)

Surface forms. "tooth enamel"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

**Whole blood** (`whole-blood`)

Surface forms. "whole blood"

Publications. 2023-carrau-delayed-engagement-of-host-defense

### Immortalised cell line

**HEK293 and HEK293T cells** (`hek293`)

Surface forms. "293T cells", "HEK-293T cells", "HEK293 and 293T cells", "HEK293 cells", "HEK293FT cells", "HEK293T cells"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2012-pham-replication-in-cells-of-hematopoie, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri, 2019-eggenberger-type-i-interferon-response-impairs, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-mccune-rapid-dissemination-and-monopoliza, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2023-oishi-archaeal-kink-turn-binding-protein, 2025-manivasagam-transcriptional-repressor-capicua-

**A549 cells** (`a549`)

Surface forms. "A549 cells"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-aguado-homologous-recombination-is-an-int, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**MDCK cells** (`mdck`)

Surface forms. "MDCK cells"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-hematopoietic-specific-targeting-o, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2014-varble-influenza-a-virus-transmission-bot, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2022-oishi-the-host-response-to-influenza-a-v, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-uhl-adar1-biology-can-hinder-effective

**BHK-21 baby hamster kidney cells** (`bhk`)

Surface forms. "baby hamster kidney cells", "BHK cells", "BHK-21 cells", "BHK21 cells"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-cullen-is-rna-interference-a-physiologica, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-carrau-delayed-engagement-of-host-defense

**Vero E6 cells** (`vero-e6`)

Surface forms. "Vero E6 cells"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2022-yaron-host-protein-kinases-required-for-, 2023-carrau-delayed-engagement-of-host-defense, 2023-oishi-archaeal-kink-turn-binding-protein

**Calu-3 cells** (`calu-3`)

Surface forms. "Calu-3 2B4 cells", "Calu-3 cells", "Calu3 cells"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat, 2017-morales-sars-cov-encoded-small-rnas-contri, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2022-yaron-host-protein-kinases-required-for-

**Vero cells** (`vero`)

Surface forms. "Vero cells"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-shapiro-noncanonical-cytoplasmic-processin, 2013-varble-an-in-vivo-rnai-screening-approach, 2023-serafini-sars-cov-2-airway-infection-result

**Caco-2 cells** (`caco-2`)

Surface forms. "Caco-2 cells"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases

**HeLa cells** (`hela`)

Surface forms. "HeLa cells"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber

**2FTGH fibrosarcoma cells** (`2ftgh`)

Surface forms. "2FTGH cells", "2FTGH fibrosarcoma cells"

Publications. 2010-schmid-transcription-factor-redundancy-en, 2014-schmid-mitogen-activated-protein-kinase-m

**Huh7 cells** (`huh7`)

Surface forms. "Huh-7 cells", "Huh7 cells"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-yaron-host-protein-kinases-required-for-

**BSC-1 cells** (`bsc-1-cells`)

Surface forms. "BSC-1 cells"

Publications. 2012-backes-degradation-of-host-micrornas-by-p

**BSRT7 cells** (`bsrt7-cells`)

Surface forms. "BSRT7 cells"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**C6 glial cells** (`c6-glial-cells`)

Surface forms. "C6 glial cells"

Publications. 2014-backes-the-mammalian-response-to-virus-in

**CAD neuronal precursor cells** (`cad-neuronal-precursor-cells`)

Surface forms. "CAD neuronal precursor cells"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-

**COS-7 cells** (`cos-7-cells`)

Surface forms. "COS-7 cells"

Publications. 2003-sharma-triggering-the-interferon-antivira

**DF-1 chicken embryonic fibroblasts** (`df-1-chicken-embryonic-fibroblasts`)

Surface forms. "DF-1 chicken embryonic fibroblasts"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Endothelial cells** (`endothelial-cells`)

Surface forms. "endothelial cells"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Genetically engineered mouse models** (`genetically-engineered-mouse-models`)

Surface forms. "genetically engineered mouse models"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**H441 human club cell line** (`h441-human-club-cell-line`)

Surface forms. "H441 human club cell line"

Publications. 2014-heaton-long-term-survival-of-influenza-vi

**Hepa 1.6 cells** (`hepa-1-6-cells`)

Surface forms. "Hepa 1.6 cells"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach

**Human bronchial epithelial cells** (`human-bronchial-epithelial-cells`)

Surface forms. "human bronchial epithelial cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

**JAWS II dendritic cell line** (`jaws-ii-dendritic-cell-line`)

Surface forms. "JAWS II dendritic cell line"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

**Jurkat T cells** (`jurkat-t-cells`)

Surface forms. "Jurkat T cells"

Publications. 2013-chua-influenza-a-virus-utilizes-subopti

**Mouse hindpaw inflammatory pain model** (`mouse-hindpaw-inflammatory-pain-model`)

Surface forms. "mouse hindpaw inflammatory pain model"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Mouse oocytes** (`mouse-oocytes`)

Surface forms. "mouse oocytes"

Publications. 2013-cullen-is-rna-interference-a-physiologica

**Mouse paw incision model** (`mouse-paw-incision-model`)

Surface forms. "mouse paw incision model"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Mouse spared nerve injury comparison dataset** (`mouse-spared-nerve-injury-comparison-dataset`)

Surface forms. "mouse spared nerve injury comparison dataset"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**MRC-5 fibroblasts** (`mrc-5`)

Surface forms. "MRC-5 fibroblasts"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**MtCC10-1 murine club cell line** (`mtcc10-1-murine-club-cell-line`)

Surface forms. "mtCC10-1 murine club cell line"

Publications. 2014-heaton-long-term-survival-of-influenza-vi

**Pancreatic endocrine cells** (`pancreatic-endocrine-cells`)

Surface forms. "pancreatic endocrine cells"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Raji B cells** (`raji-b-cells`)

Surface forms. "Raji B cells"

Publications. 2012-pham-replication-in-cells-of-hematopoie

**RAW macrophage cells** (`raw-macrophage-cells`)

Surface forms. "RAW macrophage cells"

Publications. 2014-backes-the-mammalian-response-to-virus-in

**Rederived fibroblasts** (`rederived-fibroblasts`)

Surface forms. "rederived fibroblasts"

Publications. 2019-eggenberger-type-i-interferon-response-impairs

**U2OS cells** (`u2os-cells`)

Surface forms. "U2OS cells"

Publications. 2023-paget-stress-granules-are-shock-absorber

### Invertebrate cell system

**Drosophila DL1 cells** (`drosophila-dl1`)

Surface forms. "Drosophila DL1 cells"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k

### Non-vertebrate or plant system

**Arthropods** (`arthropods`)

Surface forms. "arthropods"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2016-tenoever-the-evolution-of-antiviral-defense

**Plants** (`plants`)

Surface forms. "plants"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-, 2016-tenoever-the-evolution-of-antiviral-defense

**Amsacta moorei Ld652 cells** (`amsacta-moorei-ld652-cells`)

Surface forms. "Amsacta moorei Ld652 cells"

Publications. 2012-backes-degradation-of-host-micrornas-by-p

**Arabidopsis protoplasts** (`arabidopsis-protoplasts`)

Surface forms. "Arabidopsis protoplasts"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Archaea** (`archaea`)

Surface forms. "archaea"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

**Bacteria** (`bacteria`)

Surface forms. "bacteria"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

**C6/36 Aedes albopictus cells** (`c6-36-aedes-albopictus-cells`)

Surface forms. "C6/36 Aedes albopictus cells"

Publications. 2012-pham-replication-in-cells-of-hematopoie

**Chordates** (`chordates`)

Surface forms. "chordates"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

**Eukaryotes** (`eukaryotes`)

Surface forms. "eukaryotes"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

**Nematodes** (`nematodes`)

Surface forms. "nematodes"

Publications. 2013-tenoever-rna-viruses-and-the-host-microrna-

**Nicotiana benthamiana** (`nicotiana-benthamiana`)

Surface forms. "Nicotiana benthamiana"

Publications. 2023-uhl-adar1-biology-can-hinder-effective

**TB40/E bacterial artificial chromosome** (`tb40-e-bacterial-artificial-chromosome`)

Surface forms. "TB40/E bacterial artificial chromosome"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**Yeast assembly vector** (`yeast-assembly-vector`)

Surface forms. "yeast assembly vector"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

### Organoid, chip or stem cell system

**Adult cholangiocyte organoids** (`adult-cholangiocyte-organoids`)

Surface forms. "adult cholangiocyte organoids"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Adult hepatocyte organoids** (`adult-hepatocyte-organoids`)

Surface forms. "adult hepatocyte organoids"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Adult primary human islets** (`adult-primary-human-islets`)

Surface forms. "adult primary human islets"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Cardiomyocytes** (`cardiomyocytes`)

Surface forms. "cardiomyocytes"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Human embryonic stem cell derived SEAM whole-eye cultures** (`human-embryonic-stem-cell-derived-seam-whole-eye-cultures`)

Surface forms. "human embryonic stem cell derived SEAM whole-eye cultures"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

**Human induced pluripotent stem cells** (`human-induced-pluripotent-stem-cells`)

Surface forms. "human induced pluripotent stem cells"

Publications. 2019-eggenberger-type-i-interferon-response-impairs

**Human pluripotent stem cell derivatives** (`human-pluripotent-stem-cell-derivatives`)

Surface forms. "human pluripotent stem cell derivatives"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**IPSC-derived cardiomyocytes** (`ipsc-derived-cardiomyocytes`)

Surface forms. "iPSC-derived cardiomyocytes"

Publications. 2019-eggenberger-type-i-interferon-response-impairs

**Liver organoids** (`liver-organoids`)

Surface forms. "liver organoids"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Microfluidic human bronchial airway chip** (`microfluidic-human-bronchial-airway-chip`)

Surface forms. "microfluidic human bronchial airway chip"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Primary human bronchial airway basal stem cells** (`primary-human-bronchial-airway-basal-stem-cells`)

Surface forms. "primary human bronchial airway basal stem cells"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Stem cells** (`stem-cells`)

Surface forms. "stem cells"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense

### Primary or early-passage cell

**Mouse embryonic fibroblasts** (`mef`)

Surface forms. "mouse embryonic fibroblasts", "murine embryonic fibroblasts", "murine fibroblasts", "primary mouse embryonic fibroblasts"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-perez-influenza-a-virus-generated-small-, 2010-schmid-transcription-factor-redundancy-en, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-cullen-is-rna-interference-a-physiologica, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-mitogen-activated-protein-kinase-m, 2014-shapiro-drosha-as-an-interferon-independen, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-aguado-homologous-recombination-is-an-int, 2019-eggenberger-type-i-interferon-response-impairs, 2023-uhl-adar1-biology-can-hinder-effective, 2025-manivasagam-transcriptional-repressor-capicua-

**Bone marrow derived macrophages** (`bmdm`)

Surface forms. "bone marrow derived macrophages", "bone marrow-derived macrophages", "murine bone marrow derived macrophages"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2012-langlois-hematopoietic-specific-targeting-o, 2012-pham-replication-in-cells-of-hematopoie, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-a-versatile-rna-vector-for-deliver, 2025-manivasagam-transcriptional-repressor-capicua-

**Primary human fibroblasts** (`human-fibroblasts`)

Surface forms. "BJ human foreskin fibroblasts", "human fibroblasts", "human primary foreskin fibroblasts", "normal human dermal fibroblasts"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-pham-replication-in-cells-of-hematopoie, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-aguado-microrna-function-is-limited-to-cy, 2019-eggenberger-type-i-interferon-response-impairs

**Primary mouse lung fibroblasts** (`mouse-lung-fibroblasts`)

Surface forms. "murine lung fibroblasts", "primary lung fibroblasts", "primary mouse lung fibroblasts"

Publications. 2009-perez-microrna-mediated-species-specific, 2012-langlois-hematopoietic-specific-targeting-o, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-heaton-long-term-survival-of-influenza-vi, 2014-shapiro-drosha-as-an-interferon-independen

**Bone marrow derived dendritic cells** (`bone-marrow-derived-dendritic-cells`)

Surface forms. "bone marrow derived dendritic cells"

Publications. 2025-manivasagam-transcriptional-repressor-capicua-

**FACS-sorted olfactory sensory neuron nuclei** (`facs-sorted-olfactory-sensory-neuron-nuclei`)

Surface forms. "FACS-sorted olfactory sensory neuron nuclei"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Olfactory sensory neurons** (`olfactory-sensory-neurons`)

Surface forms. "olfactory sensory neurons"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Primary adult human cornea limbus sclera iris retinal pigment epithelium and choroid cultures** (`primary-adult-human-cornea-limbus-sclera-iris-retinal-pigment-epithelium-and-choroid-cultures`)

Surface forms. "primary adult human cornea limbus sclera iris retinal pigment epithelium and choroid cultures"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

**Primary conditional Drosha mouse lung fibroblasts** (`primary-conditional-drosha-mouse-lung-fibroblasts`)

Surface forms. "primary conditional Drosha mouse lung fibroblasts"

Publications. 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Primary ferret lung** (`primary-ferret-lung`)

Surface forms. "primary ferret lung"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat

**Primary human airway basal cells** (`primary-human-airway-basal-cells`)

Surface forms. "primary human airway basal cells"

Publications. 2025-manivasagam-transcriptional-repressor-capicua-

**Primary human bronchial epithelial cells** (`primary-human-bronchial-epithelial-cells`)

Surface forms. "primary human bronchial epithelial cells"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

**Primary human nasal epithelial cells** (`primary-human-nasal-epithelial-cells`)

Surface forms. "primary human nasal epithelial cells"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat

**Primary human neutrophils** (`primary-human-neutrophils`)

Surface forms. "primary human neutrophils"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Primary human pulmonary microvascular endothelium** (`primary-human-pulmonary-microvascular-endothelium`)

Surface forms. "primary human pulmonary microvascular endothelium"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**Primary human type II pneumocytes** (`primary-human-type-ii-pneumocytes`)

Surface forms. "primary human type II pneumocytes"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Primary mouse lung cultures from GFP transgenic mice** (`primary-mouse-lung-cultures-from-gfp-transgenic-mice`)

Surface forms. "primary mouse lung cultures from GFP transgenic mice"

Publications. 2014-schmid-a-versatile-rna-vector-for-deliver

**Primary normal human bronchial epithelial cells** (`primary-normal-human-bronchial-epithelial-cells`)

Surface forms. "primary normal human bronchial epithelial cells"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

### Stem cell system

**Mouse embryonic stem cells** (`mouse-esc`)

Surface forms. "mouse embryonic stem cells"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2019-eggenberger-type-i-interferon-response-impairs, 2023-zhang-mouse-genome-rewriting-and-tailori

**Embryoid bodies** (`embryoid-bodies`)

Surface forms. "embryoid bodies"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2019-eggenberger-type-i-interferon-response-impairs

### Tissue or organ

**Mouse lung** (`mouse-lung`)

Surface forms. "BALB/c mouse lung", "C57BL/6 mouse lung", "mouse lung", "mouse lung tissue"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-in-vivo-rnai-screening-identifies-, 2017-morales-sars-cov-encoded-small-rnas-contri, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2023-zhang-mouse-genome-rewriting-and-tailori, 2025-manivasagam-transcriptional-repressor-capicua-

**Hamster lung** (`hamster-lung`)

Surface forms. "hamster lung"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-oishi-a-diminished-immune-response-under, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result

**Mouse spleen** (`mouse-spleen`)

Surface forms. "mouse spleen"

Publications. 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in

**Brain** (`brain`)

Surface forms. "brain"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in, 2023-carrau-delayed-engagement-of-host-defense

**Liver** (`liver`)

Surface forms. "liver"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza, 2023-carrau-delayed-engagement-of-host-defense

**Mediastinal lymph node** (`mediastinal-lymph-node`)

Surface forms. "mediastinal lymph node"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-oishi-a-diminished-immune-response-under

**Mouse liver** (`mouse-liver`)

Surface forms. "mouse liver"

Publications. 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie

**Olfactory bulb** (`olfactory-bulb`)

Surface forms. "olfactory bulb"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in, 2023-carrau-delayed-engagement-of-host-defense

**Pancreas** (`pancreas`)

Surface forms. "pancreas"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza, 2023-carrau-delayed-engagement-of-host-defense

**Spleen** (`spleen`)

Surface forms. "spleen"

Publications. 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2023-carrau-delayed-engagement-of-host-defense

**Alveolar epithelium** (`alveolar-epithelium`)

Surface forms. "alveolar epithelium"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Bronchus tissue** (`bronchus-tissue`)

Surface forms. "bronchus tissue"

Publications. 2014-varble-influenza-a-virus-transmission-bot

**Club cells** (`club-cells`)

Surface forms. "club cells"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Cortical neurons** (`cortical-neurons`)

Surface forms. "cortical neurons"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Dopaminergic neurons** (`dopaminergic-neurons`)

Surface forms. "dopaminergic neurons"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Gastrointestinal tract** (`gastrointestinal-tract`)

Surface forms. "gastrointestinal tract"

Publications. 2023-carrau-delayed-engagement-of-host-defense

**Golden hamster dorsal root ganglia** (`golden-hamster-dorsal-root-ganglia`)

Surface forms. "golden hamster dorsal root ganglia"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Golden hamster lung heart and kidney** (`golden-hamster-lung-heart-and-kidney`)

Surface forms. "golden hamster lung heart and kidney"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

**Golden hamster olfactory epithelium** (`golden-hamster-olfactory-epithelium`)

Surface forms. "golden hamster olfactory epithelium"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**Hamster olfactory bulb and olfactory epithelium** (`hamster-olfactory-bulb-and-olfactory-epithelium`)

Surface forms. "hamster olfactory bulb and olfactory epithelium"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

**Hamster spinal cord** (`hamster-spinal-cord`)

Surface forms. "hamster spinal cord"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Hamster spleen** (`hamster-spleen`)

Surface forms. "hamster spleen"

Publications. 2022-oishi-a-diminished-immune-response-under

**Hamster striatum thalamus cerebellum medial prefrontal cortex and trigeminal ganglion** (`hamster-striatum-thalamus-cerebellum-medial-prefrontal-cortex-and-trigeminal-ganglion`)

Surface forms. "hamster striatum thalamus cerebellum medial prefrontal cortex and trigeminal ganglion"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

**Hamster trachea** (`hamster-trachea`)

Surface forms. "hamster trachea"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in

**Heart** (`heart`)

Surface forms. "heart"

Publications. 2023-carrau-delayed-engagement-of-host-defense

**Kidney** (`kidney`)

Surface forms. "kidney"

Publications. 2023-carrau-delayed-engagement-of-host-defense

**Lung draining lymph node** (`lung-draining-lymph-node`)

Surface forms. "lung draining lymph node"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

**Macrophages** (`macrophages`)

Surface forms. "macrophages"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Mesenteric lymph nodes** (`mesenteric-lymph-nodes`)

Surface forms. "mesenteric lymph nodes"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

**Microglia** (`microglia`)

Surface forms. "microglia"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**MLE-15 murine lung epithelial cell line** (`mle-15-murine-lung-epithelial-cell-line`)

Surface forms. "MLE-15 murine lung epithelial cell line"

Publications. 2014-heaton-long-term-survival-of-influenza-vi

**Mouse gastrointestinal tract** (`mouse-gastrointestinal-tract`)

Surface forms. "mouse gastrointestinal tract"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

**Mouse heart** (`mouse-heart`)

Surface forms. "mouse heart"

Publications. 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn

**Mouse kidney** (`mouse-kidney`)

Surface forms. "mouse kidney"

Publications. 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn

**Mouse small intestine** (`mouse-small-intestine`)

Surface forms. "mouse small intestine"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**Mouse testis** (`mouse-testis`)

Surface forms. "mouse testis"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**Mouse trachea** (`mouse-trachea`)

Surface forms. "mouse trachea"

Publications. 2023-zhang-mouse-genome-rewriting-and-tailori

**Small intestine** (`small-intestine`)

Surface forms. "small intestine"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in

**Sustentacular cells** (`sustentacular-cells`)

Surface forms. "sustentacular cells"

Publications. 2022-zazhytska-non-cell-autonomous-disruption-of-

**THP-1-derived macrophages** (`thp-1-derived-macrophages`)

Surface forms. "THP-1-derived macrophages"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

## Key concepts

154 canonical terms from 542 surface forms. Grouped by family, then ordered by number of publications.

### Cell identity and development

**Lineage tracing of infected cells** (`lineage-tracing`)

Surface forms. "bronchiolar epithelium", "cell survival of lytic infection", "club cells", "lineage tracing of infected cells", "peribronchiolar metaplasia", "tissue repair", "virulence independent of replication"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2017-morales-sars-cov-encoded-small-rnas-contri, 2019-tenoever-synthetic-virology-building-viruse, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-oishi-a-diminished-immune-response-under

**Interferon and cell identity** (`interferon-and-cell-identity`)

Surface forms. "cellular reprogramming", "differentiation potential", "germ layer specification", "piRNA pathway", "pluripotency", "pluripotency and RNAi competence"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2016-tenoever-the-evolution-of-antiviral-defense, 2019-eggenberger-type-i-interferon-response-impairs

**Cell cycle arrest** (`cell-cycle-arrest`)

Surface forms. "cell cycle arrest"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

**Limbal stem cell niche** (`limbal-stem-cell-niche`)

Surface forms. "limbal stem cell niche"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

### General virology

**Airway host response** (`airway-host-response`)

Surface forms. "airway host response"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**Bystander versus infected cell responses** (`bystander-versus-infected-cell-responses`)

Surface forms. "bystander versus infected cell responses"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

**Coinfection** (`coinfection`)

Surface forms. "coinfection"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**Dorsal root ganglia** (`dorsal-root-ganglia`)

Surface forms. "dorsal root ganglia"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Filopodial protrusions** (`filopodial-protrusions`)

Surface forms. "filopodial protrusions"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

**Gastrointestinal barrier** (`gastrointestinal-barrier`)

Surface forms. "gastrointestinal barrier"

Publications. 2020-mccune-rapid-dissemination-and-monopoliza

**Hepatocyte and cholangiocyte infection** (`hepatocyte-and-cholangiocyte-infection`)

Surface forms. "hepatocyte and cholangiocyte infection"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Host transcriptome modulation** (`host-transcriptome-modulation`)

Surface forms. "host transcriptome modulation"

Publications. 2014-shapiro-drosha-as-an-interferon-independen

**Host transcriptome remodelling** (`host-transcriptome-remodelling`)

Surface forms. "host transcriptome remodelling"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**IE2 autorepression through the cis-repression sequence** (`ie2-autorepression-through-the-cis-repression-sequence`)

Surface forms. "IE2 autorepression through the cis-repression sequence"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**IL-6** (`il-6`)

Surface forms. "IL-6"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Immediate early gene circuitry** (`immediate-early-gene-circuitry`)

Surface forms. "immediate early gene circuitry"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**In vivo RNA interference screening** (`in-vivo-rna-interference-screening`)

Surface forms. "in vivo RNA interference screening"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach

**Infected versus bystander cells** (`infected-versus-bystander-cells`)

Surface forms. "infected versus bystander cells"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Microglial and myeloid activation** (`microglial-and-myeloid-activation`)

Surface forms. "microglial and myeloid activation"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

**Negative feedback by apoptotic caspases** (`negative-feedback-by-apoptotic-caspases`)

Surface forms. "negative feedback by apoptotic caspases"

Publications. 2023-paget-stress-granules-are-shock-absorber

**PA RNA binding cleft** (`pa-rna-binding-cleft`)

Surface forms. "PA RNA binding cleft"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly

**Pancreatic beta cell infection** (`pancreatic-beta-cell-infection`)

Surface forms. "pancreatic beta cell infection"

Publications. 2020-yang-a-human-pluripotent-stem-cell-base

**Promyelocytic leukemia nuclear bodies** (`promyelocytic-leukemia-nuclear-bodies`)

Surface forms. "promyelocytic leukemia nuclear bodies"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m

**Sequential infection** (`sequential-infection`)

Surface forms. "sequential infection"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**SP100 family** (`sp100-family`)

Surface forms. "SP100 family"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m

**Strain-dependent virulence** (`strain-dependent-virulence`)

Surface forms. "strain-dependent virulence"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r

**TGF-beta signalling** (`tgf-beta-signalling`)

Surface forms. "TGF-beta signalling"

Publications. 2022-oishi-a-diminished-immune-response-under

**Transcriptional maintenance of antiviral capacity** (`transcriptional-maintenance-of-antiviral-capacity`)

Surface forms. "transcriptional maintenance of antiviral capacity"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach

**Upstream regulator prediction** (`upstream-regulator-prediction`)

Surface forms. "upstream regulator prediction"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Viral genomic RNA cleavage** (`viral-genomic-rna-cleavage`)

Surface forms. "viral genomic RNA cleavage"

Publications. 2014-shapiro-drosha-as-an-interferon-independen

**Viral interference** (`viral-interference`)

Surface forms. "viral interference"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**Viral transcriptional cascade** (`viral-transcriptional-cascade`)

Surface forms. "viral transcriptional cascade"

Publications. 2018-m-ller-mirna-mediated-targeting-of-human-

**Virus clearance** (`virus-clearance`)

Surface forms. "virus clearance"

Publications. 2014-heaton-long-term-survival-of-influenza-vi

### Host factors

**SARS-CoV-2 entry and receptor use** (`sars-cov-2-entry`)

Surface forms. "ACE2 and TMPRSS2 expression", "ACE2 binding kinetics", "ACE2 expression", "ACE2 receptor", "ACE2 surface availability", "hemagglutinin receptor specificity", "proteolytic processing of Spike", "pseudotyped entry virus", "pseudotyped particle systems", "serine protease priming of hemagglutinin", "Spike D614G", "TMPRSS2", "TMPRSS4 as an alternative protease", "viral entry efficiency", "viral entry inhibition", "viral receptor expression"

Publications. 2014-varble-influenza-a-virus-transmission-bot, 2018-han-genome-wide-crispr-cas9-screen-ide, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-daniloski-identification-of-required-host-fa, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-si-a-human-airway-on-a-chip-for-the-r, 2023-zhang-mouse-genome-rewriting-and-tailori

**Host dependency factors** (`host-dependency-factors`)

Surface forms. "druggable target identification", "essential gene function in myeloid cells", "host dependency factors", "host factor discovery", "host restriction factors", "pan-proviral versus virus-specific factors", "proviral host dependency"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2018-han-genome-wide-crispr-cas9-screen-ide, 2018-m-ller-mirna-mediated-targeting-of-human-, 2021-daniloski-identification-of-required-host-fa, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Viral tropism and cell-type permissiveness** (`viral-tropism`)

Surface forms. "cell-type permissiveness", "cell-type restriction of replication", "cell-type-specific conditional knockdown", "hematopoietic cells", "hematopoietic-specific microRNA targeting", "SARS-CoV-2 tropism", "upper respiratory tract replication", "viral tropism"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2014-varble-influenza-a-virus-transmission-bot, 2018-m-ller-mirna-mediated-targeting-of-human-, 2020-yang-a-human-pluripotent-stem-cell-base, 2023-carrau-delayed-engagement-of-host-defense

**Host-directed antiviral strategies** (`host-directed-antivirals`)

Surface forms. "alectinib repurposing", "antiviral drug target selection", "drug repurposing", "host-directed antiviral strategy", "host-directed antiviral therapy", "kinase inhibitor repurposing"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-yaron-host-protein-kinases-required-for-

**ANP32A** (`anp32a`)

Surface forms. "ANP32A"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

**ARP2 and ARP3 complex** (`arp2-and-arp3-complex`)

Surface forms. "ARP2 and ARP3 complex"

Publications. 2021-daniloski-identification-of-required-host-fa

**Cholesterol biosynthesis** (`cholesterol-biosynthesis`)

Surface forms. "cholesterol biosynthesis"

Publications. 2021-daniloski-identification-of-required-host-fa

**Class 3 PI3K** (`class-3-pi3k`)

Surface forms. "class 3 PI3K"

Publications. 2021-daniloski-identification-of-required-host-fa

**CMP-sialic acid transport** (`cmp-sialic-acid-transport`)

Surface forms. "CMP-sialic acid transport"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

**Commander complex** (`commander-complex`)

Surface forms. "Commander complex"

Publications. 2021-daniloski-identification-of-required-host-fa

**Endosomal trafficking** (`endosomal-trafficking`)

Surface forms. "endosomal trafficking"

Publications. 2021-daniloski-identification-of-required-host-fa

**Retromer complex** (`retromer-complex`)

Surface forms. "Retromer complex"

Publications. 2021-daniloski-identification-of-required-host-fa

**Sialic acid biosynthesis** (`sialic-acid-biosynthesis`)

Surface forms. "sialic acid biosynthesis"

Publications. 2018-han-genome-wide-crispr-cas9-screen-ide

**Vacuolar ATPase** (`vacuolar-atpase`)

Surface forms. "vacuolar ATPase"

Publications. 2021-daniloski-identification-of-required-host-fa

### Immunology

**Immune memory and reinfection** (`immune-memory`)

Surface forms. "adaptive immune response", "adoptive transfer", "affinity maturation", "antigen presenting cells", "antigen-specific B cells", "antigen-specific T cells", "bystander priming", "CD8 T cell priming", "cross-presentation", "germinal centre B cells", "immune memory", "immune priming", "neutralizing antibody", "neutralizing antibody potency", "regulatory T cells", "systemic antiviral priming", "transmission despite immunity", "V(D)J recombination"

Publications. 2012-langlois-hematopoietic-specific-targeting-o, 2016-tenoever-the-evolution-of-antiviral-defense, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2023-carrau-delayed-engagement-of-host-defense

**Age and immunosenescence** (`age-and-immunosenescence`)

Surface forms. "IL-17 and neutrophil recruitment", "immunosenescence", "immunosuppression", "neutrophil recruitment and transmigration"

Publications. 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-oishi-a-diminished-immune-response-under, 2023-carrau-delayed-engagement-of-host-defense

### Interferon and innate signalling

**Interferon-stimulated genes** (`interferon-stimulated-genes`)

Surface forms. "interferon-stimulated gene amplification", "interferon-stimulated gene selectivity", "interferon-stimulated gene subsets", "interferon-stimulated genes"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-backes-the-mammalian-response-to-virus-in, 2014-heaton-long-term-survival-of-influenza-vi, 2015-benitez-in-vivo-rnai-screening-identifies-, 2019-eggenberger-type-i-interferon-response-impairs, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-oishi-a-diminished-immune-response-under, 2022-oishi-the-host-response-to-influenza-a-v, 2023-carrau-delayed-engagement-of-host-defense, 2025-manivasagam-transcriptional-repressor-capicua-

**Type I interferon** (`type-i-interferon`)

Surface forms. "type I and type III interferon", "type I interferon", "type I interferon receptor", "type I interferon response", "type I interferon signaling", "type I interferon signalling", "type I interferon system"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-heaton-long-term-survival-of-influenza-vi, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2016-tenoever-the-evolution-of-antiviral-defense, 2019-eggenberger-type-i-interferon-response-impairs, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-mccune-rapid-dissemination-and-monopoliza, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-oishi-the-host-response-to-influenza-a-v, 2023-carrau-delayed-engagement-of-host-defense

**Chemokine induction** (`chemokine-induction`)

Surface forms. "chemokine induction", "inflammatory cytokine production", "leukocyte recruitment", "proinflammatory chemokines", "proinflammatory cytokine induction"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2017-morales-sars-cov-encoded-small-rnas-contri, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2020-bouhaddou-the-global-phosphorylation-landsca, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Cell-intrinsic antiviral state** (`antiviral-state`)

Surface forms. "antiviral immunity", "antiviral innate immunity", "antiviral state", "cell-intrinsic immunity", "innate antiviral state", "intrinsic antiviral response"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2015-aguado-microrna-function-is-limited-to-cy, 2018-han-genome-wide-crispr-cas9-screen-ide

**Interferon-stimulated response element** (`isre`)

Surface forms. "interferon regulatory factor binding element", "interferon-stimulated response element", "IRF7 as transactivator of interferon-stimulated response elements"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2014-schmid-mitogen-activated-protein-kinase-m, 2019-eggenberger-type-i-interferon-response-impairs

**Viral interferon antagonism** (`interferon-antagonism`)

Surface forms. "interferon antagonism", "NS1 antagonist", "NS1 interferon antagonism", "type I interferon antagonism", "viral interferon antagonism"

Publications. 2013-chua-influenza-a-virus-utilizes-subopti, 2015-benitez-in-vivo-rnai-screening-identifies-, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Capicua and transcriptional gatekeeping** (`capicua`)

Surface forms. "ATXN1L", "Capicua", "capicua and ATXN1 corepressor", "CIC binding site motif", "GAF complex", "low-complexity acidic region"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan, 2018-han-genome-wide-crispr-cas9-screen-ide, 2022-nilsson-payant-the-host-factor-anp32a-is-required, 2025-manivasagam-transcriptional-repressor-capicua-

**MAPK signalling** (`mapk-signalling`)

Surface forms. "casein kinase 1", "casein kinase II", "EGFR-MAPK signaling", "ERK activation", "GSK-3", "kinase activity rewiring", "kinase substrate motif prediction", "MAP3K8", "p38 MAPK signalling", "phospho-priming", "phosphoproteomics", "proline-rich hinge phosphorylation", "SRPK1 and SRPK2"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m, 2020-bouhaddou-the-global-phosphorylation-landsca, 2022-yaron-host-protein-kinases-required-for-, 2025-manivasagam-transcriptional-repressor-capicua-

**Pattern recognition receptors** (`pattern-recognition-receptors`)

Surface forms. "pathogen-associated molecular patterns", "pattern recognition receptor", "pattern recognition receptors"

Publications. 2015-benitez-in-vivo-rnai-screening-identifies-, 2016-tenoever-the-evolution-of-antiviral-defense, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-nilsson-payant-reduced-nucleoprotein-availability

**RIG-I-like receptors** (`rig-i-like-receptors`)

Surface forms. "MDA5", "RIG-I", "RIG-I sensing of alphavirus", "RIG-I-like receptor", "RIG-I-like receptors"

Publications. 2012-langlois-hematopoietic-specific-targeting-o, 2013-varble-an-in-vivo-rnai-screening-approach, 2015-benitez-in-vivo-rnai-screening-identifies-, 2023-paget-stress-granules-are-shock-absorber

**Transcriptional repression of interferon-stimulated genes** (`isg-repression`)

Surface forms. "cytokine derepression", "KLF4-mediated repression of antiviral induction", "transcriptional repression", "transcriptional repression of interferon-stimulated genes"

Publications. 2015-aguado-microrna-function-is-limited-to-cy, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-eggenberger-type-i-interferon-response-impairs, 2025-manivasagam-transcriptional-repressor-capicua-

**Type I interferon induction** (`type-i-interferon-induction`)

Surface forms. "feed forward amplification of innate immunity", "interferon beta enhanceosome", "interferon induction", "type I interferon induction"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2012-langlois-hematopoietic-specific-targeting-o, 2014-schmid-mitogen-activated-protein-kinase-m, 2021-nilsson-payant-reduced-nucleoprotein-availability

**IKK-related kinases** (`ikk-related-kinases`)

Surface forms. "IKK-related kinases", "IKKepsilon", "IKKε", "TBK1", "virus-activated kinase"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2007-tenoever-multiple-functions-of-the-ikk-rela, 2011-ng-i-b-kinase-ikk-regulates-the-balan

**IRF3 activation** (`irf3-activation`)

Surface forms. "C-terminal phosphorylation", "IRF-3 activation", "IRF3", "sequential multisite phosphorylation"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-schmid-transcription-factor-redundancy-en, 2022-yaron-host-protein-kinases-required-for-

**IRF7 activation** (`irf7-activation`)

Surface forms. "IRF-7 activation", "IRF3 and IRF7 heterodimer", "IRF7"

Publications. 2003-sharma-triggering-the-interferon-antivira, 2010-schmid-transcription-factor-redundancy-en, 2014-schmid-mitogen-activated-protein-kinase-m

**ISGF3** (`isgf3`)

Surface forms. "ISGF3", "ISGF3 assembly"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2010-schmid-transcription-factor-redundancy-en, 2011-ng-i-b-kinase-ikk-regulates-the-balan

**MAVS signalling** (`mavs-signalling`)

Surface forms. "MAVS signaling", "MDA5 and MAVS signaling", "RIG-I and MAVS signalling"

Publications. 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**NF-kappaB signalling** (`nf-kb-signalling`)

Surface forms. "NF-kappaB signalling", "NF-kB-driven chemokine response", "NF-κB signalling"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2022-oishi-a-diminished-immune-response-under

**Chromatin accessibility** (`chromatin-accessibility`)

Surface forms. "chromatin accessibility"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint, 2025-manivasagam-transcriptional-repressor-capicua-

**OAS and RNase L system** (`oas-rnase-l`)

Surface forms. "OAS and RNase L", "OAS and RNase L system"

Publications. 2015-benitez-in-vivo-rnai-screening-identifies-, 2023-paget-stress-granules-are-shock-absorber

**Type III interferon** (`type-iii-interferon`)

Surface forms. "type III interferon", "type III interferon signaling"

Publications. 2010-schmid-transcription-factor-redundancy-en, 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Allosteric enhancer RNA** (`allosteric-enhancer-rna`)

Surface forms. "allosteric enhancer RNA"

Publications. 2012-perez-a-small-rna-enhancer-of-viral-poly

**Enhancer remodelling** (`enhancer-remodelling`)

Surface forms. "enhancer remodelling"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Gamma-activated sequence** (`gamma-activated-sequence`)

Surface forms. "gamma-activated sequence"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**ILF3** (`ilf3`)

Surface forms. "ILF3"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Innate sensing compartment** (`innate-sensing-compartment`)

Surface forms. "innate sensing compartment"

Publications. 2012-langlois-hematopoietic-specific-targeting-o

**Interferon response** (`interferon-response`)

Surface forms. "interferon response"

Publications. 2014-backes-the-mammalian-response-to-virus-in

**PKR** (`pkr`)

Surface forms. "PKR"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Promoter motif specificity** (`promoter-motif-specificity`)

Surface forms. "promoter motif specificity"

Publications. 2010-schmid-transcription-factor-redundancy-en

**Promoter panhandle** (`promoter-panhandle`)

Surface forms. "promoter panhandle"

Publications. 2010-perez-influenza-a-virus-generated-small-

**Promoter selectivity** (`promoter-selectivity`)

Surface forms. "promoter selectivity"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela

**STAT1 dependent selection** (`stat1-dependent-selection`)

Surface forms. "STAT1 dependent selection"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**STAT1 homodimer interface** (`stat1-homodimer-interface`)

Surface forms. "STAT1 homodimer interface"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**STAT1 serine 708 phosphorylation** (`stat1-serine-708-phosphorylation`)

Surface forms. "STAT1 serine 708 phosphorylation"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**STAT1 serine phosphorylation** (`stat1-serine-phosphorylation`)

Surface forms. "STAT1 serine phosphorylation"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela

**Stress granules and biomolecular condensates** (`stress-granules`)

Surface forms. "biomolecular condensates", "stress granules"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Transcription factor complex competition** (`transcription-factor-complex-competition`)

Surface forms. "transcription factor complex competition"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**Transcription factor motif enrichment** (`transcription-factor-motif-enrichment`)

Surface forms. "transcription factor motif enrichment"

Publications. 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Transcription factor nuclear translocation** (`transcription-factor-nuclear-translocation`)

Surface forms. "transcription factor nuclear translocation"

Publications. 2003-sharma-triggering-the-interferon-antivira

**Transcription factor redundancy** (`transcription-factor-redundancy`)

Surface forms. "transcription factor redundancy"

Publications. 2010-schmid-transcription-factor-redundancy-en

**Type I interferon signalling in sensory tissue** (`type-i-interferon-signalling-in-sensory-tissue`)

Surface forms. "type I interferon signalling in sensory tissue"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Type I versus type II interferon balance** (`type-i-versus-type-ii-interferon-balance`)

Surface forms. "type I versus type II interferon balance"

Publications. 2011-ng-i-b-kinase-ikk-regulates-the-balan

**Viral promoter mutation** (`viral-promoter-mutation`)

Surface forms. "viral promoter mutation"

Publications. 2022-nilsson-payant-the-host-factor-anp32a-is-required

### Models

**Small animal models of respiratory infection** (`animal-models`)

Surface forms. "aerosol transmission", "animal models of COVID-19", "benchmarking against influenza", "clinically relevant drug exposure under flow", "contact transmission", "dengue pathogenesis models", "ferret transmission model", "golden hamster model development", "herpesvirus latency models", "organoid disease modeling", "preclinical model fidelity", "route of inoculation", "SEAM whole-eye organoid model", "small animal model", "transmission blocking"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2013-langlois-microrna-based-strategy-to-mitigat, 2014-varble-influenza-a-virus-transmission-bot, 2018-m-ller-mirna-mediated-targeting-of-human-, 2020-yang-a-human-pluripotent-stem-cell-base, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-frere-sars-cov-2-infection-in-hamsters-a, 2023-carrau-delayed-engagement-of-host-defense, 2023-zhang-mouse-genome-rewriting-and-tailori

### Pandemic pathogenesis

**COVID-19 pathogenesis** (`covid19-pathogenesis`)

Surface forms. "circulating inflammatory signal", "COVID-19 heterogeneity", "COVID-19 pathogenesis", "immunopathology", "lung immunopathology", "sterile inflammation", "systemic inflammation"

Publications. 2014-heaton-long-term-survival-of-influenza-vi, 2017-morales-sars-cov-encoded-small-rnas-contri, 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2022-zazhytska-non-cell-autonomous-disruption-of-, 2023-carrau-delayed-engagement-of-host-defense, 2025-manivasagam-transcriptional-repressor-capicua-

**Delayed engagement of host defences** (`delayed-innate-engagement`)

Surface forms. "delayed innate immune engagement", "delayed innate response", "innate immune response kinetics", "prophylaxis", "prophylaxis versus treatment", "therapeutic time window", "threat-proportional antiviral response"

Publications. 2014-schmid-mitogen-activated-protein-kinase-m, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2021-si-a-human-airway-on-a-chip-for-the-r, 2022-oishi-a-diminished-immune-response-under, 2023-carrau-delayed-engagement-of-host-defense

**Extrapulmonary dissemination** (`extrapulmonary-dissemination`)

Surface forms. "COVID-19 extrapulmonary involvement", "enteric virus dissemination", "extrapulmonary manifestations", "replication versus inoculum discrimination", "viral RNA dissemination without infectious virus", "viremia", "virus dissemination"

Publications. 2012-pham-replication-in-cells-of-hematopoie, 2020-mccune-rapid-dissemination-and-monopoliza, 2020-yang-a-human-pluripotent-stem-cell-base, 2023-carrau-delayed-engagement-of-host-defense, 2023-serafini-sars-cov-2-airway-infection-result

**Imbalanced host response** (`imbalanced-host-response`)

Surface forms. "attenuated type I and III interferon signaling", "imbalanced host response"

Publications. 2020-blanco-melo-imbalanced-host-response-to-sars-c, 2021-eriksen-sars-cov-2-infects-human-adult-don, 2021-hoagland-leveraging-the-antiviral-type-i-in, 2021-nilsson-payant-the-nf-b-transcriptional-footprint

**Anosmia and olfactory disruption** (`anosmia`)

Surface forms. "anosmia", "interchromosomal genomic compartments", "Lhx2 and Ebf transcription factors", "non-cell-autonomous transcriptional effect", "nuclear architecture disruption", "nuclear memory", "olfactory bulb inflammation", "olfactory receptor gene choice", "olfactory signal transduction genes", "sustentacular cell tropism"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a, 2022-zazhytska-non-cell-autonomous-disruption-of-

**Post-acute sequelae of SARS-CoV-2 infection** (`post-acute-sequelae`)

Surface forms. "behavioral change after recovery", "long COVID", "persistent interferon signaling after viral clearance", "post-acute sequelae of COVID-19", "post-acute sequelae of SARS-CoV-2 infection"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a, 2023-serafini-sars-cov-2-airway-infection-result

**Demyelination signature** (`demyelination-signature`)

Surface forms. "demyelination signature"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Immune-mediated apoptosis** (`immune-mediated-apoptosis`)

Surface forms. "immune-mediated apoptosis"

Publications. 2023-paget-stress-granules-are-shock-absorber

**Mechanical hypersensitivity** (`mechanical-hypersensitivity`)

Surface forms. "mechanical hypersensitivity"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Neuropathic transcriptome** (`neuropathic-transcriptome`)

Surface forms. "neuropathic transcriptome"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Neuroplasticity** (`neuroplasticity`)

Surface forms. "neuroplasticity"

Publications. 2023-serafini-sars-cov-2-airway-infection-result

**Ocular route of SARS-CoV-2 entry** (`ocular-route-of-sars-cov-2-entry`)

Surface forms. "ocular route of SARS-CoV-2 entry"

Publications. 2021-eriksen-sars-cov-2-infects-human-adult-don

**Renal tubular atrophy** (`renal-tubular-atrophy`)

Surface forms. "renal tubular atrophy"

Publications. 2022-frere-sars-cov-2-infection-in-hamsters-a

### Population genetics and evolution

**Escape from small RNA targeting** (`escape-from-silencing`)

Surface forms. "escape mutant fitness cost", "escape mutant resistance", "escape mutants", "escape variant selection", "mutational tolerance", "viral escape from silencing"

Publications. 2009-perez-microrna-mediated-species-specific, 2012-pham-replication-in-cells-of-hematopoie, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-aguado-homologous-recombination-is-an-int, 2019-tenoever-synthetic-virology-building-viruse, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-uhl-adar1-biology-can-hinder-effective

**Host-pathogen arms race** (`host-pathogen-arms-race`)

Surface forms. "conservation across coronaviruses", "convergent and divergent evolution", "host-pathogen arms race", "isogenic variant comparison", "linkage disequilibrium with ORF1b P314L", "vaccine antigen sequence choice", "variant of concern"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2021-daniloski-the-spike-d614g-mutation-increases, 2021-horiuchi-immune-memory-from-sars-cov-2-infe, 2022-yaron-host-protein-kinases-required-for-

**Viral fitness landscapes** (`fitness-landscape`)

Surface forms. "fitness-based genetic selection", "forward genetic screening", "natural selection as screen readout", "positive selection survival screen", "viral fitness landscape"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2015-benitez-in-vivo-rnai-screening-identifies-, 2018-han-genome-wide-crispr-cas9-screen-ide, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2021-daniloski-identification-of-required-host-fa

**Homologous recombination in RNA viruses** (`homologous-recombination`)

Surface forms. "genome polarity", "homologous recombination", "negative-sense RNA virus constraints", "no DNA intermediate", "positive-strand RNA virus specificity", "template switching"

Publications. 2014-schmid-a-versatile-rna-vector-for-deliver, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2018-aguado-homologous-recombination-is-an-int, 2023-uhl-adar1-biology-can-hinder-effective

**Transmission bottlenecks** (`transmission-bottleneck`)

Surface forms. "barcode control for drift", "founder effects", "founder population", "population bottlenecks", "stochastic transmission", "transmission bottleneck"

Publications. 2013-varble-an-in-vivo-rnai-screening-approach, 2014-varble-influenza-a-virus-transmission-bot, 2019-tenoever-synthetic-virology-building-viruse, 2020-mccune-rapid-dissemination-and-monopoliza

**Viral population dynamics** (`viral-population-dynamics`)

Surface forms. "barcoded library competition assay", "population monopolization", "viral population dynamics", "viral quasispecies", "virus population dynamics", "within-population competition"

Publications. 2014-varble-influenza-a-virus-transmission-bot, 2018-aguado-homologous-recombination-is-an-int, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2020-mccune-rapid-dissemination-and-monopoliza

**Host range restriction and adaptation** (`host-range-and-adaptation`)

Surface forms. "host adaptation", "host range restriction", "host tropism", "pandemic emergence", "PB2 627 polymorphism"

Publications. 2014-varble-influenza-a-virus-transmission-bot, 2019-munoz-moreno-viral-fitness-landscapes-in-divers, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Paleovirology and historical virus movement** (`paleovirology`)

Surface forms. "ancient DNA authentication", "Cocoliztli", "Colonial epidemics", "cross-population transmission", "host genetic ancestry", "molecular tip calibration", "paleovirology", "transatlantic slave trade", "viral genotype geography"

Publications. 2021-guzman-solis-ancient-viral-genomes-reveal-intro

### Small RNA biology

**Quantitative limits of microRNA function** (`microrna-quantitative-limits`)

Surface forms. "endogenous miRNA landscape stability", "Exportin-5 independence", "kinetics of microRNA action", "let-7 regulation of IL6", "microRNA", "microRNA targetome", "miR-124", "miR-142", "miR-192", "miR-23 regulation of IRF1", "miR-302/367 cluster", "miR-93 target site attenuation", "multiplicity of infection dependence", "RISC saturation", "small RNA copy number", "species-specific microRNA expression", "star strand accumulation", "strand selection", "target complementarity threshold"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-hematopoietic-specific-targeting-o, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-schmid-a-versatile-rna-vector-for-deliver, 2015-aguado-microrna-function-is-limited-to-cy, 2015-benitez-engineered-mammalian-rnai-can-elic, 2020-blanco-melo-imbalanced-host-response-to-sars-c

**Antiviral RNA interference** (`antiviral-rnai`)

Surface forms. "antiviral RNA interference", "antiviral RNA interference in vertebrates", "engineered RNAi", "RNA interference", "small RNA-mediated antiviral restriction", "virus-delivered RNA interference", "virus-derived interfering RNA", "virus-derived small interfering RNAs", "virus-derived small RNAs", "virus-encoded small interfering RNA"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-backes-degradation-of-host-micrornas-by-p, 2013-cullen-is-rna-interference-a-physiologica, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-, 2016-tenoever-the-evolution-of-antiviral-defense, 2018-aguado-homologous-recombination-is-an-int, 2019-tenoever-synthetic-virology-building-viruse, 2023-uhl-adar1-biology-can-hinder-effective

**Cytoplasmic microRNA biogenesis** (`cytoplasmic-microrna-biogenesis`)

Surface forms. "cytoplasmic Drosha translocation", "cytoplasmic hairpin processing", "cytoplasmic microprocessor", "cytoplasmic microRNA biogenesis", "cytoplasmic pri-miRNA", "cytoplasmic translocation of Drosha", "Drosha relocalization", "intron-encoded microRNA", "mirtron-like processing", "noncanonical microRNA biogenesis", "noncanonical small RNA biogenesis", "noncanonical small RNA processing"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri

**RNA-induced silencing complex** (`risc`)

Surface forms. "Argonaute 2 slicing", "Argonaute and RISC", "RISC", "RISC loading", "RNA-induced silencing complex", "RNA-induced silencing complex inactivation", "RNA-induced silencing complex loading"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-cullen-is-rna-interference-a-physiologica, 2014-backes-the-mammalian-response-to-virus-in, 2015-aguado-microrna-function-is-limited-to-cy, 2018-aguado-homologous-recombination-is-an-int

**Dicer** (`dicer`)

Surface forms. "Dicer", "Dicer dependence", "Dicer independence"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2013-cullen-is-rna-interference-a-physiologica, 2014-backes-the-mammalian-response-to-virus-in, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k

**Incompatibility of RNAi and interferon** (`rnai-interferon-incompatibility`)

Surface forms. "developmental and defence system incompatibility", "evolution of antiviral strategies", "evolution of antiviral systems", "evolutionary divergence of antiviral strategies", "incompatibility of ADAR1 and RNAi", "incompatibility of RNAi and interferon", "type I interferon as an alternative antiviral system"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2014-backes-the-mammalian-response-to-virus-in, 2015-benitez-engineered-mammalian-rnai-can-elic, 2016-tenoever-the-evolution-of-antiviral-defense, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2019-eggenberger-type-i-interferon-response-impairs, 2023-uhl-adar1-biology-can-hinder-effective

**Post-transcriptional gene silencing** (`post-transcriptional-silencing`)

Surface forms. "microRNA-mediated gene silencing", "post-transcriptional gene silencing", "post-transcriptional silencing", "translational repression"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-pham-replication-in-cells-of-hematopoie, 2015-aguado-microrna-function-is-limited-to-cy, 2017-morales-sars-cov-encoded-small-rnas-contri

**The microprocessor and Drosha-DGCR8 processing** (`microprocessor`)

Surface forms. "DGCR8 dependence", "Drosha", "Drosha and DGCR8 processing", "microprocessor", "microprocessor independence", "microRNA biogenesis machinery"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-shapiro-evidence-for-a-cytoplasmic-micropr, 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k

**MicroRNA turnover and terminal modification** (`microrna-turnover`)

Surface forms. "2-prime O-methylation", "microRNA depletion", "microRNA turnover", "nontemplated 3-prime adenylation", "poly(A) polymerase VP55", "proteasomal degradation", "small RNA tailing and degradation", "VP39 processivity factor", "VP55 poly(A) polymerase"

Publications. 2012-backes-degradation-of-host-micrornas-by-p, 2014-backes-the-mammalian-response-to-virus-in, 2015-aguado-microrna-function-is-limited-to-cy, 2025-manivasagam-transcriptional-repressor-capicua-

**Virtrons** (`virtrons`)

Surface forms. "viral microRNA synthesis", "virtron", "virtrons", "virus-encoded microRNA"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2012-shapiro-evidence-for-a-cytoplasmic-micropr

**ADAR1 and RNA editing** (`adar1`)

Surface forms. "ADAR1", "ADAR1 deficiency", "ADAR1 p110 and p150 isoforms", "adenosine to inosine RNA editing", "hypermutation"

Publications. 2007-tenoever-multiple-functions-of-the-ikk-rela, 2023-paget-stress-granules-are-shock-absorber, 2023-uhl-adar1-biology-can-hinder-effective

**RNase III nucleases as antiviral effectors** (`rnase-iii-nucleases`)

Surface forms. "interferon-independent antiviral defense", "interferon-independent defense", "microRNA-independent antiviral activity", "RNA stem loop recognition", "RNase III independence", "RNase III nucleases"

Publications. 2014-shapiro-drosha-as-an-interferon-independen, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2017-morales-sars-cov-encoded-small-rnas-contri

**Viral suppressors of RNA silencing** (`viral-suppressors-of-rna-silencing`)

Surface forms. "NS1 and small RNA silencing", "viral suppressor of RNA silencing", "viral suppressors of RNA silencing"

Publications. 2013-cullen-is-rna-interference-a-physiologica, 2015-benitez-engineered-mammalian-rnai-can-elic, 2023-uhl-adar1-biology-can-hinder-effective

**Prokaryotic and plant defence systems** (`prokaryotic-defence`)

Surface forms. "antisense RNA defense", "CRISPR-Cas", "kink-turn RNA structure", "L30 protein family", "L7Ae", "prokaryotic Argonaute", "restriction modification systems"

Publications. 2016-tenoever-the-evolution-of-antiviral-defense, 2023-oishi-archaeal-kink-turn-binding-protein

**Criteria for demonstrating antiviral RNAi** (`criteria-for-demonstrating-antiviral-rnai`)

Surface forms. "criteria for demonstrating antiviral RNAi"

Publications. 2013-cullen-is-rna-interference-a-physiologica

### Viral engineering and biocontainment

**MicroRNA target site engineering** (`mirna-target-site-engineering`)

Surface forms. "cell-type-restricted viral tropism", "microRNA response element", "microRNA target site engineering", "microRNA target site insertion", "microRNA-mediated attenuation", "microRNA-mediated species restriction", "microRNA-mediated targeting", "species-specific attenuation", "species-specific microRNA attenuation", "viral attenuation", "viral tropism control", "viral tropism restriction"

Publications. 2009-perez-microrna-mediated-species-specific, 2012-langlois-hematopoietic-specific-targeting-o, 2012-pham-replication-in-cells-of-hematopoie, 2013-langlois-microrna-based-strategy-to-mitigat, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2015-benitez-engineered-mammalian-rnai-can-elic, 2018-aguado-homologous-recombination-is-an-int, 2019-tenoever-synthetic-virology-building-viruse

**Artificial microRNAs** (`artificial-microrna`)

Surface forms. "artificial microRNA", "artificial microRNA delivery", "in vivo small RNA delivery", "RNA-based gene delivery", "small RNA delivery", "tunable small RNA dosing", "virus-delivered artificial microRNAs"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2013-varble-an-in-vivo-rnai-screening-approach, 2014-schmid-a-versatile-rna-vector-for-deliver

**RNA virus vectors** (`rna-virus-vectors`)

Surface forms. "engineered viral vectors", "replication-incompetent vector", "reporter virus design", "RNA virus vectors", "vector cytotoxicity", "vector tropism"

Publications. 2010-varble-engineered-rna-viral-synthesis-of-, 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn, 2014-schmid-a-versatile-rna-vector-for-deliver, 2018-m-ller-mirna-mediated-targeting-of-human-, 2019-tenoever-synthetic-virology-building-viruse

**Live attenuated vaccine design** (`live-attenuated-vaccine-design`)

Surface forms. "live attenuated influenza vaccine", "live attenuated vaccine design", "live-attenuated vaccine design"

Publications. 2009-perez-microrna-mediated-species-specific, 2013-tenoever-rna-viruses-and-the-host-microrna-, 2015-benitez-engineered-mammalian-rnai-can-elic

**Self-targeting viruses** (`self-targeting-virus`)

Surface forms. "self-targeting virus", "viral self-targeting"

Publications. 2010-shapiro-noncanonical-cytoplasmic-processin, 2015-benitez-engineered-mammalian-rnai-can-elic, 2015-benitez-in-vivo-rnai-screening-identifies-

**Mammalian genome writing** (`mouse-genome-writing`)

Surface forms. "biallelic engineering", "codon-level engineering of coding sequence", "genomic humanization", "iterative genome rewriting", "mammalian genome writing", "non-coding regulatory elements", "p53 mutational hotspots", "synonymous recoding"

Publications. 2009-perez-microrna-mediated-species-specific, 2023-zhang-mouse-genome-rewriting-and-tailori

**Molecular biocontainment** (`molecular-biocontainment`)

Surface forms. "biocontainment kill switch", "gain-of-function research biosafety", "molecular biocontainment"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat, 2019-tenoever-synthetic-virology-building-viruse

**Antagomir antiviral strategy** (`antagomir-antiviral-strategy`)

Surface forms. "antagomir antiviral strategy"

Publications. 2017-morales-sars-cov-encoded-small-rnas-contri

**Synthetic virology** (`synthetic-virology`)

Surface forms. "learning by building", "synthetic virology", "viral genetic circuitry"

Publications. 2019-tenoever-synthetic-virology-building-viruse

**Vaccine yield in ovo** (`vaccine-yield-in-ovo`)

Surface forms. "vaccine yield in ovo"

Publications. 2009-perez-microrna-mediated-species-specific

### Viral gene expression

**Segment 8 splicing and the molecular timer** (`segment-8-splicing`)

Surface forms. "3 prime splice acceptor site", "alternative splicing", "bicistronic segment 8", "M2 and NS2 splice products", "molecular timer", "molecular timer of infection", "NEP/NS2", "noncanonical splicing", "nuclear export protein NEP", "orthomyxovirus splicing", "segment 8 engineering", "splicing-independent virus", "suboptimal 5-prime splice site", "temporal coordination of the viral life cycle"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2013-chua-influenza-a-virus-utilizes-subopti, 2023-oishi-archaeal-kink-turn-binding-protein, 2023-zhang-mouse-genome-rewriting-and-tailori

**Viral ribonucleoprotein complexes** (`viral-ribonucleoprotein`)

Surface forms. "encapsidated genome", "exportin 1 CRM1-dependent nuclear export", "viral ribonucleoprotein", "viral ribonucleoprotein accessibility", "viral ribonucleoprotein complex", "viral ribonucleoprotein export"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2010-varble-engineered-rna-viral-synthesis-of-, 2013-chua-influenza-a-virus-utilizes-subopti, 2014-shapiro-drosha-as-an-interferon-independen, 2018-aguado-homologous-recombination-is-an-int, 2021-nilsson-payant-reduced-nucleoprotein-availability

**Defective viral genomes** (`defective-viral-genomes`)

Surface forms. "5-prime triphosphate RNA", "copy-back defective genomes", "defective viral genomes", "endogenous double-stranded RNA", "self versus non-self RNA discrimination", "self-derived double-stranded RNA"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-backes-degradation-of-host-micrornas-by-p, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-paget-stress-granules-are-shock-absorber, 2025-manivasagam-transcriptional-repressor-capicua-

**Genome segment stoichiometry** (`segment-stoichiometry`)

Surface forms. "gene expression stoichiometry", "genome segment stoichiometry", "packaging signal duplication", "segment packaging signals", "segment-specific regulation"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2013-chua-influenza-a-virus-utilizes-subopti, 2013-langlois-microrna-based-strategy-to-mitigat, 2019-tenoever-synthetic-virology-building-viruse

**Influenza nucleoprotein** (`nucleoprotein`)

Surface forms. "influenza nucleoprotein", "nucleoprotein", "nucleoprotein scaffold", "ribonucleoprotein protection of genomes", "viral nucleoprotein"

Publications. 2009-perez-microrna-mediated-species-specific, 2010-perez-influenza-a-virus-generated-small-, 2012-langlois-hematopoietic-specific-targeting-o, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2023-uhl-adar1-biology-can-hinder-effective

**Small viral RNA** (`small-viral-rna`)

Surface forms. "mini-viral RNA", "small viral RNA", "svRNA"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-langlois-hematopoietic-specific-targeting-o, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2017-morales-sars-cov-encoded-small-rnas-contri, 2021-nilsson-payant-reduced-nucleoprotein-availability

**Viral RNA-dependent RNA polymerase** (`viral-rna-polymerase`)

Surface forms. "encapsidating polymerase", "RNA-dependent RNA polymerase", "steric hindrance of RNA-dependent RNA polymerase", "viral RNA-dependent RNA polymerase"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2016-tenoever-the-evolution-of-antiviral-defense, 2017-aguado-rnase-iii-nucleases-from-diverse-k, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Transcription to replication switch** (`transcription-to-replication-switch`)

Surface forms. "cRNA intermediate", "cRNA synthesis", "polymerase processivity", "primary transcription", "replicase complex assembly", "transcription to replication switch", "vRNA synthesis"

Publications. 2010-perez-influenza-a-virus-generated-small-, 2012-perez-a-small-rna-enhancer-of-viral-poly, 2021-nilsson-payant-reduced-nucleoprotein-availability, 2022-nilsson-payant-the-host-factor-anp32a-is-required

**Allele A and allele B NS segments** (`allele-a-and-allele-b-ns-segments`)

Surface forms. "allele A and allele B NS segments"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**Hemagglutinin segment engineering** (`hemagglutinin-segment-engineering`)

Surface forms. "hemagglutinin segment engineering"

Publications. 2013-langlois-microrna-based-strategy-to-mitigat

**NS1 protein** (`ns1-protein`)

Surface forms. "NS1 protein"

Publications. 2019-munoz-moreno-viral-fitness-landscapes-in-divers

**Nucleocapsid SR-rich domain** (`nucleocapsid-sr-rich-domain`)

Surface forms. "nucleocapsid SR-rich domain"

Publications. 2022-yaron-host-protein-kinases-required-for-

**Replication kinetics** (`replication-kinetics`)

Surface forms. "replication kinetics"

Publications. 2022-oishi-the-host-response-to-influenza-a-v

**Subgenomic RNA** (`subgenomic-rna`)

Surface forms. "subgenomic RNA"

Publications. 2021-hoagland-leveraging-the-antiviral-type-i-in

**Viral egress** (`viral-egress`)

Surface forms. "viral egress"

Publications. 2020-bouhaddou-the-global-phosphorylation-landsca

## Publications referenced

- 2003-sharma-triggering-the-interferon-antivira
- 2007-tenoever-multiple-functions-of-the-ikk-rela
- 2009-perez-microrna-mediated-species-specific
- 2010-perez-influenza-a-virus-generated-small-
- 2010-schmid-transcription-factor-redundancy-en
- 2010-shapiro-noncanonical-cytoplasmic-processin
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2011-ng-i-b-kinase-ikk-regulates-the-balan
- 2012-backes-degradation-of-host-micrornas-by-p
- 2012-langlois-hematopoietic-specific-targeting-o
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
- 2012-perez-a-small-rna-enhancer-of-viral-poly
- 2012-pham-replication-in-cells-of-hematopoie
- 2012-shapiro-evidence-for-a-cytoplasmic-micropr
- 2013-chua-influenza-a-virus-utilizes-subopti
- 2013-cullen-is-rna-interference-a-physiologica
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2013-tenoever-rna-viruses-and-the-host-microrna-
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2014-backes-the-mammalian-response-to-virus-in
- 2014-heaton-long-term-survival-of-influenza-vi
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
- 2019-eggenberger-type-i-interferon-response-impairs
- 2019-munoz-moreno-viral-fitness-landscapes-in-divers
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
- 2023-zhang-mouse-genome-rewriting-and-tailori
- 2025-manivasagam-transcriptional-repressor-capicua-
