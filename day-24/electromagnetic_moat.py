import copy

input_file = 'day-24/input.txt'

def find_path(start, remaining):
  paths = []
  for comp in remaining:
    if start in comp:
      new_start = comp[0] if comp[1] == start else comp[1]
      new_rem = copy.copy(remaining)
      new_rem.remove(comp)
      path = comp + find_path(new_start, new_rem)
      paths.append(path)
  if len(paths) == 0:
    return []
  return max(paths, key=lambda path: sum(path))

def part1(input):
  components = [list(map(int,line.split('/'))) for line in input.splitlines()]
  return sum(find_path(0, components))

def find_path2(start, remaining):
  paths = []
  for comp in remaining:
    if start in comp:
      new_start = comp[0] if comp[1] == start else comp[1]
      new_rem = copy.copy(remaining)
      new_rem.remove(comp)
      path = comp + find_path2(new_start, new_rem)
      paths.append(path)
  if len(paths) == 0:
    return []
  longest = len(max(paths, key=lambda path: len(path)))
  paths = [path for path in paths if len(path) >= longest]
  return max(paths, key=lambda path: sum(path))

def part2(input):
  components = [list(map(int,line.split('/'))) for line in input.splitlines()]
  return sum(find_path2(0, components))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))