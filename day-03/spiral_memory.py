import math
from itertools import product

input_file = 'day-03/input.txt'

def get_anti_cloackwise(curr):
  direction_string = 'ULDR'
  return direction_string[(direction_string.index(curr) + 1) % len(direction_string)]

deltas = dict(zip('RLUD', [(1, 0), (-1, 0), (0, 1), (0, -1)]))

def part1(input):
  input = int(input)

  # (x,-x) corners are the odd squares, so find the odd square above input and track from there
  level = math.ceil(math.sqrt(input)) // 2
  edge_length = (2 * level + 1)
  difference = (edge_length ** 2) - input

  # We are counting from (level, -level).
  edges_around = difference // edge_length
  distance_from_corner = difference % max(edge_length - 1, 1)
  if distance_from_corner > edge_length / 2:
    distance_from_corner = edge_length - distance_from_corner

  return (2 * level) - distance_from_corner

def part_1_naive(input):
  x,y = 0,0
  dir = 'R'
  grid = { (x, y): 1 }

  for i in range(2, input + 1):
    x += deltas[dir][0]
    y += deltas[dir][1]
    grid[(x,y)] = i
    # Try turning
    next_dir = get_anti_cloackwise(dir)
    next_x = x + deltas[next_dir][0]
    next_y = y + deltas[next_dir][1]
    if not (next_x, next_y) in grid:
      dir = next_dir

  return abs(x) + abs(y)

def get_next_coordinate(x, y):
  if x == y == 0: return (1, 0)
  if y > -x and x > y: return (x, y + 1)
  if y > -x and y >= x: return (x - 1, y)
  if y <= -x and x < y: return (x, y - 1)
  if y <= -x and x >= y: return (x + 1, y)


def part2(input):
  input = int(input)

  x,y = 0,0
  grid = { (x, y): 1 }

  for i in range(2, input + 1):
    (x,y) = get_next_coordinate(x, y)
    sum_neighbours = sum(grid.get((x + i, y + j), 0) for i,j in product([-1, 0, 1], repeat = 2))
    if (sum_neighbours > input):
      return sum_neighbours
    grid[(x,y)] = sum_neighbours

  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
