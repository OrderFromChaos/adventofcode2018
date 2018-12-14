# First pass: identify all carts
# Second pass: get background.
import numpy as np
from itertools import cycle # Easy way to deal with intersections

with open('13.txt','r') as f:
    dataset = [x[:-1] for x in f.readlines()]

background = np.zeros((len(dataset),len(dataset[0])),dtype=str)
carts = [] # [x,y,heading,state]
lookup = {'^': 0, # Clockwise order starting at north
          '>': 1,
          'v': 2,
          '<': 3}

# Identify all carts and get background
for Lindex, line in enumerate(dataset):
    for Cindex, char in enumerate(line):
        if char == '>' or char == '<':
            background[Lindex,Cindex] = '-'
            carts.append([Lindex,Cindex,lookup[char]])
        elif char == '^' or char == 'v':
            background[Lindex,Cindex] = '|'
            carts.append([Lindex,Cindex,lookup[char],0])
        else:
            background[Lindex,Cindex] = char

# Simulate forward until a crash

print(carts)

# Single pass first to check if it's working
carts = sorted(carts, key=lambda x: (x[1],x[0]))
positions = set([(x[0],x[1]) for x in carts])
print(positions)
for cart in carts:
    action = background[cart[0],cart[1]]
    # Special cases: +, \, /. The rest are just += heading
    if action == '+':
        if state 
