def addMarble(marbles, marbleno, length, index):
    score = 0
    marbleno += 1
    if marbleno % 23 == 0:
#         print(marbles)
        score += marbleno
        print(index)
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
    if score > endscore + 1000:
        break
print(playerscore)
print(max(playerscore))

#    print(marbles,index,score)
