import disk_defragmentation
import fileinput

def test_part1_example_1():
  data = "flqrgnkx"
  assert disk_defragmentation.part1(data) == 8108

def test_part1():
  with open(disk_defragmentation.input_file) as f:
    data = f.read()
  expected = 8074
  assert disk_defragmentation.part1(data) == expected

def test_part2_example_1():
  data = "flqrgnkx"
  assert disk_defragmentation.part2(data) == 1242

def test_part2():
  with open(disk_defragmentation.input_file) as f:
    data = f.read()
  expected = 1212
  assert disk_defragmentation.part2(data) == expected
