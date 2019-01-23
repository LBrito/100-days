def to_rna(dna_strand):
    nucleotides = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(nucleotides[dna_strand[i]] for i in range(0, len(dna_strand)))
