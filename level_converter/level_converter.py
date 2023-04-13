from PIL import Image
from config.settings.general_config import Tile, Colors, Window
import pygame as pg

class GameObject(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, rect: pg.Rect):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = rect


def convert_level(level_difficulty):
    """Convert level image into pygame"""

    #Load image
    def load_image(level_difficulty):
        """Load level image"""
        level = Image.open(f'assets/level_maps/level_{level_difficulty}.png')
        return level
    pixels = list(load_image(level_difficulty).getdata())

    #Create sprite
    def create_sprite(position, color)->GameObject:
        """Create a sprite from a color and a position"""
        image = pg.Surface((Tile.PIXEL_SIZE, Tile.PIXEL_SIZE))
        image.fill(color)
        image = image.convert()
        rect = pg.Rect(position[0], position[1], Tile.PIXEL_SIZE, Tile.PIXEL_SIZE)
        square = GameObject(image, rect)
        return square

    walls = pg.sprite.RenderUpdates()
    path = pg.sprite.RenderUpdates()
    free_tile = pg.sprite.RenderUpdates()
    start_end = pg.sprite.RenderUpdates()

    # x, y in pygame
    x = 0
    y = 0
    x_in_image = 0
    for pixel in pixels:
        x_in_image += 1
        if x_in_image > Tile.WIDTH:
            x = 1
            y += Tile.PIXEL_SIZE
            x_in_image = 1 #Musí být 1, jinak to je o 1 pixel posunuté každé y
        else:
            x += Tile.PIXEL_SIZE
        
        if pixel == Colors.WALLS:
            square = create_sprite((x, y), Colors.WALLS)
            walls.add(square)
        elif pixel == Colors.PATH:
            square = create_sprite((x, y), Colors.PATH)
            path.add(square)
        elif pixel == Colors.START:
            square = create_sprite((x, y), Colors.START)
            start_end.add(square)
        elif pixel == Colors.END:
            square = create_sprite((x, y), Colors.END)
            start_end.add(square)
        elif pixel == Colors.BACKGROUND:
            square = create_sprite((x, y), Colors.BACKGROUND)
            free_tile.add(square)
        else:
            print(f"Level converter: Unknown color: {pixel}")



   #    -----------------------------------------------------------------------------
   #    -----------------------------------------------------------------------------
   #    -----------------------------------TESTING-----------------------------------
   #    -----------------------------------------------------------------------------
   #    -----------------------------------------------------------------------------
   #
   #screen = pg.display.set_mode((Window.WIDTH, Window.HEIGHT), pg.SCALED)
   #screen.fill((Colors.BACKGROUND))
   # while True:
   #     for event in pg.event.get():
   #         if event.type == pg.QUIT:
   #             pg.quit()
   #             quit()
   #     
   #     walls.draw(screen)
   #     path.draw(screen)
   #     free_tile.draw(screen)
   #     start_end.draw(screen)
   #     pg.display.update()
