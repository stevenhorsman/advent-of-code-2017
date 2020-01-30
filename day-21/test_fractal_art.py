import fractal_art
import pytest
import fileinput

def test_part1_example_1():
  data = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""[1:]
  assert fractal_art.part1(data,2) == 12

def test_part1():
  with open(fractal_art.input_file) as f:
    data = f.read()
  expected = 197
  assert fractal_art.part1(data) == expected

@pytest.mark.skip(reason="runs too slowly")
def test_part2():
  with open(fractal_art.input_file) as f:
    data = f.read()
  expected = 3081737
  assert fractal_art.part2(data) == expected
