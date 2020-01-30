import a_series_of_tubes
import fileinput

def test_part1_example_1():
  data = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""[1:]
  assert a_series_of_tubes.part1(data) == "ABCDEF"

def test_part1():
  with open(a_series_of_tubes.input_file) as f:
    data = f.read()
  expected = "SXPZDFJNRL"
  assert a_series_of_tubes.part1(data) == expected

def test_part2_example_1():
  data = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""[1:]
  assert a_series_of_tubes.part2(data) == 38

def test_part2():
  with open(a_series_of_tubes.input_file) as f:
    data = f.read()
  expected = 18126
  assert a_series_of_tubes.part2(data) == expected
