"""Configuration for the level generator."""
from config import Window


class Config:
    MAX_TURNING_POINTS = Window.WIDTH//8
    MIN_TURNING_POINTS = Window.WIDTH//16