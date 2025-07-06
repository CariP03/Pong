import json
import os


# Contains all configs
class GameConfig:
    # Dictionary that contains the default settings
    __DEFAULT_CONFIG = {
        "colours": {
            "BACKGROUND": (0, 0, 0),  # black
            "BALL": (255, 255, 255),  # white
            "RIGHT_PLAYER": (255, 0, 0),  # red
            "LEFT_PLAYER": (0, 0, 255),  # blue
            "TEXT": (255, 255, 255)  # white
        },
        "fonts": {
            "MIN_FONT_SIZE": 30,
            "SCORE_FONT_PATH": "resources/fonts/VT323/VT323-Regular.ttf",
            "SYSTEM_FONT_PATH": "resources/fonts/Monofett/Monofett-Regular.ttf",
        },
        "texts": {
            "DISPLAY_CAPTION": "PONG",
            "WIN_MESSAGE": "You Won! Press Q-Quit or C-Play Again",
            "LOSE_MESSAGE": "You Lost! Press Q-Quit or C-Play Again",
        },
        "ai": {
            "SKIP_PROB": 0.1,  # probability of skipping a cycle
            "SLEEP_PROB": 0.1,  # probability of sleep
            "MIN_SLEEP": 10,  # minimum number of sleep cycles
            "MAX_SLEEP": 20,  # maximum number of sleep cycles
            "SPEED_PROB": 0.6,  # probability of penalty to speed
            "SPEED_PEN": 0.5,  # percentage penalty to speed if an error occurs
        },
        "game": {
            "FRAME_RATE": 30,
            "RACKET_OFFSET": 12,  # distance between a racket and a vertical border (as the screen's width divider)
            "MAX_POINTS": 5,  # number of points necessary to win
        },
        "ratios": {
            "4:3": {
                "RACKET_WIDTH_RATIO_TV": 64,
                "RACKET_HEIGHT_RATIO_TV": 8,
                "BALL_RATIO_TV": 36,
                "X_SPEED_RATIO_TV": 40,
                "Y_SPEED_RATIO_TV": 90,
                "RACKET_SPEED_TV": 4,  # delay in ms between the transmission of the same key while holding it
            },
            "16:9": {
                "RACKET_WIDTH_RATIO_HDTV": 64,
                "RACKET_HEIGHT_RATIO_HDTV": 6,
                "BALL_RATIO_HDTV": 24,
                "X_SPEED_RATIO_HDTV": 48,
                "Y_SPEED_RATIO_HDTV": 90,
                "RACKET_SPEED_HDTV": 3,
            },
            "21:9": {
                "RACKET_WIDTH_RATIO_UW": 96,
                "RACKET_HEIGHT_RATIO_UW": 6,
                "BALL_RATIO_UW": 24,
                "X_SPEED_RATIO_UW": 80,
                "Y_SPEED_RATIO_UW": 100,
                "RACKET_SPEED_UW": 2,
            }
        },
        "resolutions": [
            (800, 600),
            (1280, 720),
            (1600, 900),
            (1920, 1080),
            (2560, 1440),
            (3840, 2160),
            (2560, 1080),
            (3440, 1440)
        ],
        "music": {
            "BOUNCE": "resources/sounds/Pop.ogg",
            "BOUNCE_VOLUME": 0.5,
            "RED_GOAL": "resources/sounds/Point-Red.wav",
            "BLUE_GOAL": "resources/sounds/Point-Blue.wav",
            "GOAL_VOLUME": 0.7,
            "BACKGROUND": "resources/sounds/Background-1.mp3",
            "BACKGROUND_VOLUME": 0.2,
            "MENU": "resources/sounds/Menu.mp3",
            "MENU_VOLUME": 0.2,
            "WIN": "resources/sounds/Gameover-Win.mp3",
            "WIN_VOLUME": 0.2,
            "LOSE": "resources/sounds/Gameover-Lose.mp3",
            "LOSE_VOLUME": 0.5
        }
    }

    # Custom configs
    configs = None

    # Path to the JSON settings file
    __SETTINGS_FILE_PATH = "src/configs.json"

    # Load configs from file
    @staticmethod
    def __load_config():
        # Check if JSON file exists
        if os.path.exists(GameConfig.__SETTINGS_FILE_PATH):
            # Try to open the file
            try:
                with open(GameConfig.__SETTINGS_FILE_PATH, "r") as file:
                    return GameConfig.__merge_config(GameConfig.__DEFAULT_CONFIG, json.load(file))
            except Exception:
                return GameConfig.__DEFAULT_CONFIG.copy()

        # If the file does not exist return default configs
        else:
            GameConfig.__save_config()  # create file
            return GameConfig.__DEFAULT_CONFIG.copy()

    # Compare two dictionaries and replace every missing key or value of the second dictionary
    # with the corresponding ones from the first
    # Preserve the structure of the first dictionary
    @staticmethod
    def __merge_config(dict_1: dict, dict_2: dict):
        merged = dict_1.copy()  # copy of the full dictionary

        for key, value in dict_2.items():
            # Check if the key is in the first dictionary
            if key in merged:
                # Check if the key itself is a dictionary
                if isinstance(merged[key], dict) and isinstance(value, dict):
                    # Recursive call
                    merged[key] = GameConfig.__merge_config(merged[key], value)

                # Use the custom value only if neither key is a dictionary
                elif not isinstance(merged[key], dict) and not isinstance(value, dict):
                    merged[key] = value

        return merged

    # Create default JSON file
    @staticmethod
    def __save_config():
        # Try to open the file in writing mode
        try:
            with open(GameConfig.__SETTINGS_FILE_PATH, "w") as file:
                json.dump(GameConfig.__DEFAULT_CONFIG, file, indent=4)
        except IOError as e:
            print(f"An error occurred while trying to create the config file: {e}")

    # Initialize configs
    @classmethod
    def initialize(cls):
        cls.configs = cls.__load_config()


# Initialize the module at the start of the program
GameConfig.initialize()
