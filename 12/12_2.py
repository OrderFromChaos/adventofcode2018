import matplotlib.pyplot as plt

raw = '''initial state: ##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##..
##.## => #
....# => .
.#.#. => #
..### => .
##... => #
##### => .
###.# => #
.##.. => .
..##. => .
...## => #
####. => .
###.. => .
.#### => #
#...# => #
..... => .
..#.. => .
#..## => .
#.#.# => #
.#.## => #
.###. => .
##..# => .
.#... => #
.#..# => #
...#. => .
#.#.. => .
#.... => .
##.#. => .
#.### => .
.##.# => .
#..#. => #
..#.# => .
#.##. => #'''

# Data parsing
raw = raw.split('\n')

growbed = list(raw[0].split(' ')[2])
ruleraw = [x.split(' => ') for x in raw[1:]]
rules = {"".join(x[0]):"".join(x[1]) for x in ruleraw}
# Jank time: assume stuff mostly goes right and not much left. This is from getting expectations from r/adventofcode
growbed = list('...........') + growbed + list('...')
prepend = len('...........')


sums = []

# Growing
for generation in range(1000):
    if generation % 1000000000 == 0:
        print('billion!')
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
    newbed = [x for x in growbed]
    for index, plant in enumerate(growbed):
        try:
            lower = index-2
            if lower < 0:
                lower = index
            neighbors = growbed[lower:index+3]
#            print(neighbors)
            repl = rules["".join(neighbors)]
        except KeyError:
            repl = '.'
        newbed[index] = repl
    growbed = newbed

    start_index = -len('...........')
    ans = 0
    for index,pot in enumerate(growbed):
        if pot == '#':
            ans += start_index + index
    sums.append(ans)

for i in sums:
    print(i)

# Find the spot where the linearity starts
expectation = sums[-1]
for i,x in enumerate(sums[::-1]):
    if x != expectation:
        print('hey I found it!')
        print(i,x)
        break
    expectation -= 32


# FORMULA FOR N GENERATIONS: (N>=142)
# (N-142)*32+4945
