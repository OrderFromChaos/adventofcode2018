
#################################################################
# This needs to be optimized with something like a binary tree. #
#################################################################

with open('3.txt','r') as f:
    data = f.readlines()

# Probably the easiest way is to just loop and check to see if each pixel is inside a box region

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

# Now convert this to [xbound, ybound]
bounddata = [[ [x[0][0], x[0][0]+x[1][0]], [x[0][1], x[0][1]+x[1][1]] ] for x in boxdata]
print(boxdata[:5])
print(bounddata[:5])

print(max([x[0][1] for x in bounddata]), max([x[1][1] for x in bounddata]))
twobounded = 0
for x in range(1001):
    for y in range(1001):
        condcount = 0
        for cond in bounddata:
            if x >= cond[0][0] and x <= cond[0][1] and y >= cond[1][0] and y <= cond[1][1]:
                condcount += 1
                if condcount == 2:
                    twobounded += 1
                    break

print(twobounded)
