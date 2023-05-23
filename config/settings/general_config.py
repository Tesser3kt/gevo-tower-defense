"""Configuration file"""
from config.settings.general_imports import *

class Window:  
    HEIGHT = 800
    WIDTH = 960

class Tile:
    PIXEL_SIZE = 16
    HEIGHT = 50 #How many tiles are in height
    WIDTH = 60 #How many tiles are in width
    # 60T*50T, 1T = 16px

class Directory:
    BASE_DIR = os.getcwd()
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    
class Economy:
    STARTING_MONEY = 100
    STARTING_LIVES = 10
    MONEY_PER_KILL = 10
    MONEY_PER_HIT = 1
    MONEY_PER_ROUND = 100
    
class Game:
    FPS = 60
    START_LEVEL = 0
    START_WAVE = 0

class Colors:
    BACKGROUND = (0, 0, 0)
    PATH = (255, 255, 0)
    START = (0, 255, 0)
    END = (255, 0, 0)
    WALLS = (255, 0, 0)
    MENU_BG = (0, 0, 255)
    MENU_TEXT = (255, 0, 255)
    BUTTONS = (55, 55, 0)

class Difficulty:
    NOOB = 0
    EASY = 1    
    NORMAL = 2
    HARD = 3
    HARDER = 4
    IMPOSSIBLE = 5
#   To by mohlo být asi nějaké menu?

class Spawn_probs:
    only_casual = {
        "casual": 1,
        "speeder" : 0,
        "camo" : 0,
        "boss" : 0,
        "bruiser" : 0}

    casual_speeder = {
        "casual" : 0.5,
        "speeder" : 0.5,
        "camo" : 0,
        "boss" : 0,
        "bruiser" : 0
    }
        
    normal = {
        "casual" : 0.25,
        "speeder" : 0.25,
        "camo" : 0.2,
        "boss" : 0.1,
        "bruiser" : 0.2
    }

    hard = {
        "casual" : 0.2,
        "speeder" : 0.2,
        "camo" : 0.2,
        "boss" : 0.1,
        "bruiser" : 0.3
    }

    harder = {
        "casual" : 0.1,
        "speeder" : 0.1,
        "camo" : 0.1,
        "boss" : 0.1,
        "bruiser" : 0.6
    }

    impossible = {
        "casual" : 0.,
        "speeder" : 0.1,
        "camo" : 0.2,
        "boss" : 0.3,
        "bruiser" : 0.4
    }

    only_boss = {
        "casual": 0,
        "speeder" : 0,
        "camo" : 0,
        "boss" : 1,
        "bruiser" : 0
    }

    only_camo = {
        "casual": 0,
        "speeder" : 0,
        "camo" : 1,
        "boss" : 0,
        "bruiser" : 0
    }

class Special_waves:
    boss_wave = [25, 35, 50, 60]
    camo_wave = [15, 30]
    speedrun_wave = [13, 26, 39, 52, 65]
    hard_wave = [12, 22, 32, 42]

class Wave_function:
    def noob_wave(wave:int) -> int:
        return wave+e**(-0.2*wave+2)*sin(10*wave)+5
    def easy_wave(wave:int) -> int:
        return wave*69
    def normal_wave(wave:int) -> int:
        return wave*69
    def hard_wave(wave:int) -> int:
        return wave*69
    def harder_wave(wave:int) -> int:
        return wave*69
    def impossible_wave(wave:int) -> int:
        return wave*420