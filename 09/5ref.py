import string
import time

start = time.time()

with open('5.txt','r') as f:
    poly = f.readlines()[0][:-1] # Remove newline

# here pol = "polarity" ie whether something is upper or lowercase
negpol = set(string.ascii_lowercase)
pospol = set(string.ascii_uppercase)


# The easiest way to do a loop and have the head move around repeatedly is a doubly-linked list.
# In this data structure, each data point has a reference to the point before it and the point after it.
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

# First, create the doubly-linked list.
d = DoubleList()
for letter in poly:
    d.append(letter)

# Then, store accepted values (non-reacted) in a new list,
# which we'll later check the length of.
newpoly = [d.head.value]

curr = d.head.next
while curr is not None:
    newpoly.append(curr.value)
    # Letters must match type (first condition) and have opposite polarity to be reacted.
    if curr.prev.value.lower() == curr.value.lower() and ((curr.prev.value in negpol and curr.value in pospol) or (curr.prev.value in pospol and curr.value in negpol)):
        newpoly.pop()
        newpoly.pop()
        if curr.next is None: # We're at the tail of the doubly-linked list
            curr.prev.prev.next = None
            newpoly.append(curr.prev.prev.value)
            curr = curr.prev.prev
        elif curr.prev.prev is None: # We're at the head of the doubly-linked list
            curr.next.prev = None
            newpoly.append(curr.next.value)
            curr = curr.next
        else: # We're somewhere in the middle
            curr.prev.prev.next = curr.next
            curr.next.prev = curr.prev.prev
            curr = curr.prev.prev
    curr = curr.next
print(len(newpoly))
print('Runtime:',time.time()-start)
