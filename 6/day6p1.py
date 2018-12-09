from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])

def manhattan_distance(CoordinateA, CoordinateB):
    return abs(CoordinateA.x - CoordinateB.x) + abs(CoordinateA.y - CoordinateB.y)
#returns a key, or None on a tie
def min_coord_key(start, coords, gridsize):
    minkey = None
    mindist = gridsize * gridsize
    for cname, coord in coords.items():
        dist = manhattan_distance(start, coord)
        if dist < mindist:
            minkey = [cname]
            mindist = dist
        elif dist == mindist:
            minkey.append(cname)
    if len(minkey) == 1:
        return minkey[0]
    else:
        return None


gridsize = 400
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
infinites = set()
#find the infinites
for yval in range(0,gridsize):
    for xval in {0, gridsize-1}:
        min_key = None
        min_val = None
        for key, coord in coordinates.items():        
            dist = manhattan_distance(coord, Coordinate(xval, yval))
            if min_key is None or dist < min_val:
                min_key = key
                min_val = dist
        if min_key is not None:
            infinites.add(min_key)
for xval in range(0, gridsize):
    for yval in {0, gridsize-1}:
        min_key = None
        min_val = None
        for key, coord in coordinates.items():
            dist = manhattan_distance(coord, Coordinate(xval, yval))
            if min_key is None or dist < min_val:
                min_key = key
                min_val = dist
        if min_key is not None:
            infinites.add(min_key)

finalcounts = {}
#populate finalcounts for ease
for cname, coord in coordinates.items():
    if cname not in infinites:
        finalcounts[cname] = 1
# spiral out from the coords that aren't eliminated or infinite to find the max
# 
eliminated = set()
cols_away = 1
AllInfOrElim = False
while not AllInfOrElim:
    for cname, coord in coordinates.items():
        #ignore the eliminated vals, or the infinites
        if cname in infinites or cname in eliminated:
            continue
        added = False
        for addx in range(-1 * cols_away, cols_away+1):
            #do the whole column
            if abs(addx) == cols_away:
                for addy in range(-1*cols_away, cols_away+1):
                    minkey = min_coord_key(Coordinate(coord.x + addx, coord.y + addy), coordinates, gridsize)
                    if minkey is None:
                        pass
                    elif minkey == cname:
                        finalcounts[cname] += 1
                        added = True
            #otherwise do just positive top and botton
            else:
                for addy in {-1*cols_away, cols_away}:
                    minkey = min_coord_key(Coordinate(coord.x + addx, coord.y + addy), coordinates, gridsize)
                    if minkey is None:
                        pass
                    elif minkey == cname:
                        finalcounts[cname] += 1
                        added = True                    
        #if we didn't add to the finalcounts, we're done with this cname
        if not added:
            eliminated.add(cname)
    #if every cname is in infinites or eliminated, break
    count = 0
    for cname in coordinates:        
        if cname in infinites or cname in eliminated:
            count += 1
        if count == len(coordinates):
            AllInfOrElim = True
    cols_away += 1
    #print(cols_away)
print(finalcounts)
maxval = 0
maxkey = ''
for cname, count in finalcounts.items():
    if count > maxval:
        maxval = count
        maxkey = cname
print(maxval, maxkey)

