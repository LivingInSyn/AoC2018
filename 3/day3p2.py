from collections import namedtuple
#named tuple for the cuts
Cut = namedtuple('Cut', ['id', 'x', 'y', 'width', 'height'])
class ClaimedCut:
    def __init__(self, cutid):
        self.ids = []
        self.ids.append(cutid)
#parse the input
cuts = []
cutids = []
with open(r'C:\Users\jeremymill\Documents\AoC2018\3\input.txt') as f:
    for line in f:
        splitline = line.replace('\n','').replace(':','').split(' ')
        cid = int(splitline[0].replace('#', ''))
        x = int(splitline[2].split(',')[0])
        y = int(splitline[2].split(',')[1])
        width = int(splitline[3].split('x')[0])
        height = int(splitline[3].split('x')[1])
        cuts.append(Cut(cid, x, y, width, height))
        cutids.append(cid)
#init a 2d array
fabric = [[None]*1000 for _ in range(1000)]
#foreach cut, increase the array value
for cut in cuts:
    for xval in range(cut.x, cut.x + cut.width):
        for yval in range(cut.y, cut.y + cut.height):
            if fabric[xval][yval] is None:
                fabric[xval][yval] = ClaimedCut(cut.id)
            else:
                fabric[xval][yval].ids.append(cut.id)
                for cutid in  fabric[xval][yval].ids:
                    if cutid in cutids:
                        cutids.remove(cutid)
            # fabric[xval][yval] += 1
            # if fabric[xval][yval] > 1 and cut.id in cutids:
            #     cutids.remove(cut.id)
#print the results
print("cutids: ", cutids)


