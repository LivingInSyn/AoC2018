import re

class PointOfLight:
    def __init__(self):
        self.x = None
        self.y = None
        self.vx = None
        self.vy = None

    def tick(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        return (self.x, self.y)

def maxmins(points):
    maxx = -100000
    minx = 100000
    maxy = -100000
    miny = 100000
    for pol in points:
        maxx = max(maxx, pol.x)
        minx = min(minx, pol.x)
        maxy = max(maxy, pol.y)
        miny= min(miny, pol.y)
    return (maxx, minx), (maxy, miny)

def tick_print_state(points, counter):
    #tick the points
    while True:
        counter = counter + 1
        for pol in points:
            pol.tick()
        #update maxmin
        maxmin_x, maxmin_y = maxmins(points)
        #range, and translations
        xrange = maxmin_x[0] + abs(maxmin_x[1]) if maxmin_x[1] < 0 else maxmin_x[0] - maxmin_x[1]
        if maxmin_x[1] == 0:
            xrange += 1
        yrange = maxmin_y[0] + abs(maxmin_y[1]) if maxmin_y[1] < 0 else maxmin_y[0] - maxmin_y[1]
        if maxmin_y[1] == 0:
            yrange += 1
        print(xrange, yrange)
        if xrange < 101 and yrange < 101:
            break
    xtranslation = abs(maxmin_x[1]) if maxmin_x[1] < 0 else -1 * maxmin_x[1]
    ytranslation = abs(maxmin_y[1]) if maxmin_y[1] < 0 else -1 * maxmin_y[1]
    #counting down y vals
    #for yval in range(maxmin_y[0] + ytranslation, -1, -1):
    for yval in range(0, maxmin_y[0] + ytranslation + 1):
        #build an array for the x vals
        line = ['.'] * (xrange + 1)
        for pol in points:
            if pol.y + ytranslation == yval:
                line[pol.x + xtranslation] = '#'
        outline = ''
        for ch in line:
            outline = outline + str(ch)
        print(outline)
    return counter

# points = []
# pol = PointOfLight()
# pol.x = 2
# pol.y = 4
# points.append(pol)
# pol = PointOfLight()
# pol.x = -1
# pol.y = 3
# points.append(pol)
# pol = PointOfLight()
# pol.x = 5
# pol.y = 3
# points.append(pol)
# maxmin_x, maxmin_y = maxmins(points)
# tick_print_state(points, maxmin_x, maxmin_y, True)
        


points = []
with open(r'C:\Users\jeremymill\Documents\AoC2018\10\input.txt') as f:
    for line in f:
        parse_line = re.findall(r'(-)?(\d+)', line)
        pol = PointOfLight()
        if len(parse_line) != 4:
            raise Exception("invalid line")
        for x in range(0, 4):
            mult = 1 if not parse_line[x][0] else -1
            if x == 0:
                pol.x = int(parse_line[x][1]) * mult
            elif x == 1:
                pol.y = int(parse_line[x][1]) * mult
            elif x == 2:
                pol.vx = int(parse_line[x][1]) * mult
            elif x == 3:
                pol.vy = int(parse_line[x][1]) * mult
        points.append(pol)
#print init state
#tick_print_state(points, True)
counter = 0
while True:
    uinput = input("Enter to continue, z to quit: ")
    if uinput == 'z':
        print(counter)
        break
    counter = tick_print_state(points, counter)
    
