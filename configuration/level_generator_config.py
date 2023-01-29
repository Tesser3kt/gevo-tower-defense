"""Configuration for the level generator."""
from config import Tile

class Config_lvl_gen:
    MAX_TURNING_POINTS = Tile.WIDTH//8
    MIN_TURNING_POINTS = Tile.WIDTH//16

    MAX_PROB = 1000
    PROB_DECREASE = 400
    MIN_STRAIGHT_LINE = 5

    PATH_COLOR = (255, 255, 0)

    RANDOM_PROBS = {
        "UP": 350,
        "DOWN": 150,
        "LEFT": 250,
        "RIGHT": 250
    }