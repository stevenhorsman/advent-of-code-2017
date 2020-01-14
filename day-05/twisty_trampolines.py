import sys

input_file = 'day-05/input.txt'

#TODO - consider pypy intepreter?

def get_steps(input, part2 = False):
  instructions = [int(line) for line in input.splitlines()]
  ip = steps = 0
  while 0 <= ip < len(instructions):
    curr_val = instructions[ip]
    if part2 and curr_val  >= 3:
      instructions[ip] -= 1
    else:
      instructions[ip] += 1
    ip += curr_val
    steps += 1
  return steps

def part1(input):
  return get_steps(input)

def part2(input):
  return get_steps(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
