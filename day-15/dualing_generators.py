input_file = 'day-15/input.txt'

gen_a_factor = 16807
gen_b_factor = 48271
def part1(input):
  gen_a, gen_b = [int(line.split(' ')[-1]) for line in input.splitlines()]

  matches = 0
  for _ in range(40000000):
    gen_a = (gen_a * gen_a_factor) % 2147483647
    gen_b = (gen_b * gen_b_factor) % 2147483647
    if gen_a & 0xFFFF == gen_b & 0xFFFF:
      matches += 1

  return matches

def part2(input):
  gen_a, gen_b = [int(line.split(' ')[-1]) for line in input.splitlines()]

  matches = 0
  for _ in range(5000000):
    while True:
      gen_a = (gen_a * gen_a_factor) % 2147483647
      if gen_a % 4 == 0:
        break
    while True:
      gen_b = (gen_b * gen_b_factor) % 2147483647
      if gen_b % 8 == 0:
        break
    if gen_a & 0xFFFF == gen_b & 0xFFFF:
      matches += 1

  return matches

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))