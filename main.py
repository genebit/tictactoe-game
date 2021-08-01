
import pygame
import sys

pygame.init()

BLACK = (25, 25, 25)
WHITE = (255, 255, 255)
RED = (255, 30, 30)

WINDOW_WIDTH, WINDOW_HEIGHT = (450, 450)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tic Tac Toe Game')

def draw_grid():
    margin = 30
    cell = 150
    for x in range(cell, WINDOW_WIDTH, cell):
        pygame.draw.line(WINDOW, WHITE, [x, margin], [x, WINDOW_HEIGHT-margin], 5)

    for y in range(cell, WINDOW_WIDTH, cell):
        pygame.draw.line(WINDOW, WHITE, [margin, y], [WINDOW_WIDTH-margin, y], 5)    

def draw_position():
    cell = 150 

    x_start = 30
    y_start = 30
    for x in range(x_start, WINDOW_WIDTH, cell):
        pygame.draw.ellipse(WINDOW, RED, [x+45, cell/2, 10, 10])
        
        for y in range(y_start, WINDOW_HEIGHT, cell):
            pygame.draw.ellipse(WINDOW, RED, [x+45, y+45, 10, 10])

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Program closed.')
                pygame.quit()
                sys.exit()

        WINDOW.fill(BLACK)
        
        draw_grid()
        draw_position()

        pygame.display.update()

if __name__ == '__main__':
    print('Game is running...')
    main()