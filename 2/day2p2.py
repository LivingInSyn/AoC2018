def load_words(path):
    input_lines = []
    with open("C:\\Users\\jeremymill\\Documents\\AoC2018\\2\\input.txt") as f:
        for line in f:
            input_lines.append(line.replace("\n",''))
    return input_lines


def word_difference(word1, word2):
    difference = 0
    for index in range(0, len(word1)):
        if word1[index] != word2[index]:
            difference = difference + 1
    return difference

def in_common(word1, word2):
    output = ''
    for index in range(0, len(word1)):
        if word1[index] == word2[index]:
            output = output + word1[index]
    return output

if __name__ == "__main__":
    #load input
    input_lines = load_words("C:\\Users\\jeremymill\\Documents\\AoC2018\\2\\input.txt")
    min_difference = 1000000
    words = None
    #iterate through the words, comparing all of them
    for primindex in range(0,len(input_lines)):
        for secindex in range(primindex + 1, len(input_lines)):
            #get the difference
            difference = word_difference(input_lines[primindex], input_lines[secindex])
            #if it's less than the current saved
            if difference < min_difference:
                min_difference = difference
                words = (input_lines[primindex], input_lines[secindex])
    #print the resulting commonality
    print(in_common(words[0], words[1]))
