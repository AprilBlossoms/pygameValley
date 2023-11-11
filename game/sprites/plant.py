import pygame

from game import config
from game.support import Tilesheet


class Plant(pygame.sprite.Sprite):
    def __init__(self, plant_type, groups, soil):
        super().__init__(groups)
        self.plant_type = plant_type
        self.soil = soil
        self.watered = False
        self.crops = Tilesheet("assets/items/crops.png", 16, 16, 37, 6)
        self.crop_images = Tilesheet("assets/pause/items.png", 16, 16, 9, 10)
        self.harvest_amount = 1

        if self.plant_type == 'carrot':
            self.frames = [
                pygame.transform.scale(self.crops.get_tile(0, 0), (32, 32)),
                pygame.transform.scale(self.crops.get_tile(1, 0), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(2, 0), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(3, 0), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(4, 0), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(5, 0), (48, 48)),
            ]
            self.harvest_img = pygame.transform.scale(self.crop_images.get_tile(0, 0), (48, 48))

        if self.plant_type == 'strawberry':
            self.harvest_amount = 2
            self.harvest_img = pygame.transform.scale(self.crop_images.get_tile(2, 0), (48, 48))
            self.frames = [
                pygame.transform.scale(self.crops.get_tile(0, 2), (32, 32)),
                pygame.transform.scale(self.crops.get_tile(1, 2), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(2, 2), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(3, 2), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(4, 2), (48, 48)),
                pygame.transform.scale(self.crops.get_tile(5, 2), (48, 48)),
            ]

        self.age = 0
        self.max_age = len(self.frames) - 1
        self.grow_speed = config.GROW_SPEED[plant_type]
        self.harvestable = False

        self.image = self.frames[self.age]
        self.y_offset = -8
        self.rect = self.image.get_rect(midbottom=soil.rect.midbottom + pygame.math.Vector2(0, self.y_offset))
        self.z = config.FARM_LAYERS['ground plant']

    def grow(self):
        if self.watered:
            self.age += self.grow_speed
            if int(self.age) > 1:
                self.z = config.FARM_LAYERS['main']
                self.hitbox = self.rect.copy().inflate(-26, -self.rect.height * 0.8)
            if self.age > self.max_age:
                self.age = self.max_age
                self.harvestable = True
            self.image = self.frames[int(self.age)]
            self.rect = self.image.get_rect(midbottom=self.soil.rect.midbottom + pygame.math.Vector2(0, self.y_offset))