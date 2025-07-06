from config import GameConfig
from music import Mixer
import random
import pygame
import ctypes
import platform

# define global variables
racket_width = 0
racket_height = 0
racket_speed = 0  # delay in ms between the transmission of the same key while holding it

ball_size = 0
ball_x_speed = 0
ball_y_speed_limit = 0

sleep_timer = 0  # number of sleep cycles for AI


# Calculate aspect ratio
def calculate_ratio(display):
    width = display.get_width()
    height = display.get_height()
    aspect_ratio = width / height

    if abs(aspect_ratio - (16 / 9)) < 0.1:
        return "16:9"
    elif abs(aspect_ratio - (21 / 9)) < 0.1:
        return "21:9"
    else:
        return "4:3"


# Calculate game's parameters based on display's resolution
def calculate_dynamic_parameters(display):
    global racket_width, racket_height, ball_size, ball_x_speed, ball_y_speed_limit, racket_speed

    ratio = calculate_ratio(display)

    ratios = GameConfig.configs["ratios"]
    if ratio == "16:9":
        racket_width = display.get_width() / ratios["16:9"]["RACKET_WIDTH_RATIO_HDTV"]
        racket_height = display.get_height() / ratios["16:9"]["RACKET_HEIGHT_RATIO_HDTV"]
        ball_size = display.get_height() / ratios["16:9"]["BALL_RATIO_HDTV"]
        ball_x_speed = display.get_width() / ratios["16:9"]["X_SPEED_RATIO_HDTV"]
        ball_y_speed_limit = int(display.get_height() / ratios["16:9"]["Y_SPEED_RATIO_HDTV"])
        racket_speed = ratios["16:9"]["RACKET_SPEED_HDTV"]

    if ratio == "21:9":
        racket_width = display.get_width() / ratios["21:9"]["RACKET_WIDTH_RATIO_UW"]
        racket_height = display.get_height() / ratios["21:9"]["RACKET_HEIGHT_RATIO_UW"]
        ball_size = display.get_height() / ratios["21:9"]["BALL_RATIO_UW"]
        ball_x_speed = display.get_width() / ratios["21:9"]["X_SPEED_RATIO_UW"]
        ball_y_speed_limit = int(display.get_height() / ratios["21:9"]["Y_SPEED_RATIO_UW"])
        racket_speed = ratios["21:9"]["RACKET_SPEED_UW"]

    if ratio == "4:3":
        racket_width = display.get_width() / ratios["4:3"]["RACKET_WIDTH_RATIO_TV"]
        racket_height = display.get_height() / ratios["4:3"]["RACKET_HEIGHT_RATIO_TV"]
        ball_size = display.get_height() / ratios["4:3"]["BALL_RATIO_TV"]
        ball_x_speed = display.get_width() / ratios["4:3"]["X_SPEED_RATIO_TV"]
        ball_y_speed_limit = int(display.get_height() / ratios["4:3"]["Y_SPEED_RATIO_TV"])
        racket_speed = ratios["4:3"]["RACKET_SPEED_TV"]


# Draws the two rackets
def draw_rackets(display, red_y, blue_y):
    RACKET_OFFSET = GameConfig.configs["game"]["RACKET_OFFSET"]

    # Red racket
    pygame.draw.rect(display, GameConfig.configs["colours"]["RIGHT_PLAYER"],
                     [display.get_width() / RACKET_OFFSET, red_y, racket_width, racket_height])
    # Blue racket
    pygame.draw.rect(display, GameConfig.configs["colours"]["LEFT_PLAYER"],
                     [display.get_width() - display.get_width() / RACKET_OFFSET, blue_y, racket_width, racket_height])


# Draw score at the top of the window
def draw_score(display, red, blue):
    # Initialize the font used for the score
    font_width_ratio = 20
    font_size = max(GameConfig.configs["fonts"]["MIN_FONT_SIZE"], int(display.get_width() / font_width_ratio))
    score_font = pygame.font.Font(GameConfig.configs["fonts"]["SCORE_FONT_PATH"], font_size)

    # Render the messages for each score
    red_msg = score_font.render(str(red), True, GameConfig.configs["colours"]["RIGHT_PLAYER"])
    blue_msg = score_font.render(str(blue), True, GameConfig.configs["colours"]["LEFT_PLAYER"])
    colon_msg = score_font.render(":", True, GameConfig.configs["colours"]["TEXT"])

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
    font_size = max(GameConfig.configs["fonts"]["MIN_FONT_SIZE"], int(display.get_width() / font_width_ratio))
    system_font = pygame.font.Font(GameConfig.configs["fonts"]["SYSTEM_FONT_PATH"], font_size)

    # Render message
    msg = system_font.render(string, True, colour)

    # Determine centered position
    msg_rect = msg.get_rect()
    start_x = (display.get_width() - msg_rect.width) / 2
    start_y = (display.get_height() - msg_rect.height) / 2

    # Set message
    display.blit(msg, [start_x, start_y])


