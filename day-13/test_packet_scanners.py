import packet_scanners
import fileinput

def test_part1_example_1():
  data = """
0: 3
1: 2
4: 4
6: 4"""[1:]
  assert packet_scanners.part1(data) == 24

def test_part1():
  with open(packet_scanners.input_file) as f:
    data = f.read()
  expected = 1588
  assert packet_scanners.part1(data) == expected

def test_part2_example_1():
  data = """
0: 3
1: 2
4: 4
6: 4"""[1:]
  assert packet_scanners.part2(data) == 10

def test_part2():
  with open(packet_scanners.input_file) as f:
    data = f.read()
  expected = 3865118
  assert packet_scanners.part2(data) == expected

def test_part2_alt_example_1():
  data = """
0: 3
1: 2
4: 4
6: 4"""[1:]
  assert packet_scanners.part2_brute_force(data) == 10

def test_part2_alt():
  with open(packet_scanners.input_file) as f:
    data = f.read()
  expected = 3865118
  assert packet_scanners.part2_brute_force(data) == expected

