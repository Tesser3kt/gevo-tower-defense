from pygame.sprite import RenderUpdates
from pygame.time import Clock
from pygame import event, QUIT, quit
from pygame import locals

from config.settings.general_config import Economy, Game, Wave_function
from game_objects.enemies.enemy_object import EnemyObject
from grafics_manager.grafics_manager import GraficsManager
import wave_maker

class GameManager:
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

    def wave_loader(self, wave_function:Wave_function, wave: int) -> list[EnemyObject]:
        """ Load wave from config"""
        enemies = wave_maker.create_wave(wave)
        #enemies in a list


    def handle_input(self):
        """ Handle input from user"""
        for event in event.get():
            if event.type == QUIT:
                quit()
            elif event.type == locals.K_ESCAPE:
                self.pause = not self.pause

    def spawn_enemy(self,wave: list(EnemyObject), frames, spawn_delay) -> None:
        """ Add enemies from list to enemies group and spawn them in intervals"""
        if len(wave) == 0:
            return None
        
        for enemy in wave:
            self.enemies.add(enemy)
            self.moving_objects.add(enemy)
            self.actual_wave.add(enemy)

        if frames % spawn_delay == 0:
            enemy = self.actual_wave[0]
            #TODO: enemy.spawn()
            self.actual_wave.remove(enemy)
        
           

    def handle_enemy_hp(self) -> None:
        """ Check if enemy is dead and kill it"""
        for enemy in self.enemies:
            if enemy.hp <= 0:
                enemy.kill()



    def update(self, frames) -> None:
        """ Update game state"""

        #TODO: load wave from config and add it below
        self.spawn_enemy(wave ,frames)

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
    
    
        