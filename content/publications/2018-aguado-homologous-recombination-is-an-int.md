---
id: 2018-aguado-homologous-recombination-is-an-int
slug: 2018-aguado-homologous-recombination-is-an-int
source_pdf: Aguado_et_al_PNAS2018.pdf
title: Homologous recombination is an intrinsic defense against antiviral RNA interference
authors: ["Lauren C. Aguado", "Tristan X. Jordan", "Emily Hsieh", "Daniel Blanco-Melo", "John Heard", "Maryline Panis", "Marco Vignuzzi", "Benjamin R. tenOever"]
first_author: Lauren C. Aguado
senior_authors: ["Benjamin R. tenOever"]
corresponding_authors: ["Benjamin R. tenOever"]
tenoever_position: 8
tenoever_role: senior
year: 2018
journal: Proceedings of the National Academy of Sciences
volume: "115"
issue: "39"
pages: null
doi: 10.1073/pnas.1810229115
pmid: "30209219"
pmcid: PMC6166822
publication_type: primary research
declared_conflicts: null
contribution_character: lab-led
research_areas: [small-rna-antiviral-defense, viral-populations-evolution]
themes: [reconstructing-antiviral-rnai, recombination-and-escape]
pathogens: ["Sendai virus", "influenza A virus", "Sindbis virus", "Semliki Forest virus", "poliovirus", "vesicular stomatitis virus"]
viral_families: ["Paramyxoviridae", "Orthomyxoviridae", "Togaviridae", "Picornaviridae"]
biological_systems: ["mouse embryonic fibroblasts", "RNase III deficient fibroblasts", "Dicer knockout fibroblasts", "Argonaute knockout fibroblasts", "A549 cells"]
host_species: ["mouse", "human"]
technologies: ["reverse genetics", "microRNA target cassette engineering", "serial passage", "deep sequencing of virus populations", "genome-wide CRISPR knockout screening", "flow cytometry", "immunofluorescence microscopy", "TCID50 titration"]
key_concepts: ["antiviral RNA interference", "microRNA-mediated targeting", "Argonaute 2 slicing", "genome polarity", "homologous recombination", "template switching", "escape variant selection", "encapsidated genome", "virus population dynamics"]
keywords: ["RNA interference", "homologous recombination", "positive-strand RNA virus", "negative-strand RNA virus", "microRNA targeting", "poliovirus", "Sindbis virus", "Sendai virus", "escape mutant", "virus evolution"]
---

## Citation

Aguado LC, Jordan TX, Hsieh E, Blanco-Melo D, Heard J, Panis M, Vignuzzi M, tenOever BR. Homologous recombination is an intrinsic defense against antiviral RNA interference. *Proceedings of the National Academy of Sciences* 2018, volume 115, issue 39, pages E9211 to E9219.

DOI 10.1073/pnas.1810229115. PMID 30209219. PMCID PMC6166822.

## One-sentence contribution

Applying one uniform small RNA-based selective pressure to four virus families in vertebrate cells shows that the ability to escape it tracks with the capacity for polymerase template switching rather than with genome polarity as such, since positive-strand viruses excise the targeted sequence while negative-strand viruses are cleared and a recombination-defective poliovirus cannot escape.

## Executive summary

RNA interference is the dominant antiviral defence in plants and invertebrates, so the ability to evade it should have shaped which viruses persist in those hosts. Testing that idea directly is difficult because most viruses that face RNA interference also encode antagonists of it. The authors sidestep this by rebuilding an RNA interference-like pressure in vertebrate cells, where viruses have no reason to carry such an antagonist. A cassette carrying perfectly complementary sites for five ubiquitously expressed host microRNAs was inserted into viral genomes, alongside a control cassette containing the same sequence in reverse orientation. Because perfect complementarity licenses Argonaute 2 cleavage, the cassette converts endogenous microRNAs into a slicing defence. The system was validated genetically, with silencing lost in cells lacking Dicer or Argonaute 2 but retained in cells lacking the other Argonautes, and with a genome-wide CRISPR screen recovering the canonical microRNA machinery and no interferon genes. Applied to essential transcripts, the pressure eliminated Sendai virus and influenza A virus, both negative-strand, with more than five logs of titre loss and near-total loss of viral reads. Sindbis virus, Semliki Forest virus and poliovirus, all positive-strand, were initially suppressed but recovered within passages through precise excision of the cassette. A poliovirus carrying a polymerase mutation that blocks homologous recombination could not excise the cassette and was undetectable by passage four, and about half of its reads at that codon had reverted to wild type.

