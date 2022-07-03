
lines = []
with open('wordlist.txt') as f:
    lines = [line.rstrip() for line in f]

print(lines)


def guess(word):

    guesses = 0
    first_word = "stare"
    point_values = {}
