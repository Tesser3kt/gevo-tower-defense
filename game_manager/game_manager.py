from pygame.sprite import RenderUpdates

class GameManager:
    def __init__(self) -> None:
        self.objects = RenderUpdates()

        self.projectiles = RenderUpdates()
        self.towers = RenderUpdates()
        self.enemies = RenderUpdates()


        self.ui = RenderUpdates()

        self.coins = RenderUpdates()
        self.lives = RenderUpdates()
        self.level = RenderUpdates()
        self.effects = RenderUpdates()
        self.heath = RenderUpdates()


