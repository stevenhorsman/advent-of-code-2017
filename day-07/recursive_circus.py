from re import match
from collections import Counter

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
  if node in programs_tree.keys():
    sub_weights[node] = [(child, get_sub_tree_weight(sub_weights, programs_tree, program_weights, child)) for child in programs_tree[node]]
    return program_weights[node] + sum(weight for label, weight in sub_weights[node])
  else:
    return program_weights[node]

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

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
