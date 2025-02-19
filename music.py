import pygame


# Contains methods to play different sounds
class Mixer:
    pygame.mixer.init()

    # Class attributes
    __BOUNCE = "resources/sounds/Pop.ogg"
    __BOUNCE_VOLUME = 0.5
    __bounce_sound = pygame.mixer.Sound(__BOUNCE)
    __bounce_sound.set_volume(__BOUNCE_VOLUME)

    __RED_GOAL = "resources/sounds/Point-Red.wav"
    __BLUE_GOAL = "resources/sounds/Point-Blue.wav"
    __GOAL_VOLUME = 0.7
    __red_sound = pygame.mixer.Sound(__RED_GOAL)
    __red_sound.set_volume(__GOAL_VOLUME)
    __blue_sound = pygame.mixer.Sound(__BLUE_GOAL)
    __blue_sound.set_volume(__GOAL_VOLUME)

    __BACKGROUND = "resources/sounds/Background-1.mp3"
    __BACKGROUND_VOLUME = 0.2
    __background_sound = pygame.mixer.Sound(__BACKGROUND)
    __background_sound.set_volume(__BACKGROUND_VOLUME)

    __MENU = "resources/sounds/Menu.mp3"
    __MENU_VOLUME = 0.2
    __menu_sound = pygame.mixer.Sound(__MENU)
    __menu_sound.set_volume(__MENU_VOLUME)

    __WIN = "resources/sounds/Gameover-Win.mp3"
    __WIN_VOLUME = 0.2
    __win_sound = pygame.mixer.Sound(__WIN)
    __win_sound.set_volume(__WIN_VOLUME)

    __LOSE = "resources/sounds/Gameover-Lose.mp3"
    __LOSE_VOLUME = 0.5
    __lose_sound = pygame.mixer.Sound(__LOSE)
    __lose_sound.set_volume(__LOSE_VOLUME)

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
