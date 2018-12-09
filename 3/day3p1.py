from collections import namedtuple
#named tuple for the cuts
Cut = namedtuple('Cut', ['id', 'x', 'y', 'width', 'height'])
#parse the input
cuts = []
with open(r'C:\Users\jeremymill\Documents\AoC2018\3\input.txt') as f:
    for line in f:
        splitline = line.replace('\n','').replace(':','').split(' ')
        cid = int(splitline[0].replace('#', ''))
        x = int(splitline[2].split(',')[0])
        y = int(splitline[2].split(',')[1])
        width = int(splitline[3].split('x')[0])
        height = int(splitline[3].split('x')[1])
        cuts.append(Cut(cid, x, y, width, height))
#init a 2d array
fabric = [[0]*1000 for _ in range(1000)]
print(fabric)
#foreach cut, increase the array value
overlaps = 0
for cut in cuts:
    for xval in range(cut.x, cut.x + cut.width):
        for yval in range(cut.y, cut.y + cut.height):
            fabric[xval][yval] += 1
            if fabric[xval][yval] == 2:
                overlaps += 1
#print the results
print("overlaps: ", overlaps)


