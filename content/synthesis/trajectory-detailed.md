---
id: trajectory-detailed
name: The Intellectual History of the Program
audience: domain scientist or review panel
---

# The intellectual history of the program

Sixty-three publications span from doctoral training in 2003 to 2025. Read chronologically they look like several unrelated careers, one in interferon signal transduction, one in small RNA biology, one in influenza genome regulation, one in viral engineering, one in population genetics and one in pandemic response. Read by question rather than by year they resolve into a smaller number of problems pursued with an unusual degree of instrument reuse, in which a reagent built to answer one question repeatedly becomes the only available way to ask another. Two commitments hold the corpus together. The first is that an antiviral response is interesting for its magnitude, composition and timing rather than for its presence. The second is that a pathogen can be rewritten, and that a perturbation written into a pathogen is subject to the same selection and reaches the same cells as the pathogen itself. Neither commitment is stated as a program in any single paper, and both are visible across many.

What follows is organised around threads and transitions. Where a claim holds only when several papers are read together, it is marked as synthesis. Where a laboratory other than this one did the work, that is said.

## The questions that persist

**What sets the composition of an antiviral response, as opposed to its existence.** This is the oldest question in the corpus. Its prehistory is Sharma 2003, doctoral training in the Hiscott laboratory, which converted the activity then known only as the virus-activated kinase into two named enzymes, IKKepsilon and TBK1, and separated an interferon regulatory factor arm from a nuclear factor kappa B arm inside the IKK family. The question itself appears in recognisable form in tenOever 2007, training-period work with the Maniatis laboratory, where mice lacking IKKepsilon made normal interferon beta and still failed to induce roughly a third of interferon-stimulated genes, with the defect persisting when interferon was supplied externally. From that point the interferon-stimulated gene set is treated as divisible. Schmid 2010 showed that much of the antiviral transcriptome is inducible in mice lacking both interferon receptors and that IRF7 and ISGF3 read overlapping but separable elements. Ng 2011, co-led with the Maniatis laboratory, explained a single phosphosite as an allocation switch between two complexes sharing a limiting STAT1 pool, and Schmid 2014 in the Journal of Biological Chemistry found the same allocation logic among the interferon regulatory factors. Two decades later the question is asked of a new pathogen in Blanco-Melo 2020, where the distinctive feature of SARS-CoV-2 is not an absent response but a misproportioned one, low interferon alongside vigorous interferon-independent chemokine output. That a kinase acting at a dimer interface to allocate a shared subunit appears in both the STAT and the IRF systems is synthesis across Ng 2011 and that paper and is asserted by neither.

**What holds the response off, and what keeps it proportionate.** Han 2018 and Manivasagam 2025, both collaborative and led by the Manicassamy laboratory, identified capicua in a survival-based screen and then placed the capicua and ATXN1L complex at an eight-nucleotide promoter motif destroyed within forty minutes of virus entry, which makes interferon-stimulated gene promoters actively repressed rather than merely unoccupied. Paget 2023, collaborative and led by the Hur laboratory, showed that stress granules buffer double-stranded RNA sensing. Proportionality also has a cost side, since Eggenberger 2019 forced the program into pluripotent stem cells with a constitutively active IRF7 and found compromised germ layer differentiation, so the response is not compatible with every cell state.

**Whether vertebrates use small RNAs against viruses, and if not, why not.** The empirical half was answered negatively and the explanatory half remains a hypothesis. This is the most internally coherent argument in the corpus and is treated below.

**How a virus with no transcription factors schedules itself.** Influenza A virus has eight segments with comparable promoters, ten major proteins and no dedicated regulators, and must still order nuclear entry, replication, export and assembly. Perez 2010 states the polymerase paradox directly, that one enzyme performs two incompatible reactions on the same template. The answer the corpus assembles is regulation by the timing and amount of products the virus already makes for other reasons, which holds for small viral RNA in Perez 2010 and Perez 2012, for the deliberately inefficient segment 8 splice site in Chua 2013 and for nucleoprotein supply in Nilsson-Payant 2021 on nucleoprotein availability.

