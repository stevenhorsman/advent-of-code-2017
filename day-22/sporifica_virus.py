input_file = 'day-22/input.txt'

def get_direction(curr, rotation):
  direction_string = '^<v>'
  if rotation == 'L':
    return direction_string[(direction_string.index(curr) + 1) % len(direction_string)]
  elif rotation == 'R':
    return direction_string[(direction_string.index(curr) - 1) % len(direction_string)]

deltas = dict(zip('><^v', [(1, 0), (-1, 0), (0, -1), (0, 1)]))

def part1(input):
  lines = input.splitlines()
  bursts = 0
  infected = {(x,y) for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] == '#'}
  curr_dir = '^'
  curr_pos = (len(lines[0]) // 2, len(lines) // 2)

  for _ in range(10000):
    if curr_pos in infected:
      curr_dir = get_direction(curr_dir, 'R')
      infected.remove(curr_pos)
    else:
      curr_dir = get_direction(curr_dir, 'L')
      infected.add(curr_pos)
      bursts += 1

    curr_pos = (curr_pos[0] + deltas[curr_dir][0], curr_pos[1] + deltas[curr_dir][1])
  return bursts

def part2(input):
  lines = input.splitlines()
  bursts = 0
  infected = {(x,y) for y in range(0,len(lines)) for x in range(0,len(lines[y])) if lines[y][x] == '#'}
  weakened = set()
  flagged = set()
  curr_dir = '^'
  curr_pos = (len(lines[0]) // 2, len(lines) // 2)

  for _ in range(10000000):
    if curr_pos in infected:
      curr_dir = get_direction(curr_dir, 'R')
      infected.remove(curr_pos)
      flagged.add(curr_pos)
    elif curr_pos in weakened:
      pass #no dir change
      weakened.remove(curr_pos)
      infected.add(curr_pos)
      bursts += 1
    elif curr_pos in flagged:
      curr_dir = get_direction(get_direction(curr_dir, 'R'),'R') #reverse
      flagged.remove(curr_pos)
    else:
      curr_dir = get_direction(curr_dir, 'L')
      weakened.add(curr_pos)

    curr_pos = (curr_pos[0] + deltas[curr_dir][0], curr_pos[1] + deltas[curr_dir][1])
  return bursts

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))