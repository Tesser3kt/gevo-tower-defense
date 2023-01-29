"""Avek sa kan dan la man"""

from enum import Enum
import random
from PIL import Image
from level_generator_config import *
from config import *


class Direction(Enum):
    """Class that contains Direction vectors"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def first_direction(start_point:tuple[int]) -> Direction:
    """Return start direction on base of start point"""
    x, y = start_point
    if x == 0:
        return Direction.RIGHT
    elif x == Tile.WIDTH-1:
        return Direction.LEFT
    elif y == 0:
        return Direction.DOWN
    else:
        return Direction.UP

def init_probs(probability:dict, first_direction:Direction) -> None:
    """Change all probabilities to zero and than change the starting direction probability to 100 %"""
    for direction in Direction:
        probability[direction.value] = 0

    probability[first_direction.value] = Config_lvl_gen.MAX_PROB

def update_probs(probability:dict, last_direction:Direction) -> None:
    """Update the probability after going in the same direction"""

    #Sníží probabilitu o 1 prob. decrease
    probability[last_direction.value] -= Config_lvl_gen.PROB_DECREASE

    #Přidá probability do 2 zbývajících směrů (směry kolmé na předchozí)
    x, y = last_direction.value
    probability[(y, x)] += Config_lvl_gen.PROB_DECREASE // 2
    probability[(-y, -x)] += Config_lvl_gen.PROB_DECREASE // 2

def draw_point(x:int, y:int, img:Image)->None:
    """Create 1 point on a specific pixel on the image"""
    img.putpixel((x, y), Config_lvl_gen.PATH_COLOR)

def my_random_direction(probability:dict) -> Direction:
    """Return a random direction based on probabilities"""
    vectors_probability = []
    for i in range(probability[Direction.UP.value]):
        vectors_probability.append(Direction.UP)
    for i in range(probability[Direction.DOWN.value]):
        vectors_probability.append(Direction.DOWN)
    for i in range(probability[Direction.RIGHT.value]):
        vectors_probability.append(Direction.RIGHT)
    for i in range(probability[Direction.LEFT.value]):
        vectors_probability.append(Direction.LEFT)
    
    return random.choice(vectors_probability)

def move_to(rnd_direction:Direction, x:int, y:int) -> tuple:
    """Change x, y to a new value based on the Direction"""
    x += rnd_direction.value[0]
    y += rnd_direction.value[1]
    return x, y

def go_geradeaus(probability:dict, direction:Direction)->None:
    """Change the probability to max in the direction you want"""
    for direction in Direction:
        probability[direction.value] = 0
    probability[direction.value] = Config_lvl_gen.MAX_PROB

def randomize_probs(probability:dict)->None:
    """Set the probability to the config values"""
    i = 0
    for direction in Direction:
        probability[direction.value] = list(Config_lvl_gen.RANDOM_PROBS.values())[i]
        i += 1
    #print(probability)

probability = {
    Direction.UP.value: 250,
    Direction.DOWN.value: 250,
    Direction.LEFT.value: 250,
    Direction.RIGHT.value: 250
}

img = Image.new('RGB', (Tile.WIDTH, Tile.HEIGHT), color = (0, 0, 0))

#Vytvoří random start na random ose a pak vybere 1 start 
start_osa_1 = 0, random.randint(5, Tile.HEIGHT-5)
start_osa_2 = random.randint(5, Tile.WIDTH-5), 0
start_osa_3 = Tile.WIDTH-1, random.randint(5, Tile.HEIGHT-5)
start_osa_4 = random.randint(5, Tile.WIDTH-5), Tile.HEIGHT-1
#Vybraný start
chosen_start = random.choice([start_osa_1, start_osa_2, start_osa_3, start_osa_4])

# Define the border pixels
border_pixels = set(
    [(x, 0) for x in range(Tile.WIDTH)] + 
    [(x, Tile.HEIGHT-1) for x in range(Tile.WIDTH)] + 
    [(0, y) for y in range(1, Tile.HEIGHT-1)] + 
    [(Tile.WIDTH-1, y) for y in range(1, Tile.HEIGHT-1)]
)

#Start direction
first_direction = first_direction(chosen_start)

#Initialize probabilities
init_probs(probability, first_direction)

x, y = chosen_start
#Nakreslí start
draw_point(*chosen_start, img)

#Posunese o pixel dál
x, y = x+first_direction.value[0], y+first_direction.value[1]
draw_point(x, y, img)
last_direction = first_direction

counter = 0 #Počet kroků rovně
while (x, y) not in border_pixels:
    direction = my_random_direction(probability)
    #Pokud je v obraze a kroků je méně, než chci, tak jdi rovně
    while last_direction == direction and counter < Config_lvl_gen.MIN_STRAIGHT_LINE and ((x, y) not in border_pixels):
        x, y = move_to(direction, x, y)
        draw_point(x, y, img)
        counter += 1
    #Else půjde podle probability
    if counter >= Config_lvl_gen.MIN_STRAIGHT_LINE:
        randomize_probs(probability)
        direction = my_random_direction(probability)
        x, y = move_to(direction, x, y)
        draw_point(x, y, img)
        update_probs(probability, last_direction)
        counter = 0

    last_direction = direction

# Save the image
img.save("level_generator.png")