**What survives a transition between hosts, tissues or species, and what can be learned only after an engineered virus exists.** Varble 2014 is the methodological centre of the first, extended by Muñoz-Moreno 2019, led by the García-Sastre laboratory, and McCune 2020, led by the Pfeiffer laboratory. tenOever 2019 is the explicit statement of the second.

## Foundations that made later questions askable

Several results function less as discoveries than as permissions.

Perez 2009 established, in the course of building an attenuated vaccine candidate, that influenza infection and NS1 leave microRNA biogenesis and silencing intact in mammalian cells. Every later use of the silencing machinery as a tool depends on that, and the same paper defines the control set such constructs require, namely a pairing-disrupted parental strain, Dicer-deficient cells and an antimiR rescue.

Varble 2010 split the overlapping NS1 and NEP reading frames of segment 8, creating an extended intron and a noncoding intergenic region, and showed that foreign sequence placed there is carried without measurable cost to replication. It was undertaken to test a prohibition rather than to build a tool, the prohibition being that an RNA virus cannot encode a microRNA because excision would fragment the genome and the genome would be a perfect target of its own product. The engineered segment it left behind carries the artificial microRNAs of Varble 2013 and Benitez 2015 on in vivo screening, the barcodes of Varble 2014 and Muñoz-Moreno 2019, and the miR-142 sites reused in Pham 2012. The Varble 2010 record names Perez 2009 as its methodological foundation for target site engineering, so the two origins join early.

Shapiro 2012 in RNA established that cytoplasmic primary microRNA processing requires Drosha and, incidentally, that endogenous Drosha relocalises to the cytoplasm after infection with parental as well as microRNA-expressing virus, so relocalisation responds to infection rather than to a substrate.

Hoagland 2021 performed a de novo assembly of the hamster genome region encoding Ifnb1, cloned a candidate transcript and validated it functionally, which is what made interferon biology readable in that species at all. Every subsequent hamster study in the corpus rests on it.

## Observation becoming mechanism

Four transitions of this shape are well supported.

Small viral RNA was found by deep sequencing the sub-40 nucleotide fraction of infected lung epithelial cells, as a discrete 22 to 27 nucleotide species matching the 5 prime terminus of each segment, distributed as a hotspot rather than as a degradation ladder and not induced by interferon or an unrelated virus (Perez 2010). Perez 2012 then supplied the mechanism, that the species is templated from the complementary RNA intermediate, stays nuclear, binds the polymerase through the PB1 and PA heterodimer with PA residue R566 most important, and promotes full-length genome synthesis in a cell-free reaction with purified trimer even when its 3 prime hydroxyl is blocked, so the effect is not priming and the first thirteen nucleotides suffice.

Cytoplasmic Drosha followed the same path across three papers. Shapiro 2012 in RNA observed the relocalisation. Shapiro 2014 showed that it matters, in that loss of Drosha but not Dicer raised Sindbis and vesicular stomatitis virus titres in primary fibroblasts, that infection or transfected double-stranded RNA drives the export within six hours through CRM1 and without RIG-I, TBK1 or IFNAR1, and that no virus-derived small interfering RNA signature accompanies the restriction despite more than 675,000 viral small RNA reads. Aguado 2017 then supplied the mechanism in cells with no mature microRNAs at all, showing that an RNA-binding Drosha mutant which cannot cleave, cannot process and cannot bind DGCR8 still suppresses the virus, that SELEX against that mutant enriches unbranched hairpins with no conserved sequence, and that a reconstituted minus-strand replicase assay shows polymerase output reduced by nearly half in fractions containing Drosha. The clamp language is interpretation and no structural evidence accompanies it.

Escape from a reconstructed silencing pressure moved from comparison to cause within one paper. Aguado 2018 applied one cassette to six viruses in four families and found negative-strand viruses cleared by more than five logs while positive-strand viruses recovered by precise excision. A poliovirus carrying the D79H polymerase substitution, which blocks homologous recombination, grew normally without the pressure and could not excise the cassette, which makes template switching rather than polarity itself the requirement.

