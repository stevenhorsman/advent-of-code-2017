input_file = 'day-19/input.txt'

def get_direction(curr, rotation):
  direction_string = '^<v>'
  if rotation == 'L':
    return direction_string[(direction_string.index(curr) + 1) % len(direction_string)]
  elif rotation == 'R':
    return direction_string[(direction_string.index(curr) - 1) % len(direction_string)]

deltas = dict(zip('><^v', [(1, 0), (-1, 0), (0, -1), (0, 1)]))

def find_path(input):
  lines = [list(line) for line in input.splitlines()]
  pipes = {(x,y): lines[y][x] for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] != ' '}
  x,y = [key[0] for key in pipes if key[1] == 0][0], 0
  path = []
  curr_dir = 'v'
  while (x,y) in pipes:
    if pipes[(x,y)] == '+':
       # Can we move left or right?
      next_dir = get_direction(curr_dir,'R')
      next_x = x + deltas[next_dir][0]
      next_y = y + deltas[next_dir][1]
      if (next_x, next_y) in pipes:
        curr_dir = next_dir
      else:
        next_dir = get_direction(curr_dir,'L')
        next_x = x + deltas[next_dir][0]
        next_y = y + deltas[next_dir][1]
        if (next_x, next_y) in pipes:
          curr_dir = next_dir
    path.append(pipes[(x, y)])  
    x += deltas[curr_dir][0]
    y += deltas[curr_dir][1]
  return path
    

def part1(input):
  return ''.join(c for c in find_path(input) if c.isalpha())

def part2(input):
  return len(find_path(input))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))