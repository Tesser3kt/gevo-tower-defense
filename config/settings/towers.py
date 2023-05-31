"""Configuration file for towers"""
from config.enums.towers_ability import Ability
from config.enums.towers_ammo import Ammo


class Basic:
    ABILITY = None
    TYPE = "projectile"

    RANGE = 2
    COST = 200

    DAMAGE = 1
    DAMAGE_PER_LEVEL = 1.5

    RELOAD_TIME = 1
    RELOAD_TIME_PER_LEVEL = -0.025

    AMMO_TYPE = Ammo.BULLET

    IMAGE = "basic"

class Eyes:
    ABILITY = Ability.ATTACK_ALL
    TYPE = "projectile"

    RANGE = 3
    COST = 325

    DAMAGE = 1.5
    DAMAGE_PER_LEVEL = 1.5

    RELOAD_TIME = 1
    RELOAD_TIME_PER_LEVEL = -0.125

    AMMO_TYPE = Ammo.BULLET

    IMAGE = "eyes"

class Cannon:
    ABILITY = Ability.SPLASH_DAMAGE
    TYPE = "splash"

    RANGE = 6
    COST = 500

    DAMAGE = 5
    DAMAGE_PER_LEVEL = 1.5

    RELOAD_TIME = 1
    RELOAD_TIME_PER_LEVEL = -0.125

    AMMO_TYPE = Ammo.ROCKET

    IMAGE = "cannon"

class Yeti:
    ABILITY = Ability.FREEZE_ENEMIES
    TYPE = "splash"

    RANGE = 3
    COST = 750

    DAMAGE = 0
    DAMAGE_PER_LEVEL = 1.5

    RELOAD_TIME = 0
    RELOAD_TIME_PER_LEVEL = 0

    FREEZE_TIME = 0.5
    FREEZE_TIME_PER_LEVEL =  0.5

    AMMO_TYPE = Ammo.SNOWFLAKE

    IMAGE = "yeti"

class Laser:
    ABILITY = Ability.DESTROYS_CAMOUFLAGE
    TYPE = "projectile"

    RANGE = 5
    COST = 1000

    DAMAGE = 0.5
    DAMAGE_PER_LEVEL = 2

    RELOAD_TIME = 0
    RELOAD_TIME_PER_LEVEL = 0

    AMMO_TYPE = Ammo.LASER

    IMAGE = "laser"

tower_types  = [Basic, Eyes, Cannon, Yeti, Laser]
tower_dict = {}

for tower in tower_types:
    tower_dict[tower.__name__.lower()] = tower