Distal inflammation in SARS-CoV-2 infection moved from observation to mechanism across two papers and in the process changed its explanation. Hoagland 2021 documented antiviral transcription in olfactory bulb, brain and small intestine at viral reads orders of magnitude below respiratory levels and proposed, explicitly as speculation, disseminated viral RNA acting as a pattern. Carrau 2023 tested that and found for airway-derived circulating interferon instead, by three independent manipulations described below.

## Mechanism becoming an engineering principle

The programmable virology arc is the clearest case in the corpus of a mechanism becoming a design vocabulary, and it rests on enabling links stated in the papers rather than on resemblance.

Perez 2009 proposed fully complementary host microRNA target sites as an attenuation mechanism, built into two positions of the nucleoprotein open reading frame at codons where the nucleotide changes preserve the side chain class, and chose miR-93 from published profiles placing it in mouse and human but not chicken. Langlois 2012 in PNAS cites Perez 2009 as the prior demonstration that replication can be made inversely proportional to a microRNA, and is the paper that first treats the design as an instrument for a host question rather than as attenuation, placing four miR-142 sites in a duplicated nucleoprotein packaging region to silence the virus in hematopoietic cells alone. Langlois 2013 names Perez 2009 as its direct precedent and Langlois 2012 in PNAS as the source of its deep sequencing, northern blot and microRNA-expressing cell line methods, and its own contribution is to choose the microRNA from a cross-species expression difference selected for the purpose, and to move the sites out of coding sequence into a duplicated packaging region so the safety layer costs no fitness.

The screening arc has an equally specific hinge. The proposal to deliver a library of artificial microRNAs from a virus so that selection identifies host restriction factors appears in the discussion of Langlois 2012 in Molecular Therapy, and the Varble 2013 record names that discussion as the source of what it implements. Benitez 2015 on in vivo screening rebuilds the same idea in influenza using the split segment 8 insertion site from Varble 2010, and changes the selective pressure from a naturally attenuated alphavirus to an NS1 mutant crippled by the host response itself, so that silencing a contributor to that response restores fitness directly. Schmid 2014 in the Journal of Virology completes a reciprocal move, installing the miR-93-targeted nucleoprotein segment from Perez 2009 into a replication-incompetent vector so that a delivery vehicle rather than a pathogen is governed by host microRNA expression.

The principles these papers yield are generalisations across designs, and tenOever 2019 states them. Modules acting purely at the RNA level avoid the fitness cost that protein-level modifications incur, which is why microRNA target site designs are singled out as stably engineered with unchanged fitness, and insertions into PB2 and into engineered segment 8 intergenic space are better tolerated than changes to coding material. The review applies one criterion across every design it surveys, whether fitness is preserved, on the ground that an attenuated recombinant reports on a different virus than the one under study. Its further claim that influenza A virus occupies an optimal fitness space is inference from the recurrence of attenuation across independent reporter designs rather than a measured result.

Escape mechanisms became design rules. Aguado 2018 and Uhl 2023 together specify how microRNA-targeting designs fail, and they fail differently by virus class. A positive-strand virus excises the cassette. A self-targeting design loses its guide, which Benitez 2015 on reconstructed silencing observed across several independent designs including one carrying a single site. And a negative-strand virus may be rescued by host ADAR1 editing confined to the target sites, established causally in Uhl 2023 by knockout abolishing escape in all 96 wells and adenoviral reconstitution restoring it, which that paper states directly as a caution for vector design.

## Engineering becoming application

The corpus supports the pattern observation to mechanism to engineering principle to application in one place with full continuity, which is the microRNA targeting line. It supports basic discovery to technological exploitation to translational opportunity in two further places with the translational step explicitly untested.

For microRNA targeting the application steps are concrete. Perez 2009 produced a vaccine candidate attenuated in mammals and unimpaired in eggs. Langlois 2013 produced a biocontainment layer for gain-of-function influenza work, using miR-192, present in human and mouse respiratory tissue and absent from ferret lung, so that the virus caused no disease in mice at ten times a lethal dose while an H3N2 version replicated and transmitted in ferrets indistinguishably from controls, framed by its authors as a molecular layer added to physical containment rather than a replacement for it. Møller 2018 carried the principle to a large DNA virus and converted it from attenuation into conditional genetics, so that the essential human cytomegalovirus gene IE2 could be studied in macrophages despite being required in the fibroblasts used for rescue. Schmid 2014 in the Journal of Virology produced an adjustable delivery vector.

