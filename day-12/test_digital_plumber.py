import digital_plumber
import fileinput

def test_part1_example_1():
  data = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""[1:]
  assert digital_plumber.part1(data) == 6

def test_part1():
  with open(digital_plumber.input_file) as f:
    data = f.read()
  expected = 378
  assert digital_plumber.part1(data) == expected

def test_part2_example_1():
  data = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""[1:]
  assert digital_plumber.part2(data) == 2
def test_part2():
  with open(digital_plumber.input_file) as f:
    data = f.read()
  expected = 204
  assert digital_plumber.part2(data) == expected
