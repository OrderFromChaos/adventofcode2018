with open('8.txt','r') as f:
    dataset = f.read()[:-1].split(' ') # Remove newline

class node:
    def __init__(self, nodeno, header, children = None, metadata = []):
        self.header = header
        self.children = children
        self.metadata = metadata
    def __repr__(self):
        return str((self.header, self.children, self.metadata))

# Have to work forward because not clear where last node starts

def readnode(posn):
    header = [int(dataset[posn]),int(dataset[posn+1])]

    if header[0] > 0: # If there are children
        nth = readnode(posn+2)
        children = [nth[0]]
        for x in range(header[0]-1): # n child
            nth = readnode(posn + 2 + nth[1])
            children += nth[0]
    else:
        nth = [0, 0]
        children = []

    metadata = dataset[nth[1] + 1: nth[1] + 1 + header[1]]
    currnode = node(header, children, metadata)
    endposn = nth[1] + header[1]
    return currnode, endposn

posn = 0
nodes = []
while posn < len(dataset)-1:
    currnode, posn = readnode(posn)
    nodes.append(currnode)
print(nodes)