For interferon the translational step is an intervention in an animal and nothing further. Hoagland 2021 showed intranasal universal interferon alpha A/D, given before challenge or one day after, lowering infectious virus and inflammatory transcripts and preventing transmission in three of five exposed animals, with a double-stranded RNA mimetic giving comparable activity, and Carrau 2023 supplies the reason the airway matters, which is that it primes every other organ. Both records are explicit that this is delivery to a rodent airway with no human dosing implication, that Hoagland 2021 used young animals that survive, and that extension to severe human disease is speculation.

For drug target selection the lesson is comparative rather than a candidate. Nilsson-Payant 2021 on nucleoprotein availability found that two compounds blocking influenza equally well differ in whether they induce IFIT1, because a nucleoprotein-directed inhibitor pushes the polymerase into making immunostimulatory short products while a polymerase-directed one does not, and the proposed bystander priming benefit is flagged as an extrapolation from cell culture. Si 2021, led at the Wyss Institute, supplies the negative counterpart, that dosing at clinically achievable concentrations under flow eliminates hydroxychloroquine and chloroquine while retaining amodiaquine, which then worked in hamsters. Oishi 2023 proposes orthomyxovirus splicing as a family-wide vulnerability that one archaeal protein can attack with no true escape after twenty passages, and carries a declared conflict of interest tied to commercialisation of L7Ae.

## Expansion from one pathogen to another

What carried across was almost always a reagent or a readout rather than a conclusion.

From influenza to cytoplasmic RNA viruses the transfer was a question. Shapiro 2010 in RNA asked whether a virus that never enters the nucleus can make a microRNA, and Langlois 2012 in Molecular Therapy extended that to a negative-sense cytoplasmic virus and into animals, specifically to answer a published objection that cytoplasmic processing was an artifact of dividing transformed cells.

From influenza to dengue the transfer was the compartment subtraction itself. Pham 2012 took the miR-142 target sites from Varble 2010 and Perez 2009 as precedent, and found no intact targeted genomes in virus recovered from spleen, only variants that had excised the whole cassette, which is the strongest compartment requirement evidence here and simultaneously a demonstration that a quantitative viral gene assay cannot distinguish escape from residual targeted replication.

From influenza outward across families the transfer was a cassette. Aguado 2018 applied one silencing cassette to six viruses in four families, and Nilsson-Payant 2021 on nucleoprotein availability then reproduced the coupling of lost replication to interferon induction across seven negative-sense viruses in six families and found it failed for the SARS-CoV-2 nucleocapsid, which is unexplained.

From mammals to other domains of life the transfer was a protein fold. Aguado 2017 showed RNase III proteins from bacteria, archaea, yeast and the urochordate Ciona intestinalis conferring antiviral activity against positive-strand but not negative-strand viruses in cells lacking Drosha and Dicer, which converts a Drosha observation into a statement about a domain. Oishi 2023 runs the same logic in reverse with an archaeal protein against a vertebrate virus, extending a feature described for influenza A virus into a family-level property spanning influenza B virus and a salmon orthomyxovirus.

From influenza to SARS-CoV-2 the transfer was an entire apparatus. Blanco-Melo 2020 used the practice of sequencing viral and host reads from the same libraries unchanged, used an NS1-deficient influenza A virus as the positive control for a full response in primary bronchial cells, drew its influenza strains from Langlois 2013, which had been undertaken to mitigate gain-of-function risk, and took its ferret system from the transmission bottleneck work of Varble 2014. Influenza then continues as a calibrated reference through Hoagland 2021, Horiuchi 2021, Frere 2022, Serafini 2023 and both Oishi 2022 papers. Treating this as a continuous research arc is synthesis, since no one of those papers claims it.

