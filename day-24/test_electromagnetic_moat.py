import electromagnetic_moat
import fileinput

def test_part1_example_1():
  data = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""[1:]
  assert electromagnetic_moat.part1(data) == 31

def test_part1():
  with open(electromagnetic_moat.input_file) as f:
    data = f.read()
  expected = 1695
  assert electromagnetic_moat.part1(data) == expected

def test_part2_example_1():
  data = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""[1:]
  assert electromagnetic_moat.part2(data) == 19

def test_part2():
  with open(electromagnetic_moat.input_file) as f:
    data = f.read()
  expected = 1673
  assert electromagnetic_moat.part2(data) == expected