## Scientific context

Different domains of life meet viruses with different defences. Prokaryotes use restriction enzymes and CRISPR systems, plants and invertebrates use RNA interference, and vertebrates use the protein-based type I and type III interferon systems. All of these acquire or exploit information about the invader to direct an otherwise nonspecific activity. In vertebrates, some sequencing studies have suggested a low-level RNA interference-like activity, but functional work has found RNA interference and interferon to be mutually incompatible, which the paper reads as evidence that RNA interference plays a minor physiological role in reducing viral replication in these hosts. The small RNA machinery itself remains, repurposed for microRNAs, and among the vertebrate Argonautes only Argonaute 2 has retained cleavage activity, which can be recruited to a transcript by inserting a perfectly complementary site. The broader question motivating the study is whether host defences bias which kinds of viruses flourish, noting the general observation that DNA viruses dominate in prokaryotes while RNA viruses dominate in eukaryotes.

## Central question

Do intrinsic features of a virus replication strategy, in the absence of any dedicated antagonist, determine whether a virus can evade an RNA interference-like defence, and if so which feature is decisive?

## Experimental strategy

The design rests on making the pressure identical across otherwise incomparable viruses. Five microRNAs expressed ubiquitously in mammalian cells were selected, and a cassette of perfectly complementary target sites for all five was built. Perfect complementarity is essential, because ordinary microRNA pairing produces only subtle repression, whereas full complementarity licenses Argonaute 2 slicing and therefore reproduces the destructive character of invertebrate and plant RNA interference. The reverse-orientation cassette is the key control, since it has identical base composition and length but cannot be bound, so any difference between the two constructs is attributable to targeting rather than to the insertion itself. Two classes of cell are used, wild-type fibroblasts as the silencing-enabled setting and RNase III deficient fibroblasts as the silencing-deficient setting, which lets the same virus pair be compared with the pressure on and off. Placement matters, and the cassette was moved from a reporter to the untranslated region of an essential transcript in each virus so the pressure would be lethal rather than cosmetic. Four families were chosen to vary both polarity and gene expression strategy, namely a nonsegmented negative-strand paramyxovirus, a segmented negative-strand orthomyxovirus, two positive-strand alphaviruses with separate nonstructural and structural messages, and a monocistronic positive-strand picornavirus. Serial passage with deep sequencing of the whole population, rather than endpoint titre alone, is what allows escape events to be seen as excisions and mapped precisely. The final test is causal rather than correlative, using a poliovirus polymerase point mutation previously shown to prevent homologous recombination.

## Key findings