One expansion produced a contrast rather than a continuation. Morales 2017, led by the Enjuanes and Sola group in Madrid with this laboratory contributing reagents, conceptual advice and manuscript writing, found small viral RNAs in SARS-CoV, but they derive from coding regions and contribute to lung immunopathology without lowering titres, where influenza small viral RNAs come from noncoding segment ends and act on the viral life cycle.

## Connections that are not thematic resemblance

Several reagent lineages join projects that share no subject.

The silencing cassette built in Aguado 2018 to ask an evolutionary question about why vertebrates abandoned RNA interference is named in the Nilsson-Payant 2021 nucleoprotein availability record as the source of the recombinant influenza and Sendai viruses used to ask a replication and innate sensing question. The splicing-independent 2A virus built in Chua 2013 supplies the decisive control in Oishi 2023 a decade later. The barcode library built as a drift control in Varble 2013 becomes the measurement in Varble 2014 and then travels to another gene in Muñoz-Moreno 2019 and another virus, route and barrier in McCune 2020. The miR-93-targeted nucleoprotein segment built for attenuation in Perez 2009 governs the output of a therapeutic vector in Schmid 2014 in the Journal of Virology.

One observation anticipates a later mechanism without any paper connecting them. Perez 2009 reported elevated nucleoprotein messenger RNA alongside very low nucleoprotein protein and interpreted this through the role of unbound nucleoprotein in the switch from transcription to replication, offering it as a proposal consistent with the data. Nilsson-Payant 2021 on nucleoprotein availability later made that quantity the determinant of whether the polymerase makes full-length genomes or short immunostimulatory fragments. Reading the first as anticipating the second is synthesis.

ADAR1 recurs across three areas with no paper asserting the link. tenOever 2007 introduced it as an IKKepsilon-dependent effector whose editing of influenza matrix messenger RNA was measured directly. Paget 2023 uses ADAR1 knockdown to generate the endogenous double-stranded RNA that granules buffer. Uhl 2023 makes it the escape route from engineered silencing. The connection is real and thin, and no publication in any of those areas asserts it.

Two evolutionary arguments converge without being claimed together. tenOever 2016 proposes that chordates lost RNA interference through incompatibility with interferon rather than redundancy, linking three premises, that systemic small RNA defence in a large organism requires amplification and circulation by an RNA-dependent RNA polymerase, that chordate receptor-mediated entry does not carry small RNAs along as plant cell-to-cell movement does, and that expressing such a polymerase in mammalian somatic cells itself triggers innate immunity, the last shown by other laboratories. Uhl 2023 supplies an independent obstacle at the level of a single interferon-associated enzyme, since ADAR1 editing destroys the sequence fidelity that perfect complementarity requires. Read side by side the vertebrate loss looks overdetermined rather than explained. Both arguments are correlative and neither paper claims the pair.

Finally, the two halves of the small RNA argument make sense only together. Backes 2014 found that destroying host microRNAs gives a virus no fitness gain, including in mice lacking both type I and type III interferon receptors, which removes the objection that a silencing contribution might be hidden beneath interferon. Benitez 2015 on reconstructed silencing then showed that the same animals are fully protected by an artificially rebuilt silencing defence, so the system mammals do not use would have worked. Neither half stands alone.

## Where lines of work stopped

An honest account of this corpus includes work that did not become a program.

The small viral RNA line ran from 2010 to 2012 and stopped. The proposal that eight svRNA-loaded replicases set segment balance was never tested by direct measurement of polymerase occupancy, no structure of the complex was obtained, and how svRNA is made remains unresolved. Its later appearance is incidental, as a band alongside mini-viral RNA on the northern blots of Nilsson-Payant 2021 on nucleoprotein availability.

The enzyme that cleaves a cytoplasmic primary microRNA transcript was never identified, and every paper in that theme says so. The virtron concept named in Shapiro 2010 does not recur as a subject of investigation, its own authors having cautioned that self-targeting makes natural virtrons unlikely to be genuine viral products.

