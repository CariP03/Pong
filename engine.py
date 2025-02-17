import random

from config import *
import pygame


# function that draws the two rackets
def draw_rackets(dis, red_coord, blue_coord):
    # red racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, RED, [dis.get_size()[0] / 12, red_coord - (x * 15), 10, 15])
    # blue racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, BLUE, [dis.get_size()[0] - dis.get_size()[0] / 12, blue_coord - (x * 15), 10, 15])


# function that defines the game logic
def game_loop():
    pygame.init()
    clock = pygame.time.Clock()

    # allow held keys
    pygame.key.set_repeat(50)

    # create display
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))

    # rackets coordinates
    y_red = dis_height / 2 - RACKET_SIZE
    y_blue = dis_height / 2 - RACKET_SIZE

    # ball coordinates
    x_ball = dis_width / 2 - BALL_SIZE
    y_ball = dis_height / 2 - BALL_SIZE
    x_change = 10 * random.choice([-1, 1])  # high initial x-speed
    y_change = random.randrange(-5, 5)

    game_over = False
    while not game_over:

        # read commands
        for event in pygame.event.get():
            # add quit command
            if event.type == pygame.QUIT:
                game_over = True

            # read moving commands
            if event.type == pygame.KEYDOWN:
                # up arrow
                if event.key == pygame.K_UP:
                    if (y_red - 15 * (RACKET_SIZE - 1)) >= 0:  # upper border check
                        y_red += -15
                # down arrow
                if event.key == pygame.K_DOWN:
                    if (y_red + 15 + RACKET_SIZE) <= dis.get_size()[1]:  # lower border check
                        y_red += 15

        # draw entities
        dis.fill(BLACK)
        draw_rackets(dis, y_red, y_blue)

        # calculate ball movement (no collisions)
        x_ball += x_change
        y_ball += y_change
        pygame.draw.rect(dis, WHITE, [x_ball, y_ball, BALL_SIZE, BALL_SIZE])  # draw the ball

        pygame.display.update()

        clock.tick(FRAME_RATE)

    pygame.quit()
    quit()
