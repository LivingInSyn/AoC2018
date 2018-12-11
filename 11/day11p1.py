

grid_size = 300
fuel_cell = [ [0] * grid_size for _ in range(grid_size)]

def get_pvalue(serial_num, x, y):
    rack_id = x + 10

    step1 = rack_id * y
    step2 = step1 + serial_num
    step3 = step2 * rack_id

    plevel_str = str(((rack_id * y) + serial_num) * rack_id)
    plevel = 0
    if len(plevel_str) > 2:
        plevel = int(plevel_str[-3]) - 5
    return plevel

print(get_pvalue(8, 3, 5))
print(get_pvalue(57, 122, 79))
print(get_pvalue(39, 217, 196))
print(get_pvalue(71, 101, 153))

serial_num = 9221
#serial_num = 18
for xval in range(1, grid_size + 1):
    rack_id = xval + 10
    for yval in range(1, grid_size + 1):
        fuel_cell[xval-1][yval-1] = get_pvalue(serial_num, xval, yval)


topsum = (0, 0, 0)

for xval in range(1, grid_size + 1):
    for yval in range(1, grid_size + 1):
        blocksum = 0
        if xval == 33 and yval == 45:
            printvals = True
        else:
            printvals = False
        for x in range(xval, xval+3):
            for y in range(yval, yval+3):
                if y >= len(fuel_cell[0]) or x >= len(fuel_cell[0]):
                    continue
                blocksum = blocksum + fuel_cell[x-1][y-1]
                if printvals:
                    print("at: ", x, y)
                    print("Added: ", fuel_cell[x-1][y-1])
                    print("blocksum: ", blocksum)
        if blocksum > topsum[0]:
            topsum = (blocksum, xval, yval)

print(topsum)
