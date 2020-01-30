import particle_swarm
import fileinput

def test_part1_example_1():
  data = """
p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"""[1:]
  assert particle_swarm.part1(data) == 0

def test_part1():
  with open(particle_swarm.input_file) as f:
    data = f.read()
  expected = 91
  assert particle_swarm.part1(data) == expected

def test_part2_example_1():
  data = """
p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"""[1:]
  assert particle_swarm.part2(data) == 1

def test_part2():
  with open(particle_swarm.input_file) as f:
    data = f.read()
  expected = 567
  assert particle_swarm.part2(data) == expected
