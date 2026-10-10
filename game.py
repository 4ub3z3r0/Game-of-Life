import pygame
import random as rd
from modules import engine

pygame.init()
screen = pygame.display.set_mode((800, 800)) # window's size
clock = pygame.time.Clock()
running = True


lines = 100
columns = 100
cell_size = min(800 // lines, 800 // columns)

grid = [  [ rd.randint(0,1) for i in range( columns )] for j in range( lines )  ]
color_grid = [  [ 0 for i in range( columns )] for j in range( lines )  ]

paused = False


def drawGrid(grid):
    for i in range(lines):
        for j in range(columns):
            if color_grid[i][j]: # if cell exists

                if color_grid[i][j] == 1: # blue if still living
                    pygame.draw.rect(screen, "blue", ((cell_size*j, cell_size*i), (cell_size, cell_size)))

                elif color_grid[i][j] == 2: # green if born
                    pygame.draw.rect(screen, "green", ((cell_size*j, cell_size*i), (cell_size, cell_size)))

                elif color_grid[i][j] == 3: # red if died
                    pygame.draw.rect(screen, "red", ((cell_size*j, cell_size*i), (cell_size, cell_size)))

                elif color_grid[i][j] == 4: # yellow if die but was born before (was green)
                    pygame.draw.rect(screen, "yellow", ((cell_size*j, cell_size*i), (cell_size, cell_size)))


while running:
    right = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # pause if space pressed
                paused = not paused
            if event.key == pygame.K_RIGHT: # next grid if right arrow pressed
                    right = True

    screen.fill("black")

    if not paused: 
        grid, color_grid = engine.nextGrid( grid, color_grid )
    else: # pause cells calculation
        if right: # go to next grid if right arrow pressed
            grid, color_grid = engine.nextGrid( grid, color_grid )

    drawGrid(grid)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(50)  # limits simultion speed to 50

pygame.quit()