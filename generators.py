from numpy import random
from numpy.lib import deprecate_with_doc

board = list(range(1, 101))


def gen_snakes(x):

    dict_snake = {}
    v_max = len(board) - 10
    v_min = 10
    
    for i in range(x):
        key = random.randint(v_min, v_max)
        value = key - random.randint(5, 10)

        if key in dict_snake:
            key = random.randint(v_min, v_max)
        elif value in dict_snake:
            value = key - random.randint(5, 10)
        else:
            dict_snake[key] = value

    print(f"Snakes - {dict_snake}")


def gen_ladders(x):
    dict_ladders = {}
    v_min = 5
    v_max = len(board)-20
    for i in range(x):
        key = random.randint(v_min, v_max)
        value = key + random.randint(5, 10)

        if key in dict_ladders:
            key = random.randint(v_min, v_max)
        elif value in dict_ladders:
            value = random.randint(5, 10)
        else:
            dict_ladders[key] = value
    
    print(f"Ladders - {dict_ladders}")
