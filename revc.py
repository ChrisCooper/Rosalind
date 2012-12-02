comp = {'A':'T',
        'C':'G',
        'G':'C',
        'T':'A'}

with open('rosalind_revc.txt', 'r') as in_f, open('output.txt', 'w') as out_f:
    s = in_f.readline().strip()
    new_s = ""
    for i in range(len(s)):
        new_s = comp[s[i]] + new_s

    out_f.write(new_s)