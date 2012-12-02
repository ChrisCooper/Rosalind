with open('rosalind_rna.txt', 'r') as f:
    for line in f:
        print(line.replace("T", "U"))