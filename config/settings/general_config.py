"""Configuration file"""
from config.settings.general_imports import *

    # 60T*50T, 1T = 16px

class Window:
    PIXEL_SIZE = 16
    TILES_IN_HEIGHT = 50 #How many tiles are in height
    TILES_IN_WIDTH = 60 #How many tiles are in width

    GUI_POS = (0, 0)
    GUI_SCALE = 4
    CARD_RECT_WIDTH = 4

    WINDOW_WIDTH = 960

    GUI_HEIGHT = (PIXEL_SIZE+2*5)*GUI_SCALE
    GUI_WIDTH = WINDOW_WIDTH

    WINDOW_HEIGHT = 800 + GUI_HEIGHT
    # TODO to scalovani je podle me jeste vetsi problem, idk
    # MUSI BYT SPRAVNE ASPECT RATIO !!!

    GAME_HEIGHT = WINDOW_HEIGHT - GUI_HEIGHT
    GAME_WIDTH = WINDOW_WIDTH

class Directory:
    BASE_DIR = os.getcwd()
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    EXCLUDED_DIRS = ["fonts", "level_maps"] #for texture_loader
    
class Economy:
    STARTING_MONEY = 4000
    STARTING_LIVES = 10
    MONEY_PER_KILL = 10
    MONEY_PER_HIT = 1
    MONEY_PER_ROUND = 100
    
class Game:
    FPS = 60
    START_LEVEL = 5
    START_WAVE = 0
    PROJECTILE_SPEED = 4
    ENEMY_SPEED = 2
    TOWER_RELOAD_TIMES = 20

class Colors:
    BACKGROUND = (55, 55, 50)
    PATH = (255, 255, 0)
    START = (0, 255, 0)
    END = (255, 0, 0)
    WALLS_VERTICAL = (200, 200, 200)
    WALLS_HORIZONTAL = (255, 255, 255)
    MENU_BG = (0, 0, 255)
    MENU_TEXT = (255, 0, 255)
    BUTTONS = (255, 255, 0)

class Difficulty:
    NOOB = 0
    EASY = 1    
    NORMAL = 2
    HARD = 3
    HARDER = 4
    IMPOSSIBLE = 5


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

class Wave_difficulty:
    class Noob_wave:
        def noob_wave(wave:int) -> float:
            return wave+e**((-0.2**0.5)*wave+2)*sin(10*wave)+5

    class Easy_wave:    
        def easy_wave(wave:int) -> float:
            return wave+e**(-0.2*wave+2)*sin(10*wave)+5

    class Normal_wave:
        def normal_wave(wave:int) -> float:
            return wave+e**(-0.1*wave+2)*sin((10**0.5)*wave)+6
        
    class Hard_wave:
        def hard_wave(wave:int) -> float:
            return wave**0.8*(e**(sin(wave)))
        
    class Harder_wave:
        def harder_wave(wave:int) -> float:
            return wave**1.5+5*(e**(sin(5*wave)))
        
    class Impossible_wave:
        def impossible_wave(wave:int) -> float:
            return wave**2*(e**(sin(wave)))
        
    waves_dict = {
        Difficulty.NOOB : Noob_wave.noob_wave,
        Difficulty.EASY : Easy_wave.easy_wave,
        Difficulty.NORMAL : Normal_wave.normal_wave,
        Difficulty.HARD : Hard_wave.hard_wave,
        Difficulty.HARDER : Harder_wave.harder_wave,
        Difficulty.IMPOSSIBLE : Impossible_wave.impossible_wave
    }


class Gui_font:
    size = 20
    path = os.path.join(Directory.ASSETS_DIR, "fonts", "UbuntuNerdFont-Bold.ttf")