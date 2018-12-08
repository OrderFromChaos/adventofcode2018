import sys
import requests

day = sys.argv[1]
url = 'https://adventofcode.com/2018/day/' + day + '/input'

cookie = {'session':''}
r = requests.post(url,cookies=cookie)
text = r.content.decode('utf-8').split('\n')
tail = [x for x in text if x] # Remove any empty stuff, like at the end
with open('./' + day + '.txt','w') as f:
    for line in tail:
        f.write(line + '\n')
