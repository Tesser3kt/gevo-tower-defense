"""Configuration for the level generator."""
from config import Window

class Config_lvl_gen:
    MAX_TURNING_POINTS = Window.WIDTH//8
    MIN_TURNING_POINTS = Window.WIDTH//16

    MAX_PROB = 1000
    PROB_DECREASE = 10

    PATH_COLOR = (255, 255, 0)