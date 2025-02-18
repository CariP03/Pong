from config import *
import random
import pygame

# define global variables
racket_width = 0
racket_height = 0
ball_size = 0


# function that calculate racket's dimensions based on display's size
def calculate_racket_size(display):
    global racket_width, racket_height
    racket_width = display.get_width() / RACKET_WIDTH_RATIO
    racket_height = display.get_height() / RACKET_HEIGHT_RATIO


# function that calculate ball's dimensions based on display's size
def calculate_ball_size(display):
    global ball_size
    ball_size = display.get_width() / BALL_RATIO


# Draws the two rackets
def draw_rackets(display, red_coord, blue_coord):
    # Red racket
    pygame.draw.rect(display, RED, [display.get_width() / RACKET_OFFSET, red_coord, racket_width, racket_height])
    # Blue racket
    pygame.draw.rect(display, BLUE, [display.get_width() - display.get_width() / RACKET_OFFSET, blue_coord,
                                     racket_width, racket_height])


# Check for collisions between the ball and one of the horizontal borders
def border_collision(display, y_ball):
    if y_ball + ball_size >= display.get_height() or y_ball <= 0:
        return True
    else:
        return False


# Check for collisions between the ball and one of rackets
def racket_collision(display, x_ball, y_ball, red_racket, blue_racket):
    # Red racket collision
    if (x_ball <= (display.get_width() / RACKET_OFFSET) + racket_width
            and red_racket <= y_ball <= red_racket + racket_height):
        return True

    # Blue racket collision
    if (x_ball + ball_size >= (display.get_width() - display.get_width() / RACKET_OFFSET)
            and blue_racket <= y_ball <= blue_racket + racket_height):
        return True

    return False


# Check whether the ball has passed one of the rackets
# Return the name of the team that has scored
def point_scored(display, x_ball, y_ball):
    if x_ball < (display.get_width() / RACKET_OFFSET):
        return "blue"
    if x_ball > (display.get_width() - display.get_width() / RACKET_OFFSET) + racket_width:
        return "red"


# Draw score at the top of the window
def draw_score(display, red, blue):
    # Initialize the font used for the score
    font_width_ratio = 20
    font_size = max(MIN_FONT_SIZE, int(display.get_width() / font_width_ratio))
    score_font = pygame.font.Font(SCORE_FONT_PATH, font_size)

    # Render the messages for each score
    red_msg = score_font.render(str(red), True, RED)
    blue_msg = score_font.render(str(blue), True, BLUE)
    colon_msg = score_font.render(":", True, WHITE)

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
    y_pct_offset = 20
    y_position = display.get_height() / y_pct_offset

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


# Draw system message
def draw_message(display, string, colour):
    # Initialize the font used for the message
    font_width_ratio = 20
    font_size = max(MIN_FONT_SIZE, int(display.get_width() / font_width_ratio))
    system_font = pygame.font.Font(SYSTEM_FONT_PATH, font_size)

    # Render message
    msg = system_font.render(string, True, WHITE)

    # Determine centered position
    msg_rect = msg.get_rect()
    start_x = (display.get_width() - msg_rect.width) / 2
    start_y = (display.get_height() - msg_rect.height) / 2

    # Set message
    display.blit(msg, [start_x, start_y])


# Defines the game logic
def game_loop(display_width, display_height, red_score, blue_score):
    # pygame configs
    pygame.init()
    pygame.key.set_repeat(50)  # allow to hold keys

    # Declare clock used to regulate game's speed
    clock = pygame.time.Clock()

    # Configure display
    display = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    pygame.display.set_caption("PONG")

    # Calculate initial entities' size
    calculate_racket_size(display)
    calculate_ball_size(display)

    # Rackets initial vertical coordinates
    y_red = display_height / 2 - racket_height / 2  # y_red is the top pixel
    y_blue = y_red

    # Ball initial coordinates
    x_ball = display_width / 2 - ball_size / 2  # x_ball is the leftmost pixel
    y_ball = display_height / 2 - ball_size / 2  # y_ball is the top pixel

    # Ball initial throw
    x_initial_speed = display_width / X_SPEED_RATIO  # determine speed based on display's width
    x_change = x_initial_speed * random.choice([-1, 1])  # determine the side towards which the ball moves

    y_max_initial_speed = int(display_height / Y_SPEED_RATIO)  # determine speed based on display's height
    y_change = random.randrange(-y_max_initial_speed, y_max_initial_speed)  # randomly determine the initial y speed

    # Start of the game loop
    game_close = False
    game_over = False
    while not game_close:
        # ask user what to do after game over
        while game_over:
            display.fill(BLACK)

            if red_score == MAX_POINTS:
                draw_message(display, WIN_MESSAGE, RED)
            else:
                draw_message(display, LOSE_MESSAGE, RED)
            pygame.display.update()

            # read key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    # quit game
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    # restart
                    if event.key == pygame.K_c:
                        game_loop(display_width, display_height, 0, 0)

        # read commands
        for event in pygame.event.get():
            # read quit command
            if event.type == pygame.QUIT:
                game_close = True

            # read screen resize
            if event.type == pygame.VIDEORESIZE:
                display_width = event.w
                display_height = event.h
                display = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)

                calculate_racket_size(display)  # recalculate rackets' dimensions based on new display
                calculate_ball_size(display)  # recalculate ball's size based on new display

                # Recalculate speed based on display's size
                x_change *= (display_width / X_SPEED_RATIO)
                y_change *= (display_height / Y_SPEED_RATIO)

            # read moving commands
            if event.type == pygame.KEYDOWN:
                # up arrow
                if event.key == pygame.K_UP:
                    if y_red > 0:  # upper border check
                        y_red += -RACKET_SPEED
                # down arrow
                if event.key == pygame.K_DOWN:
                    if y_red + racket_height < display.get_height():  # lower border check
                        y_red += RACKET_SPEED

        # Check if one team has scored
        if not game_close:  # avoid that the game restarts after the closing command
            point = point_scored(display, x_ball, y_ball)
            if point == "red":
                red_score += 1
                if red_score == MAX_POINTS:
                    game_over = True
                else:
                    game_loop(display_width, display_height, red_score, blue_score)

            if point == "blue":
                blue_score += 1
                if blue_score == MAX_POINTS:
                    game_over = True
                else:
                    game_loop(display_width, display_height, red_score, blue_score)

        # Calculate ball movement
        if border_collision(display, y_ball):
            y_change = -y_change  # change trajectory

        if racket_collision(display, x_ball, y_ball, y_red, y_blue):
            x_change = -x_change

        x_ball += x_change
        y_ball += y_change

        # Draw entities
        display.fill(BLACK)
        draw_rackets(display, y_red, y_blue)
        pygame.draw.rect(display, WHITE, [x_ball, y_ball, ball_size, ball_size])  # draw the ball
        draw_score(display, red_score, blue_score)
        pygame.display.update()

        clock.tick(FRAME_RATE)

    pygame.quit()
    quit()
