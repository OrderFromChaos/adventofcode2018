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
def f(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    else:
        return 2

vf = np.vectorize(f)

for box in boxdata:
    vals = arr[box[0][0]:box[0][0]+box[1][0], box[0][1]:box[0][1]+box[1][1]]
    arr[box[0][0]:box[0][0]+box[1][0], box[0][1]:box[0][1]+box[1][1]] = vf(vals)

# Now count the number of twos in the numpy array
print(np.count_nonzero(arr == 2))
