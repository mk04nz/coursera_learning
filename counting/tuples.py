import argparse
from itertools import product

parser = argparse.ArgumentParser(description="Generate ordered selections with repetitions from input characters")
parser.add_argument("characters", help="Characters to generate tuples from (e.g., 'abc')")
parser.add_argument("--length", type=int, default=1, help="Length of each tuple (default: 1)")

args = parser.parse_args()

total_tuples = 0
for tuple in product(args.characters, repeat=args.length):
    print(''.join(tuple))
    total_tuples += 1

print(f"Total tuples generated: {total_tuples}")
