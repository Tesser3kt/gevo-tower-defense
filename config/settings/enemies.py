"""Enemies configuration file"""
from config.enums.enemy_ability import Ability
from config.settings.general_config import Tile

class Casual:
    """casual enemy"""
    ABILITY = None
    HEALTH = 1
    SPEED = 0.5
    SIZE = Tile.PIXEL_SIZE
    DETECTABLE = True
    START_LEVEL = 1

    HEALTH_PER_LEVEL = 2
    SPEED_PER_LEVEL = 0.25

    IMAGE = "casual"

class Camo:
    """camo enemy"""
    ABILITY = Ability.MASKED
    HEALTH = 3
    SPEED = 0.5
    SIZE = Tile.PIXEL_SIZE
    DETECTABLE = False
    START_LEVEL = 1

    HEALTH_PER_LEVEL = 2
    SPEED_PER_LEVEL = 0.25

    IMAGE = "camo"

class Speeder:
    """speeder enemy"""
    ABILITY = Ability.SPEEDER
    HEALTH = 1
    SPEED = 2
    SIZE = Tile.PIXEL_SIZE
    DETECTABLE = True
    START_LEVEL = 1

    HEALTH_PER_LEVEL = 1.5
    SPEED_PER_LEVEL = 0.5

    IMAGE = "speeder"

class Boss:
    """boss enemy"""
    ABILITY = Ability.BOSS
    HEALTH = 25
    SPEED = 0.25
    SIZE = Tile.PIXEL_SIZE
    DETECTABLE = True
    START_LEVEL = 1

    HEALTH_PER_LEVEL = 10
    SPEED_PER_LEVEL = 2

    IMAGE = "boss"

class Bruiser:
    """bruiser enemy"""
    ABILITY = Ability.BRUISER
    HEALTH = 5
    SPEED = 0.5
    SIZE = Tile.PIXEL_SIZE
    DETECTABLE = True
    START_LEVEL = 1

    HEALTH_PER_LEVEL = 5
    SPEED_PER_LEVEL = 0.25

    IMAGE = "bruiser"

enemy_dict = {
    "casual": Casual,
    "camo": Camo,
    "speeder": Speeder,
    "boss": Boss,
    "bruiser": Bruiser
}