---
id: programmable-virology
name: "Programmable Virology"
question: "If a virus can be redesigned, what can be learned that cannot be learned any other way?"
themes:
  - microrna-mediated-viral-attenuation
  - cell-type-restriction-as-a-tool
  - molecular-biocontainment
  - rna-vectors-for-delivery
  - in-vivo-screening-through-fitness
  - lineage-tracing-of-infection
  - synthetic-virology-as-method
publications:
  - 2009-perez-microrna-mediated-species-specific
  - 2010-varble-engineered-rna-viral-synthesis-of-
  - 2012-langlois-hematopoietic-specific-targeting-o
  - 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
  - 2012-pham-replication-in-cells-of-hematopoie
  - 2013-langlois-microrna-based-strategy-to-mitigat
  - 2013-varble-an-in-vivo-rnai-screening-approach
  - 2014-heaton-long-term-survival-of-influenza-vi
  - 2014-schmid-a-versatile-rna-vector-for-deliver
  - 2015-benitez-in-vivo-rnai-screening-identifies-
  - 2018-han-genome-wide-crispr-cas9-screen-ide
  - 2018-m-ller-mirna-mediated-targeting-of-human-
  - 2019-tenoever-synthetic-virology-building-viruse
  - 2021-daniloski-identification-of-required-host-fa
  - 2023-zhang-mouse-genome-rewriting-and-tailori
---

## In one paragraph

This area collects the work in which a virus is treated as something to be rewritten rather than only observed. One design element carries most of it. A fully complementary target site for a host microRNA, placed in a viral transcript, makes the resident microRNA a virus-specific silencing guide, so whether the virus can replicate becomes a property of the cell it finds itself in. Perez 2009 introduced that element to attenuate a vaccine candidate in mammals while preserving growth in eggs. Over the following decade the same element was used to subtract a cell compartment from an otherwise intact infection, to build a host-conditional biocontainment layer, to limit the output of a delivery vector, and to make an essential herpesvirus gene conditionally dispensable. A reciprocal line, beginning with Varble 2010, had the virus produce small RNAs rather than respond to them, which made possible a screening format in which selection inside an infected animal is the assay. tenOever 2019 collects the resulting designs into a vocabulary and states the premise, that building a virus is a way of understanding it.

## The defining scientific question

The question is narrower than it first appears. It is not whether viruses can be engineered, which was settled by reverse genetics, but which experimental questions become answerable only after an engineered virus exists. Each paper here begins from a question conventional genetics cannot reach. What does a cell compartment contribute to infection, when removing the compartment removes everything else it does. Which host factors restrict a virus during a real infection in a real tissue, when every available screen requires a transformed cell line and an indirect readout. What happens to a cell that is infected and does not die, when every label for an infected cell decays with the virus. How can a transmission experiment be made safer without altering the transmission being measured.

In each case the answer is to move the perturbation into the pathogen, where it travels with the infection and is subject to the same selection.

## Origins

Two origins should be kept separate, because they were separate.

The first is Perez 2009, which set out to solve a vaccine problem. Live attenuated influenza vaccines relied on temperature sensitivity, a single mechanism with a fixed list of excluded recipients, and the annual reformulation cycle rewarded an attenuation strategy that transfers between backgrounds. Other laboratories had already shown that microRNA target sites in a viral untranslated region restrict lentiviruses, picornaviruses and rhabdoviruses. Influenza offered no untranslated region to use, so the sites were built into two positions of the nucleoprotein open reading frame where the nucleotide changes preserve the side chain class of the encoded amino acid, and miR-93 was chosen because published profiles place it in mouse and human but not chicken. Two facts established there matter more downstream than the vaccine candidate does. Influenza infection and NS1 leave microRNA biogenesis and silencing intact in mammalian cells, which licenses every later use of the machinery as a tool. And the control set required to interpret such a virus, a pairing-disrupted parental strain, Dicer-deficient cells and an antimiR rescue, is defined there.

The second origin is Varble 2010, which set out to test a prohibition rather than to build a tool. The argument in the literature was that an RNA virus cannot encode a microRNA, because excising the hairpin would fragment the genome and the genome would be a perfect target of its own product. Splitting the overlapping NS1 and NEP reading frames of segment 8 created an intergenic region and an extended intron, so the hairpin is excised in the spliced lariat rather than from the genome. The virus made mature miR-124 within four hours at levels comparable to abundant endogenous microRNAs, with growth matching wild type. That reframed the absence of natural RNA virus microRNAs as a question about selection, and left behind the engineered segment 8 cassette that later work in this area occupies.

## Major findings