The delivery platform reached intranasal administration in Schmid 2014 in the Journal of Virology with in vivo silencing explicitly left to future studies, and no later paper here demonstrates it. The proposal in Langlois 2013 to generalise biocontainment to filoviruses, coronaviruses and henipaviruses was not taken up, nor was its proposal to multiplex target sites across segments tested. Lineage tracing produced one paper, Heaton 2014, co-led with the Palese laboratory, and tenOever 2019 records that the design was subsequently developed by other laboratories.

Transmission bottleneck work was not returned to inside the laboratory. Varble 2014 identified the recipient rather than viral genetics as the site of restriction, since three guinea pigs cocaged with one donor carried different barcode sets despite identical exposure, and left the barrier performing the sampling unidentified. The platform moved outward to Muñoz-Moreno 2019 and McCune 2020, in both of which the contribution here is the method and its supervision.

The structural chemistry of transcription factor allocation was not pursued. Ng 2011 states that the consequences of Ser708 phosphorylation within ISGF3 are unknown, and Schmid 2014 in the Journal of Biological Chemistry does not establish MAP3K8 as a direct kinase for IRF3 or identify the modified hinge residues. Interferon and cell identity rests on Eggenberger 2019 and one Perspective, with no follow-up on pluripotency, and the phosphatase implied by the serine 300 and 302 data of Shapiro 2014 was never identified.

In the pandemic work, no viral product responsible for the low interferon phenotype is identified anywhere in the corpus. The hematopoietic progenitor signature noted in ferret trachea in Blanco-Melo 2020 was flagged as needing further work and not returned to. The NF-kappa B dependency established in culture in Nilsson-Payant 2021 on the NF-kappa B footprint could not be reproduced in the laboratory's own hamster model, which its authors state. The drug candidates arising from Bouhaddou 2020, led by the Krogan laboratory, from Daniloski 2021 and from Yaron 2022, led from Duke and Weill Cornell, are not followed up within this corpus. ILF3, nominated in Serafini 2023, was validated in mouse pain models and never tested in infected animals.

Guzmán-Solís 2021, a collaborative ancient DNA study recovering parvovirus B19 and hepatitis B genomes from dental remains in early Colonial Mexico City, has no predecessor and no successor here. Its record says it connects through personnel rather than through scientific lineage.

## Where the program revised itself

**Cytoplasmic microRNA processing.** Shapiro 2010 in RNA reported cytoplasmic processing as microprocessor independent. Shapiro 2012 in RNA, using conditional deletion rather than inference, found Drosha absolutely required, with Dicer needed only at the second cleavage, and revised the earlier reading. The correction did more than fix a result. Because a nominally nuclear RNase III enzyme found in the cytoplasm during infection is a more interesting object than an unexplained processing activity, the revision redirected the program onto Drosha localisation and produced Shapiro 2014 and Aguado 2017, which land on a position neither side of the 2013 antiviral RNA interference dispute had occupied, that a component of the silencing machinery restricts viruses in mammalian somatic cells without making small interfering RNAs at all.

**The cause of inflammation in tissues without replication.** Hoagland 2021 proposed disseminated viral RNA acting as a pattern away from the airway, resting on discordance between subgenomic RNA detection and infectious particle recovery, with neither transfer nor sensor recognition tested. Carrau 2023 from the same laboratory tested it and reported instead for airway-derived circulating interferon. Whole blood carried an interferon-stimulated gene signature with no interferon transcripts of its own, a fibroblast bioassay detected roughly sixty units per millilitre at one day, and three manipulations pointed the same way, in that dexamethasone delayed airway induction without changing early lung titres and permitted infectious virus in liver, spleen, olfactory bulb and gastrointestinal tract with transient viremia, intravenous inoculation bypassed the airway and produced productive infection of several distal organs, and prior airway infection before intravenous challenge reduced distal loads. Circulating interferon was detected only in animals with lung titres regardless of route. The revision also changes the meaning of the observation, since displaced interferon signalling becomes a protective output of the lung rather than evidence of distal infection. The reading is bounded, in that dexamethasone is not specific, the intravenous dose is a thousandfold higher so route and dose are not independent, and the bioassay does not separate type I from type III interferon.

