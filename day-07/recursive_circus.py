from re import match
from collections import Counter
import networkx as nx

input_file = 'day-07/input.txt'

def parse_data(input):
  tree = {}
  weights = {}
  for line in input.splitlines():
    m = match("^(\w+) \((\d+)\)(?: -> )?(.*)$", line)
    program = m.group(1)
    weights[program] = int(m.group(2))
    tree[program] = m.group(3).split(", ") if m.group(3) else []
  return tree, weights

def get_root(tree):
  children = {c for cs in tree.values() for c in cs}
  return (set(tree) - children).pop()

def part1(input):
  tree, weights = parse_data(input)
  return get_root(tree)

def get_sub_tree_weight(sub_weights, programs_tree, program_weights, node):
  sub_weights[node] = [(child, get_sub_tree_weight(sub_weights, programs_tree, program_weights, child)) for child in programs_tree[node]]
  return program_weights[node] + sum(weight for label, weight in sub_weights[node])
  
def get_unbalanced(sub_weights, node):
  counter = Counter(weight for (child, weight) in sub_weights[node]).most_common()
  if len(counter) == 1:
    return None
  else:
    wrong_weight = counter[1][0]
    odd_node = [child for (child, weight) in sub_weights[node] if weight == wrong_weight][0]
    return (odd_node, counter[0][0] - wrong_weight)

def part2(input):
  tree, weights = parse_data(input)
  root = get_root(tree)

  sub_weights = {}
  get_sub_tree_weight(sub_weights, tree, weights, root)

  start, weight_diff = root, 0
  while get_unbalanced(sub_weights, start) != None:
    start, weight_diff = get_unbalanced(sub_weights, start)

  return weights[start] + weight_diff

# From https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/dqw0f0c/
def create_graph(input):
  graph = nx.DiGraph()
  for line in input.splitlines():
    m = match("^(\w+) \((\d+)\)(?: -> )?(.*)$", line)
    program = m.group(1)
    graph.add_node(program, weight=int(m.group(2)))
    for child in m.group(3).split(", "):
      graph.add_edge(program, child)
  return graph

def part1_nx(input):
  graph = create_graph(input)

  # Topological sort to find the root of the tree
  ordered = list(nx.topological_sort(graph))
  return ordered[0]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
