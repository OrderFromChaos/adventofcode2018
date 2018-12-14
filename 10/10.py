import re
from ggplot import *
import numpy as np

#position=< 21518, -21209> velocity=<-2,  2>
#position=< 10842,  21423> velocity=<-1, -2>
#position=< 32189, -21209> velocity=<-3,  2>
#position=<-21158, -21218> velocity=< 2,  2>
#position=<-31794, -53194> velocity=< 3,  5>
#position=<-42469,  42743> velocity=< 4, -4>
#position=<-53120, -31873> velocity=< 5,  3>

with open('10.txt','r') as f:
    dataset = f.readlines()

data = np.zeros((len(dataset),4),dtype=int)

for index, line in enumerate(dataset):
    data[index] = np.array([int(x) for x in re.compile('[0-9\-]+').findall(line)]) # Strip to nums
print(data[:5])