# Set all entities to their starting position
def reset_entities(display):
    global ball_x_speed

    display_width = display.get_width()
    display_height = display.get_height()

    # Rackets initial vertical coordinates
    red_y = display_height / 2 - racket_height / 2  # red_y is the top pixel
    blue_y = red_y

    # Ball initial coordinates
    ball_x = display_width / 2 - ball_size / 2  # ball_x is the leftmost pixel
    ball_y = display_height / 2 - ball_size / 2  # ball_y is the top pixel

    # Ball initial throw
    ball_x_speed = ball_x_speed * random.choice([-1, 1])  # determine the side towards which the ball moves
    ball_y_speed = random.randrange(-ball_y_speed_limit, ball_y_speed_limit)  # randomly determine the initial y speed

    # Reset AI
    global sleep_timer
    sleep_timer = 0

    return red_y, blue_y, ball_x, ball_y, ball_y_speed


# Check for collisions between the ball and one of the horizontal borders
def border_collision(display, ball_y):
    if ball_y + ball_size >= display.get_height() or ball_y <= 0:
        return True
    else:
        return False


# Check for collisions between the ball and one of rackets
def racket_collision(display, ball_x, ball_y, red_y, blue_y):
    RACKET_OFFSET = GameConfig.configs["game"]["RACKET_OFFSET"]

    # Check if the top or bottom pixels of the ball are at the same height of the received racket
    def check_vertical_intersection(y_racket):
        return (y_racket <= ball_y <= y_racket + racket_height or
                y_racket <= ball_y + ball_size <= y_racket + racket_height)

    # Red racket collision
    # Check if the leftmost pixel of the ball is at the same width of the red racket
    if ball_x <= display.get_width() / RACKET_OFFSET + racket_width and check_vertical_intersection(red_y):
        return True

    # Blue racket collision
    # Check if the rightmost pixel of the ball is at the same width of the blue racket
    if (ball_x + ball_size >= display.get_width() - display.get_width() / RACKET_OFFSET and
            check_vertical_intersection(blue_y)):
        return True

    return False


# Check whether the ball has passed one of the rackets
# Return the name of the team that has scored
def point_scored(display, ball_x):
    RACKET_OFFSET = GameConfig.configs["game"]["RACKET_OFFSET"]

    if ball_x < (display.get_width() / RACKET_OFFSET):
        return "blue"
    if ball_x + ball_size > (display.get_width() - display.get_width() / RACKET_OFFSET) + racket_width:
        return "red"


# Determine blue racket movement
def AI_move(blue_y, ball_y):
    AI_parameters = GameConfig.configs["ai"]

    global sleep_timer

    # Randomly make no movement
    if random.random() < AI_parameters["SKIP_PROB"]:
        return 0

    # Force AI to sleep for a few cycles
    if sleep_timer > 0:
        sleep_timer -= 1
        return 0

    else:
        racket_center = blue_y + racket_height / 2
        ball_center = ball_y + ball_size / 2

        # Randomly sleep when the ball is moving towards opponent
        if ball_x_speed < 0 and random.random() < AI_parameters["SLEEP_PROB"]:
            sleep_timer = random.randint(AI_parameters["MIN_SLEEP"], AI_parameters["MAX_SLEEP"])
            return 0

        else:
            # Number of pixels that the AI can move per cycle
            movement = ((1000 / racket_speed) / GameConfig.configs["game"]["FRAME_RATE"])

            if abs(racket_center - ball_center) < movement:  # avoid flickering
                return 0
            # Blue racket is below the ball
            elif racket_center > ball_center:  # keep moving till the center of the racket is aligned
                if random.random() < AI_parameters["SPEED_PROB"]:
                    return -movement * AI_parameters["SPEED_PEN"]  # randomly reduce speed
                else:
                    return -movement
            # Blue racket is above the ball
            elif racket_center < ball_center:
                if random.random() < AI_parameters["SPEED_PROB"]:
                    return movement * AI_parameters["SPEED_PEN"]
                else:
                    return movement


# Check if the movement of a racket is illegal and eventually fix it
def adjust_movement(display_height, racket_y, movement):
    # moving upward
    if movement < 0:
        if racket_y + movement < 0:  # illegal position
            return movement - (racket_y + movement)  # set racket at the border
        else:
            return movement
    # moving downward
    elif movement > 0:
        if racket_y + racket_height + movement > display_height:
            return display_height - (racket_y + racket_height)
        else:
            return movement
    # no movement
    else:
        return 0


# Determine the movement of a racket for single player mode
def single_player_move(display_height, red_y, keys):
    movement = ((1000 / racket_speed) / GameConfig.configs["game"]["FRAME_RATE"])

    # Up arrow
    if keys[pygame.K_UP]:
        red_y += adjust_movement(display_height, red_y, -movement)
    # Down arrow
    if keys[pygame.K_DOWN]:
        red_y += adjust_movement(display_height, red_y, movement)

    return red_y


