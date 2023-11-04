import pygame

from game import config
from game.states.menu import Menu
from game.states.state import State

class LoadMenu(State, Menu):
    def __init__(self, game_manager, name):
        State.__init__(self, game_manager, name)
        Menu.__init__(self, game_manager)
        self.choose_image = pygame.transform.scale(
            pygame.image.load("assets/save_load/choose_save.png").convert_alpha(), (298, 196))
        self.save1_image = pygame.image.load("assets/save_load/save_one.png").convert_alpha()
        self.save2_image = pygame.image.load('assets/save_load/save_two.png').convert_alpha()
        self.save3_image = pygame.image.load("assets/save_load/save_three.png").convert_alpha()

        self.choose_x, self.choose_y = self.mid_w, self.mid_h - 150
        self.choose_rect = self.choose_image.get_rect(center=(self.choose_x, self.choose_y))
        self.save1x, self.save1y = self.mid_w - 150, self.mid_h + 100
        self.save1_rect = self.save1_image.get_rect(center=(self.save1x, self.save1y))
        self.save2x, self.save2y = self.mid_w, self.mid_h + 100
        self.save2_rect = self.save2_image.get_rect(center=(self.save2x, self.save2y))
        self.save3x, self.save3y = self.mid_w + 150, self.mid_h + 100
        self.save3_rect = self.save3_image.get_rect(center=(self.save3x, self.save3y))
        self.back_x, self.back_y = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.back_image = pygame.transform.scale(pygame.image.load("assets/save_load/back.png"), (106, 82))
        self.back_rect = self.back_image.get_rect(bottomright=(self.back_x, self.back_y))
        self.cursor_rect.center = (self.save1x, self.save1y)

        self.menu_options = {0: ["Save One", self.save1_rect.x + 80, self.save1_rect.y],
                             1: ["Save Two", self.save2_rect.x + 80, self.save2_rect.y],
                             2: ["Save Three", self.save3_rect.x + 80, self.save3_rect.y],
                             3: ["Back", self.back_rect.x + 57, self.back_rect.y]}
        self.index = 0


    def render(self, surface):
        surface.fill(config.PINK)
        surface.blit(self.choose_image, self.choose_rect)
        self.save1_button = surface.blit(self.save1_image, self.save1_rect)
        self.save2_button = surface.blit(self.save2_image, self.save2_rect)
        self.save3_button = surface.blit(self.save3_image, self.save3_rect)
        self.back_button = surface.blit(self.back_image, self.back_rect)
        self.draw_cursor()

    def move_cursor(self, actions):
        if actions['right']:
            self.index += 1
            if self.index == 4:
                self.index = 0
        if actions['left']:
            self.index -= 1
            if self.index < 0:
                self.index = 3
        self.cursor_rect.center = (self.menu_options[self.index][1], self.menu_options[self.index][2])

    def update(self, delta_time, actions):
        self.move_cursor(actions)
        pos = pygame.mouse.get_pos()
        if actions['enter']:
            if self.index == 0:
                pass
            elif self.index == 1:
                pass
            elif self.index == 2:
                pass
            elif self.index == 3:
                self.exit_state()
        if actions['left mouse']:
            if self.save1_button.collidepoint(pos):
                pass
            if self.save2_button.collidepoint(pos):
                pass
            if self.save3_button.collidepoint(pos):
                pass
            if self.back_button.collidepoint(pos):
                self.exit_state()
        self.game_manager.reset_keys()
