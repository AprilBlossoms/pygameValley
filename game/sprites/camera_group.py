import pygame

from game import config


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.offset_x_max = 1125
        self.offset_x_min = 0
        self.offset_y_max = 1680
        self.offset_y_min = 0
        l = 200
        t = 100
        w = self.display_surface.get_size()[0] - 400
        h = self.display_surface.get_size()[1] - 200
        self.camera_rect = pygame.Rect(l, t, w, h)

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - config.SCREEN_WIDTH/2
        self.offset.y = player.rect.centery - config.SCREEN_HEIGHT/2
        if self.offset.x > self.offset_x_max:
            self.offset.x = self.offset_x_max
        if self.offset.x < self.offset_x_min:
            self.offset.x = self.offset_x_min
        if self.offset.y > self.offset_y_max:
            self.offset.y = self.offset_y_max
        if self.offset.y < self.offset_y_min:
            self.offset.y = self.offset_y_min

        for layer in config.FARM_LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)