# Determine the movement of the rackets for multiplayer mode
def multiplayer_move(display_height, red_y, blue_y, keys):
    movement = ((1000 / racket_speed) / GameConfig.configs["game"]["FRAME_RATE"])

    # Red movement
    # W (up movement)
    if keys[pygame.K_w]:
        red_y += adjust_movement(display_height, red_y, -movement)
    # S (down movement)
    if keys[pygame.K_s]:
        red_y += adjust_movement(display_height, red_y, movement)

    # Blue movement
    # Up arrow
    if keys[pygame.K_UP]:
        blue_y += adjust_movement(display_height, blue_y, -movement)
    # Down arrow
    if keys[pygame.K_DOWN]:
        blue_y += adjust_movement(display_height, blue_y, movement)

    return red_y, blue_y


# Defines the game logic
def game_loop(display_width, display_height, multiplayer):
    global ball_x_speed

    if platform == "Windows":
        ctypes.windll.user32.SetProcessDPIAware()  # ignore Windows' DPI Scaling

    # Save useful configs
    texts = GameConfig.configs["texts"]
    colours = GameConfig.configs["colours"]
    game_parameters = GameConfig.configs["game"]

    Mixer.play_background()  # start background music

    # Declare clock used to regulate game's speed
    clock = pygame.time.Clock()

    # Configure display
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(texts["DISPLAY_CAPTION"])

    # Calculate parameters based on display's resolution
    calculate_dynamic_parameters(display)
    pygame.key.set_repeat(racket_speed)  # allow to hold keys

    # Set entities initial positions
    red_y, blue_y, ball_x, ball_y, ball_y_speed = reset_entities(display)

    # Initialize scores
    red_score = 0
    blue_score = 0

    # Start of the game loop
    game_close = False
    game_over = False
    while not game_close:
        # ask user what to do after game over
        while game_over:
            display.fill(colours["BACKGROUND"])

            if red_score == game_parameters["MAX_POINTS"]:
                draw_message(display, texts["WIN_MESSAGE"], colours["TEXT"])
            else:
                draw_message(display, texts["LOSE_MESSAGE"], colours["TEXT"])
            pygame.display.update()

            # read key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    # quit game
                    if event.type == pygame.QUIT or event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    # restart
                    elif event.key == pygame.K_c:
                        game_over = False
                        red_y, blue_y, ball_x, ball_y, ball_y_speed = reset_entities(display)

                        # Reset scores
                        red_score = 0
                        blue_score = 0

                        Mixer.reset_music()

        # read commands
        for event in pygame.event.get():
            # read quit command
            if event.type == pygame.QUIT:
                game_close = True

            # read screen resize
            if event.type == pygame.VIDEORESIZE:
                display_width = event.w
                display_height = event.h
                display = pygame.display.set_mode((display_width, display_height))

                calculate_dynamic_parameters(display)

        # Determine movement of rackets
        keys = pygame.key.get_pressed()

        if not multiplayer:
            # Determine player movement
            red_y = single_player_move(display_height, red_y, keys)
            # Determine AI movement
            blue_y += adjust_movement(display_height, blue_y, AI_move(blue_y, ball_y))
        else:
            # Determine both players movement
            red_y, blue_y = multiplayer_move(display_height, red_y, blue_y, keys)

        # Check if one team has scored
        if not game_close:  # avoid that the game restarts after the closing command
            point = point_scored(display, ball_x)
            if point == "red":
                red_score += 1
                Mixer.play_red_point()
                if red_score == game_parameters["MAX_POINTS"]:
                    game_over = True
                    Mixer.play_game_over("red")
                else:
                    red_y, blue_y, ball_x, ball_y, ball_y_speed = reset_entities(display)

            if point == "blue":
                blue_score += 1
                Mixer.play_blue_point()
                if blue_score == game_parameters["MAX_POINTS"]:
                    game_over = True
                    Mixer.play_game_over("blue")
                else:
                    red_y, blue_y, ball_x, ball_y, ball_y_speed = reset_entities(display)

        # Calculate ball movement
        if border_collision(display, ball_y):
            ball_y_speed = -ball_y_speed  # change trajectory
            Mixer.play_bounce()

        if racket_collision(display, ball_x, ball_y, red_y, blue_y):
            ball_x_speed = -ball_x_speed
            # Randomly change y trajectory
            ball_y_speed = random.randrange(-ball_y_speed_limit, ball_y_speed_limit)
            Mixer.play_bounce()

        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Draw entities
        display.fill(colours["BACKGROUND"])
        draw_rackets(display, red_y, blue_y)
        pygame.draw.rect(display, colours["BALL"], [ball_x, ball_y, ball_size, ball_size])  # draw ball
        draw_score(display, red_score, blue_score)
        pygame.display.update()

        clock.tick(game_parameters["FRAME_RATE"])

    pygame.quit()
    quit()
