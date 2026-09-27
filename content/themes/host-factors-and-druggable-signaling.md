---
id: host-factors-and-druggable-signaling
area: pandemic-host-response
name: Host Factors and Druggable Signaling
question: Which host proteins does SARS-CoV-2 require, and can any of them be drugged?
publications:
  - 2021-daniloski-identification-of-required-host-fa
  - 2020-bouhaddou-the-global-phosphorylation-landsca
  - 2022-yaron-host-protein-kinases-required-for-
  - 2021-si-a-human-airway-on-a-chip-for-the-r
---

## The scientific problem

In 2020 the list of human genes known to be required for SARS-CoV-2 infection ran to ACE2 and cathepsin L. Proteomic interaction maps had proposed hundreds of virus-host contacts, but interaction is not requirement. Host-directed antivirals are attractive because they can act across related viruses and are harder to escape by mutation, and because kinases in particular are a well-populated drug target class, yet none of that helps without knowing which host enzymes the virus actually depends on.

A parallel problem concerned how candidates were nominated. Repurposing screens run in cell lines produce hits at concentrations and in cellular contexts that bear little relation to a treated patient, which the confusion over hydroxychloroquine in early 2020 made unignorable.

## What this laboratory contributed

The four publications here divide sharply by contribution character, and the division matters for what can be attributed.

Daniloski 2021 in Cell carries `co-led`. The virological work, including all containment-level infections, sits with the tenOever laboratory while the screening platform and analysis sit with the Sanjana laboratory, the two being joint corresponding authors with Sanjana as lead contact. A genome-scale CRISPR knockout screen in ACE2-expressing A549 cells turned survival of infection into a selection and ranked every protein-coding gene. ACE2 and cathepsin L were recovered among the top hits, and the remaining top-ranked genes clustered in endosomal biology, including thirteen vacuolar ATPase subunits, four Retromer and four Commander members, four ARP2 and ARP3 members and three class 3 PI3K genes. Thirty genes were retested with fresh guides, by small interfering RNA, in a second line, and against 26 compounds, with PIK3C3 inhibitors among the most effective. Single-cell CRISPR profiling found that six endosomal hits share upregulated cholesterol biosynthesis when lost, and amlodipine, which raises cholesterol, reduced infection. RAB7A loss reduced surface ACE2 and accumulated it in EEA1-positive vesicles, an effect that held in cells with endogenous ACE2.

Bouhaddou 2020 carries `collaborative` and was led by the Krogan laboratory as part of a large multi-institution consortium. The tenOever contribution is listed under work supervision alongside fifteen others, with a member of that group among those performing infections, and the main point of contact is that the transcription factor activity analysis draws on expression data from Blanco-Melo 2020. The study found that over 24 hours the host response is enacted through phosphorylation rather than protein abundance, inferred activity changes for 97 of 518 human kinases, and reported activation of casein kinase II and the p38 cascade alongside downregulation of mitotic kinases with arrest between S and G2. Mapping regulated kinases onto known inhibitors gave 87 candidates, of which 68 were tested, with antiviral activity for inhibitors of casein kinase II, p38, AXL, PIKFYVE and cyclin-dependent kinases.

Yaron 2022 carries `collaborative` and was led from Duke and Weill Cornell, with tenOever among four corresponding authors and the contribution lying in infection and phosphoproteomic work at the New York sites. Starting from measured substrate specificity matrices rather than candidate screening, the authors resolved the dense phosphorylation cluster in the nucleocapsid SR-rich domain into an ordered cascade, with SRPK1 and SRPK2 priming serine 206 and serine 188, GSK-3 propagating in four-residue steps toward the amino terminus, and casein kinase 1 covering threonine 205. A double phospho-null mutant abolished the SRPK-driven shift. Knockdown of SRPK1 and treatment with SPHINX31, SRPIN340 or the approved drug alectinib reduced replication across engineered cells, Calu-3 cells and primary pneumocytes, and alectinib also suppressed the distantly related HCoV-229E.

