from collections import defaultdict
import random

import matplotlib.pyplot as plt
import numpy as np

pile = defaultdict(dict)


def sandpile(size="3x3", sand_min=3, sand_max=3, initial_min=10, initial_max=10):
    try:
        r, c = map(int, size.strip().split('x'))
        pile["r"] = r
        pile["c"] = c
    except Exception:
        print("Enter in the form <int>x<int> (eg, 4x4)")
        raise
    for row in range(1, r+1):
        for col in range(1, c+1):
            pile[(row, col)]["max"] = random.randint(sand_min, sand_max)
            pile[(row, col)]["#"] = random.randint(initial_min, initial_max)
    return pile


def run_pile(pile, save=False, labels=False):
    pad_pile(pile)
    count = 0
    while pile_unstable(pile):
        count += 1
        collapse_pile(pile)

    unpad_pile(pile)
    print("Ran for %i iterations" % count)
    plot(pile, save, labels)


def plot(pile, save, labels):
    numpy_array = convert_to_numpy_array(pile)
    plt.matshow(numpy_array, cmap=plt.get_cmap('gist_rainbow'))
    plt.colorbar(orientation='horizontal')
    plt.axis('off')
    if labels:
        it = np.nditer(numpy_array, flags=['multi_index'])
        while not it.finished:
            plt.text(it.multi_index[1], it.multi_index[0], int(it[0]), va='center', ha='center')
            it.iternext()
    if save:
        plt.savefig("./sandpile.png", bbox_inches='tight')
    plt.show()


def convert_to_numpy_array(pile):
    r = pile["r"]
    c = pile["c"]
    np_array = np.empty(shape=(r, c))
    for row in range(r):
        for col in range(c):
            np_array[row][col] = pile[(row+1, col+1)]["#"]
    return np_array


def pad_pile(pile):
    r = pile["r"]
    c = pile["c"]

    for col in range(c+2):
        pile[(0, col)]["max"] = 0
        pile[(0, col)]["#"] = 0
        pile[(r+1, col)]["max"] = 0
        pile[(r+1, col)]["#"] = 0

    for row in range(1, r+1):
        pile[(row, 0)]["max"] = 0
        pile[(row, 0)]["#"] = 0
        pile[(row, c+1)]["max"] = 0
        pile[(row, c+1)]["#"] = 0

    return pile

    # for row in range(r+2):
    #     for col in range(c+2):
    #         pile[(row, col)]["max"] = 0
    #         pile[(row, col)]["#"] = 0


def unpad_pile(pile):
    r = pile["r"]
    c = pile["c"]

    for col in range(c+2):
        del pile[(0, col)]
        del pile[(r+1, col)]

    for row in range(1, r+1):
        del pile[(row, 0)]
        del pile[(row, c+1)]
    return pile


def pile_unstable(pile):
    r = pile["r"]
    c = pile["c"]
    for row in range(1, r+1):
        for col in range(1, c+1):
            if pile[(row, col)]["#"] > pile[(row, col)]["max"]:
                return True
    return False


def get_toppable_squares(pile):
    toppable_squares = []
    r = pile["r"]
    c = pile["c"]
    for row in range(1, r+1):
        for col in range(1, c+1):
            if pile[(row, col)]["#"] > pile[(row, col)]["max"]:
                toppable_squares.append((row, col))
    return toppable_squares


def collapse_pile(pile):
    toppable_squares = get_toppable_squares(pile)
    for square in toppable_squares:
        topple(square, pile)


def topple(square, pile):
    # toppling order is clockwise - LEFT, TOP, RIGHT, BOTTOM
    r, c = square[0], square[1]
    if pile[square]["#"] >= 1:
        pile[square]["#"] -= 1
        pile[(r-1, c)]["#"] += 1

    if pile[square]["#"] >= 1:
        pile[square]["#"] -= 1
        pile[(r, c+1)]["#"] += 1

    if pile[square]["#"] >= 1:
        pile[square]["#"] -= 1
        pile[(r+1, c)]["#"] += 1

    if pile[square]["#"] >= 1:
        pile[square]["#"] -= 1
        pile[(r, c-1)]["#"] += 1
    return pile
