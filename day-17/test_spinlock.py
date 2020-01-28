import spinlock
import fileinput

def test_part1_example_1():
  data = "3"
  assert spinlock.part1(data) == 638

def test_part1():
  with open(spinlock.input_file) as f:
    data = f.read()
  expected = 926
  assert spinlock.part1(data) == expected

def test_part2():
  with open(spinlock.input_file) as f:
    data = f.read()
  expected = 10150888
  assert spinlock.part2(data) == expected
