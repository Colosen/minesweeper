import pygame

pygame.init()

# creating Pygame window
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# colours
BLUE = (128, 205, 224)
LIGHT_BLUE = (209, 246, 255)
GREY = (100, 100, 100)


def main():
    run = True
    while run: # loop during the time the window is open
        for event in pygame.event.get(): # loop through events indefinitely
            if event.type == pygame.QUIT:
                run = False # terminate program

        WIN.fill(BLUE)
        create_squares()
        pygame.display.update()

    pygame.quit()


def create_squares():
    SIDE_LENGTH = 46
    BORDER_RADIUS = 5
    BORDER_WIDTH = 2
    for i in range(20, WIDTH-20, 46): # draw 100 squares in 460x460 square
        for j in range(20, HEIGHT-20, 46):
            pygame.draw.rect(WIN, LIGHT_BLUE, rect=(i, j, SIDE_LENGTH, SIDE_LENGTH), border_radius=BORDER_RADIUS) # light blue squares
            pygame.draw.rect(WIN, GREY, rect=(i, j, SIDE_LENGTH, SIDE_LENGTH), width=BORDER_WIDTH, border_radius=BORDER_RADIUS) # grey border around every square


if __name__ == "main.py":
    main()

