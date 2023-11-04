import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self, game_manager, groups):
        self.game_manager = game_manager
        self.groups = groups
        self.image = pygame.transform.scale(pygame.image.load("assets/cursors/game_cursor.png"), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()