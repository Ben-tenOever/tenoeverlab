---
id: synthetic-virology-as-method
area: programmable-virology
name: "Synthetic Virology as a Method of Inquiry"
question: "What is the design vocabulary for rewriting a viral genome?"
publications:
  - 2019-tenoever-synthetic-virology-building-viruse
  - 2023-zhang-mouse-genome-rewriting-and-tailori
---

## The scientific problem

By the end of the 2010s a large number of engineered influenza viruses existed, produced by many laboratories for unrelated purposes, and there was no framework for saying what any of them could be used to ask. The literature was organised by virus, by reporter chemistry or by chronology, none of which separates a design that can interrogate wild-type biology from one that necessarily interrogates an attenuated variant.

Underneath that is a substantive constraint. tenOever 2019 treats the prior question as how much of the viral genome is available for modification at all, and assembles the answer from work largely done elsewhere. Packaging signals for each of the eight segments extend beyond the terminal promoter elements into the open reading frames, by a different length for each segment, mapped by a succession of groups the review credits. Genome-wide transposon insertional mutagenesis from the Palese laboratory found most amino acid insertions not tolerated, with hemagglutinin and NS1 as the exceptions, and error-prone and codon-based mutational scanning from other laboratories filled in the residue-level picture. Most reporter designs attenuate.

## What this laboratory contributed

tenOever 2019 is a single-author review with no new data, and its contribution is a taxonomy organised by what an added element does inside the viral circuit rather than by what it is made of. A tracking module reports where the virus is now. A lineage-marking module, which the review calls a browser history module, reports where it has been, including in cells that survived. A genetic override module controls whether the program runs, conditionally on host or on a drug. A positioning module carries identity without function. A silencing module turns the virus into a delivery vehicle for a perturbation of the host.

The taxonomy does work a chronological survey would not, because it sorts designs by the question each can answer and then applies one criterion across all of them, which is whether the design preserves viral fitness. An attenuated recombinant reports on a different virus than the one under study, so the criterion decides what a build is good for. Applied consistently, it produces portable lessons. Insertions into PB2 and into engineered intergenic space in segment 8 are better tolerated than changes to coding material, and modules acting purely at the RNA level avoid the fitness cost that protein-level modifications incur, which is why microRNA target site designs are singled out as stably engineered with unchanged fitness.

The review is also the clearest statement in the corpus of the premise underlying this research area, which it labels learning by building, and it lays out what each of this laboratory's designs was for. Perez 2009 supplied what the review describes as the first genetic override reported for influenza A virus. Langlois 2012 in PNAS and Langlois 2013 extended it to lineage restriction as an immunological tool and to ferret-restricted replication as a biocontainment device. Heaton 2014 used Cre delivery from PB2 with LoxP reporter mice to identify club cells as a surviving population. Chua 2013 created the segment 8 intergenic space that several later modules occupy. Varble 2014 used 22 nucleotide barcodes in that space to show that contact transmission transfers up to half the viral population while aerosol transmission founds an infection with two or three virions. Varble 2010 and Benitez 2015 used the same space to deliver artificial microRNAs, including in an in vivo screen whose greatest enrichment fell on Ddx58, Tlr7, Ifih1, Irf1, Irf7, Stat1, Adar and Rnasel.

Two general claims in the review are the author's interpretation of assembled results rather than demonstrated conclusions. The first is that influenza A virus occupies an optimal fitness space, inferred from the recurrence of attenuation across independent reporter designs. The second is that a strain's consensus sequence generally represents the optimal composition for the host it came from, inferred from deep mutational scanning rather than measured.

## How the work evolved

Zhang 2023 sits in this theme because it applies the same premise to the other half of the system. If a virus can be rewritten to ask what it does, a host genome can be rewritten to ask what the host contributes, and the reason is stated there in terms that mirror the review. Mouse models fail to reproduce human disease because the sequences setting where and when a gene is expressed, and how its transcripts are spliced, lie in noncoding regions that conventional transgenesis leaves behind, and the K18-hACE2 model in particular lacks human regulatory elements around ACE2, may miss human-specific splice isoforms, and retains an intact endogenous Ace2.

The method, mSwAP-In, alternates two marker cassettes each carrying positive and negative selection, so every payload selects for itself and against its predecessor, which enforces on-target integration and permits iteration. Mouse Ace2 was replaced with 116 or 180 kilobase human ACE2 loci and, later and biallelically, mouse Tmprss2 with human TMPRSS2. The resulting animals reproduced human tissue expression including testicular expression absent in mice, the interferon-inducible dACE2 isoform, and human chromatin accessibility patterns, and they were infectable with an unmodified SARS-CoV-2 isolate, mounted a spike-reactive antibody response and survived, while all K18-hACE2 controls died.

The contribution there is not this laboratory's. Zhang 2023 was conceptualised and led by Zhang and Boeke, and by the author contributions statement Golynker, Fajardo and Carrau performed the infections and tissue collection in the biosafety level 3 facility while tenOever participated in experimental design and in manuscript review. What ties it to this theme is the shared design premise and the shared interest in what an adequate model makes visible, with the paper benchmarking the humanised mouse against both the K18-hACE2 transgenic and the golden hamster model from this laboratory.

Zhang 2023 leaves unresolved whether the milder disease in the humanised animals is caused by expression level, by absence of the keratin 18 driven expression pattern, by human regulatory control, or by a combination, and the two ACE2 models differ in both payload length and expression level so the contribution of the extra sequence cannot be separated from the expression difference it produces. Humanising two entry genes also does not humanise the mouse, so the immune and physiological responses remain murine.

## Supporting publications

tenOever 2019 is a sole-authored review from this laboratory. Zhang 2023 is collaborative and led by the Boeke laboratory, with this laboratory supplying the virological work.

## Connections

Every other theme in this area appears in the tenOever 2019 taxonomy, which is why this theme functions as the area's summary rather than as a separate line of work. The design vocabulary it codifies originates in microrna-mediated-viral-attenuation, molecular-biocontainment, rna-vectors-for-delivery, lineage-tracing-of-infection and in-vivo-screening-through-fitness. The barcoding module belongs to transmission-bottlenecks in the viral-populations-evolution area, and the review's argument that chordate microRNAs are available for engineering because RNA viruses do not engage them belongs to the small-rna-antiviral-defense area. Zhang 2023 is also assigned to models-for-pandemic-virology in the pandemic-host-response area.

## Publications referenced
- 2019-tenoever-synthetic-virology-building-viruse
- 2023-zhang-mouse-genome-rewriting-and-tailori
- 2009-perez-microrna-mediated-species-specific
- 2012-langlois-hematopoietic-specific-targeting-o
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2014-heaton-long-term-survival-of-influenza-vi
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2015-benitez-in-vivo-rnai-screening-identifies-
