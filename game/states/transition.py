import pygame

from game import config
from game.states.menu import Menu
from game.states.state import State


class Transition(State, Menu):
    def __init__(self, game_manager, name):
        State.__init__(self, game_manager, name)
        Menu.__init__(self, game_manager)
        self.image = pygame.transform.scale(pygame.image.load("assets/transition/transition.png"), (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.detailsx, self.detailsy = self.mid_w, self.mid_h + 130
        self.okx, self.oky = self.mid_w, self.mid_h + 180
        self.cursor_rect.midtop = (self.detailsx - 45, self.detailsy)
        self.menu_options = {0: self.mid_h + 130, 1: self.mid_h + 185}
        self.index = 0

    def update(self, dt, actions):
        self.move_cursor(actions)
        if actions['enter']:
            if self.index == 0:
                pass
            elif self.index == 1:
                self.exit_state()
        self.game_manager.reset_keys()

    def move_cursor(self, actions):
        if actions['down']:
            self.index += 1
            if self.index == 2:
                self.index = 0
        if actions['up']:
            self.index -= 1
            if self.index < 0:
                self.index = 1
        self.cursor_rect.y = self.menu_options[self.index]

    def render(self, surface):
        surface.blit(self.image, self.rect)
        self.game_manager.draw_text(surface, "Details", 40, config.PINK, self.detailsx, self.detailsy)
        self.game_manager.draw_text(surface, "Okay", 40, config.PINK, self.okx, self.oky)
        self.draw_cursor()