The clearest result of the microRNA targeting line is that tropism can be set independently of host genotype, so one animal carries both a permissive and a nonpermissive compartment. Langlois 2012 in PNAS used four miR-142 sites in a duplicated nucleoprotein packaging region to build an influenza virus silenced in hematopoietic cells, and found that mice cleared it and made normal nucleoprotein- and polymerase acidic-specific CD8 T cell responses while whole lung interferon beta and IRF-7 induction fell. The authors state plainly that they cannot explain why closing a numerically minor compartment costs so much of the total interferon response, and the attribution of the lost interferon to RIG-I in hematopoietic cells is inferred, since the sensor requirement was tested in cultured primary cells. Pham 2012 ran the same subtraction against dengue virus dissemination and found no intact targeted genomes in virus recovered from spleen, only variants that had excised the whole cassette, which is the strongest evidence in the area for a compartment requirement and also a demonstration that a quantitative assay for a viral gene cannot distinguish escape from residual targeted replication.

Langlois 2013 turned the same element into biocontainment by choosing the microRNA from a cross-species expression difference selected for the purpose, using miR-192, present in human and mouse respiratory tissue and absent from ferret lung. The engineered virus caused no disease in mice at ten times a lethal dose while an H3N2 version replicated and transmitted in ferrets indistinguishably from controls.

The delivery line reached animals in Langlois 2012 in Molecular Therapy, where a vesicular stomatitis virus vector produced miR-124 at an estimated 25,000 to 35,000 copies per cell, loaded it into Argonaute 2, distributed it to five organs after intravenous delivery, and left it behind after the vector was cleared. Schmid 2014 then made the vector replication-incompetent and, by installing the miR-93-targeted nucleoprotein segment from Perez 2009, made its output adjustable.

The screening line produced the area's two most consequential biological results. Varble 2013 recovered Zfx and Mga as transcriptional maintenance factors whose loss degrades antiviral capacity, against a matched barcode library that quantified how much apparent reproducibility a bottlenecked in vivo passage generates on its own. Benitez 2015 recovered MDA5, and in doing so revised a conclusion two prior studies had treated as settled. Interferon beta induction during influenza infection requires RIG-I and not MDA5, which Benitez 2015 confirms, and yet MDA5 is required for full induction of Irf7, OAS isoforms, Ifit1, Stat1 and Isg15, and its loss measurably relieves restriction. An interferon-induction readout can miss a sensor's contribution.

Separately, Heaton 2014 showed that a subpopulation of lung cells survives productive influenza infection. A Cre-expressing virus used with a lox-stop-tdTomato reporter mouse marked cells permanently, and marked cells persisted at 10 and 21 days after infectious virus was undetectable, confined to the epithelium of larger airways, carrying Cc10 as their only retained lineage marker and an amplified interferon-stimulated gene and chemokine programme. Ablating them reduced bronchiolar epithelial necrosis.

## How the work evolved

The progression from observation to engineering principle to application can be traced through specific enabling links, which is worth doing because the lineage is otherwise easy to assert loosely.

Perez 2009 proposed microRNA response elements as an attenuation mechanism and demonstrated that the silencing machinery works during infection. Pham 2012 cites it as the precedent and takes the miR-142 target sites themselves from Varble 2010, which is where the two origin lines first join. Langlois 2012 in PNAS cites Perez 2009 as the prior demonstration that replication can be made inversely proportional to a microRNA, and it is that paper which first treats the design as an instrument for a host question rather than as attenuation. Langlois 2013 in turn cites Langlois 2012 in PNAS for its deep sequencing, northern blot and miR-142-expressing cell line methods, and cites Perez 2009 as the direct precedent, and its contribution is to move the target sites out of coding sequence into a duplicated packaging region so the safety layer costs no fitness.

The screening arc has an equally specific hinge. The proposal to deliver a library of artificial microRNAs from a virus so that selection identifies host restriction factors appears in the discussion of Langlois 2012 in Molecular Therapy, and Varble 2013 implements it and cites that paper as the source. Benitez 2015 rebuilds the same idea in influenza using the split segment 8 insertion site from Varble 2010, and changes the selection pressure from a naturally attenuated alphavirus to an NS1 mutant crippled by the host response itself. Schmid 2014 completes the reciprocal move, using Perez 2009's attenuating segment to govern a delivery vector rather than a pathogen. Møller 2018 is the last extension of the targeting principle in this corpus, carrying it to a large DNA virus manipulated through a bacterial artificial chromosome and turning it from attenuation into conditional genetics, so that IE2 could be studied in macrophages despite being essential in the fibroblasts required for rescue.

