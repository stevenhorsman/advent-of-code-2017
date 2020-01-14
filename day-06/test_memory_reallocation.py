import memory_reallocation
import fileinput

def test_part1_example_1():
  data = "0 2 7 0"
  assert memory_reallocation.part1(data) == 5

def test_part1():
  with open(memory_reallocation.input_file) as f:
    data = f.read()
  expected = 4074
  assert memory_reallocation.part1(data) == expected

def test_part2_example_1():
  data = "0 2 7 0"
  assert memory_reallocation.part2(data) == 4

def test_part2():
  with open(memory_reallocation.input_file) as f:
    data = f.read()
  expected = 2793
  assert memory_reallocation.part2(data) == expected
