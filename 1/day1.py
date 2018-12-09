counter = 0
with open('input.txt') as f:
    for line in f:
        multiplier = 1
        if line.startswith('-'):
            multiplier = -1
        counter = counter + (multiplier * int(line[1:]))
print(counter)
