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

class cart:
    def __init__(self, x, y, heading, state):
        self.x = x
        self.y = y
        self.heading = heading
        self.state = state
    def heading(self):
        # Gets the vector of heading instead of just the <^>v notation
        


def left(heading):
    left = '<^>v'
    if heading in {'^','>','v'}:
        return left[left.index(heading)-1]
    elif heading == '<':
        return 'v'
    else:
        raise Exception('Failed to find cart heading in list of accepted headings!',heading)
def right(heading):
    left = '<^>v'
    if heading in {'<','^','>'}:
        return left[left.index(heading)+1]
    elif heading == 'v':
        return '<'
    else:
        raise Exception('Failed to find cart heading in list of accepted headings!',heading)

actions = cycle([
left,
straight,
right
])



# Identify all carts and get background
for Lindex, line in enumerate(dataset):
    for Cindex, char in enumerate(line):
        if char == '>' or char == '<':
            background[Lindex,Cindex] = '-'
            carts.append([Lindex,Cindex,lookup[char],cycle(actions)])
        elif char == '^' or char == 'v':
            background[Lindex,Cindex] = '|'
            carts.append([Lindex,Cindex,lookup[char],cycle(actions)])
        else:
            background[Lindex,Cindex] = char

# Simulate forward until a crash

print(carts)

# Single pass first to check if it's working
carts = sorted(carts, key=lambda x: (x[1],x[0]))
positions = set([(x[0],x[1]) for x in carts])
print(positions)
for cart in carts:
    on = background[cart[0],cart[1]]
    # Special cases: +, \, /. The rest are just += heading
    if on == '+':
        cart[2] = cart[3].__next__()
    elif on == '/':
        # I should have written this in a much more natural form. Maybe class-based for carts?
