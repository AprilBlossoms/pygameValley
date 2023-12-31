import pygame
from game import config
from game.support import Tilesheet


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=config.FARM_LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * .6, -self.rect.height * .75)


class Water(Generic):
    def __init__(self, pos, frames, groups):
        self.frames = frames
        self.frame_index = 0
        super().__init__(pos, self.frames[self.frame_index], groups, config.FARM_LAYERS['ground'])

    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class Tree(Generic):
    def __init__(self, pos, surf, groups, name, player_add):
        super().__init__(pos, surf, groups, z=config.FARM_LAYERS['house top'])
        self.name = name
        self.player_add = player_add
        self.alive = True
        self.inv_tiles = Tilesheet("assets/pause/items.png", 16, 16, 12, 10)
        if self.name == 'Small':
            self.health = 4
            stump_path = "assets/stumps/small.png"
        if self.name == 'Medium':
            self.health = 6
            stump_path = "assets/stumps/medium.png"
        if self.name == 'Large':
            self.health = 8
            stump_path = "assets/stumps/large.png"

        self.stump_surf = pygame.image.load(stump_path).convert_alpha()

    def damage(self):
        self.health -= 1

    def check_death(self):
        if self.health <= 0:
            self.image = self.stump_surf
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.hitbox = self.rect.copy().inflate((-10, -self.rect.height * 0.6))
            self.alive = False
            if self.name == 'Small':
                self.player_add('materials', 'wood', pygame.transform.scale(self.inv_tiles.get_tile(0, 7), (48, 48)), 2)
            if self.name == 'Medium':
                self.player_add('materials', 'wood', pygame.transform.scale(self.inv_tiles.get_tile(0, 7), (48, 48)), 3)
            if self.name == 'Large':
                self.player_add('materials', 'wood', pygame.transform.scale(self.inv_tiles.get_tile(0, 7), (48, 48)), 4)

    def update(self, dt):
        if self.alive:
            self.check_death()


class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        self.surface_rect = surf.get_rect(center=pos)
        super().__init__(pos, surf, groups)
        self.pos = pos
        self.name = name


class Farmable(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = -1
        self.tilled = False
        self.watered = False
        self.plant = False


class Stump(Generic):
    def __init__(self, pos, surf, groups, name, player_add):
        super().__init__(pos, surf, groups, z=config.FARM_LAYERS['house top'])
        self.name = name
        self.player_add = player_add
        self.alive = True
        self.health = 8
        self.inv_tiles = Tilesheet("assets/pause/items.png", 16, 16, 12, 10)

    def damage(self):
        self.health -= 1

    def check_death(self):
        if self.health <= 0:
            self.alive = False
            self.kill()
            self.player_add('materials', 'wood', pygame.transform.scale(self.inv_tiles.get_tile(0, 7), (48, 48)), 5)

    def update(self, dt):
        if self.alive:
            self.check_death()