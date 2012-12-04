import sys

s = sys.stdin.read().splitlines()

sub = s[1]
s = s[0]

i = 0
locs = []
while True:
	i = s.find(sub, i)
	if i == -1:
		break
	i += 1
	locs.append(str(i))

print(" ".join(locs))