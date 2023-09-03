import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # window setup
pygame.display.set_caption("PONG") # window title

FPS = 60 # frames per second constant
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    VELOCITY = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))
    
    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY
        
# drawing
def draw(win, paddles):
    win.fill(BLACK)
    
    for paddle in paddles:
        paddle.draw(win)
    
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue;
        else:
            pygame.draw.rect(win, WHITE, (WIDTH//2 - (PADDLE_WIDTH//2), i, 10, HEIGHT//20))

    pygame.display.update() # updates display and performs above drawing operations

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up = True)
    if keys[pygame.K_s] and left_paddle.y -+ left_paddle.VELOCITY + left_paddle.height <= HEIGHT:
        left_paddle.move(up = False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up = True)
    if keys[pygame.K_DOWN] and right_paddle.y -+ right_paddle.VELOCITY + right_paddle.height <= HEIGHT:
        right_paddle.move(up = False)
    

# Event Loop
def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Main Loop
    while run:
        clock.tick(FPS) # max of 60 frames per second
        draw(WIN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        
    pygame.quit()

if __name__ == '__main__': # ensures that this file is the entry point and not an imported module
    main()