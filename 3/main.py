
import re

regexp = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

def build_coords_array(line):
    match = regexp.match(line)
    #id = match.group(0)
    x = int(match.group(2))
    y = int(match.group(3))
    w = int(match.group(4))
    h = int(match.group(5))
    result = []
    for i in range(x, x + w):
        for j in range(y, y + h):
            result.append((i, j))
    return result

file = open("./data.txt", "r")
lines = file.readlines()
sum = []
current = []
result = []
for line in lines:
    current = build_coords_array(line)
    if len(sum) > 0:
        overlap = list(set(sum) & set(current))
        if len(overlap) > 0:
            result.extend(overlap)
    sum.extend(current)
    
print("total overlaps: ", len(result))
unique = list(set(result))
print("unque overlaps: ", len(unique))

for line in lines:
    current = build_coords_array(line)
    overlap = list(set(unique) & set(current))
    if len(overlap) == 0:
        print("not overlapping: ", line)
