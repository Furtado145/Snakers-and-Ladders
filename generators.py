from numpy import random

qtd = random.randint(5, 10)
board = list(range(1, 101))


def gen_snakes(x):

    dict_snake = {}
    v_max = len(board) - 10
    v_min = 10
    
    for i in range(x):
        key = random.randint(v_min, v_max)
        value = key - random.randint(5, 10)

        board.pop(key)
        board.pop(value)

        dict_snake[key] = value

    print(f"Snakes - {dict_snake}")


def gen_ladders(x):
    dict_ladders = {}
    v_min = 5
    v_max = len(board)-20
    for i in range(x):
        key = random.randint(v_min, v_max)
        value = key + random.randint(5, 10)

        board.pop(key)
        board.pop(value)

        dict_ladders[key] = value
    
    print(f"Ladders - {dict_ladders}")


print(qtd) 

gen_snakes(qtd)
gen_ladders(qtd)

