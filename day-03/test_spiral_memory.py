import spiral_memory
import fileinput

def test_part1_example_1():
  data = "1"
  assert spiral_memory.part1(data) == 0

def test_part1_example_2():
  data = "12"
  assert spiral_memory.part1(data) == 3

def test_part1_example_3():
  data = "23"
  assert spiral_memory.part1(data) == 2

def test_part1_example_5():
  data = "49"
  assert spiral_memory.part1(data) == 6

def test_part1_example_4():
  data = "1024"
  assert spiral_memory.part1(data) == 31

def test_part1():
  with open(spiral_memory.input_file) as f:
    data = f.read()
  expected = 480
  assert spiral_memory.part1(data) == expected

def test_part2():
  with open(spiral_memory.input_file) as f:
    data = f.read()
  expected = 349975
  assert spiral_memory.part2(data) == expected
