import numpy as np
from generators import gen_snakes, gen_ladders


# Call generators to get new skakes and ladders
def gen_dict_sal():
    gen_dict_sal.qtd = np.random.randint(5, 10)
    snk = gen_snakes(gen_dict_sal.qtd)
    lad = gen_ladders(gen_dict_sal.qtd)

    snk.update(lad)
    return snk


# Func to verify is the posiction is a key value of a snake or a ladder
def snake_and_ladders(pos):
    dict_sal = gen_dict_sal()

    pos = dict_sal.get(pos, pos)

    return pos


# Func to roll die
def roll_die(player):
    dado = np.random.randint(1, 6)
    player += dado

    player = snake_and_ladders(player)

    return player


# Getting num of snakes
l_snakes = []

# Winning count
p1_wins = p2_wins = 0

# How many games will be played?
num_games = 10000

# Lets play

for i in range(num_games):
    # Active the func to gen new snakes and ladders every match
    sal = gen_dict_sal()
    l_snakes.append(gen_dict_sal.qtd)

    # Initial positions
    p1 = p2 = 1

    # GOAL
    goal = 100

    while True:
        msg = f"Rodada {i + 1}: "

        p1 = roll_die(p1)
        if p1 > goal:
            p1_wins += 1
            # print(msg + "Player1 Venceu!")
            break

        p2 = roll_die(p2)
        if p2 > goal:
            p2_wins += 1
            # print(msg + "Player2 Venceu!")
            break

    i += 1

print(f"Palyer 1 - {p1_wins}\nPlayer 2 - {p2_wins}\nMédia de cobras = {sum(l_snakes) / num_games}")