1. Each of the five microRNA mimics individually silenced a reporter carrying the cassette in silencing-deficient cells, while an unrepresented microRNA did not, and the cassette was also silenced by endogenous microRNAs in wild-type cells.
2. Expressed from Sendai virus, the cassette suppressed the reporter in wild-type and Argonaute 1, 3 and 4 knockout fibroblasts but not in cells lacking Dicer or Argonaute 2, while the reverse-orientation control was expressed in all genotypes (Figure 1, B and C). Silencing therefore requires the slicing-competent Argonaute.
3. A genome-wide CRISPR knockout screen selecting cells that had lost silencing recovered Drosha, Dicer, Argonaute 2 and DGCR8, along with TP53, miR-21 and XPO5, all of which act on the available cytoplasmic microRNA pool. No interferon signature genes were implicated, which the authors take as evidence that the pressure is RNA interference activity alone (Figure 1E).
4. With the cassette in the untranslated region of the Sendai virus nucleoprotein transcript, the targeted and control viruses were indistinguishable in silencing-deficient cells, while in silencing-enabled cells the targeted virus lost nucleoprotein entirely, fell more than five logs in titre within one passage and was undetectable by passage four (Figure 2, B through D). Sequencing of the targeted virus in silencing-enabled cells recovered only two reads aligning to the reporter open reading frame (Figure 2H).
5. The same cassette in the untranslated region of influenza A virus segment five produced no difference in silencing-deficient cells but abolished nucleoprotein production and reduced infectious units by about five logs in silencing-enabled cells, with no evidence from sequencing that the cassette had been excised.
6. Sindbis virus carrying the cassette between the nonstructural and structural regions showed only an initial delay in capsid expression under pressure and reached comparable levels by six hours after infection (Figure 3C). A separate construct expressing the targeted reporter from an extra promoter confirmed that silencing was active during Sindbis virus infection despite this replication.
7. Serial passage with deep sequencing showed the control Sindbis virus stable over 96 hours, while the targeted virus gave rise by passage four to a single dominant species that had excised the cassette while retaining a functional subgenomic promoter (Figure 3, D and E). Three amino acid substitutions in nonstructural proteins, K232T, N370K and G595V, rose in frequency across three independent experiments. The paper does not determine whether these substitutions contribute to escape.
8. At passage zero the Sindbis virus population was already heterogeneous, with roughly 90 percent intact genome and three distinct excision events making up the remainder. The authors interpret this as complementation within the population, in which intact genomes supply structural messages while excised genomes supply untargeted nonstructural messages.
9. A Semliki Forest virus chimera replicating more slowly than Sindbis virus was undetectable under pressure through 36 hours but recovered by 48 hours, and passage produced a dominant genome with a precise excision that left the downstream subgenomic promoter intact. Replication kinetics therefore do not explain the failure of the negative-strand viruses to escape. The reported composition of the early heterogeneous population, given as about 65 percent wild-type genome and 45 percent excision events, sums to more than 100 percent in the text as extracted, so those specific proportions should be checked against the figure.
10. Poliovirus, which makes all its proteins from one RNA, lost about two logs under pressure at first but escaped by excising the cassette, demonstrating that escape does not depend on a multi-transcript genome organisation (Figure 4).
11. Introducing the D79H substitution into the poliovirus polymerase, previously characterised as blocking homologous recombination, left titres comparable to the parent in silencing-deficient cells but rendered the virus undetectable by passage four under pressure. Sequencing showed no excision, poor genomic coverage, and reversion of roughly half the reads at that codon to the wild-type sequence (Figure 4, B through D). This is the causal evidence that recombination, rather than polarity itself, is the escape mechanism.

## Mechanistic model

The data support a specific and limited model. When a perfectly complementary target is placed in an essential viral transcript, Argonaute 2 cleaves it, and a virus survives only if it can remove the target from its genome. Removal occurs by precise excision, and the requirement for polymerase-mediated template switching is established by the recombination-defective poliovirus, which cannot excise and is cleared. Negative-strand viruses are cleared because they do not perform this reaction efficiently, which the authors attribute, following other work, to their genomes being encapsidated and therefore less accessible to the polymerase for template jumping. That structural explanation is cited reasoning rather than a result of this study. Several further statements in the discussion are labelled by the authors as speculation or inference and should not be read as demonstrated. These include the proposal that inefficient homologous recombination is directly responsible for the lower representation of negative-strand RNA viruses across the tree of life, the suggestion that exclusive polymerase control over the first message gives negative-strand viruses compensating advantages in controlling RNA structures and avoiding detection, and the framing of defective interfering particle formation as mechanistically distinct from template jumping. The study also does not establish that the same excision route would operate against naturally occurring antiviral RNA interference, and the authors state that excision of targeted genomic material would not be as straightforward in a physiological setting.

## Conceptual or technical advance

The principal advance is a comparative assay. By reconstructing a slicing-competent small RNA defence out of endogenous vertebrate microRNAs, the authors create a selective pressure that is genuinely the same across four virus families and that no tested virus has evolved to antagonise, which removes the usual confound in comparing evasion capacity. Pairing the targeted cassette with a reverse-orientation control of identical sequence isolates targeting from insertion burden, and pairing silencing-enabled with RNase III deficient cells isolates the pressure from everything else about the infection. Reading escape by whole-population deep sequencing rather than titre turns evasion into a mapped genomic event. Biologically, the work reframes the polarity difference in RNA interference susceptibility as a consequence of recombination capacity, a proposition made testable and then tested with a single polymerase substitution. It also has a practical implication for microRNA-based attenuation strategies, since it predicts which virus classes will regain fitness by excision.

