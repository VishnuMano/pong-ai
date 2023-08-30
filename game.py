import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # window setup
pygame.display.set_caption("PONG") # window title

# Event Loop
def main():
    run = True
    # Main Loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == '__main__':
    main()