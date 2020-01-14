import itertools
from collections import Counter

input_file = 'day-06/input.txt'

def find_repeat(input, get_cycle_length = False):
  banks = [int(block) for block in input.split()]
  seen = {}
  steps = 0
  while tuple(banks) not in seen:
    seen[tuple(banks)] = steps
    # Find biggest bank
    # i, m = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
    max_value = max(banks)
    index = banks.index(max_value)
    banks[index] = 0

    # Distribute amongst others
    # Smarter, but less efficient
    # counter = Counter(itertools.islice(itertools.cycle(range(len(banks))), index + 1, index + max_value + 1))
    # for counts in counter.items():
    #   banks[counts[0]] += counts[1]
    for _ in range(0, max_value):
      index = (index + 1) % len(banks)
      banks[index] += 1
    steps += 1
  if get_cycle_length:
    steps -= seen[tuple(banks)]
  return steps

def part1(input):
  return find_repeat(input)

def part2(input):
  return find_repeat(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
