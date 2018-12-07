import string

with open('7.txt','r') as f:
    dataset = f.readlines()
first = dataset[0].index('must') - 2
second = dataset[0].index('can') - 2
dataset = [[x[first],x[second]] for x in dataset]

uppers = string.ascii_uppercase
depend = {letter:[] for letter in uppers}
for rel in dataset:
    depend[rel[1]] += rel[0]

print(depend)

maxlayer = max([len(depend[key]) for key in depend])
layers = {i:[key for key in depend if len(depend[key]) == i] for i in range(maxlayer)}
instructions = ''
for layer in layers:
    instructions += ''.join(sorted(layers[layer]))
print(instructions)

# This is less trivial than I thought it was, so time to do a proper, non-jank implementation of a DAG

class node:
    def __init__(self,parents=[],children=[]):
        self.parents = parents
        self.children = children
    def __repr__(self):
        return 'node(parents=' + str(self.parents) + ', children=' + str(self.children) + ')'

class dagmod: # Directed acyclic graph
    # Collection of nodes

    head = None
    nodes = {letter:node() for letter in string.ascii_uppercase}

    def initfromdepend(self, depend):
        for d in depend:
            self.nodes[d].parents = depend[d]
        # Now figure out whom is a child of who
        for letter in self.nodes:
            par = self.nodes[letter].parents
            for daddy in par:
                self.nodes[daddy].children += letter

#        for letter in self.nodes:
#            print(letter, self.nodes[letter])

        for letter in self.nodes:
            if self.nodes[letter].parents == None:
                self.head = self.nodes[letter]

graph = dagmod()
graph.initfromdepend(depend)

start = graph.head
print(start)
#while there_are_children:
#    pass
