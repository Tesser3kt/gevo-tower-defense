"""Enemies configuration file"""

class Casual:
    """casual enemy"""
    ABILITY = None
    HEALTH = 1
    SPEED = 0.5

    UPGRADED_HEALTH = HEALTH + 2
    UPGARDED_SPEED = SPEED + 0.25

    IMAGE = "casual.png"
    IMAGE_UPGRADE_1 = "casual_upgrade_1.png"
    IMAGE_UPGRADE_2 = "casual_upgrade_2.png"
    IMAGE_UPGRADE_3 = "casual_upgrade_3.png"
    IMAGE_UPGRADE_4 = "casual_upgrade_4.png"
    IMAGE_UPGRADE_5 = "casual_upgrade_5.png"

class Camo:
    """camo enemy"""
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


class Speeder:
    """speeder enemy"""
    ABILITY = "Speeder"
    HEALTH = 1
    SPEED = 2

    UPGARDED_HEALTH = HEALTH + 2
    UPGARDED_SPEED = SPEED + 0.5

    IMAGE = "speeder.png"
    IMAGE_UPGRADE_1 = "speeder_upgrade_1.png"
    IMAGE_UPGRADE_2 = "speeder_upgrade_2.png"
    IMAGE_UPGRADE_3 = "speeder_upgrade_3.png"
    IMAGE_UPGRADE_4 = "speeder_upgrade_4.png"
    IMAGE_UPGRADE_5 = "speeder_upgrade_5.png"

class Boss:
    """boss enemy"""
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

class Bruiser:
    """bruiser enemy"""
    ABILITY = "Bruiser"
    HEALTH = 5
    SPEED = 0.5

    UPGARDED_HEALTH = HEALTH + 5
    UPGARDED_SPEED = SPEED + 0.25

    IMAGE = "bruiser.png"
    IMAGE_UPGRADE_1 = "bruiser_upgrade_1.png"
    IMAGE_UPGRADE_2 = "bruiser_upgrade_2.png"
    IMAGE_UPGRADE_3 = "bruiser_upgrade_3.png"
    IMAGE_UPGRADE_4 = "bruiser_upgrade_4.png"
    IMAGE_UPGRADE_5 = "bruiser_upgrade_5.png"