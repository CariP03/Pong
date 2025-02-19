import pygame

# Declare colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Declare fonts
MIN_FONT_SIZE = 30
SCORE_FONT_PATH = "resources/fonts/VT323/VT323-Regular.ttf"
SYSTEM_FONT_PATH = "resources/fonts/Monofett/Monofett-Regular.ttf"

# Declare strings
DISPLAY_CAPTION = "PONG"
WIN_MESSAGE = "You Won! Press Q-Quit or C-Play Again"
LOSE_MESSAGE = "You Lost! Press Q-Quit or C-Play Again"

# Game parameters
FRAME_RATE = 30
RACKET_OFFSET = 12  # distance between a racket and a vertical border (as the screen's width divider)
MAX_POINTS = 2  # number of points necessary to win

# AI parameters
SKIP_PROB = 0.1  # probability of skipping a cycle
SLEEP_PROB = 0.1  # probability of sleep
MIN_SLEEP = 10  # minimum number of sleep cycles
MAX_SLEEP = 20  # maximum number of sleep cycles
SPEED_PROB = 0.6  # probability of penalty to speed
SPEED_PEN = 0.5  # percentage penalty to speed if an error occurs

# Declare entities' ratios
# For 4:3
RACKET_WIDTH_RATIO_TV = 64
RACKET_HEIGHT_RATIO_TV = 8
BALL_RATIO_TV = 36
X_SPEED_RATIO_TV = 40
Y_SPEED_RATIO_TV = 90
RACKET_SPEED_TV = 4  # delay in ms between the transmission of the same key while holding it
# For 16:9
RACKET_WIDTH_RATIO_HDTV = 64
RACKET_HEIGHT_RATIO_HDTV = 6
BALL_RATIO_HDTV = 24
X_SPEED_RATIO_HDTV = 48
Y_SPEED_RATIO_HDTV = 90
RACKET_SPEED_HDTV = 3
# For 21:9
RACKET_WIDTH_RATIO_UW = 96
RACKET_HEIGHT_RATIO_UW = 6
BALL_RATIO_UW = 24
X_SPEED_RATIO_UW = 80
Y_SPEED_RATIO_UW = 100
RACKET_SPEED_UW = 2

# Declare resolutions
RESOLUTIONS = [
    (800, 600),
    (1280, 720),
    (1600, 900),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160),
    (2560, 1080),
    (3440, 1440)
]
