---
id: limits-of-microrna-function
area: small-rna-antiviral-defense
name: The Functional Limits of MicroRNAs
question: What does the microRNA system actually do on the timescale of an infection?
publications:
  - 2015-aguado-microrna-function-is-limited-to-cy
  - 2012-backes-degradation-of-host-micrornas-by-p
---

## The scientific problem

Claims about microRNAs in antiviral immunity had been made in both directions and at very different magnitudes. Some reports assigned microRNAs as much as half of the antiviral activity of type I interferon. Others found many human viruses refractory to inhibition by endogenous microRNAs. Meanwhile, separate work indicated that the silencing complex may not be available during infection at all, since it is inactivated by cellular stress and ribosylated beyond roughly eight hours of infection. Settling this requires a clean subtraction. MicroRNAs must be removed quickly, in cells that are not transformed and not already responding to a replicating virus, and the removal must not itself provoke an antiviral response. Blocking microRNA synthesis does not achieve this, because existing pools must first turn over.

## What this laboratory contributed

Backes 2012, co-led with Sara Cherry, supplies the enzyme on which everything else in this theme depends. Small RNA deep sequencing during poxvirus infection of Drosophila cells, of the natural tiger moth host of an entomopoxvirus, and of mammalian cells showed that mature microRNAs acquire short nontemplated adenosine tracts and then disappear, while endogenous small interfering RNAs do not. Chemical inhibitors placed the activity in early infection, and knockdown together with reconstitution identified VP55, the catalytic subunit of the viral poly(A) polymerase, as both necessary and sufficient, with the processivity factor VP39 inactive in either assay. A synthetic miR-124 carrying seven adenosines was destroyed after transfection into uninfected cells, so the nuclease step is supplied by the host. Tailed guides remained associated with Argonaute 2 while star strands were not tailed, which places the modification after strand selection, and a guide bearing a 3 prime terminal 2 prime O-methyl group was completely protected. The paper also reports a functional consequence, that transfected mimetics of the dominant fibroblast microRNAs resisted degradation and roughly halved virus yield, and the authors state explicitly that this restriction could be direct or indirect. Two further elements are interpretation. No direct interaction between VP55 and Argonaute is shown, and the proposal that terminal 2 prime O-methylation evolved partly as a cellular countermeasure protecting antipathogen small RNAs is explicitly speculative and rests on comparative arguments about HEN1 distribution.

Aguado 2015 built the clean subtraction. VP55 was placed in a replication-incompetent adenovirus with a modified fibre, which removes roughly 90 percent of the abundant microRNAs in primary human fibroblasts within a day, does not induce interferon-stimulated genes, and alters under 0.35 percent of the transcriptome in Dicer-deficient cells where any change must be microRNA independent. The control vector changed only 48 genes relative to mock, none of them interferon-stimulated genes or intrinsic response components.

The results split the question in two. Removing microRNAs changed 12 of the 1,548 genes induced by transfected double-stranded RNA in primary fibroblasts, and 12 of the 179 induced by six hours of interferon beta, with IRF1 among them and a miR-23 site in its untranslated region confirmed by reporter and by site mutation. Extending interferon treatment to 24 hours raised the microRNA-sensitive set only to 78, still without central mediators of the response. Nine days of depletion, by contrast, changed more than 1,700 transcripts, and IFIH1, IRF3, IRF7, RELA, RELB, IFNB, IFNAR1, STAT2 and IRF9 remained unchanged even then. What did respond was dominated by chemokines and cytokines, including IL8, CXCL1, CXCL2, CXCL6, CCL2, CCL7, IL1B, IL11, IL33, CSF1, CSF2 and IL6, and these were absent from the Dicer-deficient control dataset, which argues they reflect genuine microRNA targeting rather than direct VP55 action. IL6 derepression was reversed by a chemically protected let-7 mimic that resists VP55, and a reporter carrying the IL6 untranslated region lost let-7 responsiveness when the predicted site was mutated. Intranasal delivery of the vector to mice raised six of eighteen measured lung cytokines at the protein level within 48 hours.

## How the work evolved

The reagent moved through three vehicles and the interpretation sharpened each time. In Backes 2012 VP55 was the finding, a reason why a family of large DNA viruses does not exploit host microRNAs. In Backes 2014 it was delivered from a replicating vesicular stomatitis virus to ask whether a virus gains fitness by destroying host small RNAs, and the inflammatory environment created by the replicating vector confounded any attempt to separate microRNA effects on cytokines from secondary interferon-stimulated gene induction. Aguado 2015 is presented by its own authors as the correction of that confound, and the substitution of an inert adenovirus for a replicating rhabdovirus is what allowed the positive part of the answer to emerge.

The conceptual result is a separation of two questions that had been conflated. Whether microRNAs act during the antiviral response and whether they act on it are different, and the answers differ. The supporting argument is a timescale argument, which reconciles conflicting literature by noting that assays run over hours will find nothing even where genuine targets exist. That argument is the experimental counterpart of the kinetic constraint proposed in tenOever 2013.

Several boundaries are stated in the paper. The approach detects only repression active at baseline and would miss a microRNA whose function requires induction. Transfected double-stranded RNA and recombinant interferon beta stand in for infection, so no virus replication phenotype is measured. The nine-day depletion regime is not a physiological state, and the authors accordingly frame its relevance as chronic infection or persistence rather than acute disease. The in vivo work is a single 48-hour timepoint in mouse lung with no pathogen present, so it shows derepression rather than a consequence for infection outcome. The proposal that infection-driven inactivation of the silencing complex is itself a mechanism for derepressing inflammatory transcripts, and that influenza NS1 would thereby dampen cytokine output, draws on other laboratories' work and is not tested here.

## Supporting publications

Backes 2012 is also assigned to the theme on whether mammalian antiviral RNA interference exists, where the same enzyme figures in the argument that host microRNAs impose a cost on a virus.

## Connections

The cytokine target set identified here is where this area meets innate immune signalling, and specifically the question of how the magnitude of the interferon response is set. The finding that core interferon machinery is microRNA insensitive even after nine days of depletion is the strongest single piece of evidence in the corpus against microRNAs being a component of the intrinsic antiviral response, and it supports the negative conclusion of Backes 2014 from a different direction, by ablation of the host pathway rather than by viral fitness.

## Publications referenced

- 2015-aguado-microrna-function-is-limited-to-cy
- 2012-backes-degradation-of-host-micrornas-by-p
- 2014-backes-the-mammalian-response-to-virus-in
- 2013-tenoever-rna-viruses-and-the-host-microrna-
