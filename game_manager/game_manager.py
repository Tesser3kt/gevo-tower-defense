#pygame imports
from pygame.sprite import RenderUpdates
from pygame.time import Clock
from pygame import event, QUIT, quit
from pygame import locals

# python imports
import logging

# project imports

# config
from config.settings.enemies import *
from config.settings.towers import *
from config.settings.general_config import Economy, Game, Wave_function

# objects
from game_objects.enemies.enemy_object import EnemyObject
from game_objects.towers.tower_object import TowerObject
from game_objects.towers.tower_type import TowerType
from game_objects.towers.projectile_tower import ProjectileTower
from game_objects.towers.splash_tower import SplashTower

# other
from grafics_manager.grafics_manager import GraphicsManager
from game_manager import wave_maker, spawn_delay
from level_converter.level_converter import convert_level

class GameManager:
    """ The ultimate class that controls everything everywhere """
    def __init__(self) -> None:
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.living_enemies = RenderUpdates()
        self.not_spawned_enemies = RenderUpdates()
        self.effects = RenderUpdates()


        self.moving_objects = RenderUpdates()
        self.static_objects = RenderUpdates()

        self.ui = RenderUpdates()

        self.coins:int = Economy.STARTING_MONEY
        self.lives:int = Economy.STARTING_LIVES
        self.level:int = Game.START_LEVEL
        self.wave:int = Game.START_WAVE


        self.clock = Clock()

        self.running = True
        self.pause = False
        self.wave_running = False

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#-------------------------------------- HANDLE ENEMIES ------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------


    def get_start(self, level:int) -> tuple:
        """ Get start position from level"""

        logging.debug(f"Getting start position from level {level}")
        return convert_level(level)["start"][0].x, convert_level(level)["start"][0].y
    

    def wave_loader(self, wave: int) -> list[EnemyObject]:

        """ Load wave from config and return a list of EnemyObjects. The wave is randomized"""
        logging.debug(f"Loading wave {wave}")
        enemies = wave_maker.create_wave(wave)
        #name of enemies in a list
        enemy_objects = []
        x,y = self.get_start(self.level)

        for enemy in enemies:
            try:
                hp = enemy_dict[enemy].HEALTH
                size = enemy_dict[enemy].SIZE
                image = ... #TODO: image
                speed = enemy_dict[enemy].SPEED
                direction = ... #TODO: direction
                animation = ... #TODO: animation
                animation_index = ... #TODO: animation_index
                detectable = enemy_dict[enemy].DETECTABLE
                lvl = enemy_dict[enemy].START_LEVEL
            except:
                logging.error(f"Cannot load informations about enemy: {enemy}")
            try :
                enemy_objects.append(EnemyObject(hp, x, y, size, size, image, speed, direction, animation, animation_index, detectable, lvl))
            except:
                logging.error(f"Cannot create enemy {enemy}")

        logging.debug(f"Loaded wave {wave} with {len(enemy_objects)} enemies")

        # EnemyObjects in a list
        return enemy_objects
    
    def add_enemies_to_group(self, enemies: list(EnemyObject)) -> None:
        """ Add enemies in list to not_spawned_enemies group. Called after wave_loader"""
        logging.debug(f"Adding {len(enemies)} enemies to not_spawned_enemies group")
        for enemy in enemies:
            self.not_spawned_enemies.add(enemy)
    
    
    def spawn_enemy(self, frames:int, spawn_delay:int) -> None:
        """ Transfer enemy from not_spawned to living and moving groups in intervals. Called every frame"""
        if len(self.not_spawned_enemies) == 0:
            return None
        
        if frames % spawn_delay == 0:
            enemy = self.not_spawned_enemies[0]
            self.not_spawned_enemies.remove(self.not_spawned_enemies[0])

            self.living_enemies.add(enemy)
            self.moving_objects.add(enemy)

            logging.debug(f"Spawned enemy {enemy} with spawn delay {spawn_delay}")
            # Enemy is in living group and moving objects group --> One group will be drawn every frame


    def move_enemy(self, enemy: EnemyObject, position:tuple) -> None:
        """ Move enemy to position"""

        logging.debug(f"Moving enemy {enemy} to position {position}")
        enemy.x = position[0]
        enemy.y = position[1]
        #TODO animation index change?
           

    def handle_enemy_hp(self) -> None:
        """ Check if enemy is dead and kill it"""

        for enemy in self.living_enemies:
            if enemy.hp <= 0:
                enemy.kill()
        
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------ HANDLE TOWERS ---------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def buy_tower(self, tower:TowerType, position:tuple) -> TowerObject:
        """ Buy tower if player has enough coins and create tower object and add it in static objects + towers group"""
        if self.coins >= tower_dict[tower].PRICE:
            self.coins -= tower_dict[tower].PRICE
            if tower_dict[tower].TYPE == "projectile":
                x,y = position
                width = Tile.PIXEL_SIZE
                height = Tile.PIXEL_SIZE
                image = ... # TODO: image
                animation = ... # TODO: animation
                animation_index = ... # TODO: animation index
                damage = tower_dict[tower].DAMAGE
                reload_time = tower_dict[tower].RELOAD_TIME
                tower_type = tower
                projectile_animation = ... # TODO: animation
                projectile_animation_index = ... # TODO: animation index

                tower_object = ProjectileTower()#TODO počkat, než Jáchym mi dá pořadí argumentů

                self.static_objects.add(tower_object)
                self.towers.add(tower_object)
            elif tower_dict[tower].TYPE == "splash":
                x,y = position
                width = Tile.PIXEL_SIZE
                height = Tile.PIXEL_SIZE
                image = ... # TODO: image
                animation = ... # TODO: animation
                animation_index = ... # TODO: animation index
                damage = tower_dict[tower].DAMAGE
                reload_time = tower_dict[tower].RELOAD_TIME
                tower_type = tower
                projectile_animation = ... # TODO: animation
                projectile_animation_index = ... # TODO: animation index

                tower_object = SplashTower()#TODO počkat, než Jáchym mi dá pořadí argumentů

                self.static_objects.add(tower_object)
                self.towers.add(tower_object)
            else:
                logging.error(f"Cannot buy tower {tower} because it has unknown type")
            return True
        else:
            return False
        

        

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------ IMPORTANT ---------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def handle_input(self):
        """ Handle input from user"""

        for event in event.get():
            if event.type == QUIT:
                quit()
            elif event.type == locals.K_ESCAPE:
                self.pause = not self.pause


    def update(self, frames) -> None:
        """ Update game state every frame"""

        if not self.wave_running:
            # Load wave
            wave = self.wave_loader(self.wave)
            self.add_enemies_to_group(wave)        
        # Spawn enemies in intervals
        self.spawn_enemy(frames, spawn_delay.spawn_delay(self.not_spawned_enemies[0], self.not_spawned_enemies[1]))


        self.handle_enemy_hp()
    

    def run(self) -> None:
        """ Main game loop"""

        frames = 0
        while self.running:
            frames += 1 #nevim jestli maji bezet kdyz je pauza
            self.clock.tick(Game.FPS)

            self.handle_input()

            if self.pause:
                continue

            self.update()
    
    