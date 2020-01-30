from collections import defaultdict, deque

input_file = 'day-23/input.txt'

class Program:
  def __init__(self, lines, reg_a = 0):
    self.lines = lines
    self.pc = 0
    self.regs = defaultdict(int)
    self.regs['a'] = reg_a
    self.mul = 0

  def run(self):
    while self.tick():
      pass

  def get(self, x):
    try:
      v = int(x)
      return v
    except:
      return self.regs[x]

  def tick(self):
    if not (0 <= self.pc < len(self.lines)):
      return False

    line = self.lines[self.pc].split()
    instruction, parameters = line[0], line[1:]
    
    x = y = None
    if len(parameters) == 2:
      x, y = parameters[0], self.get(parameters[1])
    else:
      x = parameters[0]

    if instruction == 'set':
      self.regs[x] = y
    elif instruction == 'sub':
      self.regs[x] -= y
    elif instruction == 'mul':
      self.regs[x] *= y
      self.mul += 1
    elif instruction == 'jnz':
      if self.get(x) != 0:
        self.pc += y
        return True # skip the pc += 1
    self.pc += 1
    return True

def part1(input):
  program = Program([line.split('#')[0] for line in input.splitlines()])
  program.run()
  return program.mul

# logic from https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/drnjwq7/
def part2(input):
  program = Program([line.split('#')[0] for line in input.splitlines()], 1)
#TODO - some hot-swap replacement?
  h = 0
  for x in range(108100,125100 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
  
  return h

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))