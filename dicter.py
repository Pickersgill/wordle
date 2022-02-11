import json
import re

src = open("./dictionary_compact.json")

data = json.load(src)

n = 0
fives = []

for i in data:
    w = i.lower()
    if re.search(r"^[a-z]{5}$", w):
        fives.append(w)

out = open("./words.txt", "w")
out.write("\n".join(fives))

print(fives)


