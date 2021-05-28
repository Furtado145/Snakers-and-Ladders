# %%
import numpy as np


def snakes_and_ladders(pos):
    dict_sal = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22,
                3: 16, 5: 7, 15: 25, 18: 20, 21: 32}

    if pos in dict_sal:
        if pos < dict_sal.get(pos):
            print(f'    {pos} -- ESCADA!!! --> {dict_sal.get(pos)}')
        else:
            print(f'    {pos} -- COBRA!!! --> {dict_sal.get(pos)}')
        pos = dict_sal.get(pos)

    return pos


def roll_die(player):
    dado = np.random.randint(1, 6)
    print('    Valor do dado:', dado)
    player += dado
    # CHECK POSITION
    player = snakes_and_ladders(player)
    print('    final da rodada pos: ', player)
    return player


# %%

# Wining Counting
p1_wins = p2_wins = 0

# INITIAL POSITIONS
p1 = p2 = 1

# GOAL
max = 100


# %%

# STARTING
while True:
    print(f"\nPlayer 1 - posicao atual = {p1}")
    p1 = roll_die(p1)
    if p1 > max:
        p1_wins += 1
        print('Player1 Wins')
        break

    print(f"\nPlayer 2 - posicao atual = {p2}")
    p2 = roll_die(p2)
    if p2 > max:
        p2_wins += 1
        print('Player2 Wins')
        break
 
# %%
