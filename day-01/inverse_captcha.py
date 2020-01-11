import sys

input_file = 'day-01/input.txt'

def sum_matches(input, lookahead):
  return sum(int(input[i])
    for i in range(len(input))
    if input[i] == input[(i + lookahead) % len(input)])

def sum_matches_with_zip(input, lookahead):
  return sum(int(a) for a, b in zip(input, input[lookahead:] + input[:lookahead]) if a == b)

def part1(input):
 return sum_matches(input, 1)

def part2(input):
  half_length = len(input) // 2
  return sum_matches(input, half_length)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
