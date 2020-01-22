import knot_hash
import fileinput

def test_part1_example_1():
  data = "3, 4, 1, 5"
  assert knot_hash.part1(data, 5) == 12

def test_part1():
  with open(knot_hash.input_file) as f:
    data = f.read()
  expected = 3770
  assert knot_hash.part1(data) == expected

def test_part2_example_1():
  data = ""
  assert knot_hash.part2(data) == "a2582a3a0e66e6e86e3812dcb672a272"

def test_part2_example_2():
  data = "AoC 2017"
  assert knot_hash.part2(data) == "33efeb34ea91902bb2f59c9920caa6cd"

def test_part2_example_3():
  data = "1,2,3"
  assert knot_hash.part2(data) == '3efbe78a8d82f29979031a4aa0b16a9d'

def test_part2_example_4():
  data = "1,2,4"
  assert knot_hash.part2(data) == '63960835bcdc130f0b66d7ff4f6a5a8e'

def test_part2():
  with open(knot_hash.input_file) as f:
    data = f.read()
  expected = 'a9d0e68649d0174c8756a59ba21d4dc6'
  assert knot_hash.part2(data) == expected
