def remove_pairs(inputstring):
    stringindex = 1
    while stringindex < len(inputstring):
        letterone = inputstring[stringindex-1]
        lettertwo = inputstring[stringindex]
        if letterone.lower() == lettertwo.lower():
            if letterone.isupper() and lettertwo.islower() or letterone.islower() and lettertwo.isupper():
                inputstring = inputstring[:stringindex-1] + inputstring[stringindex+1:]
                stringindex = max(1, stringindex - 1)
                #stringindex -= 1
            else:
                stringindex += 1
        else:
            stringindex += 1
    return inputstring

with open(r'C:\Users\jeremymill\Documents\AoC2018\5\input.txt') as f:
    for line in f:
        res = remove_pairs(line)
        print("res: ", res)
        print("len: ", len(res))
        print("len: ", len(res.strip()))
#9296 was right



