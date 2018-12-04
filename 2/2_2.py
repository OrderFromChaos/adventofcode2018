with open('2.txt','r') as f:
    data = f.readlines()

correct = []
for i, key in enumerate(data[:-1]):
    for match in data[i+1:]:
        diff = len(key) - sum([x == y for x,y in zip(key,match)])
        if diff == 1:
            correct.append(''.join([x for x,y in zip(key,match) if x==y]))
print(correct)
