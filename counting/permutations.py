import argparse
from itertools import permutations

parser = argparse.ArgumentParser(description="Generate ordered selections without repetitions from input characters")
parser.add_argument("characters", help="Characters to generate permutations from (e.g., 'abc')")
parser.add_argument("--length", type=int, default=1, help="Length of each permutations (default: 1)")

args = parser.parse_args()

total_permutations = 0
for combination in permutations(args.characters, args.length):
    print(''.join(combination))
    total_permutations += 1

print(f"Total permutations generated: {total_permutations}")
