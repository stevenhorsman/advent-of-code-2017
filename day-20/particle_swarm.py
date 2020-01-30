import re
from collections import Counter

input_file = 'day-20/input.txt'

class Particle:
  def __init__(self, input_string):
    # From https://www.reddit.com/r/adventofcode/comments/7kz6ik/2017_day_20_solutions/dric7uj/
    pos_match = re.search('p=<(-?\d+),(-?\d+),(-?\d+)>', input_string)
    self.pos = [int(pos_match.group(1)), int(pos_match.group(2)), int(pos_match.group(3))]
    vel_match = re.search('v=<(-?\d+),(-?\d+),(-?\d+)>', input_string)
    self.vel = [int(vel_match.group(1)), int(vel_match.group(2)), int(vel_match.group(3))]
    acc_match = re.search('a=<(-?\d+),(-?\d+),(-?\d+)>', input_string)
    self.acc = [int(acc_match.group(1)), int(acc_match.group(2)), int(acc_match.group(3))]

  def update(self):
    for axis in range(0, len(self.vel)):
      self.vel[axis] += self.acc[axis]
      self.pos[axis] += self.vel[axis]

  def get_origin_distance(self):
    return sum(abs(x) for x in self.pos)

def part1(input):
  particles = [Particle(line) for line in input.splitlines()]
  for _ in range(200):
    for particle in particles:
      particle.update()

  return particles.index(min(particles, key=lambda p: p.get_origin_distance()))

def part2(input):
  particles = [Particle(line) for line in input.splitlines()]
  for _ in range(200):
    for particle in particles:
      particle.update()
    # find particles in the same position and remove them from list. use counter?
    counter = Counter([tuple(p.pos) for p in particles])
    collisions = [x for x in counter if counter[x] > 1]
    particles = [p for p in particles if tuple(p.pos) not in collisions]
  return len(particles)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))