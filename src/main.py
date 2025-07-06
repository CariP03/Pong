import pygame
import engine
import setup


if __name__ == "__main__":
    pygame.init()
    res = setup.select_resolution()
    multiplayer = setup.is_multiplayer()
    engine.game_loop(res[0], res[1], multiplayer)
