input_file = 'day-17/input.txt'

def part1(input):
  input = int(input)
  buffer = [0]
  curr_pos = 0
  for i in range(1, 2017 + 1):
    curr_pos = ((curr_pos + input) % len(buffer)) + 1
    buffer.insert(curr_pos, i)
  return buffer[curr_pos+1]

# zero is at the start, so only keep track of the last value added after it
def part2(input):
  input = int(input)
  curr_pos = 0
  buff_1 = 0
  for i in range(1, 50000000 + 1):
    curr_pos = ((curr_pos + input) % i) + 1
    if curr_pos == 1:
      buff_1 = i
  return buff_1

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))