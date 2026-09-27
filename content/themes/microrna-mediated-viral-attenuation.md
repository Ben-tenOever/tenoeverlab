---
id: microrna-mediated-viral-attenuation
area: programmable-virology
name: "MicroRNA-Mediated Viral Attenuation"
question: "Can host microRNA expression be used to decide which species or tissue a virus may replicate in?"
publications:
  - 2009-perez-microrna-mediated-species-specific
  - 2013-langlois-microrna-based-strategy-to-mitigat
  - 2012-pham-replication-in-cells-of-hematopoie
---

## The scientific problem

Attenuating a virus has historically meant damaging it. Temperature sensitivity, cold adaptation and passage in a foreign substrate all reduce replication by degrading some part of the viral machinery, which means the attenuated virus differs from the wild type in ways the experimenter does not control and that the phenotype travels poorly to a new strain. Perez 2009 frames the problem in those terms, noting that the licensed live attenuated influenza vaccine of the time relied on a single temperature-sensitive mechanism with a fixed list of excluded recipients, and that the annual reformulation cycle rewards an attenuation strategy that transfers easily between backgrounds.

A different kind of attenuation had become conceivable because host microRNAs are expressed unevenly. A minority are restricted to particular species or lineages, and a fully complementary target site placed in a viral transcript converts the resident microRNA into a virus-specific silencing guide. Other laboratories had shown this for lentiviruses, picornaviruses and rhabdoviruses, in each case by inserting target sequence into a viral untranslated region. What was unresolved was whether the approach could become a controllable engineering parameter, and whether it could be applied to a virus whose transcript architecture leaves no untranslated region to work with.

## What this laboratory contributed

Perez 2009 supplies the founding demonstration and, more importantly, the design discipline that the rest of the theme reuses. Influenza mRNAs terminate shortly after the stop codon, so target sites were built into the nucleoprotein open reading frame at two positions where the nucleotide changes preserve the side chain class of the encoded amino acid. The targeting microRNA, miR-93, was chosen from published small RNA profiles because it is present in mouse and human and absent from chicken, which places the attenuating signal in the vaccine recipient and not in the egg used for manufacture. The doubly targeted virus lost more than two logs of lethality in mice while reaching roughly 10^8 plaque forming units per millilitre in embryonated eggs.

Three controls in that paper define what a microRNA-restricted virus must show before its phenotype can be read. A parental virus carrying the identical amino acid substitutions with the pairing disrupted separates silencing from protein damage. Replication in Dicer-deficient fibroblasts and rescue by a locked nucleic acid inhibitor of miR-93 tie the restriction to the silencing pathway and to the specific microRNA. Nucleoprotein mRNA accumulated while the protein did not, which the authors read as translational repression. Perez 2009 also reports that neither influenza infection nor NS1 disrupts microRNA biogenesis or silencing in mammalian cells, which is the licensing observation for everything that follows.

Pham 2012 carries the logic to a second virus family. Four miR-142 sites in the variable region of the dengue virus 3-prime untranslated region excluded replication from macrophages and dendritic cells, and the virus failed to reach spleen and liver by three inoculation routes. That paper also supplies the theme's most instructive negative results. The 157 nucleotide insert itself cost about one log of growth, independent of its sequence, so every comparison is between two insertion-bearing viruses. A variant with seed and central pairing disrupted was still repressed at the protein level while repression at the RNA level weakened, which the authors describe as an enigma and leave unresolved. And sequencing of virus recovered from spleen found no intact targeted genomes, only variants that had excised the whole cassette, which establishes that a quantitative assay for a viral gene cannot distinguish escape from residual targeted replication.

Langlois 2013 shows how the design parameters can be tuned deliberately rather than accepted. Small RNA deep sequencing across human lung cells, primary ferret lung and MDCK cells, arbitrated by northern blot where the two disagreed, selected miR-192 on the basis of a cross-species expression difference chosen for a purpose. Target sites were placed downstream of the hemagglutinin stop codon in a duplicated packaging region, leaving both the protein and the packaging signal untouched. That placement, and the packaging-signal duplication that makes it possible, is the maturation of the method, because it removes the amino acid substitutions that Perez 2009 had to accept and that were themselves mildly attenuating in vivo.

## How the work evolved

The arc runs from insertion inside a coding sequence, with a fitness cost the authors could bound but not remove, to insertion in engineered noncoding space with no measurable cost. Alongside that, the choice of microRNA moves from opportunistic to designed. Perez 2009 took miR-93 from published profiles. Langlois 2013 sequenced the small RNA pools of the exact tissues that mattered and treated the species difference as a specification.

What did not get resolved is escape. Perez 2009 recovered no revertants over ten serial passages in A549 cells or from more than twenty five clones per in vivo cohort, and Langlois 2013 recovered none from seventeen plaques from mouse lung or after ferret transmission. Both bound escape below a sampling depth rather than excluding it. Pham 2012 shows the opposite outcome under sustained pressure in an animal, where the entire recoverable population had excised the cassette. Reading the three together, the coupling of a target site to conserved codons, which Perez 2009 proposed as the constraint tying escape to a fitness cost, is not something any single paper demonstrates, and the dengue result shows that a cassette in noncoding sequence has no such constraint.

## Supporting publications

Perez 2009 and Pham 2012 are lab-led. Langlois 2013 is co-led, with three corresponding authors, and the ferret transmission work sits with the Perez and García-Sastre groups rather than with this laboratory.

## Connections

Langlois 2013 is also the biocontainment application, treated in the molecular-biocontainment theme. Pham 2012 is the point at which the same construct becomes a compartment-subtraction experiment, which is the cell-type-restriction-as-a-tool theme. The reciprocal use of a miR-93 target site to limit a delivery vector rather than a pathogen appears in Schmid 2014, in the rna-vectors-for-delivery theme. The premise that chordate microRNA machinery is available for this kind of exploitation because RNA viruses do not naturally engage it belongs to the small-rna-antiviral-defense area.

## Publications referenced
- 2009-perez-microrna-mediated-species-specific
- 2013-langlois-microrna-based-strategy-to-mitigat
- 2012-pham-replication-in-cells-of-hematopoie
- 2014-schmid-a-versatile-rna-vector-for-deliver
