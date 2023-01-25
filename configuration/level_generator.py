from enum import Enum
import random
from PIL import Image, ImageDraw
from level_generator_config import *
from config import *
import time

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def first_direction(start_point:tuple[int]) -> Direction:
    """return start direction on base of start point"""
    x, y = start_point
    if x == 0:
        return Direction.RIGHT
    elif x == Window.WIDTH-1:
        return Direction.LEFT
    elif y == 0:
        return Direction.DOWN
    else:
        return Direction.UP

def init_probs(probability:dict, first_direction:Direction) -> None:
    """Initialize starting probability"""
    for direction in Direction:
        probability[direction.value] = 0

    probability[first_direction.value] = Config_lvl_gen.MAX_PROB

def update_probs(probability:dict, last_direction:Direction) -> None:
    probability[last_direction.value] -= Config_lvl_gen.PROB_DECREASE

    x, y = last_direction.value
    probability[(y, x)] += Config_lvl_gen.PROB_DECREASE // 2
    probability[(-y, -x)] += Config_lvl_gen.PROB_DECREASE // 2

def draw_point(x:int, y:int, img:Image)->None:
    img.putpixel((x, y), Config_lvl_gen.PATH_COLOR)

probability = {
    Direction.UP.value: 70,
    Direction.DOWN.value: 20,
    Direction.LEFT.value: 5,
    Direction.RIGHT.value: 5
}

img = Image.new('RGB', (Window.WIDTH, Window.HEIGHT), color = (0, 0, 0))

#Osy startu 
start_osa_1 = 0, random.randint(5, Window.HEIGHT-5)
start_osa_2 = random.randint(5, Window.WIDTH-5), 0
start_osa_3 = Window.WIDTH-1, random.randint(5, Window.HEIGHT-5)
start_osa_4 = random.randint(5, Window.WIDTH-5), Window.HEIGHT-1

chosen_start = random.choice([start_osa_1, start_osa_2, start_osa_3, start_osa_4])

first_direction = first_direction(chosen_start)
init_probs(probability, first_direction)

x, y = chosen_start
draw_point(*chosen_start, img)
x, y = x+first_direction.value[0], y+first_direction[1]


while #nejsem na kraji
