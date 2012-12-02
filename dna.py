freq = {}
for c in "ACGT":
    freq[c] = 0

with open('rosalind_dna.txt', 'r') as f:
    for line in f:
        for c in line:
            freq[c] += 1

print(" ".join([str(freq[c]) for c in "ACGT"]))