import pygame

from game.overlay.overlay import Overlay
from game.states.pause.inventory_item import InventoryItem


class Game:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def game_loop(self):
        self.game_manager.dt = self.game_manager.clock.tick() / 1000
        self.game_manager.check_events()
        self.game_manager.render()
        self.game_manager.update()
        self.game_manager.game_cursor.update()
        self.overlay = Overlay(self.player)
        self.overlay.display(self.game_manager.screen)

    def player_add(self, type, item, img, amount):
        if item in self.player.inventory.items[type]:
            self.player.inventory.items[type][item] += amount
            for i in range(1, 28):
                if self.player.inventory.slots['inventory'][str(i)]['item']:
                    if self.player.inventory.slots['inventory'][str(i)]['item'].name == item:
                        self.player.inventory.slots['inventory'][str(i)]['amount'] += amount
        else:
            self.player.inventory.add(InventoryItem(item, type, img), amount)
            self.player.inventory.items[type][item] = amount