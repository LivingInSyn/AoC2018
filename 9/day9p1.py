def get_index(last_index, num_marbles, is_23 = False):
    if not is_23:
        up_by_2 = last_index + 2
        modded = up_by_2 % (num_marbles + 1)
        if modded == 0:
            modded += 1
        return modded
    else:
        down_by_7 = last_index - 7
        if down_by_7 < 0:
            minv = 6 - last_index
            val = num_marbles - 1 - minv
            return val
        modded = down_by_7 % (num_marbles - 1)
        return modded

lasti = 3
num_marbles = 86
get_index(3, 86, True)



players = 418
last_marble_val = 70769
player = -1
marble_val = 1
marbles = [0]
index = 0
scores = {}
for player_val in range(0, players):
    scores[player_val] = 0
while True:
    player = (player + 1) % players
    if marble_val % 23 != 0:
        index = get_index(index, len(marbles))
        marbles.insert(index, marble_val)
    else:
        index = get_index(index, len(marbles), True)
        scores[player] += (marble_val + marbles[index])
        del marbles[index]
    marble_val += 1
        
    if marble_val == last_marble_val+1:
        # print("Player: ", player+1)
        # print("index: ",index)
        # print("marbleval: ", marble_val)
        # print("marbles: ", marbles)
        # print("")
        print(scores)
        highscore = 0
        highplayer = -1
        for iterplayer, score in scores.items():
            if score > highscore:
                highscore = score
                highplayer = iterplayer
        if highplayer > -1:
            #pass
            print(highscore)
        break
    # print("Player: ", player+1)
    # print("index: ",index)
    # print("marbleval: ", marble_val)
    # print("marbles: ", marbles)
    # print("")
