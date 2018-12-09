from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])

def manhattan_distance(CoordinateA, CoordinateB):
    return abs(CoordinateA.x - CoordinateB.x) + abs(CoordinateA.y - CoordinateB.y)

def all_coord_md_lt(coordinates, testcoord, dist):
    if testcoord.x == 6 and testcoord.y == 6:
        a = 'hi'
    running_dist = 0
    for cname, coord in coordinates.items():
        running_dist += manhattan_distance(coord, testcoord)
        if running_dist >= dist:
            return False
    return True

gridsize = 400
distsize = 10000
#parse the coords from the file
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
counter = 0
coordinates = {}
#build the set of points
with open(r'C:\Users\jeremymill\Documents\AoC2018\6\input.txt') as f:
    for line in f:
        line = line.strip().split(', ')
        x = int(line[0])
        y = int(line[1])
        coordinates[letters[counter]] = Coordinate(x, y)
        counter += 1

#get and set the max x, min x, max y, min y
max_x = 0
max_y = 0
min_x = gridsize
min_y = gridsize
for cname, coord in coordinates.items():
    if coord.x < min_x:
        min_x = coord.x 
    if coord.x > max_x:
        max_x = coord.x
    if coord.y < min_y:
        min_y = coord.y 
    if coord.y > max_y:
        max_y = coord.y
#find the middle to spiral out from
middlex = max_x - min_x
middley = max_y - min_y
#spiral out from the middle
area = 0
if all_coord_md_lt(coordinates, Coordinate(middlex, middley), distsize):
    area += 1
cols_away = 1
added_one = True
added_first = False
while added_one or not added_first:
    added_one = False
    for addx in range(-1*cols_away, cols_away + 1):
        #do the whole column
        if abs(addx) == cols_away:
            for addy in range(-1*cols_away, cols_away+1):
                if all_coord_md_lt(coordinates, Coordinate(middlex + addx, middley + addy), distsize):
                    #print('adding ', middlex + addx, middley + addy)
                    area += 1
                    added_one = True
                    added_first = True
        #otherwise do just positive top and botton
        else:
            for addy in {-1*cols_away, cols_away}:
                if all_coord_md_lt(coordinates, Coordinate(middlex + addx, middley + addy), distsize):
                    #print('adding ', middlex + addx, middley + addy)
                    area += 1
                    added_one = True
                    added_first = True
    cols_away += 1
print(area)