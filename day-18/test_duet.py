import duet
import fileinput

def test_part1_example_1():
  data = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""[1:]
  assert duet.part1(data) == 4

def test_part1():
  with open(duet.input_file) as f:
    data = f.read()
  expected = 4601
  assert duet.part1(data) == expected

def test_part2_example_1():
  data = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""[1:]
  assert duet.part2(data) == 3

def test_part2():
  with open(duet.input_file) as f:
    data = f.read()
  expected = 6858
  assert duet.part2(data) == expected
