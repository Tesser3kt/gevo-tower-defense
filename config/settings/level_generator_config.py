"""Configuration for the level generator."""
from config.settings.general_config import Tile

class Config_lvl_gen:
    MAX_TURNING_POINTS = Tile.WIDTH//8
    MIN_TURNING_POINTS = Tile.WIDTH//16

#Probs for difficulties
    PROBS = [
        (3000, 0, 4000),
        (750, 5, 4000),
        (450, 10, 4000),
        (250, 5, 8000),
        (20, 10, 4000),
        (0, 40, 100)
    ] # (PROB_DECREASE, MIN_STRAIGHT_LINE, MAX_PROB)

    PROB_NUMERATOR = 3
    PROB_DIVISOR = 4
