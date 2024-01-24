from random import randint

import pygame

from game.overlay.overlay import Overlay
from game.states.farmhouse import Farmhouse
from game.states.pause.inventory_item import InventoryItem


class Game:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.raining = randint(0, 10) > 3
        self.minute_timer = 0
        self.hour = 7
        self.minute = 0
        self.year = 1
        self.seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
        self.season_index = 0
        self.days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.days_full = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.day_index = 0
        self.day = 1
        self.paused = False
        self.overlay = Overlay(self.game_manager.player)

    def game_loop(self):
        self.game_manager.dt = self.game_manager.clock.tick(60) / 1000
        self.update_time(self.game_manager.dt)
        self.game_manager.check_events()
        self.game_manager.render()
        self.game_manager.update()
        self.game_manager.game_cursor.update()
        self.overlay.display(self.game_manager.screen)







