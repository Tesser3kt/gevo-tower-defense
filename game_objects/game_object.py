from pygame import Surface, Rect


class GameObject(Surface):
    """ The most general of the clases """
    
    def __init__(
        self, x:int, y:int, width:int, height:int, image:Surface
        ) -> None:

        self.rect=Rect(x,y,width,height)
        self.image=image

    def update(self)->None:    
        """update"""

