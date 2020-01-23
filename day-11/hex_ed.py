input_file = 'day-11/input.txt'

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

#Use cube co-ordinates system:https://www.redblobgames.com/grids/hexagons/
deltas = dict(zip(['n','ne','nw','s','se','sw'], [(0, 1, -1), (1, 0, -1), (-1, 1, 0), (0, -1, 1), (1, -1, 0), (-1, 0, 1)]))
def get_distances(input):
  directions = [dir.strip() for dir in input.split(',')]
  x,y,z = 0,0,0
  distances = []
  for dir in directions:
    x += deltas[dir][0]
    y += deltas[dir][1]
    z += deltas[dir][2]
    distances.append(get_dist(x,y,z))
  return distances

# Get the distance from the origin
def get_dist(x, y, z):
  return (abs(x) + abs(y) + abs(z)) / 2

# Get distance from origin at the end
def part1(input):
  return get_distances(input)[-1]

# Get furthest distance from origin during path
def part2(input):
  return max(get_distances(input))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
