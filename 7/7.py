import string
from operator import attrgetter

with open('7.txt','r') as f:
    dataset = f.readlines()
first = dataset[0].index('must') - 2
second = dataset[0].index('can') - 2
dataset = [[x[first],x[second]] for x in dataset]

uppers = string.ascii_uppercase
depend = {letter:[] for letter in uppers}
for rel in dataset:
    depend[rel[1]] += rel[0]

class node:
    def __init__(self,value=None,parents=[],children=[]):
        self.value = value
        self.parents = parents
        self.children = children
    def __repr__(self):
        return 'node(value=' + str(self.value) + ', parents=' + str(self.parents) + ', children=' + str(self.children) + ')'

class dagmod: # Directed acyclic graph
    # Collection of nodes

    heads = []
    nodes = {letter:node(value=letter) for letter in string.ascii_uppercase}

    def initfromdepend(self, depend):
        for d in depend:
            self.nodes[d].parents = depend[d]

        # Now initialize children based on parents
        for letter in self.nodes: # These are keys for nodes
            par = self.nodes[letter].parents # Look up the current node's parents
            for daddy in par: # Then for each parent, add the current letter to that parent's children
                parnode = self.nodes[daddy]
                # You have to be kinda careful here; with {a: obj}, you cannot safely edit obj by itself. You have to create a new obj
                self.nodes[daddy] = node(parnode.value, parnode.parents, parnode.children + [letter])

        for letter in self.nodes: # Do any of them even have no children? (nope and some reference themselves...)
            if self.nodes[letter].children == []:
                print(letter, self.nodes[letter])

        # Find the nodes at the top of the list
        for letter in self.nodes:
            if self.nodes[letter].parents == []:
                self.heads.append(self.nodes[letter])

graph = dagmod()
graph.initfromdepend(depend)

traversal = graph.heads
instructions = ""
while traversal != []:
    print(len(traversal))
    # Can't do this in waves; need to update travsort with every new node removal
    travsort = sorted(traversal, key = lambda x: x.value)
    graphnode = travsort[0]
    instructions += graphnode.value
    traversal.remove(graphnode)
    traversal += [graph.nodes[x] for x in graphnode.children] # Just [] if there are no children. hence the base condition is satisfied
print(instructions)
