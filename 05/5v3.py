import string
import sys

with open('5.txt','r') as f:
    poly = f.readlines()[0][:-1] # Remove newline

negpol = set(string.ascii_lowercase)
pospol = set(string.ascii_uppercase)

poly = list(poly)

while True:
    print(len(poly))
    sys.stdout.flush()
    deletion_indices = []
    for ind, curr in enumerate(poly[1:]):
        if (poly[ind] in negpol and curr in pospol) or (poly[ind] in pospol and curr in negpol):
            deletion_indices.append(ind)
            deletion_indices.append(ind+1)
    if deletion_indices == []:
        print(len(poly))
        break
    loc = 0
    while loc < len(deletion_indices)-1:
        del poly[deletion_indices[loc]]
        deletion_indices = [x-1 for x in deletion_indices]
        loc += 1
