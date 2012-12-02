with open('rosalind_hamm.txt', 'r') as f:
    combo = zip(f.readline().strip(), f.readline().strip())
    print(len(filter(lambda a: a[0] != a[1], combo)))