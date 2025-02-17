from config import *
import pygame


# function that draws the two rackets
def draw_rackets(dis, dis_width, dis_height):
    # red racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, RED, [dis_width / 12, dis_height / 2 - (x * 15), 10, 15])
    # blue racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, BLUE, [dis_width - dis_width / 12, dis_height / 2 - (x * 15), 10, 15])
    pygame.display.update()


# function that defines the game logic
def game_loop():
    pygame.init()

    # create display
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))

    game_over = False
    while not game_over:

        # add quit command
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # draw entities
        draw_rackets(dis, dis_width, dis_height)

    pygame.quit()
    quit()
