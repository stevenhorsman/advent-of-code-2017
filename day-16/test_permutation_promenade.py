import permutation_promenade
import fileinput

def test_part1_example_1():
  check_part1_example("s3", "cdeab")

def test_part1_example_2():
  check_part1_example("s1", "eabcd")

def test_part1_example_3():
  check_part1_example("s1,x3/4", "eabdc")

def test_part1_example_4():
  check_part1_example("s1,x3/4,pe/b", "baedc")

def check_part1_example(instruction, expected):
  assert permutation_promenade.part1(instruction,5) == expected

def test_part1():
  with open(permutation_promenade.input_file) as f:
    data = f.read()
  expected = "bkgcdefiholnpmja"
  assert permutation_promenade.part1(data) == expected

def test_part2():
  with open(permutation_promenade.input_file) as f:
    data = f.read()
  expected = 'knmdfoijcbpghlea'
  assert permutation_promenade.part2(data) == expected
