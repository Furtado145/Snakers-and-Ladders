# %% 

import numpy as np
import generators

# %%


def gen_dict_sal():
    qtd = np.random.randint(5, 10)

    snk = generators.gen_snakes(5)
    lad = generators.gen_ladders(5)

    dict_sal = snk + lad
    
# %%
def snake_and_ladders(pos):
    
    pos = gen_dict_sal.dict_sal.get(pos, pos)

    return pos


# %%
def roll_die(player):
    dado = np.random.randint(1, 6)
    player += dado

    player = snake_and_ladders(player)

    return player


# Winning count
p1_wins = p2_wins = 0

# How many games will be played?
num_games = 10

# Lets play

for i in range(num_games):

    # Initial positions
    p1 = p2 = 1

    # GOAL
    goal = 100

    while True:
        msg = f"Rodada {i+1}: "

        p1 = roll_die(p1)
        if p1 > goal:
            p1_wins += 1
            print(msg + "Player1 Venceu!")
            break

        p2 = roll_die(p2)
        if p2 > goal:
            p2_wins += 1
            print(msg + "Player2 Venceu!")
            break

    i += 1

print(f"""Palyer 1 - {p1_wins}
Player 2 - {p2_wins} """)

# %%
