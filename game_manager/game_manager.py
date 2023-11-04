# pygame imports
from pygame.sprite import RenderUpdates
from pygame.time import Clock
from pygame import QUIT, quit, font, locals, display, SCALED,event 
from pygame.transform import scale
import pygame as pg
# python imports
import logging
import math
import random


# --- PROJECT IMPORTS ---

# config
from config.settings.enemies import *
from config.settings.towers import *
from config.settings.general_config import Economy, Game, Difficulty, Wave_difficulty, Window, Colors

# objects
# from game_objects.enemies.enemy_object import EnemyObject
from game_objects.towers.projectile_tower import ProjectileTower
from game_objects.towers.splash_tower import SplashTower
from game_objects.tiles.tile_object import TileObject
from game_objects.tiles.tile_type import TileType
from game_objects.towers.tower_type import TowerType
from game_objects.towers.tower_object import TowerObject
from game_objects.enemies.enemy_object import EnemyObject
from game_objects.mobile_object import MobileObject

# other
from graphics_manager.graphics_manager import GraphicsManager
from game_manager import wave_maker, spawn_delay
from level_converter.level_converter import convert_level
from level_generator.level_generator import generate_level
from level_generator.wall_generator import create_walls

from ai.ai import AI


# texture loader
#from texture_loader.texture_loader import TextureLoader

# gui
from gui.gui import Gui

class GameManager:
    """ The ultimate class that controls everything everywhere """
    def __init__(self) -> None:
        self.gui = None
        self.graphics_manager = None
        self.ai = None

        self.changed_rects = []
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.living_enemies = RenderUpdates()
        self.enemies = RenderUpdates()
        self.not_spawned_enemies = []
        self.effects = RenderUpdates()
        self.tiles = RenderUpdates()
        self.occupied_tiles = RenderUpdates()
        self.default_tiles = RenderUpdates()
        self.wall_tiles = RenderUpdates()
        self.projectiles = RenderUpdates()

        self.moving_objects = RenderUpdates()
        self.static_objects = RenderUpdates()

        self.ui = RenderUpdates()

        self.coins:int = Economy.STARTING_MONEY
        self.new_coins:int = Economy.STARTING_MONEY
        self.lives:int = Economy.STARTING_LIVES
        self.new_lives:int = Economy.STARTING_LIVES
        self.level:int = Game.START_LEVEL
        self.wave:int = Game.START_WAVE
        self.new_wave:int = Game.START_WAVE
        self.frames = 0

        self.converted_level = []
        self.clicked_card = None #Sprite, Rect  --> Tuple
        self.clicked_tower_type = None #TowerType

        self.clock = Clock()

        self.running = True
        self.pause = False
        self.wave_running = False

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#-------------------------------------- STARTER THINGS ------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------   


    def init_modules(self) -> None:
        """ Initialize some modules"""
        font.init()
        self.graphics_manager = GraphicsManager()
        self.gui = Gui(self.graphics_manager)


    def initialize(self):
        """ Initialize game"""
        generate_level(self.level)
        create_walls(self.level)
        self.graphics_manager.init_graphics()
        self.graphics_manager.load_all_textures()

        self.converted_level = convert_level(self.level)

        self.ai = AI(self.converted_level, self.enemies)
        # self.ai.find_paths(self.converted_level["start"])



#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#---------------------------------------- GUI ---------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def update_gui(self) -> None:
        self.gui.show_stats(self.lives, self.coins, self.wave)
        self.gui.show_towers(self.graphics_manager.textures)

    def update_changed_rects(self) -> None:
        self.graphics_manager.rects_to_update = self.changed_rects
        self.graphics_manager.update()
        self.changed_rects = []

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#---------------------------------------- SHOW MAP ----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def show_map(self) -> None:
        """ Show map on screen"""
        special_wall = False
        for tile in self.converted_level:
            for rect in self.converted_level[tile]:    
                if tile == "walls":
                    t_type = TileType.WALL
                elif tile == "path":
                    t_type = TileType.OCCUPIED
                elif tile == "start":
                    t_type = TileType.OCCUPIED
                elif tile == "end":
                    t_type = TileType.OCCUPIED
                elif tile == "free_tile":
                    t_type = TileType.DEFAULT
                elif tile == "special_wall":
                    tile = "walls"
                    t_type = TileType.WALL
                    special_wall = True
                else:
                    print("Unknown tile type")

                if special_wall:
                    image = self.graphics_manager.textures["game_objects"]["tiles"]["horizontal_wall"][0]
                else:
                    image = self.graphics_manager.textures["game_objects"]["tiles"][tile][0]
                image = scale(image, (Window.PIXEL_SIZE, Window.PIXEL_SIZE))     

                tile_object = TileObject(rect.x, rect.y, Window.PIXEL_SIZE, Window.PIXEL_SIZE, image, t_type)

                if t_type == TileType.OCCUPIED:
                    self.occupied_tiles.add(tile_object)
                elif t_type == TileType.DEFAULT:
                    self.default_tiles.add(tile_object)
                elif t_type == TileType.WALL:
                    self.wall_tiles.add(tile_object)
                self.tiles.add(tile_object)
                self.static_objects.add(tile_object)
        self.graphics_manager.draw_group(self.tiles, True)
                
                

# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------
# #-------------------------------------- HANDLE ENEMIES ------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------

    def get_start(self) -> tuple:
        """ Get start position from level"""
        logging.debug(f"Getting start position from level {self.level}")
        return self.converted_level["start"][0].x, self.converted_level["start"][0].y

    def enemies_creator(self, level:Difficulty, wave: int):
        """ Load wave from config. The wave is randomized"""
        logging.debug(f"Loading wave {wave}")

        wave_function = Wave_difficulty.waves_dict[level]
        number_of_enemies = int(wave_function(wave))  
        if number_of_enemies < 2:
            number_of_enemies = 2
        enemies = wave_maker.create_wave(number_of_enemies, wave)
        #name of enemies in a list
    
        enemy_objects = []
        x,y = self.get_start()
        

        for enemy_name in enemies:
            try:
                hp = enemy_dict[enemy_name].HEALTH
                size = enemy_dict[enemy_name].SIZE
                image = self.graphics_manager.textures["game_objects"]["enemies"][enemy_dict[enemy_name].IMAGE][0]
                image = scale(image, (size, size))
                speed = enemy_dict[enemy_name].SPEED
                direction = (0, 0)
                animation_index = 0
                animation = self.graphics_manager.textures["game_objects"]["enemies"][enemy_dict[enemy_name].IMAGE]
                detectable = enemy_dict[enemy_name].DETECTABLE
                lvl = enemy_dict[enemy_name].START_LEVEL
            except KeyError:
                logging.debug(f"Enemy {enemy_name} is not in enemy_dict", KeyError)
            
            enemy = EnemyObject(hp, x, y, size, size, image, speed, direction, animation, animation_index, detectable, lvl)
            enemy_objects.append(enemy)

            # Adding the enemy into groups
            self.not_spawned_enemies.append(enemy)
            self.enemies.add(enemy)

        logging.info(f"Loaded wave {wave} with {number_of_enemies} enemies")
        
    
    def spawn_enemy(self, spawn_delay:int) -> None:
        """ Transfer enemy from not_spawned to living and moving groups in intervals. Called every frame"""
        if len(self.not_spawned_enemies) == 0:
            return 
        
        if self.frames % spawn_delay == 0:
            enemy = self.not_spawned_enemies.pop(0)

            self.living_enemies.add(enemy)
            self.moving_objects.add(enemy)

            logging.debug(f"Spawned enemy {enemy} with spawn delay {spawn_delay}")
            # Enemy is in living group and moving objects group --> One group will be drawn every frame
           
    def enemy_update(self) -> None:
        for enemy in self.living_enemies:
            if enemy.hp <= 0:
                enemy.kill()

            # else:
                # enemy_direction = self.ai.get_next_step(enemy)
            end = self.converted_level["end"]
            end_x, end_y = end[0].x, end[0].y
            start = self.converted_level["start"]
            start_x, start_y = start[0].x, start[0].x
            vector = (end_x-start_x, end_y-start_y)
            v_vector = (vector[0]**2 + vector[1]**2)**0.5
            vector = vector[0] / v_vector, vector[1] / v_vector



            enemy.direction = vector
            enemy.speed = Game.ENEMY_SPEED
            enemy.move()
            # print(vector)

        self.graphics_manager.draw_group(self.living_enemies, True)


    def next_wave(self) -> None:
        self.wave_running = True
        self.wave += 1
        self.enemies_creator(self.level, self.wave)
        self.spawn_enemy(spawn_delay.spawn_delay(self.not_spawned_enemies[0], self.not_spawned_enemies[1]))

    def kill_all_enemies(self) -> None:
        """ Kill all enemies in the game"""
        for enemy in self.living_enemies:
            enemy.kill()
        for enemy in self.not_spawned_enemies:
            enemy.kill()
        self.wave_running = False

        
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------ HANDLE TOWERS ---------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def buy_tower(self, tower:TowerType, position:tuple) -> TowerObject:
        """ Buy tower and place it on map. Also check if the position is valid"""
        if self.coins >= tower.COST:

            x,y = position
            width = Window.PIXEL_SIZE*4
            height = Window.PIXEL_SIZE*4
            image_name = tower.IMAGE
            image = self.graphics_manager.textures["game_objects"]["towers"][image_name][0]
            image = scale(image, (width, height))
            animation = self.graphics_manager.textures["game_objects"]["towers"][image_name]
            damage = tower.DAMAGE
            reload_time = tower.RELOAD_TIME
            tower_type = tower
            projectile_animation = self.graphics_manager.textures["game_objects"]["projectiles"][tower.AMMO_TYPE.value]

            if tower.TYPE == "projectile":
                tower_object = ProjectileTower(x, y, width, height, image, animation, damage, reload_time, tower_type, projectile_animation)

            elif tower.TYPE == "splash":
                tower_object = SplashTower(x, y, width, height, image, animation, damage, reload_time, tower_type, projectile_animation)

            else:
                logging.error(f"Cannot buy tower {tower} because it has unknown type")
                return False
            

            sus_tiles = []
            # Sus tiles are all tiles under Tower Object 
            for x in range(tower_object.rect.width//Window.PIXEL_SIZE):
                for y in range(tower_object.rect.height//Window.PIXEL_SIZE):
                    sus_tiles.append((tower_object.rect.x+x*Window.PIXEL_SIZE,tower_object.rect.y+y*Window.PIXEL_SIZE))

            the_tiles = []
            for tile in sus_tiles:
                the_tiles += [o for o in self.default_tiles if o.rect.topleft == tile]
                if len(the_tiles) == Window.CARD_RECT_WIDTH**2:
                    for a_tile in the_tiles:
                        self.default_tiles.remove(a_tile)
                        self.occupied_tiles.add(a_tile)
                        a_tile.type = TileType.OCCUPIED
                elif tile in [o.rect.topleft for o in self.occupied_tiles]:
                    tower_object.kill()
                    return False
                elif tile in [o.rect.topleft for o in self.towers]:
                    tower_object.kill()
                    return False
                elif tile in [o.rect.topleft for o in self.wall_tiles]:
                    tower_object.kill()
                    return False
                elif tile == sus_tiles[-1]:
                    logging.error("Nezna tile type, nemuze zkontrolovat co je pod towerkou")
                    tower_object.kill()
                    return False
                # SEM SE TO NORMALNE NEMUZE DOSTAT, JENOM KDYZ TO BUDE NEJAKY NOVY TILE TYPE
     
            self.static_objects.add(tower_object)
            self.towers.add(tower_object)
            self.graphics_manager.draw_object(tower_object, True)
            self.changed_rects.append(tower_object.rect)
            self.coins -= tower.COST
            return True
        else:
            print("Not enough money")
            return False
        
    def create_projectile(self, tower):
        projectile = MobileObject(tower.rect.x, tower.rect.y, Window.PIXEL_SIZE, Window.PIXEL_SIZE, tower.projectile_animation[0], Game.PROJECTILE_SPEED, (0, 0))
        self.projectiles.add(projectile)
        return projectile
            
    def shoot(self):   
        """ Shoot from tower"""
        if self.frames % Game.TOWER_RELOAD_TIMES == 0:
            if len(self.projectiles) < len(self.living_enemies):
                for tower in self.towers:
                # Find closest enemy
  
                    projectile = self.create_projectile(tower)
                    self.projectiles.add(projectile)



    def update_projectiles(self):
        target = None
        shortest_distance = 9999999999

        for projectile in self.projectiles:
            for enemy in self.enemies:
                distance = ((projectile.rect.x - enemy.rect.x) ** 2 + (projectile.rect.y - enemy.rect.y) ** 2)
                if distance < shortest_distance:
                    shortest_distance = distance
                    target = enemy

            if not target:
                self.projectiles.empty()
            else:
                vector = (target.rect.x-projectile.rect.x, target.rect.y-projectile.rect.y)
                v_vector = (vector[0]**2 + vector[1]**2)**0.5
                if v_vector != 0:
                    vector = (vector[0] / v_vector, vector[1] / v_vector)

                projectile.direction = vector
                projectile.speed = Game.PROJECTILE_SPEED
                projectile.move()


    def projectile_hit(self):
        if pg.sprite.groupcollide(self.projectiles, self.living_enemies, True, True):
            print("Hit")
            self.coins += Economy.MONEY_PER_KILL
        if pg.sprite.groupcollide(self.projectiles, self.wall_tiles, True, False):
            print("Hit wall")


        


    
        


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------ HANDLE CLICK ON TOWER CARD --------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
 
    def click_on_card(self):
        if self.clicked_card:
            self.graphics_manager.draw_rect(self.clicked_card[1], Colors.MENU_BG, False, self.gui.background)  
        clicked_cards = [card for card in self.gui.tower_cards if card.rect.collidepoint(pg.mouse.get_pos())]
        if not clicked_cards:
            return
        clicked_card = clicked_cards[0]
        rectangle = clicked_card.rect.copy()
        self.clicked_card = clicked_card, rectangle
        rectangle.x -= Window.CARD_RECT_WIDTH
        rectangle.y -= Window.CARD_RECT_WIDTH
        rectangle.width += 2*Window.CARD_RECT_WIDTH
        rectangle.height += 2*Window.CARD_RECT_WIDTH

        for rect, type in self.gui.tower_pos_types:
            if rect == self.clicked_card[0].rect.topleft:
                self.clicked_tower_type = type

        return True
    
    def handle_click_on_map(self):
        """ Handle click on map for tower placement"""
        clicked_tiles = [tile for tile in self.tiles if tile.rect.collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]-Window.GUI_HEIGHT)]
        if not clicked_tiles:
            return False # kdyz kliknu mimo mapu (GUI)
        clicked_tile = clicked_tiles[0]
        rectangle = clicked_tile.rect.copy()
        self.buy_tower(self.clicked_tower_type, (rectangle.x, rectangle.y)) # Can be succesful or not

        self.clicked_card = None
        self.clicked_tower_type = None
        self.gui.create_gui(self.lives, self.coins, self.wave, self.graphics_manager.textures)

# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------ IMPORTANT ---------------------------------------------------
# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------

    def handle_input(self):
        """ Handle input from user"""

        for event in pg.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.pause = not self.pause
                    # self.gui.pause_text(self.pause)
                if event.key == pg.K_SPACE:
                    self.kill_all_enemies()
                    self.next_wave()

            elif (event.type == pg.MOUSEBUTTONDOWN and event.button == 1) and self.click_on_card():
                self.graphics_manager.draw_rect(self.clicked_card[1], Colors.BUTTONS, False, self.gui.background)
                self.gui.show_tower_info(self.clicked_tower_type)

            elif self.clicked_card and (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
                self.handle_click_on_map()
 



    def update(self) -> None:
        """ Update game state every frame"""
        self.update_gui()
        self.update_changed_rects()
        if len(self.living_enemies) == 0 and len(self.not_spawned_enemies) == 0:
            self.wave_running = False
            self.next_wave()

        # Tohle az bude spawn delay existovat
        # self.spawn_enemy(spawn_delay.spawn_delay(self.not_spawned_enemies[0], self.not_spawned_enemies[1]))
        self.spawn_enemy(10)
        self.enemy_update()
        self.shoot()
        self.update_projectiles()
        self.projectile_hit()

        pg.sprite.groupcollide(self.living_enemies, self.wall_tiles, True, False)


        self.graphics_manager.draw_group(self.tiles, True)
        self.graphics_manager.draw_group(self.towers, True)
        self.graphics_manager.draw_group(self.living_enemies, True)
        self.graphics_manager.draw_group(self.projectiles, True)

    def run(self) -> None:
        """ Main game loop"""

        self.init_modules()
        self.initialize()
        self.show_map()

        self.gui.create_gui(self.lives, self.coins, self.wave, self.graphics_manager.textures)

        # prvni start wavky
        self.next_wave()

        self.frames = 0
        while self.running:
            self.clock.tick(Game.FPS)
            self.handle_input()

            if self.pause:
                continue

            self.frames += 1 #bezi kdzy neni pauza
            self.lives = self.frames
            self.update()
    
    
