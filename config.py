import pygame

pygame.init()

# Declare colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Declare fonts
MIN_FONT_SIZE = 30
SCORE_FONT_PATH = "resources/VT323/VT323-Regular.ttf"
SYSTEM_FONT_PATH = "resources/Monofett/Monofett-Regular.ttf"

# Declare strings
DISPLAY_CAPTION = "PONG"
WIN_MESSAGE = "You Won! Press Q-Quit or C-Play Again"
LOSE_MESSAGE = "You Lost! Press Q-Quit or C-Play Again"

# Game parameters
FRAME_RATE = 30
RACKET_OFFSET = 12  # distance between a racket and a vertical border (as the screen's width divider)
RACKET_SPEED = 4  # delay in ms between the transmission of the same key while holding it
MAX_POINTS = 10  # number of points necessary to win

# AI parameters
SKIP_PROB = 0.2  # probability of skipping a cycle
SLEEP_PROB = 0.1  # probability of sleep
MIN_SLEEP = 10  # minimum number of sleep cycles
MAX_SLEEP = 20  # maximum number of sleep cycles
SPEED_PROB = 0.5  # probability of penalty to speed
SPEED_PEN = 0.5  # percentage penalty to speed if an error occurs

# Declare entities' ratios
RACKET_WIDTH_RATIO = 64
RACKET_HEIGHT_RATIO = 8
BALL_RATIO = 48
X_SPEED_RATIO = 40
Y_SPEED_RATIO = 90
