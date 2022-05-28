import argparse
import wordle
import logging
from datetime import date
import json
log = logging.getLogger("wordle_cli")

today = date.today()

logging.basicConfig(
    handlers=[
        logging.FileHandler(
            filename="{}-wordle.log".format(today), 
            encoding='utf-8', 
            mode='a+'
        ),
        logging.StreamHandler()
    ],
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s", 
    datefmt="%Y-%m-%dT%H-%M-%S",
    level=logging.INFO
)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('wordle', type=str, help='a representation of a wordle board')
args = parser.parse_args()

wordle_list = wordle.parse_wordle_string(args.wordle)
words = wordle.wordle_candidates(wordle_list)

response = {}
response["wordle"] = json.loads(args.wordle)
response["words"] = words
log.info(response)
