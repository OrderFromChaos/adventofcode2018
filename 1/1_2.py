from itertools import cycle

with open('1.txt','r') as f:
    data = [int(x) for x in f.readlines()]

history = {0}
curr = 0
for num in cycle(data): # Repeat until you find a repeat
    curr += num
    if curr in history:
        print(curr)
        break
    else:
        history.add(curr)