## Relationship to the broader research program

The study grows out of a sustained line in the laboratory on the relationship between small RNA silencing and vertebrate antiviral immunity. Its reference list cites the group's own earlier findings that the mammalian response to virus infection is independent of small RNA silencing, that RNase III nucleases from diverse kingdoms can serve as antiviral effectors, that engineered mammalian RNA interference can provide antiviral protection that removes the requirement for the interferon response, and a review on the evolution of antiviral defence systems. The cassette design itself is attributed to the engineered mammalian RNA interference work. Situating this paper against the laboratory's later work on virus population structure and on host transcriptional responses would be category 3 synthesis and is not attempted here.

## Related publications

- Benitez and colleagues, 2015, methodological foundation. Cited as the source of the microRNA silencing cassette design used throughout.
- Aguado and colleagues, 2017, predecessor. The laboratory's report that RNase III nucleases from diverse kingdoms act as antiviral effectors, cited as the origin of the RNase III deficient cells used as the silencing-deficient setting.
- Backes and colleagues, 2014, predecessor. Cited for the finding that the mammalian response to virus infection is independent of small RNA silencing, part of the argument that vertebrate viruses lack RNA interference antagonists.
- tenOever, 2016, review or synthesis. The laboratory's review on the evolution of antiviral defence systems, which supplies the comparative framing.
- tenOever, 2013, review or synthesis. Cited for exploitation of the host microRNA machinery by engineering perfect target sites.
- Pham, Langlois and tenOever, 2012, application. Cited among prior studies that used microRNA targeting to restrict a positive-strand RNA virus, with complete silencing achieved.

## Limitations and boundaries

The defence tested here is engineered rather than natural. It uses five fixed target sites placed at one chosen location in each genome, so the results describe escape from a single concentrated target region and not from the dispersed, regenerating small RNA population that a plant or invertebrate would produce, a limitation the authors state directly when they note that excision of naturally targeted material would not be as straightforward. All work is in cultured fibroblast and epithelial cell lines, with no animal infection, and the host cells are vertebrate cells that do not normally mount this defence. The comparison covers four families and six viruses, with only two negative-strand representatives, so the polarity generalisation rests on a small sample even though the poliovirus experiment supplies a mechanism. The recombination requirement is demonstrated by one polymerase substitution in one virus, and that mutant reverted under pressure, which complicates interpretation of its failure to persist. The escape-associated amino acid substitutions seen in Sindbis virus are correlative and untested. Read proportions reported for the early Semliki Forest virus population are internally inconsistent in the extracted text. The evolutionary claims about the representation of negative-strand viruses in nature are inference from the assay and are flagged as speculative by the authors themselves.

## Audience summaries

### 25 words

Faced with the same engineered small RNA attack, positive-strand RNA viruses cut the targeted sequence out of their genomes, while negative-strand viruses, unable to recombine, were eliminated.

### 75 words

RNA interference is the main antiviral defence in plants and insects, and vertebrate viruses have no reason to resist it. The authors built such a defence in mammalian cells by giving viruses perfectly matched binding sites for five common host microRNAs. Sendai and influenza viruses were wiped out. Sindbis, Semliki Forest and polioviruses recovered by precisely deleting the targeted sequence. A poliovirus unable to recombine could not delete it and was cleared.

### 150 words

A cassette of perfectly complementary sites for five ubiquitous host microRNAs converts endogenous Argonaute 2 into a slicing antiviral defence, with a reverse-orientation cassette as a sequence-matched control and RNase III deficient fibroblasts as the silencing-off condition. Genetic tests and a genome-wide CRISPR screen confirmed that the pressure runs through the microRNA machinery, implicating Drosha, Dicer, DGCR8, Argonaute 2, TP53, miR-21 and XPO5, with no interferon genes. Placed in essential transcripts, the cassette cleared Sendai virus and influenza A virus by more than five logs. Sindbis virus, a Semliki Forest virus chimera and poliovirus were suppressed initially but recovered by passage through precise excision of the cassette that preserved downstream promoter elements, with heterogeneous populations at early passage consistent with complementation. A poliovirus carrying the recombination-defective D79H polymerase substitution could not excise the cassette and became undetectable, establishing template switching rather than polarity itself as the escape requirement.
