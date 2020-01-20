import re

input_file = 'day-09/input.txt'

def process_input(input, remove_garbage = True):
   # Chars after ! are ignored
  input = re.sub('!.', '', input)

  # chars with < > are garbage
  if remove_garbage:
    input = re.sub('<.*?>', '', input)
  return input

def part1(input):
  input = process_input(input)

  depth = total = 0
  for char in input:
    if char == '{':
      depth += 1
      total += depth
    elif char == '}':
      depth -= 1

  return total

def part2(input):
  input = process_input(input, False)
  garbage = re.findall( r'<(.*?)>', input)
  return sum(len(match) for match in garbage)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
