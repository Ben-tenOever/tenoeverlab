---
id: calibration-of-interferon-in-vivo
area: innate-immune-signaling
name: Calibration of the Interferon Response In Vivo
question: In a whole animal, which cells produce the interferon response, when does it arrive, and what happens when the timing is wrong?
publications:
  - 2012-langlois-hematopoietic-specific-targeting-o
  - 2014-heaton-long-term-survival-of-influenza-vi
  - 2020-blanco-melo-imbalanced-host-response-to-sars-c
  - 2021-nilsson-payant-the-nf-b-transcriptional-footprint
  - 2021-hoagland-leveraging-the-antiviral-type-i-in
  - 2023-carrau-delayed-engagement-of-host-defense
---

## The scientific problem

Cell culture leaves the organism-level questions open. A lung is a mixture of epithelial and immune cells in very unequal numbers, so the compartment contributing most of the interferon is not predictable from which cells are most often infected. Timing is a variable in its own right, since a response arriving after a virus has established itself is not the same response delivered early, and a response can outlast the virus that triggered it. And whether the response appears where the virus replicates, or somewhere else, determines what a measurement means. The problem is calibration. Which cells produce the response, when it arrives relative to replication, whether it is proportionate, and what follows when it is mistimed or displaced.

## What this laboratory contributed

Five of the six publications are `lab-led` with tenOever as senior and corresponding author. Heaton 2014 is `co-led`, with Peter Palese and tenOever as joint senior and corresponding authors.

Langlois 2012 made the compartment question answerable. Target sites for miR-142, a microRNA confined to hematopoietic lineages, were placed in a duplicated packaging region of the influenza nucleoprotein segment, producing a replication-competent virus silenced in immune cells and intact in epithelium, with silencing verified from small viral RNA through to virus recovered from the draining lymph node and escape mutants excluded by sequencing. Infected mice lost weight, cleared virus and generated nucleoprotein and polymerase acidic specific CD8 T cells indistinguishably from controls despite losing direct antigen presentation in culture, which the authors read as sufficiency of cross-presentation. What fell was innate signalling, since interferon beta and IRF-7 induction dropped in macrophages and in whole lung even though lung tissue is predominantly nonhematopoietic. Interferon beta induction required RIG-I in the primary cells tested, but no hematopoietic-restricted knockout was used, so the in vivo sensor attribution is inferred, and the authors state they cannot explain why removing a numerically minor compartment produces so large a deficit.

Heaton 2014 turned timing into a lineage question. An influenza A virus carrying Cre recombinase on PB2 permanently marks any cell in which replication and protein synthesis occurred. Marked cells persisted at 10 and 21 days, past recoverable infectious virus, were confined to the epithelium of larger airways, and carried Cc10 as the only retained lineage marker, implicating club cells. Survivors held an amplified interferon-stimulated gene signature and elevated Cxcl10, Ccl20 and Ccl5 without Ccl2, and ablating them with a Cre-inducible diphtheria toxin receptor reduced bronchiolar epithelial necrosis. The authors are explicit that the link between the interferon-stimulated gene signature and survival is correlative, that lineage assignment rests on marker transcripts, and that surviving non-club cells complicate the ablation result.

Blanco-Melo 2020 applied comparative profiling to a new pathogen, positioning SARS-CoV-2 against SARS-CoV-1, MERS-CoV, influenza A virus, parainfluenza virus 3 and respiratory syncytial virus across cell lines, primary bronchial epithelium, ferrets and patient material. The recurring pattern was low type I and type III interferon with partial interferon-stimulated gene induction alongside strong chemokine and IL-6 expression. Ruxolitinib abolished interferon-stimulated gene induction while leaving chemokine induction largely intact, separating the two arms, and interferon beta pretreatment restricted the virus, so the low output is not resistance. Interferon induction proved strongly multiplicity dependent, which the authors flag rather than resolve, and no viral antagonist is assigned.

Nilsson-Payant 2021 on the nuclear factor kappa B footprint inverted the interpretation of that imbalance. In ACE2-expressing A549 cells the dominant early signature was tumour necrosis factor alpha signalling through NF-kappa B, with no interferon signature and no STAT1 or IRF3 phosphorylation, concentrated by single-cell sequencing in infected rather than bystander cells, and with ATAC sequencing showing opening sites enriched for REL, RELA and NFKB1 motifs at distal enhancers. Silencing RelA reduced and silencing NF-kappa B1 eliminated nucleocapsid protein, and RELA knockout cells were rescued by a RelA DNA-binding domain fused to a VPR activator while the equivalent IRF3 construct restricted the virus. The inflammation therefore reflects a viral requirement rather than a failure of evasion. Which target genes are required was not determined, and the work is in vitro, with the authors noting they could not reproduce the effect in their hamster model.

