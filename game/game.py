import pygame

from game.overlay.overlay import Overlay


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
