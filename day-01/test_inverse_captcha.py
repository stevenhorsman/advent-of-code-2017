import inverse_captcha
import fileinput

def test_part1_example_1():
  data = "1122"
  assert inverse_captcha.part1(data) == 3

def test_part1_example_2():
  data = "1111"
  assert inverse_captcha.part1(data) == 4

def test_part1_example_3():
  data = "1234"
  assert inverse_captcha.part1(data) == 0

def test_part1_example_4():
  data = "91212129"
  assert inverse_captcha.part1(data) == 9

def test_part1():
  with open(inverse_captcha.input_file) as f:
    data = f.read()
  expected = 1253
  assert inverse_captcha.part1(data) == expected

def test_part2_example_1():
  data = "1212"
  assert inverse_captcha.part2(data) == 6

def test_part2_example_2():
  data = "1221"
  assert inverse_captcha.part2(data) == 0

def test_part2_example_3():
  data = "123425"
  assert inverse_captcha.part2(data) == 4

def test_part2_example_4():
  data = "123123"
  assert inverse_captcha.part2(data) == 12
  
def test_part2_example_5():
  data = "12131415"
  assert inverse_captcha.part2(data) == 4

def test_part2():
  with open(inverse_captcha.input_file) as f:
    data = f.read()
  expected = 1278
  assert inverse_captcha.part2(data) == expected
