import pygame

class InventoryItem:
    def __init__(self, name, item_type, img):
        self.name = name
        self.item_type = item_type
        self.img = pygame.image.load(img)