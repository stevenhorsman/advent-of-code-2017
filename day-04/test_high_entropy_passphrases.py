import high_entropy_passphrases
import fileinput

def test_part1_example_1():
  data = "aa bb cc dd ee"
  assert high_entropy_passphrases.part1(data) == 1

def test_part1_example_2():
  data = "aa bb cc dd aa"
  assert high_entropy_passphrases.part1(data) == 0

def test_part1_example_3():
  data = "aa bb cc dd aaa"
  assert high_entropy_passphrases.part1(data) == 1

def test_part1():
  with open(high_entropy_passphrases.input_file) as f:
    data = f.read()
  expected = 325
  assert high_entropy_passphrases.part1(data) == expected

def test_part2_example_1():
  data = "abcde fghij"
  assert high_entropy_passphrases.part2(data) == 1

def test_part2_example_2():
  data = "abcde xyz ecdab"
  assert high_entropy_passphrases.part2(data) == 0

def test_part2_example_3():
  data = "a ab abc abd abf abj"
  assert high_entropy_passphrases.part2(data) == 1

def test_part2_example_4():
  data = "iiii oiii ooii oooi oooo"
  assert high_entropy_passphrases.part2(data) == 1
  
def test_part2_example_5():
  data = "oiii ioii iioi iiio"
  assert high_entropy_passphrases.part2(data) == 0

def test_part2():
  with open(high_entropy_passphrases.input_file) as f:
    data = f.read()
  expected = 119
  assert high_entropy_passphrases.part2(data) == expected
