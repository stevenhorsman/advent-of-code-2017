import itertools, math
from collections import defaultdict

input_file = 'day-13/input.txt'

def part1(input):
  scanners = [[int(line.split(': ')[0]), int(line.split(': ')[1])] for line in input.splitlines()]
  #Scanner at top at time 2*(range - 1).
  return sum(time * rang for time, rang in scanners if (time % (2 * (rang - 1))) == 0)

def part2_brute_force(input):
  scanners = [[int(line.split(': ')[0]), int(line.split(': ')[1])] for line in input.splitlines()]
  return next(delay for delay in itertools.count() if not any(((delay + time) % (2 * (rang - 1))) == 0 for time, rang in scanners))

# From https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6h46k/
# reverse Chinese remainder theorem deal (least positive integer that is not equal to -depth mod (2 * width - 2) for each...)
def part2(input):
  scanners = [[int(line.split(': ')[0]), int(line.split(': ')[1])] for line in input.splitlines()]

  neq = defaultdict(list) # of the form {b:[a1,a2...]} where delay != a_i (mod b)
  for time, rang in scanners:
    top = (2 * (rang - 1))
    neq[top] += [-time % top]
  moduli = sorted(neq.keys())

  prev_lcm=1
  lcm = 1
  residues = [0] #mod 1
  for m in moduli:
      g = math.gcd(m,lcm) # simple Euclidean algorithm
      prev_lcm = lcm
      lcm = int(lcm*m/g)  #new modulus
      residues = [x for i in residues
            for x in range(i,lcm,prev_lcm)
            if x % m not in neq[m]]

  return sorted(residues)[0]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))