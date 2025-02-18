from config import *
import random
import pygame


# function that draws the two rackets
def draw_rackets(dis, red_coord, blue_coord):
    # red racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, RED, [dis.get_size()[0] / 12, red_coord - (x * 15), 10, 15])
    # blue racket
    for x in range(RACKET_SIZE):
        pygame.draw.rect(dis, BLUE, [dis.get_size()[0] - dis.get_size()[0] / 12, blue_coord - (x * 15), 10, 15])


# function that check for collisions between the ball and one of the horizontal borders
def border_collision(dis, x_ball, y_ball):
    if y_ball + BALL_SIZE >= dis.get_size()[1] or y_ball <= 0:
        return True
    else:
        return False


# function that check for collisions between the ball and one of rackets
def racket_collision(dis, x_ball, y_ball, red_racket, blue_racket):
    # red racket collision
    if x_ball <= (dis.get_size()[0] / 12) + 10 and red_racket - 15 * (RACKET_SIZE - 1) <= y_ball <= red_racket:
        return True
    # blue racket collision
    if (x_ball >= (dis.get_size()[0] - dis.get_size()[0] / 12) - 10 and
            blue_racket - 15 * (RACKET_SIZE - 1) <= y_ball <= blue_racket):
        return True

    return False


# function that checks whether the ball has passed one of the rackets
# returns the name of the team that scored a point
def point_scored(dis, x_ball, y_ball):
    if x_ball <= (dis.get_size()[0] / 12):
        return "blue"
    if x_ball >= (dis.get_size()[0] - dis.get_size()[0] / 12):
        return "red"


# function to print score
def draw_score(red, blue, display):
    # Render the messages for each score
    red_msg = SCORE_FONT.render(str(red), True, RED)
    blue_msg = SCORE_FONT.render(str(blue), True, BLUE)
    colon_msg = SCORE_FONT.render(":", True, WHITE)

    # Get the rectangles (rect) for each rendered text
    red_rect = red_msg.get_rect()
    colon_rect = colon_msg.get_rect()
    blue_rect = blue_msg.get_rect()

    # Define a spacing between the elements (in pixels)
    spacing = 10

    # Calculate the total width of the score display (red score + spacing + colon + spacing + blue score)
    total_width = red_rect.width + colon_rect.width + blue_rect.width + 2 * spacing

    # Compute the starting x position to center the score on the screen
    start_x = (display.get_width() - total_width) / 2
    y_position = display.get_size()[1] / 20

    # Set the position of the red score
    red_rect.topleft = (start_x, y_position)
    # Set the position of the colon right after the red score, with spacing
    colon_rect.topleft = (red_rect.topright[0] + spacing, y_position)
    # Set the position of the blue score right after the colon, with spacing
    blue_rect.topleft = (colon_rect.topright[0] + spacing, y_position)

    # Draw the messages on the display
    display.blit(red_msg, red_rect)
    display.blit(colon_msg, colon_rect)
    display.blit(blue_msg, blue_rect)


# function that defines the game logic
def game_loop(red_score, blue_score):
    pygame.init()
    clock = pygame.time.Clock()

    # allow held keys
    pygame.key.set_repeat(50)

    # create display
    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption("PONG")

    # rackets coordinates
    y_red = dis_height / 2 - RACKET_SIZE
    y_blue = dis_height / 2 - RACKET_SIZE

    # ball coordinates
    x_ball = dis_width / 2 - BALL_SIZE
    y_ball = dis_height / 2 + BALL_SIZE
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

        # calculate ball movement
        if border_collision(dis, x_ball, y_ball):
            y_change = -y_change  # change trajectory
            print("BORDER")

        if racket_collision(dis, x_ball, y_ball, y_red, y_blue):
            x_change = -x_change
            print("RACKET")

        x_ball += x_change
        y_ball += y_change
        pygame.draw.rect(dis, WHITE, [x_ball, y_ball, BALL_SIZE, BALL_SIZE])  # draw the ball

        # check if one team has scored
        point = point_scored(dis, x_ball, y_ball)
        if point == "red":
            red_score += 1
            game_loop(red_score, blue_score)

        if point == "blue":
            blue_score += 1
            game_loop(red_score, blue_score)

        draw_score(red_score, blue_score, dis)

        pygame.display.update()
        clock.tick(FRAME_RATE)

    pygame.quit()
    quit()
