from game_object import GameObject
from pygame.sprite import Sprite

class ActiveObjects(GameObject):
    """ Class for objects that move """

    def __init__(
        self, x: int, y: int, width:int, height:int, sprite: Sprite, speed:int, direction:tuple
        ) -> None:
        super().__init__(x,y,width,height,sprite)
        self.speed=speed
        self.direction=direction
    
    def move(self):
        """ Moves the object by its speed in its direction """
        
        self.x+=self.direction[0]*self.speed
        self.y+=self.direction[1]*self.speed
