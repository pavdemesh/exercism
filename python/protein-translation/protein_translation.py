def proteins(strand):
    # Create a list to store decoded proteins
    proteins_list = []
    # Create and populate dictionary of codon to protein correlations and STOP codons
    codons_to_proteins ={"AUG": "Methionine",
                        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
                        "UUA": "Leucine", "UUG": "Leucine",
                        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
                        "UAU": "Tyrosine", "UAC": "Tyrosine",
                        "UGU": "Cysteine", "UGC": "Cysteine",
                        "UGG": "Tryptophan",
                        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}
    # Iterate over indices of "strand", increment index by 3, stop 2 indexes before end                    
    for i in range(0, len(strand) - 2, 3):
        # Concatenate codon from three chars
        codon = strand[i] + strand[i+1] + strand[i+2]
        # Check if codon == STOP, then stop iteration (break)
        if codons_to_proteins[codon] == "STOP":
            break
        # If codon was not STOP, assign corresponding value to protein
        protein = codons_to_proteins[codon]
        # Add protein to the list of proteins
        proteins_list.append(protein)
    # Return the list if proteins
    return proteins_list