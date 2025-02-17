from config import *
import pygame


# function that defines the game logic
def game_loop():
    pygame.init()

    # create display
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.update()

    game_over = False
    while not game_over:

        # add quit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

    pygame.quit()
    quit()
