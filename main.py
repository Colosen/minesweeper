from random import randrange
import gui

LENGTH, HEIGHT = 10, 10
BOMBS = 20
minefield = []


def create_minefield():
    global minefield
    minefield = [[0 for i in range(LENGTH)] for j in range(HEIGHT)]

    counter = 0
    while counter <= BOMBS:
        x = randrange(0, LENGTH)
        y = randrange(0, HEIGHT)
        if minefield[x][y] != -1: # bombs are denoted by -1
            minefield[x][y] = -1
            counter += 1
    
    pretty_print(minefield)
    return minefield


def place_numbers():
    global minefield
    for i in range(0, LENGTH):
        for j in range(0, HEIGHT):
            if minefield[i][j] != -1:
                neighbours = count_neighbours(i, j)
                minefield[i][j] = neighbours
    print("Bombs placed!!")
    pretty_print(minefield)


@staticmethod
def count_neighbours(a, b):
    neighbours = 0
    for i in (a-1, a, a+1):
        for j in (b-1, b, b+1):
            if i != a or j != b: # we do not need to count the square itself whose neighbours we're counting
                if i in range(0, 10) and j in range(0, 10): # to check if the square is within bounds
                    if minefield[i][j] == -1: #neighbour at i, j located
                        neighbours += 1
    return neighbours


@staticmethod
def pretty_print(minefield):
    SPACE = 2
    gap = 0
    for i in range(0, LENGTH):
        for j in range(0, HEIGHT):
            gap = SPACE - len(str(minefield[i][j]))
            print(gap*" " + str(minefield[i][j]), end="")
        print()


create_minefield()
place_numbers()
gui.main()