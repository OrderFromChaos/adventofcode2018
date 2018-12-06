from scipy.spatial import ConvexHull
from scipy.spatial.distance import cityblock # :)
import numpy as np
from collections import Counter

np.set_printoptions(threshold = 50*50)

# Taking a guess here. I think if I exclude points that compose the
# convex hull of this vector cluster, then I will have excluded all infinite-
# regioned points.

dataset = np.loadtxt('6.txt',delimiter=', ', dtype=int)
hull = ConvexHull(dataset)
nonhull = np.array([x for x in range(len(dataset)) if x not in hull.vertices])
# I'm going to wait to use this until later (picking out solutions in the middle)

print(dataset)
print(len(dataset))

# I guess I'll just do this the straightforward way (manhattan over some large region)
# Or not, this has terrible complexity and I should have known right away
#manhattan = np.zeros((400,400)) # Larger than max extents of entire dataset
#for x in range(400):
#    for y in range(400):
#        # Compute manhattan on all points
#        distances = {ind:cityblock(np.array([x,y]),z) for ind,z in enumerate(dataset)}
#        manhattan[x,y] = min(distances, key=distances.get)
#
#print(manhattan)

# Next solution: voronoi-like
# Set a seed at each number start, then work out in a number of epochs.

#def region_to_search(pos, epoch): # Should only look at the current epoch rhombus edge
#    if epoch == 0:
#        return [pos]
#    else:
#        search = []
#        # Only return if inside the 400,400 bounds
#        north, south = [np.array(0,epoch),np.array(0,-epoch)]
#        search.append(north)
#        search.append(south)
#        # Create top right
#        # for i in range(epoch):
#        # So as it turns out, triangulation is a hard problem.
#        # Maybe there's an easier solution?
#
#suitable = [x+1 for x in range(dataset)] # Indices moved up by 1 because we start with 0s
#epoch = 0
#while suitable:
#    # As soon as a search region fails to return a number, remove that index from the suitable list
#    # Eventually all should fail to find something
#    failed = []
#    for seed in suitable:
#        found = False
#        search = region_to_search(dataset[seed-1], epoch)
#        for point in search:
#            if manhattan[point] == 0:
#                manhattan[point] = seed
#                found = True
#        if not found:
#            failed.append(seed)
#    for seedfail in failed:
#        suitable.remove(seedfail)
#    epoch += 1

manhattan = np.zeros((400,400), dtype=int) # Same size as last attempt

# Easier solution: create seeds, search for nearest neighbors, add in if they're zero
# Initial seed
for index, x in enumerate(dataset):
    manhattan[x[0],x[1]] = index + 1 # Want to reserve 0 for nothing currently there

# There's probably a way to define this with itertools, but it's small enough that it doesn't matter
sweeps = [[-1,0],  # Left edge
          [-1,-1],
          [-1,1],
          [0,1],   # Middle two points
          [0,-1],
          [1,0],   # Right edge
          [1,-1],
          [1,1]]
sweeps = [np.array(x) for x in sweeps] # So we have access to element-wise subtraction

# Oh boy, this is at least n**4 in the worst case.
# Good times...
# while 0 in np.unique(manhattan):

print(np.unique(manhattan, return_counts=True))

runno = 1
while 0 in np.unique(manhattan):
    print('Run',runno,'...')
    print('    Currrent number of zeroes',np.unique(manhattan, return_counts=True)[1][1])
    for x in range(400):
        for y in range(400):
            if manhattan[x,y] not in {-1,0}:
                challenger = manhattan[x,y] # Current beacon to take the spot
                curpos = np.array([x,y])
                # Start sweeping around for 0s to conquer
                for direction in sweeps:
                    newdir = curpos + direction
                    if 0 < newdir[0] < 400 and 0 < newdir[1] < 400 and manhattan[newdir[0], newdir[1]] == 0: # Is a valid index in the numpy array and is 0
                        # Now we have to check again to see if there's anything nearby. If there is, set to -1
                        # If not, set to the current number we're sweeping from (challenger).
                        for direction2 in sweeps:
                            newdir2 = newdir + direction2
                            if 0 < newdir2[0] < 400 and 0 < newdir2[1] < 400:
                                if manhattan[newdir2[0], newdir2[1]] not in {0,-1,challenger}:
                                    manhattan[newdir[0], newdir[1]] = -1
                                    break
                        else: # This is a Python thing...
                            manhattan[newdir[0], newdir[1]] = challenger
    runno += 1
freq = np.unique(manhattan, return_counts=True)
print(freq)
print(freq[1][nonhull])
