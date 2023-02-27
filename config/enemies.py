"""Enemies configuration file"""

class Normal:
    """Normal enemy"""
    ABILITY = None
    HEALTH = 1
    SPEED = 0.5

    UPGRADED_HEALTH = HEALTH + 2
    UPGARDED_SPEED = SPEED + 0.25

    IMAGE = "normal.png"
    IMAGE_UPGRADE_1 = "normal_upgrade_1.png"
    IMAGE_UPGRADE_2 = "normal_upgrade_2.png"
    IMAGE_UPGRADE_3 = "normal_upgrade_3.png"
    IMAGE_UPGRADE_4 = "normal_upgrade_4.png"
    IMAGE_UPGRADE_5 = "normal_upgrade_5.png"

class Camo:
    """Camo enemy"""
    ABILITY = "Masked"
    HEALTH = 3
    SPEED = 0.5

    UPGARDED_HEALTH = HEALTH + 2
    UPGARDED_SPEED = SPEED + 0.25

    IMAGE = "camo.png"
    IMAGE_UPGRADE_1 = "camo_upgrade_1.png"
    IMAGE_UPGRADE_2 = "camo_upgrade_2.png"
    IMAGE_UPGRADE_3 = "camo_upgrade_3.png"
    IMAGE_UPGRADE_4 = "camo_upgrade_4.png"
    IMAGE_UPGRADE_5 = "camo_upgrade_5.png"


class Fast:
    """Fast enemy"""
    ABILITY = "Fast"
    HEALTH = 1
    SPEED = 2

    UPGARDED_HEALTH = HEALTH + 2
    UPGARDED_SPEED = SPEED + 0.5

    IMAGE = "fast.png"
    IMAGE_UPGRADE_1 = "fast_upgrade_1.png"
    IMAGE_UPGRADE_2 = "fast_upgrade_2.png"
    IMAGE_UPGRADE_3 = "fast_upgrade_3.png"
    IMAGE_UPGRADE_4 = "fast_upgrade_4.png"
    IMAGE_UPGRADE_5 = "fast_upgrade_5.png"

class Boss:
    """Boss enemy"""
    ABILITY = "Boss"
    HEALTH = 25
    SPEED = 0.25

    UPGARDED_HEALTH = HEALTH * 1.5
    UPGARDED_SPEED = SPEED + 2

    IMAGE = "boss.png"
    IMAGE_UPGRADE_1 = "boss_upgrade_1.png"
    IMAGE_UPGRADE_2 = "boss_upgrade_2.png"
    IMAGE_UPGRADE_3 = "boss_upgrade_3.png"
    IMAGE_UPGRADE_4 = "boss_upgrade_4.png"
    IMAGE_UPGRADE_5 = "boss_upgrade_5.png"

class Tank:
    """Tank enemy"""
    ABILITY = "Tank"
    HEALTH = 5
    SPEED = 0.5

    UPGARDED_HEALTH = HEALTH + 5
    UPGARDED_SPEED = SPEED + 0.25

    IMAGE = "tank.png"
    IMAGE_UPGRADE_1 = "tank_upgrade_1.png"
    IMAGE_UPGRADE_2 = "tank_upgrade_2.png"
    IMAGE_UPGRADE_3 = "tank_upgrade_3.png"
    IMAGE_UPGRADE_4 = "tank_upgrade_4.png"
    IMAGE_UPGRADE_5 = "tank_upgrade_5.png"