import collections

# calculate checksum
file = open("./data.txt")
lines = file.readlines()
twocount = 0
threecount = 0 
for line in lines:
    chars = list(line)
    counter = collections.Counter(chars)
    if 2 in counter.values():
        twocount += 1
    if 3 in counter.values():
        threecount +=1
print("checksum", twocount * threecount)

# find lines with only one differing character
for line1 in lines:
    for line2 in lines:
        if line1 == line2:
            break
        chars1 = list(line1)
        chars2 = list(line2)
        same = [i for i, j in zip(chars1, chars2) if i == j]
        if (len(chars1) == len(same) + 1):
            print("similar: ", line1, " <=> ", line2)
            print("same chars: ", "".join(same))