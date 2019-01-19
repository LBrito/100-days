def proteins(strand):
    proteins = []
    for codon in split_into_codons(strand):
        protein = to_protein(codon)
        if protein == "STOP":
            return proteins
        else:
            proteins.append(protein)
    return proteins


def split_into_codons(strand):
    return [strand[i: i + 3] for i in range(0, len(strand), 3)]


def to_protein(codon):
    return get_protein({
        "AUG": 0,
        "UUU": 1, "UUC": 1,
        "UUA": 2, "UUG": 2,
        "UCU": 3, "UCC": 3, "UCA": 3, "UCG": 3,
        "UAU": 4, "UAC": 4,
        "UGU": 5, "UGC": 5,
        "UGG": 6,
        "UAA": 7, "UAG": 7, "UGA": 7
    }.get(codon))


def get_protein(index):
    return ["Methionine",
            "Phenylalanine",
            "Leucine",
            "Serine",
            "Tyrosine",
            "Cysteine",
            "Tryptophan",
            "STOP"][index]

