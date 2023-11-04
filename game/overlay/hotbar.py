import pygame

from game import config
from game.states.pause.inventory_item import InventoryItem


class Hotbar:
    def __init__(self, player):
        self.player = player
        self.selector_image = pygame.transform.scale(pygame.image.load("assets/overlay/hotbar_selector.png"), (50, 55))
        self.hotbar_image = pygame.transform.scale(pygame.image.load("assets/overlay/hotbar.png"), (500, 64))

        self.hotbar_rect = self.hotbar_image.get_rect(center=((config.SCREEN_WIDTH/2), config.SCREEN_HEIGHT - 30))

        self.hotbar1 = self.selector_image.get_rect(
            topleft=(self.hotbar_rect.topleft[0] + 11, self.hotbar_rect.topleft[1] + 5))
        self.hotbar2 = self.selector_image.get_rect(
            topleft=(self.hotbar1.topright[0] + 4, self.hotbar1.topright[1]))
        self.hotbar3 = self.selector_image.get_rect(
            topleft=(self.hotbar2.topright[0] + 4, self.hotbar1.topright[1]))
        self.hotbar4 = self.selector_image.get_rect(
            topleft=(self.hotbar3.topright[0] + 3, self.hotbar1.topright[1]))
        self.hotbar5 = self.selector_image.get_rect(
            topleft=(self.hotbar4.topright[0] + 3, self.hotbar1.topright[1]))
        self.hotbar6 = self.selector_image.get_rect(
            topleft=(self.hotbar5.topright[0] + 3, self.hotbar1.topright[1]))
        self.hotbar7 = self.selector_image.get_rect(
            topleft=(self.hotbar6.topright[0] + 3, self.hotbar1.topright[1]))
        self.hotbar8 = self.selector_image.get_rect(
            topleft=(self.hotbar7.topright[0] + 3, self.hotbar1.topright[1]))
        self.hotbar9 = self.selector_image.get_rect(
            topleft=(self.hotbar8.topright[0] + 4, self.hotbar1.topright[1]))

        hoe = InventoryItem("hoe", "tools", "assets/overlay/hoe.png")
        hoe.img = pygame.transform.scale(hoe.img, (42, 42))
        water = InventoryItem("water", "tools", "assets/overlay/water.png")
        water.img = pygame.transform.scale(water.img, (42, 42))
        axe = InventoryItem("axe", "tools", "assets/overlay/axe.png")
        axe.img = pygame.transform.scale(axe.img, (42, 42))
        pickaxe = InventoryItem("pickaxe", "tools", "assets/overlay/pickaxe.png")
        pickaxe.img = pygame.transform.scale(pickaxe.img, (42, 42))

        self.tools = {
            'hoe': hoe,
            'water': water,
            'axe': axe,
            'pickaxe': pickaxe
        }

        self.slots = {
            '1': {'item': self.tools[self.player.selected_tool], 'rect': self.hotbar1},
            '2': {'item': None, 'amount': 0, 'rect': self.hotbar2},
            '3': {'item': None, 'amount': 0, 'rect': self.hotbar3},
            '4': {'item': None, 'amount': 0, 'rect': self.hotbar4},
            '5': {'item': None, 'amount': 0, 'rect': self.hotbar5},
            '6': {'item': None, 'amount': 0, 'rect': self.hotbar6},
            '7': {'item': None, 'amount': 0, 'rect': self.hotbar7},
            '8': {'item': None, 'amount': 0, 'rect': self.hotbar8},
            '9': {'item': None, 'amount': 0, 'rect': self.hotbar9},
        }