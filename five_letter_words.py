f_words = open("words.txt", "r")
f_five = open("five_letter_words.txt", "w")

words_lines = f_words.readlines()
 
count = 0
# Strips the newline character
for line in words_lines:
    line = line.upper().strip()
    count += 1
    if len(line) == 5:
        f_five.write(line + "\n")

f_words.close()
f_five.close()