import pygame
from random import randrange

LENGTH, HEIGHT = 10, 10
BOMBS = 20


def create_minefield():
    minefield = [[0 for i in range(LENGTH)] for j in range(HEIGHT)]

    counter = 0
    while counter <= BOMBS:
        x = randrange(0, LENGTH)
        y = randrange(0, HEIGHT)
        if minefield[x][y] != -1: # bombs are denoted by -1
            minefield[x][y] = -1
            counter += 1
    
    pretty_print(minefield)


def pretty_print(minefield):
    global LENGTH
    global HEIGHT
    SPACE = 2
    gap = 0
    for i in range(0, LENGTH):
        for j in range(0, HEIGHT):
            gap = SPACE-len(str(minefield[i][j]))
            print(gap*" "+str(minefield[i][j]), end="")
        print()


create_minefield()