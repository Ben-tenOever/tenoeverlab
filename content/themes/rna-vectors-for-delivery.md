---
id: rna-vectors-for-delivery
area: programmable-virology
name: "RNA Virus Vectors for Small RNA Delivery"
question: "Can an RNA virus deliver a functional small RNA to tissues in an animal?"
publications:
  - 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
  - 2014-schmid-a-versatile-rna-vector-for-deliver
  - 2010-varble-engineered-rna-viral-synthesis-of-
---

## The scientific problem

Two obstacles sat in front of this theme, one conceptual and one practical.

The conceptual obstacle was a prohibition. MicroRNAs are excised from a primary transcript in the nucleus by Drosha and DGCR8, and Varble 2010 sets out the argument advanced for why an RNA virus therefore cannot encode one. Cleavage of a hairpin carried in the genome would fragment that genome, and the genome would additionally present a perfect complement to the microRNA it produced. Virus-encoded microRNAs had been recovered only from nuclear DNA viruses with large coding capacity.

The practical obstacle was delivery, which Langlois 2012 in Molecular Therapy and Schmid 2014 both name as the step separating RNA interference as a laboratory technique from RNA interference as a therapy. Lentiviral vectors integrate, and DNA virus vectors had been reported to saturate nuclear export and Argonaute, with lethal consequences in mice in work from the Kay group that Schmid 2014 cites.

## What this laboratory contributed

Varble 2010 removes the prohibition by building around it. Segment 8 of influenza A/PR/8/34 was reconfigured so that the overlapping NS1 and NEP reading frames were split, creating an intergenic region and an extended intron, into which the murine miR-124-2 locus was inserted. The hairpin is then excised in the spliced lariat rather than from the genome, which separates the two proposed obstacles experimentally. The recombinant virus produced mature miR-124 by four hours after infection at levels comparable to abundant endogenous microRNAs, in an orientation-dependent and splicing-dependent and Dicer-dependent manner, with protein expression and multicycle growth matching wild type. Target sites on the genomic strand were not silenced while identical sites in messenger RNA were. The authors attribute genome protection to nuclear localisation and ribonucleoprotein organisation, and no structural or biochemical test of that occlusion is reported, so it is an inference from two absences. The absence of Drosha cleavage is likewise bounded below assay sensitivity rather than excluded.

That paper reframes the absence of natural RNA virus microRNAs as a question about selection rather than about physical possibility, and it leaves behind a reusable cassette. The split segment 8 with an intergenic insertion site, the scrambled-insert control, and the pairing of small RNA northern blotting with stem-loop RT-PCR recur throughout this area.

Langlois 2012 in Molecular Therapy extends the platform on three axes at once, to a cytoplasmic virus, to negative polarity, and into animals. The murine pri-miR-124 locus was inserted between the glycoprotein and polymerase genes of vesicular stomatitis virus and compared against Sindbis and influenza vectors carrying the same locus. Production required Dicer, reached an estimated 25,000 to 35,000 copies per cell against fewer than fifteen in mock-infected fibroblasts, associated with Argonaute 2, and repressed reporters by roughly sixty to ninety percent. Intravenous delivery in interferon alpha receptor knockout mice placed miR-124 in lung, spleen, liver, kidney and heart. In wild-type mice the microRNA remained at high relative levels at five days after viral leader RNA had fallen, and induction of the miR-124 target Ptbp1 was reduced from roughly thirtyfold to less than fivefold.

That paper is also candid about a real liability rather than a hypothetical one. Star strand accumulation reached as much as forty percent of reads mapping to the viral pri-miR-124 in the cytoplasmic vectors, the star strand loaded and repressed its own reporter, and the proposed fixes through duplex thermodynamics are untested there.

Schmid 2014 addresses the two properties a delivery vector needs beyond reaching a tissue, which are that it should not replicate and that its output should be adjustable. Replacing the segment 4 open reading frame of a hemagglutinin-deleted virus-like vector with a primary microRNA transcript gave roughly threefold more miR-124 in primary human fibroblasts than the replication-competent segment 8 virus, and one vector carried a green fluorescent protein message on segment 4 and a microRNA on segment 8 at once. The tuning step inverts the attenuation logic of this area. A nucleoprotein segment bearing miR-93 target sites, taken directly from Perez 2009, lets the host silencing machinery limit the vector itself, which cut small RNA output about fivefold, preserved target knockdown, and removed the cytotoxicity that left roughly fifty percent cell survival with the untargeted vector. Producing such a vector required a cell line complementing both hemagglutinin and nucleoprotein.

## How the work evolved

The sequence is capability, then animal, then engineered control. Varble 2010 is cell culture and eggs only, with no animal infection and no test of insert retention in vivo. Langlois 2012 in Molecular Therapy supplies the animal work and the quantification, and Schmid 2014 supplies replication incompetence and dose control. The record for Varble 2010 marks that arc as synthesis visible across papers rather than a claim made by any one of them.

The theme has a clear boundary. Schmid 2014 shows delivery in the animal and says explicitly that in vivo silencing will require future studies, so no paper here demonstrates target knockdown in a tissue from the replication-incompetent vector. Langlois 2012 in Molecular Therapy measures function in vivo only as reduced induction of one transcript in whole lung, which contains uninfected cells, and its tissue distribution data come from animals lacking type I interferon signalling. Only one microRNA locus was tested, murine miR-124-2, and the therapeutic framing in all three discussions is extrapolation. Langlois 2012 in Molecular Therapy frames the vectors as suited to acute phenotypes lasting less than about a week, which is an honest statement of what a non-integrating RNA virus can offer.

This is where the theme hands off rather than continuing. The discussion of Langlois 2012 in Molecular Therapy contains the explicit proposal that a virus could deliver a library of artificial microRNAs only to infected cells so that selection identifies host restriction factors, and that proposal is what Varble 2013 implements. The delivery line as a therapeutic programme does not continue in this corpus. The screening line does.

## Supporting publications

All three are lab-led. Varble 2010 includes the García-Sastre group as coauthors and Langlois 2012 in Molecular Therapy draws its Sindbis vector from the laboratory's own earlier noncanonical processing work with Shapiro.

## Connections

The reciprocal use of miR-93 target sites to restrict rather than deliver comes from Perez 2009 in the microrna-mediated-viral-attenuation theme. The star strand and cytoplasmic processing questions belong to the noncanonical-microrna-biogenesis theme in the small-rna-antiviral-defense area, which is where Varble 2010 and Langlois 2012 in Molecular Therapy are also assigned. The screening platform these papers make possible is the in-vivo-screening-through-fitness theme.

## Publications referenced
- 2012-langlois-in-vivo-delivery-of-cytoplasmic-rn
- 2014-schmid-a-versatile-rna-vector-for-deliver
- 2010-varble-engineered-rna-viral-synthesis-of-
- 2009-perez-microrna-mediated-species-specific
- 2013-varble-an-in-vivo-rnai-screening-approach
