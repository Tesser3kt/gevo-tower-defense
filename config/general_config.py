"""Configuration file"""
from config.enemies import *
from config.projectiles import *
from config.towers import *

import os


class Window:  
    HEIGHT = 800
    WIDTH = 960

class Tile:
    PIXEL_SIZE = 16
    HEIGHT = 50
    WIDTH = 60
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

class Colors:
    BACKGROUND = (0, 0, 0)
    PATH = (255, 255, 0)
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

# Asi to může být random, ale tak prozatím jsem to dal sem
class Nooob_spawn_probs:
    NORMAL = 1
    FAST = 0
    CAMO = 0
    BOSS = 0
    TANK = 0

class Easy_spawn_probs:
    NORMAL = 0.5
    FAST = 0.5
    CAMO = 0
    BOSS = 0
    TANK = 0
    
class NORMAL_spawn_probs:
    NORMAL = 0.25
    FAST = 0.25
    CAMO = 0.2
    BOSS = 0.1
    TANK = 0.2

class Hard_spawn_probs:
    NORMAL = 0.2
    FAST = 0.2
    CAMO = 0.2
    BOSS = 0.1
    TANK = 0.3

class Harder_spawn_probs:
    NORMAL = 0.1
    FAST = 0.1
    CAMO = 0.1
    BOSS = 0.1
    TANK = 0.6

class Impossible_spawn_probs:
    NORMAL = 0.1
    FAST = 0.1
    CAMO = 0.2
    BOSS = 0.2
    TANK = 0.4
