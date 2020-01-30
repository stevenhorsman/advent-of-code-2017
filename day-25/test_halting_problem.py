import halting_problem
import fileinput

def test_part1_example_1():
  data = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""[1:]
  assert halting_problem.example(data) == 3

def test_part1():
  with open(halting_problem.input_file) as f:
    data = f.read()
  expected = 4225
  assert halting_problem.part1(data) == expected