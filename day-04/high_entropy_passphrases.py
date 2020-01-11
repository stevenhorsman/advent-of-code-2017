input_file = 'day-04/input.txt'

def no_duplicates(words):
  return len(words) == len(set(words))

def part1(input):
  return sum(no_duplicates(passphrase.split()) for passphrase in input.splitlines())

def part2(input):
  sort_words = lambda words : [''.join(sorted(word)) for word in words.split()]
  return sum(no_duplicates(sort_words(passphrase)) for passphrase in input.splitlines())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))
