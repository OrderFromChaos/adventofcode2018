from scipy.spatial import ConvexHull
from scipy.spatial.distance import cityblock # :)
import numpy as np

# Taking a guess here. I think if I exclude points that compose the
# convex hull of this vector cluster, then I will have excluded all infinite-
# regioned points.

dataset = np.loadtxt('6.txt',delimiter=', ', dtype=int)
hull = ConvexHull(dataset)
nonhull = np.array([x for x in range(len(dataset)) if x not in hull.vertices])
# I'm going to wait to use this until later (picking out solutions in the middle)

print(nonhull)

print(dataset)
print(len(dataset))

manhattan = np.zeros((400,400), dtype=int) # Same size as last attempt

for x in range(400):
    if x % 20 == 0:
        print('on x',x)
    for y in range(400):
        distances = {ind:cityblock(np.array([x,y]),vect) for ind, vect in enumerate(dataset)}
        smallest = min(distances.items(), key=lambda x: x[1])
        manhattan[x,y] = smallest[0]

freq = np.unique(manhattan, return_counts = True)
print(freq)
highest = 0
highind = 0
for i,x in enumerate(freq[1]):
    if i in nonhull and x > highest:
        highest = x
        highind = i
print(highest,highind)
