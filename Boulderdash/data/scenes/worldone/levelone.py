import pygame
from data.boulder import Boulder
from data.player import Player
from data.portal import Portal
from lib.background import Background
from lib.clutter import Clutter
from lib.scene import Scene
from lib.tile import Tile

class LevelOne(Scene):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.player = None
        self.boulder = None
        self.bg = None
        self.portal = None
        self.clutterInit = False

    def loop(self):
        if self.bg is None:
            self.initBg()
        if self.player is None:
            self.player = Player(self.core)
            self.add(self.player)
        if self.boulder is None:
            self.boulder = Boulder(self.core)
            self.add(self.boulder)
            self.boulder.y = 300
        if self.portal is None:
            self.portal = Portal(self.core, (3450, 450))
            self.add(self.portal)
        if not self.clutterInit:
            self.initClutter()

        if self.player.x >= 300:
            self.boulder.started = True

        super().loop()

    def initClutter(self):
        self.add(Clutter(self.core, (400, 245), "data/assets/objects/Tree_2.png"))
        self.add(Clutter(self.core, (1450, 400), "data/assets/objects/Tree_1.png"))
        self.add(Clutter(self.core, (1750, 355), "data/assets/objects/Mushroom_1.png"))
        self.add(Clutter(self.core, (2100, 270), "data/assets/objects/Tree_3.png"))
        self.add(Clutter(self.core, (2100, 270), "data/assets/objects/Tree_3.png"))
        self.add(Clutter(self.core, (3300, 500), "data/assets/objects/Bush (1).png"))
        self.clutterInit = True

    def reset(self):
        self.objects = []
        self.player = None
        self.boulder = None
        self.bg = None
        self.portal = None
        self.clutterInit = False

    def initBg(self):
        self.bg = Background(self.core, "data/assets/background/BG.png")
        self.add(self.bg)
        floorstartimg = pygame.image.load("data/assets/tiles/1.png")
        floorimg = pygame.image.load("data/assets/tiles/2.png")
        floorendimg = pygame.image.load("data/assets/tiles/3.png")
        waterimg = pygame.image.load("data/assets/tiles/17.png")
        floatstartimg = pygame.image.load("data/assets/tiles/13.png")
        floatendimg = pygame.image.load("data/assets/tiles/15.png")
        tilew, tileh = 100, 100
        tiley = (self.core.screen.get_height() / 1.2) - tileh
        tiles = []
        
        tiles.append(Tile(self.core, floorstartimg, (0 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorimg, (1 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorimg, (2 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (3 * tilew, tiley, tilew, tileh), isfloor=False))
        for x in range(4, 10):
            if x == 9:
                tiles.append(Tile(self.core, floorendimg, (x * tilew, tiley, tilew, tileh)))
                continue
            tiles.append(Tile(self.core, floorimg, (x * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floatstartimg, ((11 * tilew), tiley - 50, tilew, tileh)))
        tiles.append(Tile(self.core, floatendimg, ((12 * tilew), tiley - 50, tilew, tileh)))
        tiles.append(Tile(self.core, floatstartimg, ((14 * tilew), tiley - 100, tilew, tileh)))
        tiles.append(Tile(self.core, floatendimg, ((15 * tilew), tiley - 100, tilew, tileh)))
        tiles.append(Tile(self.core, floatstartimg, ((17 * tilew), tiley - 150, tilew, tileh)))
        tiles.append(Tile(self.core, floatendimg, ((18 * tilew), tiley - 150, tilew, tileh)))
        for x in range(20, 24):
            if x == 20:
                tiles.append(Tile(self.core, floorstartimg, (x * tilew, tiley, tilew, tileh)))
            elif x == 23:
                tiles.append(Tile(self.core, floorendimg, (x * tilew, tiley, tilew, tileh)))
            else:
                tiles.append(Tile(self.core, floorimg, (x * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorstartimg, (25 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (26 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorimg, (27 * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, waterimg, (28 * tilew, tiley, tilew, tileh), isfloor=False))
        tiles.append(Tile(self.core, floorimg, (29 * tilew, tiley, tilew, tileh)))
        for x in range(30, 34):
            if x == 33:
                tiles.append(Tile(self.core, floorendimg, (x * tilew, tiley, tilew, tileh)))
            tiles.append(Tile(self.core, floorimg, (x * tilew, tiley, tilew, tileh)))
        tiles.append(Tile(self.core, floorendimg, (34 * tilew, tiley, tilew, tileh)))
        
        for tile in tiles:
            self.add(tile)        
