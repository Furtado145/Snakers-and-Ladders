import numpy as np

board = list(range(1, 101))


# Generate a dict of random snakes in game
def gen_snakes(x):
    dict_snk = {}
    v_max = len(board) - 10
    v_min = 10

    for i in range(x):
        key = np.random.randint(v_min, v_max)

        if key in dict_snk:
            key = np.random.randint(v_min, v_max)

        value = key - np.random.randint(5, 10)
        if value in dict_snk:
            value = key - np.random.randint(5, 10)

        dict_snk[key] = value

    return dict_snk


# Generate a dict of random ladders in game
def gen_ladders(x):
    snk = gen_snakes(x)

    dict_lad = {}
    v_min = 5
    v_max = len(board) - 20

    for i in range(x):
        key = np.random.randint(v_min, v_max)
        if key in dict_lad or key in snk:
            key = np.random.randint(v_min, v_max)

        value = key + np.random.randint(5, 10)
        if value in dict_lad or value in snk:
            value = key + np.random.randint(5, 10)

        dict_lad[key] = value

    return dict_lad
