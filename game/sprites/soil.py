from random import choice
import pygame
from game import config
from game.sprites.plant import Plant
from game.support import import_folder


class SoilLayer:
    def __init__(self, all_sprites, collision_sprites, farmable_sprites):
        self.all_sprites = all_sprites
        self.collision_sprites = collision_sprites
        self.farmable_sprites = farmable_sprites
        self.soil_sprites = pygame.sprite.Group()
        self.water_sprites = pygame.sprite.Group()
        self.water_surfs = import_folder("assets/soil/soil_water")
        self.plant_sprites = pygame.sprite.Group()
        self.soil_surf = pygame.transform.scale(pygame.image.load("assets/soil/soil.png"), (48, 48))

    def till_soil(self, target_pos):
        for sprite in self.farmable_sprites.sprites():
            if sprite.rect.collidepoint(target_pos):
                if not sprite.tilled:
                    SoilTile((sprite.rect.x, sprite.rect.y), self.soil_surf, [self.all_sprites, self.soil_sprites])
                    sprite.tilled = True

    def water_soil(self, target_pos):
        for sprite in self.farmable_sprites.sprites():
            if sprite.rect.collidepoint(target_pos):
                if sprite.tilled:
                    if not sprite.watered:
                        surf = pygame.transform.scale(choice(self.water_surfs), (48, 48))
                        WaterTile(sprite.rect.topleft, surf, [self.all_sprites, self.water_sprites])
                        sprite.watered = True
        for sprite in self.plant_sprites.sprites():
            if sprite.rect.collidepoint(target_pos):
                sprite.watered = True

    def water_all(self):
        for sprite in self.farmable_sprites.sprites():
            if not sprite.watered and sprite.tilled:
                surf = pygame.transform.scale(choice(self.water_surfs), (48, 48))
                WaterTile(sprite.rect.topleft, surf, [self.all_sprites, self.water_sprites])
                sprite.watered = True
        for sprite in self.plant_sprites.sprites():
            sprite.watered = True

    def remove_water(self):
        for sprite in self.farmable_sprites.sprites():
            if sprite.watered:
                sprite.watered = False
        for sprite in self.plant_sprites.sprites():
            sprite.watered = False
        for sprite in self.water_sprites.sprites():
            sprite.kill()

    def plant_seed(self, target_pos, seed):
        for sprite in self.farmable_sprites.sprites():
            if sprite.rect.collidepoint(target_pos):
                if sprite.tilled:
                    if not sprite.plant:
                        plant = Plant(seed, [self.all_sprites, self.plant_sprites, self.collision_sprites], sprite)
                        sprite.plant = plant
                        if sprite.watered:
                            plant.watered = True
                        return True
        return False

    def update_plants(self):
        for plant in self.plant_sprites.sprites():
            plant.grow()
class SoilTile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = config.FARM_LAYERS['soil']


class WaterTile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = config.FARM_LAYERS['soil water']