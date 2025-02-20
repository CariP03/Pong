import pygame
from config import GameConfig


# Contains methods to play different sounds
class Mixer:
    pygame.mixer.init()

    # Class attributes
    __bounce_sound = pygame.mixer.Sound(GameConfig.configs["music"]["BOUNCE"])
    __bounce_sound.set_volume(GameConfig.configs["music"]["BOUNCE_VOLUME"])

    __red_sound = pygame.mixer.Sound(GameConfig.configs["music"]["RED_GOAL"])
    __red_sound.set_volume(GameConfig.configs["music"]["GOAL_VOLUME"])
    __blue_sound = pygame.mixer.Sound(GameConfig.configs["music"]["BLUE_GOAL"])
    __blue_sound.set_volume(GameConfig.configs["music"]["GOAL_VOLUME"])

    __background_sound = pygame.mixer.Sound(GameConfig.configs["music"]["BACKGROUND"])
    __background_sound.set_volume(GameConfig.configs["music"]["BACKGROUND_VOLUME"])

    __menu_sound = pygame.mixer.Sound(GameConfig.configs["music"]["MENU"])
    __menu_sound.set_volume(GameConfig.configs["music"]["MENU_VOLUME"])

    __win_sound = pygame.mixer.Sound(GameConfig.configs["music"]["WIN"])
    __win_sound.set_volume(GameConfig.configs["music"]["WIN_VOLUME"])

    __lose_sound = pygame.mixer.Sound(GameConfig.configs["music"]["LOSE"])
    __lose_sound.set_volume(GameConfig.configs["music"]["LOSE_VOLUME"])

    # Play bounce sound
    @classmethod
    def play_bounce(cls):
        Mixer.__bounce_sound.play()

    # Play goal sound for red
    @classmethod
    def play_red_point(cls):
        Mixer.__red_sound.play()

    # Play goal sound for blue
    @classmethod
    def play_blue_point(cls):
        Mixer.__blue_sound.play()

    # Play background music
    @classmethod
    def play_background(cls):
        Mixer.__background_sound.play(-1)

    # Stop background music
    @classmethod
    def stop_background(cls):
        Mixer.__background_sound.stop()

    # Play menu music
    @classmethod
    def play_menu(cls):
        Mixer.__menu_sound.play()

    # Play win music
    @classmethod
    def play_win(cls):
        Mixer.__win_sound.play(-1)

    # Stop win music
    @classmethod
    def stop_win(cls):
        Mixer.__win_sound.stop()

    # Play lose music
    @classmethod
    def play_lose(cls):
        Mixer.__lose_sound.play()

    # Stop lose music
    @classmethod
    def stop_lose(cls):
        Mixer.__lose_sound.stop()

    # Call the appropriate game over music
    # Receive the winner name as argument ("red" or "blue")
    @classmethod
    def play_game_over(cls, winner):
        Mixer.stop_background()

        if winner == "red":
            Mixer.play_win()
        else:
            Mixer.play_lose()

    # Reset music after game over
    @classmethod
    def reset_music(cls):
        Mixer.stop_win()
        Mixer.stop_lose()
        Mixer.play_background()
