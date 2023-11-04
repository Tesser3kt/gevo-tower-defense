class Tower:
    def __init__(self, x, y, range, damage):
        self.x = x
        self.y = y
        self.range = range
        self.damage = damage

    def shoot(self, enemies):
        for enemy in enemies:
            distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
            if distance <= self.range:
                enemy.health -= self.damage
                return True
        return False
