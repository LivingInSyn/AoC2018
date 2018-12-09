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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
with open(r'C:\Users\jeremymill\Documents\AoC2018\5\input.txt') as f:
    for line in f:
        minlength = 9297
        winningletter = None
        line = line.strip()
        #length = len(remove_pairs(line))
        for letter in alphabet:
            testline = line.replace(letter, '')
            testline = testline.replace(letter.upper(), '')
            length = len(remove_pairs(testline))
            if length < minlength:
                minlength = length
                winningletter = letter
        print(minlength)
        print(winningletter)



