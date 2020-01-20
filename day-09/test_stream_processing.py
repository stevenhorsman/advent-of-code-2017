import stream_processing
import fileinput

def test_part1_example_1():
  data = "{}"
  assert stream_processing.part1(data) == 1

def test_part1_example_2():
  data = "{{{}}}"
  assert stream_processing.part1(data) == 6

def test_part1_example_3():
  data = "{{},{}}"
  assert stream_processing.part1(data) == 5

def test_part1_example_4():
  data = "{{{},{},{{}}}}"
  assert stream_processing.part1(data) == 16

def test_part1_example_5():
  data = "{<a>,<a>,<a>,<a>}"
  assert stream_processing.part1(data) == 1

def test_part1_example_6():
  data = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
  assert stream_processing.part1(data) == 9

def test_part1_example_7():
  data = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
  assert stream_processing.part1(data) == 9

def test_part1_example_8():
  data = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
  assert stream_processing.part1(data) == 3

def test_part1():
  with open(stream_processing.input_file) as f:
    data = f.read()
  expected = 14421
  assert stream_processing.part1(data) == expected

def test_part2_example_1():
  data = "<>"
  assert stream_processing.part2(data) == 0

def test_part2_example_2():
  data = "<random characters>"
  assert stream_processing.part2(data) == 17

def test_part2_example_3():
  data = "<<<<>"
  assert stream_processing.part2(data) == 3

def test_part2_example_4():
  data = "<{!>}>"
  assert stream_processing.part2(data) == 2
  
def test_part2_example_5():
  data = "<!!>"
  assert stream_processing.part2(data) == 0

def test_part2_example_6():
  data = "<!!!>>"
  assert stream_processing.part2(data) == 0
  
def test_part2_example_7():
  data = "<{o\"i!a,<{i<a>"
  assert stream_processing.part2(data) == 10

def test_part2():
  with open(stream_processing.input_file) as f:
    data = f.read()
  expected = 6817
  assert stream_processing.part2(data) == expected
