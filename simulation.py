from guess import guess
from collections import Counter

lines = []
with open('wordlist.txt', encoding='utf-8-sig') as f:
    lines = [line.rstrip() for line in f]

def simulation():
    data = []
    dic = {}
    new = lines[:100]
    for word in new:
        data.append(int(guess(word)[-1]))
    c = Counter(data)
    print(c.items())
    avg = sum(data)/len(data)
    return avg
print(simulation())
