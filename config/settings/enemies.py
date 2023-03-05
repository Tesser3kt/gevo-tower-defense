"""Enemies configuration file"""
from config.enums.enemy_ability import Ability

class Casual:
    """casual enemy"""
    ABILITY = None
    HEALTH = 1
    SPEED = 0.5

    HEALTH_PER_LEVEL = 2
    SPEED_PER_LEVEL = 0.25

    IMAGE = "casual"

class Camo:
    """camo enemy"""
    ABILITY = Ability.MASKED
    HEALTH = 3
    SPEED = 0.5

    HEALTH_PER_LEVEL = 2
    SPEED_PER_LEVEL = 0.25

    IMAGE = "camo"

class Speeder:
    """speeder enemy"""
    ABILITY = Ability.SPEEDER
    HEALTH = 1
    SPEED = 2

    HEALTH_PER_LEVEL = 1.5
    SPEED_PER_LEVEL = 0.5

    IMAGE = "speeder"

class Boss:
    """boss enemy"""
    ABILITY = Ability.BOSS
    HEALTH = 25
    SPEED = 0.25

    HEALTH_PER_LEVEL = 10
    SPEED_PER_LEVEL = 2

    IMAGE = "boss"

class Bruiser:
    """bruiser enemy"""
    ABILITY = Ability.BRUISER
    HEALTH = 5
    SPEED = 0.5

    HEALTH_PER_LEVEL = 5
    SPEED_PER_LEVEL = 0.25

    IMAGE = "bruiser"