from operator import xor
from functools import reduce
from collections import Counter
import networkx as nx

input_file = 'day-14/input.txt'

def create_grid(input):
  grid = set()
  for i in range(128):
    row_bin = '{:0128b}'.format(int(knot_hash(input + '-' + str(i)), 16))
    for j in range(len(row_bin)):
      if row_bin[j] == '1':
        grid.add((j,i))
  return grid

def part1(input):
  return len(create_grid(input))

def part2(input):
  grid = create_grid(input)
  graph = nx.generators.grid_2d_graph(128, 128)
  for x in range(128):
    for y in range(128):
      if (x,y) not in grid:
        graph.remove_node((x,y))
  return nx.number_connected_components(graph)

# TODO - refactor to run from day10
def one_round(input, curr_pos = 0, skip_size = 0, knot_list = list(range(0,256))):
  list_size = len(knot_list)
  for length in input:
    # Reverse list between curr_pos and curr_pos+length, which wraps around
    to_reverse_indices = [(curr_pos + x) % list_size for x in range(length)]
    replace_vals = reversed([knot_list[i] for i in to_reverse_indices])
    for i, v in zip(to_reverse_indices, replace_vals):
      knot_list[i] = v
    curr_pos = (curr_pos + length + skip_size) % list_size
    skip_size += 1
  return (knot_list, curr_pos, skip_size)

def knot_hash(input):
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