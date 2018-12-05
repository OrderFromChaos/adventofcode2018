import string
import re
import time

start = time.time()

with open('5.txt','r') as f:
    poly = f.readlines()[0][:-1] # Remove newline

negpol = set(string.ascii_lowercase)
pospol = set(string.ascii_uppercase)

class DoubleNode:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleList:
    head = None
    tail = None

    def append(self, value):
        if self.head is None: # If it's just one
            self.head = self.tail = DoubleNode(value, None, None)
        else: # If there's more than one
            new_node = DoubleNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node

# NOTE: THERE IS A DELETION CASE WITH THE FIRST TWO CHARS. SO BE CAREFUL.

# The solution from part A may be used to do part B.

sizes = dict()
def reactPoly(subpoly):
    d = DoubleList()
    for letter in subpoly:
        d.append(letter)
    newpoly = [d.head.value]

    curr = d.head.next
    while curr is not None:
        newpoly.append(curr.value)
        if curr.prev.value.lower() == curr.value.lower() and ((curr.prev.value in negpol and curr.value in pospol) or (curr.prev.value in pospol and curr.value in negpol)):
            newpoly.pop()
            newpoly.pop()
            if curr.next is None:
                curr.prev.prev.next = None
                newpoly.append(curr.prev.prev.value)
                curr = curr.prev.prev
            elif curr.prev.prev is None:
                curr.next.prev = None
                newpoly.append(curr.next.value)
                curr = curr.next
            else:
                curr.prev.prev.next = curr.next
                curr.next.prev = curr.prev.prev
                curr = curr.prev.prev
        curr = curr.next
    return ''.join(newpoly)

basereact = reactPoly(poly)

for upper, lower in zip(string.ascii_uppercase,string.ascii_lowercase):
    subpoly = re.sub('[' + upper + lower + ']','', basereact)
    newpoly = reactPoly(subpoly)
    sizes[upper] = len(newpoly)

for key in sizes:
    print(key, sizes[key])

print(time.time()-start)
