from numpy import random
import numpy as np

board = list(range(1, 101))


def gen_snakes(x):
    dict_snk = {}
    v_max = len(board) - 10
    v_min = 10

    for i in range(x):
        key = random.randint(v_min, v_max)

        if key in dict_snk:
            key = random.randint(v_min, v_max)

        value = key - random.randint(5, 10)
        if value in dict_snk:
            value = key - random.randint(5, 10)

        dict_snk[key] = value

    # print(f"Snakes - {dict_snake}")

    return dict_snk


def gen_ladders(x):
    dict_lad = {}
    v_min = 5
    v_max = len(board) - 20
    for i in range(x):
        key = random.randint(v_min, v_max)
        if key in dict_lad or key in dict_snake:
            key = random.randint(v_min, v_max)

        value = key + random.randint(5, 10)
        if value in dict_lad or value in dict_snake:
            value = key + random.randint(5, 10)

        dict_lad[key] = value

    # print(f"Ladders - {dict_ladders}")

    return dict_lad


qtd = np.random.randint(5, 10)

dict_snake = gen_snakes(qtd)

dict_ladders = gen_ladders(qtd)
