from random import randint

import pygame

from game.overlay.overlay import Overlay
from game.states.farmhouse import Farmhouse
from game.states.pause.inventory_item import InventoryItem


class Game:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.raining = randint(0, 10) > 3

    def game_loop(self):
        self.game_manager.dt = self.game_manager.clock.tick() / 1000
        self.game_manager.check_events()
        self.game_manager.render()
        self.game_manager.update()
        self.game_manager.game_cursor.update()
        self.overlay = Overlay(self.player)
        self.overlay.display(self.game_manager.screen)

    def player_add(self, type, item, img, amount):
        already_added = False
        for i in range(1, 28):
            if self.player.inventory.slots['inventory'][str(i)]['item']:
                if self.player.inventory.slots['inventory'][str(i)]['item'].name == item and self.player.inventory.slots['inventory'][str(i)]['item'].item_type == type:
                    self.player.inventory.slots['inventory'][str(i)]['amount'] += amount
                    already_added = True
        for i in range(1, 10):
            if self.player.inventory.slots['hotbar'][str(i)]['item']:
                if self.player.inventory.slots['hotbar'][str(i)]['item'].name == item and self.player.inventory.slots['hotbar'][str(i)]['item'].item_type == type:
                    self.player.inventory.slots['hotbar'][str(i)]['amount'] += amount
        if not already_added:
            self.player.inventory.add(InventoryItem(item, type, img), amount)


    def zone(self, zone):
        if zone == 'Farmhouse':
            self.game_manager.farmhouse = Farmhouse(self.game_manager, "Farmhouse", self.player.inventory)
            self.game_manager.farmhouse.enter_state()
        if zone == "Farm":
            self.game_manager.farmhouse.exit_state()

