from game_object import GameObject
from pygame.sprite import Sprite

class InactiveObject(GameObject):
    """ Class for objects that dont move """

    def __init__(self, x: int, y: int,  width:int, height:int, image: Sprite) -> None:
        super().__init__(x, y, width, height, image) 
    
    def update(self)->None:
        """update"""
        GameObject.update(self)