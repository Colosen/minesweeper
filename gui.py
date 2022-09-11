import pygame
from pygame import font

pygame.init()
pygame.font.init()

# creating font
my_font = pygame.font.SysFont('Comic Sans MS', 35)

# creating Pygame window
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# creating cover
COVER = pygame.Surface((WIDTH, HEIGHT))

# colours
BLUE = (128, 205, 224)
LIGHT_BLUE = (209, 246, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)

def main(minefield):
    run = True
    while run: # loop during the time the window is open
        for event in pygame.event.get(): # loop through events indefinitely
            if event.type == pygame.QUIT:
                run = False # terminate program

        WIN.fill(BLUE)
        COVER.fill(BLUE)
        create_squares(WIN)
        print_numbers(minefield)
        create_squares(COVER)
        WIN.blit(COVER, (0, 0))
        pygame.display.update()

    pygame.quit()


def create_squares(window):
    SIDE_LENGTH = 46
    BORDER_RADIUS = 5
    BORDER_WIDTH = 2
    for i in range(20, WIDTH-20, 46): # draw 100 squares in 460x460 square
        for j in range(20, HEIGHT-20, 46):
            pygame.draw.rect(window, LIGHT_BLUE, rect=(i, j, SIDE_LENGTH, SIDE_LENGTH), border_radius=BORDER_RADIUS) # light blue squares
            pygame.draw.rect(window, GREY, rect=(i, j, SIDE_LENGTH, SIDE_LENGTH), width=BORDER_WIDTH, border_radius=BORDER_RADIUS) # grey border around every square


def print_numbers(minefield):

    for i in range(0, 10):
        for j in range(0, 10):
            text_surface = my_font.render(str(minefield[i][j]), True, BLACK)
            x = 20 + 15 + 46*i
            y = 20 + 15 + 46*j
            WIN.blit(text_surface, (x, y))


if __name__ == "main.py":
    main()