**What an interferon-induction readout can miss.** Two prior studies from other laboratories had treated influenza detection as exclusively through RIG-I on the basis of interferon beta induction. Benitez 2015 on in vivo screening agrees on that point, since interferon beta induction was abolished only by loss of RIG-I, and shows that MDA5 is nonetheless required for full induction of Irf7, OAS isoforms, Ifit1, Stat1 and Isg15 in an RNase L-dependent manner. The general lesson, that an interferon-induction readout can miss a sensor's contribution, is the durable part.

**What most of NS1 is for.** The attenuation of NS1-deficient virus framed an expectation that Chua 2013 tested against. Silencing NS1 by more than ninety percent barely affected replication or interferon-regulated gene induction in cell lines, primary cells or mice, whereas altering the nuclear export protein in either direction was costly, and optimising the splice site cost about two logs in culture and nearly abolished replication in mice. The bound the authors state is that silencing removes more than ninety percent rather than all of NS1, so residual activity cannot be excluded.

**What a reagent was evidence for.** The vaccinia enzyme VP55, identified in Backes 2012 as the subunit that tails RISC-loaded microRNAs and marks them for host decay, was read differently as its vehicle changed. In 2012 its existence was evidence that host microRNAs impose a cost on a virus. Delivered from a replicating virus in Backes 2014 it showed no fitness gain, but the inflammatory environment of that vector confounded any separation of microRNA effects on cytokines from secondary interferon-stimulated gene induction. Aguado 2015 is presented by its own authors as the correction of that confound, substituting an inert adenovirus, and it is what allowed the positive part of the answer to emerge, that microRNA function during infection is confined largely to cytokine control, with core interferon machinery unchanged even after nine days of depletion.

**An interpretation inverted rather than a result corrected.** Blanco-Melo 2020 described the SARS-CoV-2 inflammatory arm as the striking feature of an imbalanced response. Nilsson-Payant 2021 on the NF-kappa B footprint showed the same phenotype to be a viral requirement rather than an escape from control, since loss of p65 or p50 blocks viral protein accumulation while a chimeric RelA activator restores it and the equivalent IRF3 construct restricts the virus. Which target genes the virus requires was not determined.

**Two revisions belonging to collaborators.** Paget 2023, led by the Hur laboratory, reverses the prevailing reading of stress granules in double-stranded RNA sensing. Yang 2020, led by the Chen, Evans and Schwartz groups, found that ACE2 protein abundance does not predict permissiveness across human lineages.

**A disagreement inside the corpus, left standing.** tenOever 2013 argues from thresholds of copy number, silencing capacity and kinetics that chordate microRNAs cannot be antiviral. Cullen 2013, a Minireview led by Bryan Cullen with Sara Cherry and tenOever, is more cautious than this laboratory's own review of the same year. It accepts the mouse embryonic stem cell evidence, declines to settle the somatic case, and specifies the experiment that would settle it, noting that the viral proteins on which the positive claims rest also antagonise interferon so the two explanations have not been separated. That the intermediate step in the sequence was more cautious than the laboratory's own position is worth recording as it stands.

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
- 2021-guzman-solis-ancient-viral-genomes-reveal-intro
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2021-horiuchi-immune-memory-from-sars-cov-2-infe
- 2021-nilsson-payant-reduced-nucleoprotein-availability
- 2021-nilsson-payant-the-nf-b-transcriptional-footprint
- 2021-si-a-human-airway-on-a-chip-for-the-r
- 2022-frere-sars-cov-2-infection-in-hamsters-a
- 2022-oishi-a-diminished-immune-response-under
- 2022-oishi-the-host-response-to-influenza-a-v
- 2022-yaron-host-protein-kinases-required-for-
- 2023-carrau-delayed-engagement-of-host-defense
- 2023-oishi-archaeal-kink-turn-binding-protein
- 2023-paget-stress-granules-are-shock-absorber
- 2023-serafini-sars-cov-2-airway-infection-result
- 2023-uhl-adar1-biology-can-hinder-effective
- 2025-manivasagam-transcriptional-repressor-capicua-
