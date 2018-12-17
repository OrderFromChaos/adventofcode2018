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

class node:
    def __init__(self,value=None,parents=set(),children=set()):
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
            self.nodes[d].parents = set(depend[d])

        # Now initialize children based on parents
        for letter in self.nodes: # These are keys for nodes
            par = self.nodes[letter].parents # Look up the current node's parents
            for daddy in par: # Then for each parent, add the current letter to that parent's children
                parnode = self.nodes[daddy]
                # You have to be kinda careful here; with {a: obj}, you cannot safely edit obj by itself. You have to create a new obj
                self.nodes[daddy] = node(parnode.value, parnode.parents, parnode.children.union(set(letter)))

#        for letter in self.nodes: # Do any of them even have no children? (nope and some reference themselves...)
#            if self.nodes[letter].children == []:
#                print(letter, self.nodes[letter])

        # Find the nodes at the top of the list
        for letter in self.nodes:
            if self.nodes[letter].parents == set():
                self.heads.append(self.nodes[letter])

graph = dagmod()
graph.initfromdepend(depend)
for letter in graph.nodes:
    print(letter, graph.nodes[letter])

traversal = graph.heads
instructions = ""
seen = set()
lastchosen = '0'
# Go through the graph. Start at the heads, then work in alphabetical order
while traversal != []:
    print(len(traversal),lastchosen) # Keep track of progress
#    for i in traversal:
#        print(i)
    # All prerequisites are covered
    available = [x for x in traversal if x.parents.issubset(seen)] # This syntax means all elts in x.parents are in seen as well
#    print('    ', [x.value for x in available])
    availsort = sorted(available, key=lambda x: x.value)
    bestnode = availsort[0] # Then set the next traversal to sort()[0]

    # Append the string value of bestnode to instructions
    instructions += bestnode.value
    lastchosen = bestnode.value
    seen.add(bestnode.value) # Now that the condition is satisfied, add it to the seen set()
    traversal.remove(bestnode) # No longer a need to traverse that node
    traversal += [graph.nodes[x] for x in bestnode.children if graph.nodes[x] not in traversal and x not in seen] # Add all nodes that aren't currently in the traversal list
print(instructions)
