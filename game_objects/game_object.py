from pygame import Surface, Rect
from pygame.sprite import Sprite


class GameObject(Sprite):
    """ The most general of the clases """
    
    def __init__(
        self, x:int, y:int, width:int, height:int, image:Surface
        ) -> None:
        Sprite.__init__(self)
        self.rect=Rect(x,y,width,height)
        self.image=image

    def update(self)->None:    
        """update"""

