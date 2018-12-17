raw = '''initial state: #..#.#..##......###...###
...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
'''

# Data parsing
raw = raw.split('\n')

growbed = raw[0].split(' ')[2]
rules = {x.split(' => ')[0]:'#' for x in raw[1:]}


# Growing
for generation in range(20):
    # Extension condition
    end = len(growbed)-1
    for i in range(0,5):
        if growbed[end-i] == '#':
            break
    else: # Only runs if no break operation
        i = 0 # This ensures that the number of things to add to the end is correct
    if i > 0:
        growbed += ['.']*i

    # Actual growing
    for plant in growbed:
    
