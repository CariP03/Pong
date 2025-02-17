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
    pygame.display.update()


# function that defines the game logic
def game_loop():
    pygame.init()
    clock = pygame.time.Clock()

    # allow held keys
    pygame.key.set_repeat(100)

    # create display
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))

    # coordinates
    y_red = dis_height / 2
    y_blue = dis_height / 2

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
                    y_red += -15
                # down arrow
                if event.key == pygame.K_DOWN:
                    y_red += 15

        # draw entities
        dis.fill(BLACK)
        draw_rackets(dis, y_red, y_blue)

        clock.tick(FRAME_RATE)

    pygame.quit()
    quit()
