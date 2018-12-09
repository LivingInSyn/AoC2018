has2 = 0
has3 = 0
with open("C:\\Users\\jeremymill\\Documents\\AoC2018\\2\\input.txt") as f:
    for line in f:
        linecopy = line
        seentwo = False
        seenthree = False
        while len(linecopy) > 0:
            if linecopy.count(linecopy[0]) == 2 and not seentwo:
                seentwo = True
                has2 = has2 + 1
            elif linecopy.count(linecopy[0]) == 3 and not seenthree:
                seenthree = True
                has3 = has3 + 1
            if seenthree and seentwo:
                break
            linecopy = linecopy.replace(linecopy[0], '')
            
print(has2, has3)
print(has2 * has3)