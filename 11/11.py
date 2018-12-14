import numpy as np
serial = 9435 # Int

def hundreds(num):
    string = str(num)
    if len(string) < 3:
        return 0
    else:
        return int(string[-3])

powerans = np.zeros((300,300),dtype=int)

# First generate the power answers for the whole matrix
for x in range(1,301):
    rackid = x + 10
    for y in range(1,301):
        power = hundreds((rackid*y + 94325)*rackid) - 5
        powerans[x-1,y-1] = power

# Now sweep through for 3x3s
maxima = [ [[0,0],0] ] # [ [x,y],power ]

for x in range(1,298):
    for y in range(1,298):
        powersum = np.sum(powerans[x:x+3,y:y+3])
        if powersum > maxima[0][1]:
            maxima = [ [[x,y], powersum] ]
        elif powersum == maxima[0][1]:
            maxima.append([[x,y], powersum])

print(maxima)
