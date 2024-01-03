import pygame
from data.crate import Crate
from lib.animation import Animation
from lib.clutter import Clutter
from lib.collider import Collider
from lib.tile import Tile

class Boulder:

    def __init__(self, core):
        self.core = core
        self.started = False
        self.x = -600
        self.y = 0
        self.w = 443
        self.h = 443
        self.speed = 3
        self.initSprites()
        self.collider = Collider(self, debug=False)

    def loop(self):
        if self.started:
            if self.x >= self.core.screen.get_width() / 2:
                self.speed = 0
            self.x += self.speed
            self.collider.updaterect(self.x, self.y, self.w, self.h)
            self.checkcolliding()
            self.anim.play()

    def initSprites(self):
        boulderimg = pygame.image.load("data/assets/objects/boulder.png")
        scaled = pygame.transform.scale(boulderimg, (self.w, self.h))
        sprites = []
        sprites.append(pygame.transform.rotate(scaled, 315))
        sprites.append(pygame.transform.rotate(scaled, 225))
        sprites.append(pygame.transform.rotate(scaled, 135))
        sprites.append(pygame.transform.rotate(scaled, 45))
        self.anim = Animation(self.core, sprites, self, delay=5)

    def checkcolliding(self):
        for obj in self.core.scene.objects:
            if isinstance(obj, Tile) or \
                isinstance(obj, Crate) or \
                isinstance(obj, Clutter):
                if self.collider.colliding(obj):
                    self.core.scene.remove(obj)
        if self.collider.colliding(self.core.scene.player):
            self.core.scene.reset()

    def reset(self):
        self.x = -500
        self.started = False
