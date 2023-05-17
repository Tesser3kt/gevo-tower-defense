from PIL import Image
from config.settings.general_config import Colors
from config.settings.general_config import Tile
NUMBER_OF_WALLS  = 5
from random import randint

def load_image(lvl):
    img = Image.open(f"assets/level_maps/level_{lvl}.png")
    return img
    
def draw_point(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Colors.WALLS)

def save_image(img: Image, lvl: int):
    img.save(f"assets/level_maps/level_{lvl}.png")

def generate_walls(img: Image, lvl: int):
    for wall in range(NUMBER_OF_WALLS):
        x = randint(0, Tile.WIDTH)
        y = randint(0, Tile.HEIGHT)
        draw_point(x, y, img)