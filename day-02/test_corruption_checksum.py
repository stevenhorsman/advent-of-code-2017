import corruption_checksum
import fileinput

def test_part1_example_1():
  data = """
5 1 9 5
7 5 3
2 4 6 8"""[1:]
  assert corruption_checksum.part1(data) == 18

def test_part1():
  with open(corruption_checksum.input_file) as f:
    data = f.read()
  expected = 50376
  assert corruption_checksum.part1(data) == expected

def test_part2_example_1():
  data = """
5 9 2 8
9 4 7 3
3 8 6 5"""[1:]
  assert corruption_checksum.part2(data) == 9

def test_part2():
  with open(corruption_checksum.input_file) as f:
    data = f.read()
  expected = 267
  assert corruption_checksum.part2(data) == expected