Si 2021 carries `collaborative` and was conceived and led at the Wyss Institute by Si, Bai and Ingber. The tenOever contribution was development of the hamster infection model and testing of drug efficacy against native SARS-CoV-2 in vivo. On a perfused airway chip maintained at published human maximum plasma concentrations, only amodiaquine, toremifene and clomiphene reduced entry of spike-pseudotyped particles, while hydroxychloroquine, chloroquine and arbidol did not, and the three that failed on chip had also failed in trials. Amodiaquine then reduced native SARS-CoV-2 in hamsters prophylactically, therapeutically and in a co-caging transmission model, where hydroxychloroquine had no significant effect.

## How the work evolved

Four different starting points converge on host-directed intervention. A forward genetic screen ranks requirement directly. A phosphoproteomic survey reads activity states and converts them into compound candidates. A specificity-matrix approach resolves one viral substrate and arrives at an approved drug. A tissue-engineered model filters candidates other assays had already nominated. The recurring position is that the host rather than the virus is the tractable target, and the recurring difficulty is that requirement is easier to establish than mechanism.

The limits are specific and should not be smoothed. Daniloski 2021 does not establish causal ordering between the cholesterol change and the infection block, nor which step of the life cycle is affected, and the authors say the mechanism of the cholesterol effect remains to be elucidated. In Bouhaddou 2020 kinase activities are inferred from substrate regulation rather than measured, discovery proteomics was performed in Vero E6 cells with sites mapped onto human orthologs, the cytokine experiment cannot separate p38 activity from reduced replication, and the filopodial budding evidence is correlative imaging with no perturbation. Yaron 2022 assigns sites computationally and does not establish why nucleocapsid phosphorylation is needed, all infection work is in culture, and the supporting clinical observation amounts to two case reports. In Si 2021 every chip experiment with SARS-CoV-2 used spike-pseudotyped particles, which report entry only, so the chip data speak to prophylaxis against initial infection rather than to therapy, drug absorption into the device was not quantified, and the concordance argument rests on a small number of drugs chosen from prior reports.

## Supporting publications

- **2021-daniloski-identification-of-required-host-fa.** Genome-scale CRISPR ranking of host requirements, converging on endosomal machinery, with cholesterol biosynthesis as a shared consequence and RAB7A controlling surface ACE2.
- **2020-bouhaddou-the-global-phosphorylation-landsca.** Led by the Krogan laboratory. Time-resolved phosphoproteomics showing signalling rather than abundance as the dominant response layer, and converting inferred kinase activity into tested inhibitors.
- **2022-yaron-host-protein-kinases-required-for-.** Led from Duke and Weill Cornell. Resolves nucleocapsid SR-rich domain phosphorylation into an ordered SRPK, GSK-3 and casein kinase 1 cascade whose inhibition suppresses two coronaviruses.
- **2021-si-a-human-airway-on-a-chip-for-the-r.** Led at the Wyss Institute. A perfused human airway chip dosed at clinically achievable concentrations separates candidates that survive into a hamster model from those that do not.

## Connections

The entry biology here meets the viral side of the same step in tropism and permissive tissues, where Daniloski 2021 in eLife shows the Spike D614G substitution raising entry efficiency, so receptor availability and Spike processing state are addressed from opposite directions by the same two laboratories and neither paper connects them. Bouhaddou 2020 depends on the transcriptional datasets from the imbalanced host response for its transcription factor inference, and the interferon-stimulated gene products that rise after alectinib treatment in Yaron 2022 touch the same question without resolving its direction. Si 2021 also belongs to models for pandemic virology, since its central claim concerns model fidelity rather than any one drug, and its hamster arm is the same model built in interferon as intervention.

## Publications referenced
- 2021-daniloski-identification-of-required-host-fa
- 2020-bouhaddou-the-global-phosphorylation-landsca
- 2022-yaron-host-protein-kinases-required-for-
- 2021-si-a-human-airway-on-a-chip-for-the-r
- 2020-blanco-melo-imbalanced-host-response-to-sars-c
- 2021-daniloski-the-spike-d614g-mutation-increases
