from game_object import GameObject
from pygame.surface import Surface

class ActiveObject(GameObject):
    """ Class for objects that do something on their own """

    def __init__(
        self, x:int, y:int, width:int, height:int, image:Surface, animation:list[Surface], animation_index:int = 0
        ) -> None:

        super().__init__(x,y,width,height,image)
        self.animation=animation
        self.animation_index=animation_index
    
    def update(self)->None:
        """update"""
        GameObject.update(self)
        self.continue_animation()

    def continue_animation(self):
        """ Moves the animation one frame ahead """

        self.animation_index+=1
        self.animation_index %= len(self.animation)
        self.image=self.animation[self.animation_index]

 
          