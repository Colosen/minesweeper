import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# colours
BLUE = (128, 205, 224)
LIGHT_BLUE = (209, 246, 255)
GREY = (100, 100, 100)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BLUE)
        for i in range(20, WIDTH-20, 46):
            for j in range(20, HEIGHT-20, 46):
                pygame.draw.rect(WIN, LIGHT_BLUE, rect=(i, j, 48, 48), border_radius=5)
                pygame.draw.rect(WIN, GREY, rect=(i, j, 48, 48), width=2, border_radius=5)
        pygame.display.update()

    pygame.quit()


if __name__ == "main.py":
    main()

