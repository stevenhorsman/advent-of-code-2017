import hex_ed
import fileinput

def test_part1_example_1():
  data = "ne,ne,ne"
  assert hex_ed.part1(data) == 3

def test_part1_example_2():
  data = "ne,ne,sw,sw"
  assert hex_ed.part1(data) == 0

def test_part1_example_3():
  data = "ne,ne,s,s"
  assert hex_ed.part1(data) == 2

def test_part1_example_4():
  data = "se,sw,se,sw,sw"
  assert hex_ed.part1(data) == 3

def test_part1():
  with open(hex_ed.input_file) as f:
    data = f.read()
  expected = 743
  assert hex_ed.part1(data) == expected

def test_part2():
  with open(hex_ed.input_file) as f:
    data = f.read()
  expected = 1493
  assert hex_ed.part2(data) == expected
