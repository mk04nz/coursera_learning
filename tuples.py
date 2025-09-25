import argparse
from itertools import product

parser = argparse.ArgumentParser(description="Generate ordered selections with repetitions from input characters")
parser.add_argument("characters", help="Characters to generate combinations from (e.g., 'abc')")
parser.add_argument("--length", type=int, default=1, help="Length of each combination (default: 1)")

args = parser.parse_args()

total_combinations = 0
for combination in product(args.characters, repeat=args.length):
    print(''.join(combination))
    total_combinations += 1

print(f"Total combinations generated: {total_combinations}")
