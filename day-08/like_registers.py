from collections import defaultdict

input_file = 'day-08/input.txt'

def get_max_reg(input, all_time_max = False):
  max_value = 0
  registers = defaultdict(int) #Registers ininitally zero
  for line in input.splitlines():
    reg, op, val, _, cond_reg, cond_op, cond_val = line.split()
    if eval(str(registers[cond_reg]) + cond_op + cond_val):
      if op == "dec":
        val = -int(val)
      registers[reg] += int(val)
      max_value = max(max_value, registers[reg])
  if not all_time_max:
    max_value = max(registers.values())
  return max_value

def part1(input):
  return get_max_reg(input)

def part2(input):
  return get_max_reg(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
