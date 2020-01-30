import coprocessor_conflagration
import fileinput

def test_part1():
  with open(coprocessor_conflagration.input_file) as f:
    data = f.read()
  expected = 6241
  assert coprocessor_conflagration.part1(data) == expected

def test_part2():
  with open(coprocessor_conflagration.input_file) as f:
    data = f.read()
  expected = 909
  assert coprocessor_conflagration.part2(data) == expected
