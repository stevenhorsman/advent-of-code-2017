import like_registers
import fileinput

def test_part1_example_1():
  data = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""[1:]
  assert like_registers.part1(data) == 1

def test_part1():
  with open(like_registers.input_file) as f:
    data = f.read()
  expected = 3745
  assert like_registers.part1(data) == expected

def test_part2_example_1():
  data = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""[1:]
  assert like_registers.part2(data) == 10

def test_part2():
  with open(like_registers.input_file) as f:
    data = f.read()
  expected = 4644
  assert like_registers.part2(data) == expected
