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

# Declare messages
WIN_MESSAGE = "You Won! Press Q-Quit or C-Play Again"
LOSE_MESSAGE = "You Lost! Press Q-Quit or C-Play Again"

# Game parameters
FRAME_RATE = 30
RACKET_OFFSET = 12  # distance between a racket and a vertical border (as the screen's width divider)
RACKET_SPEED = 15  # number of pixels the racket moves per single button press
MAX_POINTS = 10  # number of points necessary to win

# Declare entities' ratios
RACKET_WIDTH_RATIO = 64
RACKET_HEIGHT_RATIO = 8
BALL_RATIO = 48
X_SPEED_RATIO = 80
Y_SPEED_RATIO = 120
