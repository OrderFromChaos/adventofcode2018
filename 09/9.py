### Taken from problem 5. Will use in a circular fashion
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


# Any time that head points at tail will cause an infinite regress, so we'll use lists, L.insert(i,x), and % instead
#marbles = DoubleList()
#marbles.append(0)
#marbles.append(1)
#marbles.tail.next = marbles.head # Tail is currently pointing at a head with .prev=None
#marbles.head.prev = marbles.tail # Head is pointing at a tail with a head of .prev=None
#marbles.tail.next = None # I think this causes infinite regress...

def addMarble(marbles, marbleno, length, index):
    score = 0
    marbleno += 1
    if marbleno % 23 == 0:
        print(marbles)
        score += marbleno
        index -= 7
        score += marbles.pop(index)
        length -= 1
    else:
        index = index + 2
        if index > length: # We want it to insert at the end, but not try to insert past that
            index = index % length
        marbles.insert(index,marbleno)
        length += 1
    return marbles, marbleno, length, index, score

# Initializing variables
marbles = [0,1]
marbleno = 1
length = 2
index = 1
score = 0

# Game state variables
players = 10
playerscore = [0]*players
endscore = 1618
currentplayer = 0

while score != endscore:
    marbles, marbleno, length, index, score = addMarble(marbles, marbleno, length, index)
    # Now who does the score get assigned to?
    if score != 0:
        #print(score)
        playerscore[currentplayer] += score
    currentplayer += 1
    if currentplayer == 10:
        currentplayer = 0
print(playerscore)
print(max(playerscore))

#for i in range(25):
#    marbles, marbleno, length, index, score = addMarble(marbles,marbleno,length,index)
#    print(marbles,index,score)
