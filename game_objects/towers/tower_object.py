from active_object import ActiveObject
from immobile_object import ImmobileObject

from pygame.surface import Surface


class TowerObject(ActiveObject,ImmobileObject):
    """ Most general class for tower objects """

    def __init__(self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_speed:int, projectile_type:object, animation_index: int = 0, lvl:int=1,
     ) -> None:
        ActiveObject.__init__(x,y,width,height,image,animation,animation_index,lvl)
        ImmobileObject.__init__(x,y,width,height,height,image)

        self.damage=damage
        self.reload_speed=reload_speed
        self.projectile_type=projectile_type

    def update(self):
        ActiveObject.update(self)
        ImmobileObject.update(self)
    
    def find_nearest_enemy(self)->tuple[int]:
        """ Claculates where the neares enemy is and turns the direction """
        
        pass

    def turn_to_enemy(self)->list[Surface]:
        """ Changes the animation of object to be turned the right way """
        pass

    def fire(self):
        """ Fires the coresponding projectile type to the neares enemy """

        pass