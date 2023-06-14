from ai.ai import AI
from level_converter.level_converter import convert_level,create_rect
import pygame as pg

lvl = convert_level(2)
lvl["end"].append(create_rect((960,704)))
ai = AI(lvl,[])
ai.find_paths(lvl["start"])
print(ai.available_paths)