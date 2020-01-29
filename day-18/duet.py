from collections import defaultdict, deque

input_file = 'day-18/input.txt'

class Program:
  def __init__(self, pid, lines, out_queue, in_queue):
    self.part1 = pid == -1
    self.lines = lines
    self.pc = 0
    self.regs = defaultdict(int)
    self.regs['p'] = pid
    self.sent = 0
    self.out_queue = out_queue
    self.in_queue = in_queue
    self.sent = 0

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

    if instruction == 'snd':
      self.sent +=1
      self.out_queue.append(self.regs[x])
    elif instruction == 'set':
      self.regs[x] = y
    elif instruction == 'add':
      self.regs[x] += y
    elif instruction == 'mul':
      self.regs[x] *= y
    elif instruction == 'mod':
      self.regs[x] %= y
    elif instruction == 'rcv':
      if self.part1:# recover the last sound output if reg val != 0
        if self.regs[x] != 0:
          return False
      else:
        if not self.in_queue:
          return False
        self.regs[x] = self.in_queue.popleft()
    elif instruction == 'jgz':
      if self.get(x) > 0:
        self.pc += y
        return True # skip the pc += 1
    self.pc += 1
    return True

def part1(input):
  queue = deque()
  program = Program(-1, input.splitlines(), queue, queue)
  program.run()
  return queue.pop()

def part2(input):
  lines = input.splitlines()
  queue_0, queue_1 = deque(), deque()
  program_0 = Program(0, lines, queue_0, queue_1)
  program_1 = Program(1, lines, queue_1, queue_0)

  while True:
    if not program_0.tick() and not program_1.tick():
      break
  
  return program_1.sent

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))