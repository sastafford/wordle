from typing import List
import string
import logging
import json

log = logging.getLogger("wordle")

def is_word_length_size(word: str, size: int):
    return len(word) == size

def clean_word(word: str) -> str: 
    return word.upper().strip()

def transform_wordle_guess(word: string, clue: string):
    zip_itr = zip(word, clue) 
    cast_second_element_to_int = lambda x: (x[0], int(x[1]))
    return [cast_second_element_to_int(i) for i in zip_itr]

def initial_wordle_combinations(size: int) -> List:
    facts = []
    for i in range(size):
        facts.append(list(string.ascii_uppercase))
    return facts

def eliminate_letter(possible_letters: list, letter: str) -> List:
    return [i for i in possible_letters if i != letter]

def letters_not_in_word(wordle_guesses: List) -> List:
    return [letter[0] for letter in wordle_guesses if letter[1] == 0]

def letters_in_word(word, letters):
    return all(letter in word for letter in letters)

def guess(wordle_combinations, wordle_guess) -> List:
    results = []
    drop_letters = letters_not_in_word(wordle_guess)
    
    for i, guess in enumerate(wordle_guess):
        letter = guess[0]
        clue = guess[1]
        possible_letters = [letter for letter in wordle_combinations[i] if letter not in drop_letters]

        if clue < 2: 
            results.append(eliminate_letter(possible_letters, letter))
        elif clue == 2:
            results.append([letter])
        else:
            raise Exception(letter + ", " + clue) 
    return results

def permutations(word, possible_letter_list: List[List], must_contain=[]):
    if len(possible_letter_list) == 1:
        word_candidates = [word + i for i in possible_letter_list[0]]
        return [x for x in word_candidates if letters_in_word(x, must_contain)]
   
    perm_list = []
    for letter in possible_letter_list[0]:
        new_word = word + letter
        new_words = permutations(new_word, possible_letter_list[1:], must_contain)
        perm_list.extend(new_words)

    return perm_list

def get_dictionary() -> List[str]:
    f_words = open("five_letter_words.txt")
    words = f_words.readlines()

    words_no_newlines = []
    for word in words:
        words_no_newlines.append(word.strip())
    
    f_words.close()
    return words_no_newlines

def parse_wordle_string(wordle_string: str) -> List[tuple]:
    wordle_json = json.loads(wordle_string)
    return [i for i in wordle_json.items()]


def wordle_candidates(wordle_guesses: List[tuple]) -> List:
    log.debug(wordle_guesses)
    
    guesses = initial_wordle_combinations(5)
    for wordle_guess in wordle_guesses:
        tuple_wordle_guess = transform_wordle_guess(wordle_guess[0], wordle_guess[1])
        log.debug(tuple_wordle_guess)
        guesses = guess(guesses, tuple_wordle_guess)
        log.debug(guesses)
        letters_in_word = [i[0] for i in tuple_wordle_guess if i[1] == 1]
    
    p = permutations("", guesses, letters_in_word)
     
    dictionary = set(get_dictionary())
    word_candidates = list(
        set(p).intersection(dictionary)
    )
    return word_candidates
