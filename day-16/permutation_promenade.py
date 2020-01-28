input_file = 'day-16/input.txt'

def one_round(input, programs):
  for instruction in input.split(','):
    if instruction[0] == 's':
      moved = int(instruction[1:])
      programs = programs[-moved:] + programs[:-moved]
    elif instruction[0] == 'x':
      swap_a, swap_b = map(int, instruction[1:].split('/'))
      programs[swap_a], programs[swap_b] = programs[swap_b], programs[swap_a]
    elif instruction[0] == 'p':
      swap_a, swap_b = map(programs.index, instruction[1:].split('/'))
      # equivalent to swap_a, swap_b = [programs.index(x) for x in instruction[1:].split('/')]
      programs[swap_a], programs[swap_b] = programs[swap_b], programs[swap_a]
  return programs

def part1(input, length=16):
  programs = [chr(x + 97) for x in range(length)]
  programs = one_round(input, programs)
  return ''.join(programs)

def part2(input, length=16):
  reps = 1000000000
  programs = [chr(x + 97) for x in range(length)]
  seen = []
  for i in range(reps):
    s = ''.join(programs)
    if s in seen:
      return seen[reps % i]
      break
    seen.append(s)
    programs = one_round(input, programs)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))