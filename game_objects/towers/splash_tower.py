from pygame.surface import Surface
from game_objects.towers.tower_type import TowerType
from game_objects.towers.tower_object import TowerObject

class SplashTower(TowerObject):
    """ Class for splash tower objects """

    def __init__(self, x: int, y: int, width: int, height: int, image: Surface,
     animation: list[Surface],damage:int,reload_time:int,
     tower_type:TowerType, animation_index: int = 0, lvl:int=1,
     splash_animation:list[Surface]=[]
    )->None:

        TowerObject.__init__(self,x,y,width,height,image,animation,damage,reload_time,
    tower_type,animation_index,lvl)
        self.splash_animation=splash_animation

    def update(self):
        TowerObject.update(self)

    def fire(self)->object:
        pass
        #return new splash projectile with same x,y like the tower and animation from the splash animation
