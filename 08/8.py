import sys
from time import sleep
sys.setrecursionlimit(1000)

with open('8.txt','r') as f:
    dataset = f.read()[:-1].split(' ') # Remove final newline

# dataset = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ') # Testing purposes

### General process:
# v Header <----------
# v Child n times    ^
# v Metadata n times |
# ------------------>|

class node:
    def __init__(self, header, children = [], metadata = []):
        self.header = header
        self.children = children
        self.metadata = metadata
    def __repr__(self):
        return str((self.header, self.children, self.metadata))

# Have to work forward because not clear where last node starts

def readnode(posn):
    header = [int(dataset[posn]), int(dataset[posn+1])]
    posn += 2 # So now it's pointing at the first child
    currnode = node(header)

    localchildren = []
    for children in range(currnode.header[0]):
        child_node, posn = readnode(posn)
        localchildren.append(child_node)
    currnode.children = localchildren

    # Posn should now be correctly updated to end position past child
    localmetadata = []
    for metadata in range(currnode.header[1]):
        localmetadata.append(int(dataset[posn]))
        posn += 1
    currnode.metadata = localmetadata
    # Since posn updates after the metadata append step, posn should now be (last metadata index + 1)
    return currnode, posn

# Create graph representation
posn = 0
nodes = []
while posn < len(dataset)-1:
    currnode, endposn = readnode(posn)
    nodes.append(currnode)
    posn = endposn

# Now define how to sum together all the metadata
def countMetadata(graph):
    ans = 0
    for currnode in graph:
        ans += sum(currnode.metadata)
        ans += countMetadata(currnode.children)
    return ans

# Now define how to do the second check (metadata = child indices)
def countMetaChildren(root):
    ans = 0
    if root.children: # There exist children
        for index in root.metadata:
            if index != 0:
                try:
                    child = root.children[index-1] # They start with one-based indexing
                    ans += countMetaChildren(child)
                except IndexError:
                    pass
    else:
        ans += sum(root.metadata)
    return ans

print(nodes)
print('check 1:',countMetadata(nodes))
print('check 2:',countMetaChildren(nodes[0]))
