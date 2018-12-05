import string

with open('5.txt','r') as f:
    poly = f.readlines()[0][:-1] # Remove newline

negpol = set(string.ascii_lowercase)
pospol = set(string.ascii_uppercase)

while True:
    norxn = True
    newpoly = str()
    for previous, curr in zip(poly,poly[1:]):
        # Note that this will stop one before the end,
        # So a special condition must account for that
        if (previous in negpol and curr in pospol) or (previous in pospol and curr in negpol):
            norxn = False
        else:
            newpoly.append(previous
