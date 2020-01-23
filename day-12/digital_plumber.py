import re
import networkx as nx

input_file = 'day-12/input.txt'

def create_graph(input):
  graph = nx.Graph()
  for line in input.splitlines():
    program, neighbours = line.split(' <-> ')
    graph.add_node(program)
    for neighbour in [prog.strip() for prog in neighbours.split(",")]:
      graph.add_edge(program, neighbour)
  return graph

def part1(input):
  graph = create_graph(input)
  return len(nx.node_connected_component(graph, '0'))

def part2(input):
  graph = create_graph(input)
  return nx.number_connected_components(graph)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
