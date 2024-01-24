import pygame

from game import config
from game.game import Game
from game.states.farm import Farm

from game.states.load_menu import LoadMenu
from game.states.menu import Menu
from game.states.state import State


class Title(State, Menu):
    def __init__(self, game_manager, name):
        State.__init__(self, game_manager, name)
        Menu.__init__(self, game_manager)

        self.new_image = pygame.transform.scale(pygame.image.load("assets/title/new_game.png"), (128, 128))
        self.load_image = pygame.transform.scale(pygame.image.load("assets/title/load_game.png"), (128, 128))
        self.exit_image = pygame.transform.scale(pygame.image.load("assets/title/exit.png"), (128, 128))

        self.new_x, self.new_y = self.mid_w - 200, self.mid_h
        self.load_x, self.load_y = self.mid_w - 70, self.mid_h
        self.exit_x, self.exit_y = self.mid_w + 60, self.mid_h

        self.new_rect = pygame.Rect(self.new_x, self.new_y, 128, 128)
        self.load_rect = pygame.Rect(self.load_x, self.load_y, 128, 128)
        self.exit_rect = pygame.Rect(self.exit_x, self.exit_y, 128, 128)

        self.cursor_rect.center = (self.new_x, self.new_y)

        self.menu_options = {0: ['New Game', self.mid_w - 130], 1: ['Load', self.mid_w], 2: ['Exit', self.mid_w + 130]}
        self.index = 0

    def move_cursor(self, actions):
        if actions['right']:
            self.index += 1
            if self.index == 3:
                self.index = 0
        if actions['left']:
            self.index -= 1
            if self.index < 0:
                self.index = 0
        self.cursor_rect.x = self.menu_options[self.index][1]

    def update(self, delta_time, actions):
        self.move_cursor(actions)
        pos = pygame.mouse.get_pos()
        if actions['enter']:
            if self.index == 0:
                self.game_manager.farm = Farm(self.game_manager, "Farm")
                self.game_manager.player = self.game_manager.farm.player
                self.game_manager.playing = True
                self.game_manager.farm.enter_state()
            elif self.index == 1:
                self.game_manager.load_menu = LoadMenu(self.game_manager, "Load Menu")
                self.game_manager.load_menu.enter_state()
            elif self.index == 2:
                self.game_manager.running, self.game_manager.playing = False, False
        if actions['left mouse']:
            if self.new_button.collidepoint(pos):
                self.game_manager.farm = Farm(self.game_manager, "Farm")
                self.game_manager.player = self.game_manager.farm.player
                self.game_manager.playing = True
                self.game_manager.farm.enter_state()
            if self.load_button.collidepoint(pos):
                self.game_manager.load_menu = LoadMenu(self.game_manager, "Load Menu")
                self.game_manager.load_menu.enter_state()
            if self.exit_button.collidepoint(pos):
                self.game_manager.running, self.game_manager.playing = False, False

        self.game_manager.reset_keys()

    def render(self, surface):
        self.game_manager.screen.fill(config.PINK)
        self.new_button = self.game_manager.screen.blit(self.new_image, self.new_rect)
        self.load_button = self.game_manager.screen.blit(self.load_image, self.load_rect)
        self.exit_button = self.game_manager.screen.blit(self.exit_image, self.exit_rect)
        self.draw_cursor()