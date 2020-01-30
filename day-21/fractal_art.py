from collections import Counter
import numpy

input_file = 'day-21/input.txt'

#Heavily based on https://www.reddit.com/r/adventofcode/comments/7l78eb/2017_day_21_solutions/drk8j2m/
def transform_rules(input, output):
  rules = []
  for k in [0, 1, 2, 3]:
      rot = numpy.rot90(input, k=k)
      rules.append((rot, output))
      rules.append((numpy.fliplr(rot), output))
      rules.append((numpy.flipud(rot), output))
  return rules

def transform(state, rules):
  for (key, val) in rules:
    if numpy.alltrue(state == key):
      return val

def iterate(state, rules):
  size = 3
  if len(state) % 2 == 0:
    size = 2
  
  out = size + 1
  #split into 2x2 squares
  split_no = len(state) // size
  new_grid = numpy.empty([out*split_no, out*split_no], dtype=object)
  for row in range(split_no):
    for col in range(split_no):
      split = state[size*row:size*row + size, size*col:size*col + size]
      new_grid[out*row:out*row + out, out*col:out*col + out] = transform(split, rules[size])
  return new_grid

def part1(input, iterations=5):
  state = numpy.array([list(line) for line in ['.#.','..#','###']])

  two_rules = []
  three_rules = []
  for line in input.splitlines():
    in_string, out_string = line.split(' => ')
    input = numpy.array([list(split) for split in in_string.split('/')])
    output = numpy.array([list(split) for split in out_string.split('/')])
    if len(input) == 3:
      three_rules.extend(transform_rules(input, output))
    elif len(input) == 2:
      two_rules.extend(transform_rules(input, output))
  rules = {2:two_rules, 3:three_rules}

  for i in range(iterations):
    print('iteration',i)
    state = iterate(state, rules)

  return Counter(''.join(state.flatten()))['#']

#TODO - optimise
def part2(input):
  return part1(input, 18)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))