import pygame

from game import config

class Menu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.mid_w, self.mid_h = config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)

    def draw_cursor(self):
        self.game_manager.draw_text(self.game_manager.screen, "*", 60, config.WHITE, self.cursor_rect.x, self.cursor_rect.y)