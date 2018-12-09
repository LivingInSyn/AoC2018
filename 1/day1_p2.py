input_nums = []
with open('input.txt') as f:
    for line in f:
        multiplier = 1
        if line.startswith('-'):
            multiplier = -1
        input_nums.append(multiplier * int(line[1:]))
seen = [0]
counter = 0
sawdouble = False
while not sawdouble:
    for in_num in input_nums:
        counter = counter + in_num
        if counter in seen:
            print('found it!, ', counter)
            sawdouble = True
            break
        seen.append(counter)
        #print(seen, counter)
        #input()
        #print(len(seen), counter)







# with open('input.txt') as f:
#     for line in f:
#         multiplier = 1
#         if line.startswith('-'):
#             multiplier = -1
#         counter = counter + (multiplier * int(line[1:]))


#         if counter in seen:
#             print('found it!')
#             print(counter)
#             sawdouble = True
#             break
#         else:
#             pass
#             #print("not in seen...")
#         seen.append(counter)
#         if len(seen) > 20:
#             print(seen)
#             break
# if not sawdouble:
#     if counter in seen:
#         print('saw at end', counter)
#     else:
#         print('never seen')