Some lines stop. The delivery platform reached intranasal delivery in Schmid 2014 with in vivo silencing explicitly left to future studies, and no later paper in this corpus demonstrates it. The biocontainment proposal to generalise to filoviruses, coronaviruses and henipaviruses was not taken up here. The lineage tracing design produced one paper and was then developed by other laboratories, as tenOever 2019 records. The targeting element proved portable across many questions, and only the screening application became a sustained programme.

The two CRISPR screens in this area, Han 2018 led by the Manicassamy laboratory and Daniloski 2021 co-led with the Sanjana laboratory, share the logic of survival as selection but sit in cell culture, which is the constraint the in vivo platform was built to escape. Their relation to the earlier work is convergence rather than descent, and both make that convergence visible by returning regulators of cell-intrinsic immunity alongside replication machinery. Zhang 2023, led by the Boeke laboratory, applies the same design premise to the host genome instead of the viral one.

## Principal publications

Perez 2009 is the founding paper and the source of the design discipline. Varble 2010 is the enabling engineering for everything that delivers rather than restricts. Langlois 2012 in PNAS is the paper that converts attenuation into an instrument. Varble 2013 and Benitez 2015 are the screening platform. tenOever 2019 is the statement of the premise and the taxonomy of the designs.

## Connections to other areas

The premise that chordate microRNAs are available for this exploitation rests on the argument, developed in the small-rna-antiviral-defense area, that RNA viruses do not naturally engage them, and the noncanonical biogenesis questions raised by Varble 2010 and Langlois 2012 in Molecular Therapy belong there as well. The MDA5 result in Benitez 2015 and the interferon calibration result in Langlois 2012 in PNAS belong jointly to the innate-immune-signaling area, and capicua from Han 2018 to the homeostatic repression of interferon-stimulated genes. The engineered segment 8 space developed here carries the barcode libraries that measure transmission bottlenecks and fitness landscapes in the viral-populations-evolution area. Daniloski 2021 and Zhang 2023 are shared with the pandemic-host-response area.

## Current implications

The transferable result is methodological. A perturbation encoded in a pathogen is subject to the same selection as the pathogen, so it can be read out by fitness rather than by a surrogate, and it reaches whatever cells the pathogen reaches rather than whatever cells a transfection reaches. That argument does not depend on microRNAs, and the same reasoning underlies the CRISPR screens in this area even though their perturbation is delivered conventionally.

The second implication concerns what a build teaches. tenOever 2019 applies one criterion across every design it surveys, whether fitness is preserved, on the grounds that an attenuated recombinant reports on a different virus than the one under study. That criterion produced a usable generalisation, that modules acting purely at the RNA level avoid the cost that protein-level modifications incur, and the recurrence of attenuation across independent reporter designs is what the review reads as evidence that the virus occupies an optimal fitness space. That reading is the author's interpretation of assembled data rather than a measured result.

## Open questions

Escape is unresolved. Perez 2009 and Langlois 2013 recovered no revertants within their sampling, which bounds escape frequency loosely, and Pham 2012 shows total cassette excision under sustained pressure in an animal. The proposal in Perez 2009 that placing target sites in conserved codons ties escape to a fitness cost is not demonstrated in any single paper, and the dengue result shows that a cassette in noncoding sequence carries no such constraint. Whether multiplexed sites across multiple segments would close the gap, as Langlois 2013 proposes, was not tested.

The mechanism of silencing in these constructs is also incomplete. Perez 2009 reports translational repression for coding-sequence sites, Langlois 2013 does not dissect it, and Pham 2012 describes the repression of its seed-mismatched variant as an enigma and offers steric interference with flavivirus genome cyclisation as a hypothesis supported only by the character of the escape mutants.

Three biological questions raised here were left open by the papers that raised them. Langlois 2012 in PNAS cannot explain the magnitude of the interferon deficit relative to the size of the compartment silenced. Benitez 2015 does not identify the ligand MDA5 recognises during infection. And Heaton 2014 leaves the relationship between the interferon-stimulated gene signature of surviving club cells and their survival explicitly correlative.

## Publications referenced
- 2009-perez-microrna-mediated-species-specific
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2012-langlois-hematopoietic-specific-targeting-o
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
- 2012-pham-replication-in-cells-of-hematopoie
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2013-varble-an-in-vivo-rnai-screening-approach
- 2014-heaton-long-term-survival-of-influenza-vi
- 2014-schmid-a-versatile-rna-vector-for-deliver
- 2015-benitez-in-vivo-rnai-screening-identifies-
- 2018-han-genome-wide-crispr-cas9-screen-ide
- 2018-m-ller-mirna-mediated-targeting-of-human-
- 2019-tenoever-synthetic-virology-building-viruse
- 2021-daniloski-identification-of-required-host-fa
- 2023-zhang-mouse-genome-rewriting-and-tailori
