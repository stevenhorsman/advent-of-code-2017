import sporifica_virus
import fileinput

def test_part1_example_1():
  data = """
..#
#..
..."""[1:]
  assert sporifica_virus.part1(data) == 5587

def test_part1():
  with open(sporifica_virus.input_file) as f:
    data = f.read()
  expected = 5280
  assert sporifica_virus.part1(data) == expected

def test_part2_example_1():
  data = """
..#
#..
..."""[1:]
  assert sporifica_virus.part2(data) == 2511944

def test_part2():
  with open(sporifica_virus.input_file) as f:
    data = f.read()
  expected = 2512261
  assert sporifica_virus.part2(data) == expected
