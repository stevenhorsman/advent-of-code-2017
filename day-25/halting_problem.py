from collections import defaultdict

input_file = 'day-25/input.txt'

def run(steps, state, states):
  tape = defaultdict(int)
  cursor = 0
  for _ in range(steps):
    val = tape[cursor]
    action = states[state][val]
    tape[cursor] = action[0]
    if action[1] == 'R':
      cursor +=1
    else:
      cursor -= 1
    state = action[2]
  return tape

def example(input):
  state = 'A'
  steps = 6
  states = {'A': ((1,'R','B'), (0,'L','B')),
    'B': ((1,'L','A'), (1,'R','A'))}
  tape = run(steps, state, states)

  return sum(tape.values())

def part1(input):
  states = {'A': ((1,'R','B'), (1,'L','E')),
    'B': ((1,'R','C'), (1,'R','F')),
    'C': ((1,'L','D'), (0,'R','B')),
    'D': ((1,'R','E'), (0,'L','C')),
    'E': ((1,'L','A'), (0,'R','D')),
    'F': ((1,'R','A'), (1,'R','C'))}

  steps = 12523873
  state = 'A'
  tape = run(steps, state, states)
  return sum(tape.values())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))