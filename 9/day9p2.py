class Marble:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printline(root, num_marbles):
    oline = str(root.value)
    cmarble = root.right
    for _ in range(0, num_marbles-1):
        oline = oline + ' ' + str(cmarble.value)
        cmarble = cmarble.right
    print(oline)

m0 = Marble(0)
m1 = Marble(1)
m2 = Marble(2)
m0.right = m2
m0.left = m1
m1.right = m0
m1.left = m2
m2.right = m1
m2.left = m0
printline(m0, 3)


# players = 418
# last_marble_val = 70769 * 100
players = 9
last_marble_val = 26
player = -1
marble_val = 1
current_marble = Marble(0)
current_marble.right = current_marble
current_marble.left = current_marble
rootmarble = current_marble
scores = {}
for player_val in range(0, players):
    scores[player_val] = 0
while True:
    printline(rootmarble, marble_val)
    print(current_marble.value)
    player = (player + 1) % players
    if marble_val % 23 != 0:
        for _ in range(0,2):
            current_marble = current_marble.right
        newmarble = Marble(marble_val)
        newmarble.left = current_marble.left
        newmarble.right = current_marble
        current_marble.left = newmarble
        current_marble = newmarble
    else:
        for _ in range(0,7):
            current_marble = current_marble.left
        current_marble.left.right = current_marble.right
        current_marble.right.left = current_marble.left
        scores[player] += (marble_val + current_marble.value)
        current_marble = current_marble.right
    marble_val += 1
    if marble_val == last_marble_val+1:
        print(scores)
        break
    print("Player: ", player+1)
    print("marbleval: ", marble_val)
    print("")


# def get_index(last_index, num_marbles, is_23 = False):
#     if not is_23:
#         up_by_2 = last_index + 2
#         modded = up_by_2 % (num_marbles + 1)
#         if modded == 0:
#             modded += 1
#         return modded
#     else:
#         down_by_7 = last_index - 7
#         if down_by_7 < 0:
#             minv = 6 - last_index
#             val = num_marbles - 1 - minv
#             return val
#         modded = down_by_7 % (num_marbles - 1)
#         return modded

# players = 418
# last_marble_val = 70769 * 100
# player = -1
# marble_val = 1
# marbles = [0]
# index = 0
# scores = {}
# for player_val in range(0, players):
#     scores[player_val] = 0
# while True:
#     if marble_val % 10000 == 0:
#         print((marble_val / last_marble_val) * 100, "%")
#     player = (player + 1) % players
#     if marble_val % 23 != 0:
#         index = get_index(index, len(marbles))
#         marbles.insert(index, marble_val)
#     else:
#         index = get_index(index, len(marbles), True)
#         scores[player] += (marble_val + marbles[index])
#         del marbles[index]
#     marble_val += 1
        
#     if marble_val == last_marble_val +1:
#         # print("Player: ", player+1)
#         # print("index: ",index)
#         # print("marbleval: ", marble_val)
#         # print("marbles: ", marbles)
#         # print("")
#         print(scores)
#         highscore = 0
#         highplayer = -1
#         for iterplayer, score in scores.items():
#             if score > highscore:
#                 highscore = score
#                 highplayer = iterplayer
#         if highplayer > -1:
#             #pass
#             print(highscore)
#         break
#     # print("Player: ", player+1)
#     # print("index: ",index)
#     # print("marbleval: ", marble_val)
#     # print("marbles: ", marbles)
#     # print("")
