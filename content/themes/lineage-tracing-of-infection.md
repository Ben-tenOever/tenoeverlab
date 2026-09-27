---
id: lineage-tracing-of-infection
area: programmable-virology
name: "Lineage Tracing of Infected Cells"
question: "What happens to a cell that is infected and does not die?"
publications:
  - 2014-heaton-long-term-survival-of-influenza-vi
---

## The scientific problem

Every method for identifying an infected cell reports on a viral product. Viral RNA, viral protein, and virus-encoded reporters all decay, so an assay built on any of them detects cells that are currently infected and is blind to cells that were infected and are no longer. Heaton 2014 states the gap in those terms and notes the biological question it closes off. Severe influenza outcomes had been associated with proinflammatory signalling that outlasts detectable virus, and nothing available could ask whether cells that had themselves been infected were maintaining that signal, because by the time the question becomes interesting the label is gone.

The assumption being tested is stronger than a methodological one. Infected cells were understood to be eliminated, either by replication-driven apoptosis and necrosis or by immune clearance. Whether any cell survives a productive influenza infection had not been asked in a way that could be answered.

## What this laboratory contributed

The design converts a transient viral event into a permanent mark on the host genome. Cre recombinase was inserted downstream of a PTV-1 2A site at the 3-prime end of the PB2 segment of A/Puerto Rico/8/1934, so Cre is produced wherever the polymerase segment is expressed, and mice carrying a lox-stop-tdTomato cassette then label any cell in which that expression occurred, permanently and independently of whether virus remains.

Validation of the label matters as much as the result. Reporter activation required active replication rather than uptake of infected cell debris, since lysed material from infected cells applied under neutralising antibody produced no signal and pretreatment with type I interferon abolished it. The recombinant virus retained influenza pathogenicity, with the median lethal dose shifting from 50 to 240 plaque forming units, and the paper notes that this comparison was performed once.

Marked cells were present at 5, 10 and 21 days, while infectious virus was undetectable in lung by day 10. Sorted day 5 marked cells yielded virus in eleven of twelve embryonated eggs and day 10 marked cells did not, and day 5 viral reads mapped across all eight segments, which the authors read as arguing against reporter activation by defective particle entry. The survivors were productively infected and then cleared the virus, and histology placed them in the epithelium of larger airways and never in alveoli.

Two further layers turn the observation into a functional claim. RNA sequencing of sorted marked and unmarked cells from the same lungs identified Cc10 as the only cell type marker retained in survivors, while Sftpc was almost entirely lost by day 5, implicating club cells. Survivors carried a higher magnitude interferon-stimulated gene signature than their neighbours in the same tissue and selectively elevated Cxcl10, Ccl20 and Ccl5 without appreciable Ccl2 induction, a pattern reproduced by murine and human club cell lines. Substituting a Cre-inducible diphtheria toxin receptor strain for the reporter strain converted the same genetic logic into an ablation experiment, and removing the marked survivors at day 5 significantly reduced bronchiolar epithelial necrosis at day 10 without altering overall infiltration scores.

## How the work evolved

This theme has one paper in the corpus, and the honest description is that the laboratory built the tool, obtained the result, and did not return to it. The field did. tenOever 2019 records that the same Cre design was produced independently by the Schwemmle laboratory, that expression from PB2 was well tolerated while expression from NS1 through a 2A site attenuated substantially, and that the club cell observation was subsequently developed by other groups, with Hamilton and colleagues characterising surviving club cells as inherently more resistant and carrying altered responses to virus and interferon for weeks after clearance, and with Chambers and colleagues and Fiege and colleagues attributing the resistance to unusually strong antiviral gene induction combined with evasion of CD8-mediated clearance.

What Heaton 2014 did not establish, and said so, is causation in either direction. The link between the elevated interferon-stimulated gene signature and survival is explicitly described as correlative, and the club cell line comparison shows higher intrinsic interferon responsiveness in that lineage without showing that the responsiveness is what permitted survival in vivo. The depletion experiment removes all marked survivors rather than club cells specifically, and the authors state that contributions from surviving non-club cells complicate interpretation. Lineage assignment rests on marker transcripts and anatomical concordance rather than on an independent club cell genetic label. Time points stop at 21 days, so nothing is established about whether the survivor population resolves.

## Supporting publications

Heaton 2014 is co-led, with Peter Palese and tenOever as joint senior and corresponding authors, and the reporter virus builds on prior mutagenesis and rescue work from the Palese laboratory.

## Connections

The design belongs to the same engineering family as the microRNA-targeted viruses, and tenOever 2019 places it in that taxonomy as a lineage-marking module distinct from a tracking module, on the grounds that it reports where the virus has been rather than where it is. It is the methodological inverse of the cell-type-restriction-as-a-tool theme, since one design marks the cells that supported replication and the other excludes replication from a chosen compartment. The finding that an acute respiratory infection leaves behind a transcriptionally altered epithelial population connects to the post-acute-sequelae theme in the pandemic-host-response area, a connection the record for this paper marks as synthesis requiring those papers side by side.

## Publications referenced
- 2014-heaton-long-term-survival-of-influenza-vi
- 2019-tenoever-synthetic-virology-building-viruse
