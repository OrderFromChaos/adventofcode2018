from datetime import datetime, timedelta
from collections import Counter

with open('4.txt','r') as f:
    data = f.readlines()

# Data currently looks like this:
# [1518-07-27 00:04] falls asleep
# [1518-03-07 00:04] Guard #1823 begins shift
# (non-ordered)

parseTime = lambda x: datetime.strptime(x,'[%Y-%m-%d %H:%M]')
# the following fxn returns [guard no., action]
def parseAction(x):
    if x == 'falls asleep':
        return [None,1]
    elif x == 'wakes up':
        return [None,2]
    else: # Guard no. goes on duty
        return [int(x.split(' ')[1].strip('#')),0]

# Go through data list and get time and metadata (such as "falls asleep")
parsed = []
for guardinfo in data:
    guardinfo = guardinfo.strip() # Remove pesky \n's
    spliton = guardinfo.index(']')+1
    parsed.append([parseTime(guardinfo[:spliton]),parseAction(guardinfo[spliton+1:])])

for i in parsed[:10]:
    print(i)

parsed = sorted(parsed, key = lambda x: x[0])
# Now that the data is in order, collate guard info.
# Note that guard data is LIFO, so a stack is the natural answer.
# HOWEVER - Only one guard is on duty at a time.
guards = dict()
current = -1 # Presumption (which is correct) here is that the first event is going to be eventtag=0
sleeptime = []
for event in parsed:
    eventtag = event[1][1]
    if eventtag == 0: # Meaning a new guard
        if current != -1: # Whether or not to purge sleeptime
            try:
                guards[current] += sleeptime
            except KeyError:
                guards[current] = sleeptime
            sleeptime = []
        current = event[1][0]

    else: # Presumption: each sleep( is followed later by a )
        sleeptime.append(event[0])

for guard in guards:
    print(guard, guards[guard])

# I know this looks silly, but datetime was telling me that timedelta had no .minute or .minutes attribute...
timeAsleep = lambda x: sum([(z-y).total_seconds()//60  for y,z in zip(x[::2],x[1::2])])
maxtime = 0
bigsleeper = 0
for guard in guards:
    slept = timeAsleep(guards[guard])
    if slept > maxtime:
        maxtime = slept
        bigsleeper = guard
print(bigsleeper, maxtime)

largestmin = (0,0,0) # Guard, minute, and incidence
for guard in {x:guards[x] for x in guards if guards[x] != []}:
# for guard in {1823:guards[1823]}:
    sleepminutes = []
    for start, stop in zip(guards[guard][::2],guards[guard][1::2]):
        while start != stop:
            sleepminutes.append(start.minute)
            start += timedelta(minutes=1)
    freq_max = Counter(sleepminutes).most_common(1)[0]
    if freq_max[1] > largestmin[2]:
        largestmin = (guard,freq_max[0],freq_max[1])
        print(guard,largestmin)
print(largestmin)
