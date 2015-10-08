from monstergame.qq.Sprite import Sprite
from monstergame.qq.qq import SPRITE_CACHE, DX, DY

__author__ = 'cbayley'


class Player(Sprite):
    """ Display and animate the player character."""

    is_player = True

    def __init__(self, pos=(1, 1)):
        self.frames = SPRITE_CACHE["player.png"]
        Sprite.__init__(self, pos)
        self.direction = 2
        self.animation = None
        self.image = self.frames[self.direction][0]

    def walk_animation(self):
        """Animation for the player walking."""

        # This animation is hardcoded for 4 frames and 16x24 map tiles
        for frame in range(4):
            self.image = self.frames[self.direction][frame]
            yield None
            self.move(3*DX[self.direction], 2*DY[self.direction])
            yield None
            self.move(3*DX[self.direction], 2*DY[self.direction])

    def update(self, *args):
        """Run the current animation or just stand there if no animation set."""

        if self.animation is None:
            self.image = self.frames[self.direction][0]
        else:
            try:
                self.animation.next()
            except StopIteration:
                self.animation = None