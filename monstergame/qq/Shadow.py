import pygame
from monstergame.qq.qq import SPRITE_CACHE

class Shadow(pygame.sprite.Sprite):
    """Sprite for shadows."""

    def __init__(self, owner):
        pygame.sprite.Sprite.__init__(self)
        self.image = SPRITE_CACHE["shadow.png"][0][0]
        self.image.set_alpha(64)
        self.rect = self.image.get_rect()
        self.owner = owner

    def update(self, *args):
        """Make the shadow follow its owner."""

        self.rect.midbottom = self.owner.rect.midbottom