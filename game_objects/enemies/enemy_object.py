from active_object import ActiveObject
from mobile_object import MobileObject

from pygame.surface import Surface


class EnemyObejct(ActiveObject,MobileObject):
    """ Most general class for enemy objects """

    def __init__(self, hp:int, 
    x: int, y: int, width:int, height:int, image: Surface, 
    speed:int, direction:tuple[int],
    animation:list[Surface], animation_index:int = 0,
    detectable:bool=True,lvl:int=1
    ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index,lvl)
        MobileObject.__init__(x,y,width,height,image,speed,direction)

        self.hp=hp
        self.detectable=detectable

    def update(self)->None:
        ActiveObject.update(self)
        MobileObject.update(self)
