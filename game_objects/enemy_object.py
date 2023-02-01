from active_object import ActiveObject
from mobile_object import MobileObject

from pygame.sprite import Sprite
from pygame.surface import Surface


class Enemy_obejct(ActiveObject,MobileObject):
    def __init__(self, hp:int,
    x: int, y: int, width:int, height:int, image: Sprite, 
    speed:int, direction:tuple[int],
    animation:list[Surface], animation_index:int = 0,
    ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index)
        MobileObject.__init__(x,y,width,height,image,speed,direction)

        self.hp=hp
    def update(self)->None:
        ActiveObject.update(self)
        MobileObject.update(self)
    
    def find_path(self)->None:
        #from current position and paths avalible determine
        #in which direction should the enemy go
        #change the direction in the object so the function returns None
        pass