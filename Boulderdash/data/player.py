import pygame
from lib.animation import Animation
from lib.background import Background
from lib.collider import Collider
from lib.constants import g
from lib.tile import Tile

class Player:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.w = 64
        self.h = 64
        self.speed = 3
        self.maxspeed = 3
        self.moving = False
        self.jumping = False
        self.jumpforce = 10
        self.jumpstart = 0
        self. jumpheight = 100
        self.falling = False
        self.collider = Collider(self, debug=False)
        self.facingleft = False
        self.initSprites()
        self.currentanim = self.idleAnim

    def loop(self):
        if self.y >= self.core.screen.get_height():
            self.core.scene.reset()
        
        self.checkfalling()
        self.checkmoving()
        self.checkjumping()

        self.w = self.currentanim.sprites[self.currentanim.currentframe].get_width()
        self.h = self.currentanim.sprites[self.currentanim.currentframe].get_height()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        
        if self.jumping or self.falling:
            self.currentanim = self.fallLeftAnim if self.facingleft else self.fallRightAnim
        self.currentanim.play()

    def checkmoving(self):
        keys = pygame.key.get_pressed()
        self.moving = False
        if keys[pygame.K_a]:
            self.facingleft = True
            self.currentanim = self.runLeftAnim
            self.moving = True
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.facingleft = False
            self.currentanim = self.runRightAnim
            self.moving = True
            self.x += self.speed
        if not self.moving and not self.jumping:
            self.currentanim = self.idleAnim

    def checkjumping(self):
        for event in self.core.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.onplatform():
                    self.jumping = True
                    self.jumpstart = self.y
        if self.jumping:
            self.y -= self.jumpforce
            if self.y <= self.jumpstart - self.jumpheight:
                self.jumping = False
                self.falling = True

    def checkfalling(self):
        if self.onplatform():
            self.falling = False
            self.jumping = False
        else:
            self.falling = True
            self.y += g

    def onplatform(self):
        for obj in self.core.scene.objects:
            if obj == self: continue
            if isinstance(obj, Tile):
                if self.collider.colliding(obj) and obj.isfloor:
                    if self.collider.rect.bottom <= obj.collider.rect.top + (g * 2): # the + (g * 2) is to avoid player bottom < tile top on collision
                        return True
                    return False
        return False

    def initSprites(self):
        spritesheet = pygame.image.load("data/assets/characters/player.png")
        idlesprites = [
            spritesheet.subsurface(15, 10, 40, 55),
            spritesheet.subsurface(15, 573, 40, 55)
        ]
        runsprites = [
            spritesheet.subsurface(15, 10, 40, 55),
            spritesheet.subsurface(86, 10, 40, 55),
            spritesheet.subsurface(156, 10, 40, 55),
            spritesheet.subsurface(226, 10, 40, 55),
            spritesheet.subsurface(296, 10, 40, 55),
            spritesheet.subsurface(366, 10, 40, 55),
            spritesheet.subsurface(436, 10, 40, 55),
            spritesheet.subsurface(507, 10, 40, 55),
            spritesheet.subsurface(578, 10, 40, 55)
        ]
        jumpsprites = [
            spritesheet.subsurface(2, 219, 50, 60),
            spritesheet.subsurface(72, 219, 50, 60),
            spritesheet.subsurface(148, 219, 50, 60),
            spritesheet.subsurface(212, 219, 50, 60),
            spritesheet.subsurface(295, 219, 50, 60),
            spritesheet.subsurface(368, 219, 50, 60),
            spritesheet.subsurface(437, 219, 50, 60),
            spritesheet.subsurface(500, 219, 50, 60),
            spritesheet.subsurface(573, 219, 50, 66)
        ]
        self.idleAnim = Animation(self.core, idlesprites, self, delay=10)
        self.runLeftAnim = Animation(self.core, runsprites, self, flipx=True)
        self.runRightAnim = Animation(self.core, runsprites, self)
        self.fallRightAnim = Animation(self.core, jumpsprites, self)
        self.fallLeftAnim = Animation(self.core, jumpsprites, self, flipx=True)
