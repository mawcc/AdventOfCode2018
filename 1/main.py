file = open("./data.txt", "r")
lines = file.readlines()
frequency = 0
reached_frequencies = []
duplicate_found = False
while not duplicate_found:
    for line in lines:
        frequency += int(line)
        if frequency in reached_frequencies:
            print("found twice: ", frequency)
            duplicate_found = True
        else:
            reached_frequencies.append(frequency)
            print(len(reached_frequencies))