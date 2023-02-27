"""Configuration file"""
import enemies, towers, projectiles


class Window:  
    HEIGHT = 800
    WIDTH = 960

class Tile:
    PIXEL_SIZE = 16
    HEIGHT = 50
    WIDTH = 60

class Directory:
    BASE_DIR = "Amogus"
    ASSETS_DIR = "Amogus"
    
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
#   IDK CO TO JE TO NADTÍM

    NOOB_SPAWN_PROBS = {
        "enemies.Normal" : 1, 
        "enemies.Fast" : 0,
        "enemies.Camo" : 0,
        "enemies.Boss" : 0,
        "enemies.Tank" : 0
    }

    EASY_SPAWN_PROBS = {
        "enemies.Normal" : 0.5,
        "enemies.Fast" : 0.5,
        "enemies.Camo" : 0,
        "enemies.Boss" : 0,
        "enemies.Tank" : 0
    }

    NORMAL_SPAWN_PROBS = {
        "enemies.Normal" : 0.25,
        "enemies.Fast" : 0.25,
        "enemies.Camo" : 0.2,
        "enemies.Boss" : 0.1,
        "enemies.Tank" : 0.2
    }

    HARD_SPAWN_PROBS = {
        "enemies.Normal" : 0.4,
        "enemies.Fast" : 0.2,
        "enemies.Camo" : 0.2,
        "enemies.Boss" : 0.1,
        "enemies.Tank" : 0.1
    }

    HARDER_SPAWN_PROBS = {
        "enemies.Normal" : 0.2,
        "enemies.Fast" : 0.2,
        "enemies.Camo" : 0.2,
        "enemies.Boss" : 0.2,
        "enemies.Tank" : 0.2
    }

    IMPOSSIBLE_SPAWN_PROBS = {
        "enemies.Normal" : 0.05,
        "enemies.Fast" : 0.05,
        "enemies.Camo" : 0.1,
        "enemies.Boss" : 0.5,
        "enemies.Tank" : 0.3
    }

