from game_object import GameObject
from pygame.sprite import Sprite

class MobileObject(GameObject):
    """ Class for objects that move """

    def __init__(
        self, x: int, y: int, width:int, height:int, image: Sprite, speed:int, direction:tuple[int]
        ) -> None:
        super().__init__(x,y,width,height,image)
        self.speed=speed
        self.direction=direction
    
    def update(self)->None:
        """update"""
        GameObject.update(self)
        self.move()
    
    def move(self):
        """ Moves the object by its speed in its direction """

        self.rect=self.rect.move(self.direction[0]*self.speed, self.direction[1]*self.speed)

