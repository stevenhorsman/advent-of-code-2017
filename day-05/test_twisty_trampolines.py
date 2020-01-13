import twisty_trampolines
import fileinput

def test_part1_example_1():
  data = """
0
3
0
1
-3"""[1:]
  assert twisty_trampolines.part1(data) == 5

def test_part1():
  with open(twisty_trampolines.input_file) as f:
    data = f.read()
  expected = 351282
  assert twisty_trampolines.part1(data) == expected

def test_part2_example_1():
  data = """
0
3
0
1
-3"""[1:]
  assert twisty_trampolines.part2(data) == 10

def test_part2():
  with open(twisty_trampolines.input_file) as f:
    data = f.read()
  expected = 24568703
  assert twisty_trampolines.part2(data) == expected
