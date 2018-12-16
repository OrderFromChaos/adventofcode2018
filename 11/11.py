import numpy as np
serial = 9435 # Input number

def hundreds(num):
    string = str(num)
    if len(string) < 3:
        return 0
    else:
        return int(string[-3])

powerans = np.zeros((300,300),dtype=int)

# First generate the power answers for the whole matrix
for x in range(1,301): # Row
    rackid = x + 10
    for y in range(1,301): # Column
        power = hundreds((rackid*y + serial)*rackid) - 5
        powerans[x-1,y-1] = power


# Now sweep through for NxNs
maxima = [ [[0,0],0] ] # [ [x,y],power ]
for boxsize in range(1,301):
    for x in range(1,301-boxsize):
        for y in range(1,301-boxsize):
            powersum = np.sum(powerans[x:x+boxsize,y:y+boxsize])
            if powersum > maxima[0][1]:
                maxima = [ [[x,y], powersum, boxsize] ]
            elif powersum == maxima[0][1]:
                maxima.append([[x,y], powersum,boxsize])

print(maxima)
print('Format: [x,y], powersum, boxsize')
print('Note this starts at index 1, so add 1 to x and y')
