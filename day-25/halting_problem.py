from collections import defaultdict
import yaml, re

input_file = 'day-25/input.txt'

def run(steps, state, states):
  tape = defaultdict(int)
  cursor = 0
  for _ in range(steps):
    val = tape[cursor]
    tape[cursor], dir, state = states[state][val]
    cursor += {"right": 1, "left": -1}[dir]
  return tape

def process_line(line):
  m = re.search(r"\w", line)
  alpha_start = m.start()
  last_space = line.rfind(' ')
  return line[:alpha_start] + line[last_space:].replace('.','')

def parse_input(input):
  lines = input.splitlines()

  state = lines[0].split()[-1][0]
  steps = int(lines[1].split()[-2])

  lines = [process_line(line) for line in lines[3:] if len(line) > 0]
  states = yaml.load('\n'.join(lines))
  return state, steps, states

def part1(input):
  state, steps, states = parse_input(input)
  # states = {'A': ((1,'R','B'), (0,'L','B')),
  #   'B': ((1,'L','A'), (1,'R','A'))}
  tape = run(steps, state, states)
  return sum(tape.values())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))