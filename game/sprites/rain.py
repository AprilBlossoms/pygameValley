from random import randint, choice

import pygame

from game import config
from game.sprites.sprites import Generic
from game.support import import_folder


class Rain:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.rain_drops = import_folder("assets/rain/drops")
        self.rain_floor = import_folder("assets/rain/floor")
        self.floor_w, self.floor_h = 46 * 48, 36 * 38

    def create_floor(self):
        Drop(surf=choice(self.rain_floor), pos=(randint(0, self.floor_w), randint(0, self.floor_h)), moving=False, groups=self.all_sprites, z=config.FARM_LAYERS['rain floor'])

    def create_drops(self):
        Drop(surf=choice(self.rain_drops), pos=(randint(0, self.floor_w), randint(0, self.floor_h)), moving=True, groups=self.all_sprites, z=config.FARM_LAYERS['rain drops'])

    def update(self):
        self.create_floor()
        self.create_drops()

class Drop(Generic):
    def __init__(self, surf, pos, moving, groups, z):
        super().__init__(pos, surf, groups, z)
        self.lifetime = randint(400, 500)
        self.start_time = pygame.time.get_ticks()
        self.surf = surf
        self.moving = moving
        if self.moving:
            self.pos = pygame.math.Vector2(self.rect.topleft)
            self.direction = pygame.math.Vector2(-2, 4)
            self.speed = randint(200, 250)

    def update(self, dt):
        if self.moving:
            self.pos += self.direction * self.speed * dt
            self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()