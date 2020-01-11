import itertools 

input_file = 'day-02/input.txt'

def part1(input):
  lines = [[int(value) for value in line.split()] for line in input.splitlines()]
  return sum(max(line) - min(line) for line in lines)

def part2(input):
  lines = [[int(value) for value in line.split()] for line in input.splitlines()]
  return sum(a // b for line in lines for a,b in itertools.combinations(sorted(line, reverse = True), 2) if a % b == 0)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
