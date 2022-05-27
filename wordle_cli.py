import argparse
import wordle

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('wordle', type=str, help='a representation of a wordle board')
args = parser.parse_args()

wordle_list = wordle.parse_wordle_string(args.wordle)

print(wordle.wordle_candidates(wordle_list))