import dualing_generators
import fileinput

def test_part1_example_1():
  data = """
Generator A starts with 65
Generator B starts with 8921"""[1:]
  assert dualing_generators.part1(data) == 588

def test_part1():
  with open(dualing_generators.input_file) as f:
    data = f.read()
  expected = 650
  assert dualing_generators.part1(data) == expected

def test_part2_example_1():
  data = """
Generator A starts with 65
Generator B starts with 8921"""[1:]
  assert dualing_generators.part2(data) == 309

def test_part2():
  with open(dualing_generators.input_file) as f:
    data = f.read()
  expected = 336
  assert dualing_generators.part2(data) == expected