Hoagland 2021 and Carrau 2023 moved the question into a naturally permissive animal. Hoagland 2021 built a longitudinal multi-tissue hamster atlas, including a de novo assembled and functionally validated Ifnb1 transcript that made interferon biology readable in the model at all. Interferon-stimulated gene and chemokine peaks appeared in trachea several days before lung, and antiviral programs appeared in olfactory bulb, brain and small intestine despite viral reads orders of magnitude lower, tentatively attributed to disseminated viral RNA. Intranasal universal interferon alpha A/D given before challenge or one day after lowered infectious virus and inflammatory transcripts, shifted the infiltrate from neutrophils toward macrophages and prevented transmission in three of five contact animals, with a double-stranded RNA mimetic giving comparable activity.

Carrau 2023 tested that attribution and found for the alternative. Whole blood carried an interferon-stimulated gene signature with no interferon transcripts of its own, and a fibroblast bioassay detected roughly sixty units per millilitre of circulating interferon at one day. Three manipulations then pointed the same way. Dexamethasone delayed airway induction without changing early lung titres and permitted infectious virus in liver, spleen, olfactory bulb and gastrointestinal tract with transient viremia. Intravenous inoculation bypassed the airway and produced productive infection of kidney, liver, spleen, heart and gastrointestinal tract. Prior airway infection before intravenous challenge reduced distal loads. Circulating interferon was detected only in animals with lung titres regardless of route. Dexamethasone is not specific, the intravenous dose is a thousandfold higher, and interferon was measured by a bioassay that does not distinguish type I from type III.

## How the work evolved

The frame widens steadily. Langlois 2012 asks which compartment produces interferon. Heaton 2014 asks what happens to infected cells afterwards and finds inflammation that outlives the virus. Blanco-Melo 2020 establishes what an abnormally small interferon response looks like across four levels of system. Nilsson-Payant 2021 on nuclear factor kappa B reinterprets that imbalance as something the virus needs. Hoagland 2021 maps response and replication as separable in space and intervenes by delivering interferon locally. Carrau 2023 closes the loop by showing the displaced response is explained by circulating interferon and is functionally protective.

A visible correction runs through it. Hoagland 2021 proposed disseminated viral material as the cause of distal inflammation, and Carrau 2023 from the same laboratory tested that proposal and reported for circulating airway-derived interferon instead. The recurring design, treating the site of replication and the site of response as separable variables and building interventions that decouple them, is synthesis across these papers rather than a claim in any one.

## Supporting publications

- **2012-langlois-hematopoietic-specific-targeting-o.** Makes viral tropism an experimental variable and shows that replication in the hematopoietic compartment is dispensable for CD8 T cell priming but accounts for much of the in vivo interferon response.
- **2014-heaton-long-term-survival-of-influenza-vi.** Permanently marks infected cells and finds surviving airway club cells that sustain interferon-stimulated gene and chemokine expression after clearance and contribute to bronchiolar damage.
- **2020-blanco-melo-imbalanced-host-response-to-sars-c.** Positions the SARS-CoV-2 response against five other respiratory viruses and defines low interferon with strong interferon-independent chemokine induction as its signature.
- **2021-nilsson-payant-the-nf-b-transcriptional-footprint.** Shows that SARS-CoV-2 engages NF-kappa B and not the IRFs, and that NF-kappa B-driven transcription is required for replication.
- **2021-hoagland-leveraging-the-antiviral-type-i-in.** Provides a longitudinal multi-tissue hamster atlas with a newly annotated Ifnb1 and shows that intranasal interferon limits virus, pathology and transmission.
- **2023-carrau-delayed-engagement-of-host-defense.** Shows that airway-derived circulating interferon primes distal organs and restricts tropism, and that delaying or bypassing the airway response permits viremia and distal infection.

## Connections

Langlois 2012 and Heaton 2014 both belong to programmable virology, since the miR-142 restricted virus and the Cre reporter virus are engineering achievements before they are immunology results. Nilsson-Payant 2021 on nuclear factor kappa B, Blanco-Melo 2020, Hoagland 2021 and Carrau 2023 are shared with pandemic host response and disease, where the same material is read for what it says about COVID-19 rather than about calibration. Blanco-Melo 2020 uses the NS1-deficient influenza A virus as its reference for an unantagonised response, linking it to influenza genome regulation, and cites Sharma 2003 for TBK1, the one explicit citation back to the training-period origin of this area. The post-clearance inflammatory state in Heaton 2014 prefigures the post-acute sequelae theme.

## Publications referenced
- 2003-sharma-triggering-the-interferon-antivira
- 2012-langlois-hematopoietic-specific-targeting-o
- 2014-heaton-long-term-survival-of-influenza-vi
- 2020-blanco-melo-imbalanced-host-response-to-sars-c
- 2021-hoagland-leveraging-the-antiviral-type-i-in
- 2021-nilsson-payant-the-nf-b-transcriptional-footprint
- 2023-carrau-delayed-engagement-of-host-defense
