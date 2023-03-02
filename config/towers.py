"""Configuretion file for towers"""

class Basic:
    ABIILITY = None

    RANGE = 2
    COST = 200

    DAMAGE = 1
    UPGRADED_DAMAGE = DAMAGE * 1.5

    RECHARGE_TIME = 1
    RECHARGE_TIME_UPGRADE = RECHARGE_TIME//1.125

    AMMO_TYPE = "Bullet"

    IMAGE = "basic.png"
    IMAGE_UPGRADE_1 = "Basic_upgrade_1.png"
    IMAGE_UPGRADE_2 = "Basic_upgrade_2.png"
    IMAGE_UPGRADE_3 = "Basic_upgrade_3.png"
    IMAGE_UPGRADE_4 = "Basic_upgrade_4.png"
    IMAGE_UPGRADE_5 = "Basic_upgrade_5.png"

class Eyes:
    ABLILITY = "Can attack all enemy types"

    RANGE = 3
    COST = 325

    DAMAGE = 1.5
    UPGRADED_DAMAGE = DAMAGE * 1.5

    RECHARGE_TIME = 1
    RECHARGE_TIME_UPGRADE = RECHARGE_TIME//1.25

    AMMO_TYPE = "Bullet"

    IMAGE = "eyes.png"
    IMAGE_UPGRADE_1 = "eyes_upgrade_1.png"
    IMAGE_UPGRADE_2 = "eyes_upgrade_2.png"
    IMAGE_UPGRADE_3 = "eyes_upgrade_3.png"
    IMAGE_UPGRADE_4 = "eyes_upgrade_4.png"
    IMAGE_UPGRADE_5 = "eyes_upgrade_5.png"

class Cannon:
    ABLILITY = "Splash damage"

    RANGE = 6
    COST = 500

    DAMAGE = 5
    UPGRADED_DAMAGE = DAMAGE * 1.5

    RECHARGE_TIME = 1
    RECHARGE_TIME_UPGRADE = RECHARGE_TIME//1.25

    AMMO_TYPE = "Rocket"

    IMAGE = "cannon.png"
    IMAGE_UPGRADE_1 = "cannon_upgrade_1.png"
    IMAGE_UPGRADE_2 = "cannon_upgrade_2.png"
    IMAGE_UPGRADE_3 = "cannon_upgrade_3.png"
    IMAGE_UPGRADE_4 = "cannon_upgrade_4.png"
    IMAGE_UPGRADE_5 = "cannon_upgrade_5.png"

class Yeti:
    ABILITY = "Freeze enemies"

    RANGE = 3
    COST = 750

    DAMAGE = 0
    UPGRADED_DAMAGE = DAMAGE * 1.5

    RECHARGE_TIME = 0
    RECHARGE_TIME_UPGRADE = RECHARGE_TIME//1.25

    FREEZE_TIME = 0.5
    UPGRADED_FREEZE_TIME = FREEZE_TIME * 1.5

    AMMO_TYPE = "Snowflake"

    IMAGE = "yeti.png"
    IMAGE_UPGRADE_1 = "yeti_upgrade_1.png"
    IMAGE_UPGRADE_2 = "yeti_upgrade_2.png"
    IMAGE_UPGRADE_3 = "yeti_upgrade_3.png"
    IMAGE_UPGRADE_4 = "yeti_upgrade_4.png"
    IMAGE_UPGRADE_5 = "yeti_upgrade_5.png"

class Laser:
    ABILITY = "Destroys camouflage paint from hidden cars, therefore they act like normal enemies"

    RANGE = 5
    COST = 1000

    DAMAGE = 0.5
    UPGRADED_DAMAGE = DAMAGE * 2

    RECHARGE_TIME = 0
    RECHARGE_TIME_UPGRADE = RECHARGE_TIME//1.25

    AMMO_TYPE = "Laser"

    IMAGE = "laser.png"
    IMAGE_UPGRADE_1 = "laser_upgrade_1.png"
    IMAGE_UPGRADE_2 = "laser_upgrade_2.png"
    IMAGE_UPGRADE_3 = "laser_upgrade_3.png"
    IMAGE_UPGRADE_4 = "laser_upgrade_4.png"
    IMAGE_UPGRADE_5 = "laser_upgrade_5.png"