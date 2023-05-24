#pygame imports
from pygame.sprite import RenderUpdates
from pygame.time import Clock
from pygame import event, QUIT, quit
from pygame import locals

# python imports
import logging

# project imports
from config.settings.enemies import *
from config.settings.general_config import Economy, Game, Wave_function
from game_objects.enemies.enemy_object import EnemyObject
from grafics_manager.grafics_manager import GraficsManager
from game_manager import wave_maker
from level_converter.level_converter import convert_level

class GameManager:
    """ The ultimate class that controls everything everywhere """
    def __init__(self) -> None:
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.enemies = RenderUpdates()
        self.effects = RenderUpdates()

        self.actual_wave = RenderUpdates()

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
    

    def handle_input(self):
        """ Handle input from user"""

        for event in event.get():
            if event.type == QUIT:
                quit()
            elif event.type == locals.K_ESCAPE:
                self.pause = not self.pause


    def spawn_enemy(self,wave: list(EnemyObject), frames:int, spawn_delay:int) -> None:
        """ Add enemies from list to enemies group and spawn them in intervals"""

        if len(wave) == 0:
            return None
        
        for enemy in wave:
            self.enemies.add(enemy)
            self.moving_objects.add(enemy)
            self.actual_wave.add(enemy)
            #isn't actual_wave the same as enemies?

        if frames % spawn_delay == 0:
            enemy = self.actual_wave[0]
            #TODO: enemy.spawn()
            self.actual_wave.remove(enemy)
        

    def move_enemy(self, enemy: EnemyObject, position:tuple) -> None:
        """ Move enemy to position"""

        logging.debug(f"Moving enemy {enemy} to position {position}")
        enemy.x = position[0]
        enemy.y = position[1]
        #animation index change?
           

    def handle_enemy_hp(self) -> None:
        """ Check if enemy is dead and kill it"""

        for enemy in self.enemies:
            if enemy.hp <= 0:
                enemy.kill()


    def update(self, frames) -> None:
        """ Update game state"""

        wave = self.wave_loader(self.wave)
        self.spawn_enemy(wave, frames, spawn_delay)

        #TODO: projectiles

        #TODO: tower rotation

        #TODO: idk

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
    
    