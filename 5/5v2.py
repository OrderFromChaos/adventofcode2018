import string

with open('5.txt','r') as f:
    poly = f.readlines()[0][:-1] # Remove newline

print(len(poly))

negpol = set(string.ascii_lowercase)
pospol = set(string.ascii_uppercase)

loc = 1
while loc < len(poly)-1:
    # Read forward
    loc += 1
    if (poly[loc-1] in negpol and poly[loc] in pospol) or (poly[loc-1] in pospol and poly[loc] in negpol):
        poly = poly[:loc-1] + poly[loc+1:]
        loc -= 2

print(len(poly))
