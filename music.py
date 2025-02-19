from config import *


# Play bounce sound
def play_bounce():
    bounce_sound = pygame.mixer.Sound(BOUNCE)
    bounce_sound.set_volume(BOUNCE_VOLUME)
    bounce_sound.play()


# Play goal sound for red
def play_red_point():
    goal_sound = pygame.mixer.Sound(RED_GOAL)
    goal_sound.set_volume(GOAL_VOLUME)
    goal_sound.play()


# Play goal sound for blue
def play_blue_point():
    goal_sound = pygame.mixer.Sound(BLUE_GOAL)
    goal_sound.set_volume(GOAL_VOLUME)
    goal_sound.play()


# Play background music
def play_background():
    background_sound = pygame.mixer.Sound(BACKGROUND)
    background_sound.set_volume(BACKGROUND_VOLUME)
    background_sound.play(-1)


# Play menu music
def play_menu():
    menu_sound = pygame.mixer.Sound(MENU)
    menu_sound.set_volume(MENU_VOLUME)
    menu_sound.play()


# Play win music
def play_win():
    win_sound = pygame.mixer.Sound(WIN)
    win_sound.set_volume(WIN_VOLUME)
    win_sound.play(-1)


# Play lose music
def play_lose():
    win_sound = pygame.mixer.Sound(LOSE)
    win_sound.set_volume(LOSE_VOLUME)
    win_sound.play()
