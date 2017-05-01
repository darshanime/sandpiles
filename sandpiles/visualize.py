import random
import glob
import os
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import imageio

pile = defaultdict(dict)


def sandpile(size="3x3", sand_min=3, sand_max=3, initial_min=10, initial_max=10):
    """
    size --> the dimensions of the grid. Can be rectangles
    sand_min --> the minimum capacity of any square
    sand_max --> the maximum capacity of any square
    initial_min --> the minimum initial sand on any square
    initial_max --> the maximum initial sand on any square
    """
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


def run_pile(pile, picture=False, labels=False, gif=False):
    pad_pile(pile)
    count = 0
    while pile_unstable(pile):

        if gif:
            make_snap(pile, count)

        count += 1
        collapse_pile(pile)

    if gif:
        make_snap(pile, count)
        if create_gif():
            print("Created sandpiles.gif")
        else:
            print("Could not create sandpiles.gif")

    unpad_pile(pile)
    print("Ran for %i iterations" % count)
    plt = plot(pile, labels)
    if picture:
        plt.colorbar(orientation='horizontal')
        plt.savefig('./sandpiles.png', bbox_inches='tight')


def create_gif():
    with imageio.get_writer('./sandpiles.gif', mode='I', duration=0.33) as writer:
        for filename in glob.glob('/tmp/sandpile_*.png'):
            image = imageio.imread(filename)
            writer.append_data(image)
            # the image is in memory, can be deleted on disk
            os.remove(filename)
    return True


def make_snap(pile, count):
    plt = plot(pile, labels=False)
    filename = "/tmp/sandpile_%s.png" % count
    plt.savefig(filename, bbox_inches='tight')


def plot(pile, labels):
    numpy_array = convert_to_numpy_array(pile)
    plt.matshow(numpy_array, cmap=plt.get_cmap('gist_rainbow'))
    plt.axis('off')
    if labels:
        it = np.nditer(numpy_array, flags=['multi_index'])
        while not it.finished:
            plt.text(it.multi_index[1], it.multi_index[0], int(it[0]), va='center', ha='center')
            it.iternext()
    return plt


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
