import sys

def gc_content(s):
	return len(filter(lambda c: c in "CG", s)) * 100.0 / len(s)

dna = {}
current = ""

for line in sys.stdin.read().splitlines():
	if line[0] == ">":
		current = line[1:]
		dna[current] = ""
	else:
		dna[current] += line.strip()

top = max(dna, key=lambda k: gc_content(dna[k]))

print(top)
print("%0.3f%%" % gc_content(dna[top]))