from operator import xor
from functools import reduce

input_file = 'day-10/input.txt'

# Tidy up from https://www.reddit.com/r/adventofcode/comments/7irzg5/2017_day_10_solutions/dr109d3/
def part1(input, list_size = 256):
  input = [int(x.strip()) for x in input.split(",")]
  knot_list, _, _ = one_round(input, knot_list=list(range(0,list_size)))
  return knot_list[0] * knot_list[1]

def one_round(input, curr_pos = 0, skip_size = 0, knot_list = list(range(0,256))):
  list_size = len(knot_list)
  for length in input:
    # Reverse list between curr_pos and curr_pos+length, which wraps around
    to_reverse_indices = [(curr_pos + x) % list_size for x in range(length)]
    replace_vals = reversed([knot_list[i] for i in to_reverse_indices])
    for i, v in zip(to_reverse_indices, replace_vals):
      knot_list[i] = v
    # Alternative:
    # to_reverse = []
    # for x in range(length):
    #   n = (curr_pos + x) % list_size
    #   to_reverse.append(knot_list[n])
    # to_reverse.reverse()
    # for x in range(length):
    #   n = (curr_pos + x) % list_size
    #   knot_list[n] = to_reverse[x]
    curr_pos = (curr_pos + length + skip_size) % list_size
    skip_size += 1
  return (knot_list, curr_pos, skip_size)

def part2(input):
  input = [ord(x) for x in input] + [17, 31, 73, 47, 23]
  curr_pos = 0
  skip_size = 0
  knot = list(range(256))
  for _ in range(64):
    knot, curr_pos, skip_size = one_round(input, curr_pos, skip_size, knot)
  
  sparse_hash = knot
  
  dense_hash = []
  for x in range(16):
    subslice = sparse_hash[16*x:16*(x+1)]
    dense_hash.append(format(reduce(xor, subslice), '02x'))

  return ''.join(dense_hash)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
