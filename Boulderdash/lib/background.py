import pygame
from data.boulder import Boulder
from data.crate import Crate
from data.portal import Portal
from lib.clutter import Clutter
from lib.tile import Tile

class Background:

    def __init__(self, core, image):
        self.core = core
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (1366, 768))
        self.x = 0
        self.y = 0

    def loop(self):
        player = self.core.scene.player
        delta = 0
        if player.x >= (self.core.screen.get_width() / 2) and player.moving:
            player.speed = 0
            if not player.facingleft:
                delta = player.maxspeed * -1
            self.x += delta
            self.movestuff(delta)
            if self.x <= self.core.screen.get_width() * -1:
                self.x = 0
        else:
            player.speed = player.maxspeed
        self.core.screen.blit(self.image, (self.x, self.y))
        self.core.screen.blit(self.image, (self.x + self.image.get_width(), self.y))

    def movestuff(self, delta):
        for obj in self.core.scene.objects:
            if isinstance(obj, Crate) or \
                isinstance(obj, Portal) or \
                isinstance(obj, Clutter) or \
                isinstance(obj, Tile) or \
                isinstance(obj, Boulder):
                obj.x += delta