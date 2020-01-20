import recursive_circus
import fileinput

def test_part1_example_1():
  data = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""[1:]
  assert recursive_circus.part1(data) == "tknk"

def test_part1():
  with open(recursive_circus.input_file) as f:
    data = f.read()
  expected = "fbgguv"
  assert recursive_circus.part1(data) == expected

def test_part1_nx():
  with open(recursive_circus.input_file) as f:
    data = f.read()
  expected = "fbgguv"
  assert recursive_circus.part1_nx(data) == expected

def test_part2_example_1():
  data = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""[1:]
  assert recursive_circus.part2(data) == 60

def test_part2():
  with open(recursive_circus.input_file) as f:
    data = f.read()
  expected = 1864
  assert recursive_circus.part2(data) == expected