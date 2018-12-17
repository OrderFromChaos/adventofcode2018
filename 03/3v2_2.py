import numpy as np

with open('3.txt','r') as f:
    data = f.readlines()

# First parse the file into something useable
# #1 @ 1,3: 4x4
boxdata = [x[x.index('@')+2:-1].split(':') for x in data]
boxdata = [[x[0].split(','),x[1].strip().split('x')] for x in boxdata]
# [ [[1,3],[4,4]], ...
def deepIntConv(L):
    if type(L) == str:
        return int(L)
    else: # A list
        return [deepIntConv(x) for x in L]
boxdata = deepIntConv(boxdata)

# Then draw on a numpy array
arr = np.zeros((1000,1000))
def f(x,boxno):
    if x == 0:
        return boxno
    else: # Some intersect
        return -1

vf = np.vectorize(f)

for boxno, box in enumerate(boxdata):
    vals = arr[box[0][0]:box[0][0]+box[1][0], box[0][1]:box[0][1]+box[1][1]]
    arr[box[0][0]:box[0][0]+box[1][0], box[0][1]:box[0][1]+box[1][1]] = vf(vals, boxno+1)

# Compute expectation values from boxdata, then compare to actual counts
expectations = {boxno+1: box[1][0]*box[1][1] for boxno, box in enumerate(boxdata)}

unique, counts = np.unique(arr, return_counts=True)
actual = dict(zip(unique, counts))

for boxno in expectations:
    try:
        if expectations[boxno] == actual[boxno]:
            print('Found it!',boxno)
    except KeyError:
        pass
