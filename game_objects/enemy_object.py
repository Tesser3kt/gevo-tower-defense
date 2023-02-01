from active_object import ActiveObject
from mobile_object import MobileObject

from pygame.sprite import Sprite
from pygame.surface import Surface


class EnemyObejct(ActiveObject,MobileObject):
    def __init__(self, hp:int, 
    x: int, y: int, width:int, height:int, image: Sprite, 
    speed:int, direction:tuple[int],
    animation:list[Surface], animation_index:int = 0,
    detectable:bool=True,
    ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index)
        MobileObject.__init__(x,y,width,height,image,speed,direction)

        self.hp=hp
        self.detectable=detectable

    def update(self)->None:
        ActiveObject.update(self)
        MobileObject.update(self)