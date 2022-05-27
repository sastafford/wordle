from mimetypes import init
from wordle import *

def test_transform_wordle_guess():
    name = "STAIN"
    clue = "00001"
    result = transform_wordle_guess(name, clue)
    assert(len(result) == 5)        
    assert(result[0] == ("S", 0))
    assert(result[4] == ("N", 1))                                       

def test_is_word_five_letters():
    assert(is_word_length_size("guess", 5) == True)
    assert(is_word_length_size("abc", 5) == False)

def test_clean_word():
    assert(clean_word("hello") == "HELLO")
    assert(clean_word("hello ") == "HELLO")
    assert(clean_word(" hello ") == "HELLO")

def test_get_initial_wordle_combos():
    x = initial_wordle_combinations(5)
    assert(len(x) == 5)
    assert(len(x[0]) == 26)

def test_eliminate_letter():
    combos = initial_wordle_combinations(1)[0]
    x = eliminate_letter(combos, "A")
    assert(len(x) == 25)

def test_single_letter_guess():
    combos = initial_wordle_combinations(1)
    x = guess(combos, [("S", 0)])
    assert(len(x[0]) == 25)
    y = guess(x, [("A", 1)])
    assert(len(y[0]) == 24)
    z = guess(y, [("D", 2)])
    assert(len(z[0]) == 1)

def test_two_letter_guess():
    combos = initial_wordle_combinations(3)
    x = guess(combos, [("S", 0), ("A", 1), ("Z", 2)])
    assert(len(x[0]) == 25)
    assert(len(x[1]) == 24)
    assert(len(x[2]) == 1)

def test_permutations():
    p = permutations("word", [["A", "B", "C"]])
    assert(len(p) == 3)
    assert(p[2] == "wordC")
    
    p = permutations("WORD", [["A", "B"], ["C", "D"]])
    assert(len(p) == 4)
    assert(p[2] == "WORDBC")
    
    p = permutations("WORD", [["A", "B"], ["C", "D"], ["E", "F"]])
    assert(len(p) == 8)
    assert(p[3] == "WORDADF")

def test_letters_in_word():
    assert(letters_in_word("WORD", ["W"]))
    assert(not(letters_in_word("WORD", ["S"])))

def test_permutations_with_letters():
    must_contain = ["B"]
    p = permutations("WORD", [["A", "B"]], must_contain)
    assert(len(p) == 1)

    p = permutations("WORD", [["A", "B"], ["D", "E"]], must_contain)
    assert(len(p) == 2)

def test_dictionary():
    dictionary = get_dictionary()
    assert(len(dictionary) > 5000)

def test_letters_not_in_word():
    wordle_guess = [("A", 0), ("B", 1), ("C", 0)]
    x = letters_not_in_word(wordle_guess)
    assert(x == ["A", "C"])

def test_two_wordle_candidates():
    x = wordle_candidates([("TREND", "00110"), ("UNCLE", "01001")])
    assert("SEVEN" in x)
    assert("BEGIN" in x)
    assert("TRAIN" not in x)

def test_three_wordle_candidates():
    x = wordle_candidates([("TREND", "00110"), ("UNCLE", "01001"), ("NAMES","10120")])
    assert("MONEY" in x)

def test_parse_string_to_list():
    wordle_string = "{ \"HATER\": \"01101\", \"TRACK\": \"21200\" }"
    x = parse_wordle_string(wordle_string)
    assert(x[0][0] == "HATER")
    assert(len(x) == 2)