from collections import Counter

with open('2.txt','r') as f:
    data = f.readlines()
twos = 0
threes = 0
for i in data:
    freq = Counter(i)
    if any([freq[x] == 2 for x in freq]):
        twos += 1
    if any([freq[x] == 3 for x in freq]):
        threes += 1
print(twos*threes)
