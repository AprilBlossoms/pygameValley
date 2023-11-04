import pygame

from game import config
from game.sprites.cursor import Cursor
from game.states.title import Title


class GameStateManager:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Pygame Valley")
        self.clock = pygame.time.Clock()
        self.running, self.playing = True, False
        self.state_stack = []
        self.load_states()
        self.cursor_group = pygame.sprite.Group()
        self.game_cursor = Cursor(self, self.cursor_group)
        self.game_cursor.rect.center = pygame.mouse.get_pos()
        self.dt = 0

        self.actions = {'left': False, 'right': False, 'up': False, 'down': False, 'move left': False,
                        'move right': False, 'move up': False, 'move down': False, 'enter': False, 'left mouse': False,
                        'right mouse': False, 'inventory': False, 'escape': False, 'map': False, 'crafting': False,
                        'tab': False, 'hotbar left': False, 'hotbar right': False, 'back': False}


    def load_states(self):
        self.title = Title(self, "Title")
        self.state_stack.append(self.title)

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        self.screen.blit(pygame.transform.scale(self.screen, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)), (0, 0))
        self.screen.blit(self.game_cursor.image, self.game_cursor.rect)
        pygame.display.flip()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = True
                    print("enter")
                elif event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                elif event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                elif event.key == pygame.K_UP:
                    self.actions['up'] = True
                elif event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                elif event.key == pygame.K_w:
                    self.actions['move up'] = True
                elif event.key == pygame.K_s:
                    self.actions['move down'] = True
                elif event.key == pygame.K_a:
                    self.actions['move left'] = True
                elif event.key == pygame.K_d:
                    self.actions['move right'] = True
                elif event.key == pygame.K_i:
                    self.actions['inventory'] = True
                elif event.key == pygame.K_m:
                    self.actions['map'] = True
                elif event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = True
                elif event.key == pygame.K_c:
                    self.actions['crafting'] = True
                elif event.key == pygame.K_TAB:
                    self.actions['tab'] = True
                elif event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = True
                elif event.key == pygame.K_q:
                    self.actions['hotbar left'] = True
                elif event.key == pygame.K_e:
                    self.actions['hotbar right'] = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['left mouse'] = True
                    print("left mouse")
                elif event.button == 3:
                    self.actions['right mouse'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = False
                elif event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                elif event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                elif event.key == pygame.K_UP:
                    self.actions['up'] = False
                elif event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                elif event.key == pygame.K_w:
                    self.actions['move up'] = False
                elif event.key == pygame.K_s:
                    self.actions['move down'] = False
                elif event.key == pygame.K_a:
                    self.actions['move left'] = False
                elif event.key == pygame.K_d:
                    self.actions['move right'] = False
                elif event.key == pygame.K_i:
                    self.actions['inventory'] = False
                elif event.key == pygame.K_m:
                    self.actions['map'] = False
                elif event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = False
                elif event.key == pygame.K_c:
                    self.actions['crafting'] = False
                elif event.key == pygame.K_TAB:
                    self.actions['tab'] = False
                elif event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = False
                elif event.key == pygame.K_q:
                    self.actions['hotbar left'] = False
                elif event.key == pygame.K_e:
                    self.actions['hotbar right'] = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions['left mouse'] = False
                elif event.button == 3:
                    self.actions['right mouse'] = False

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def draw_text(self, surface, text, size, color, x, y):
        font = pygame.font.Font("assets/fonts/StardewValley.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def manager_loop(self):
        while self.running and not self.playing:
            self.check_events()
            self.render()
            self.update()
            self.cursor_group.draw(self.screen)
            self.game_cursor.update()
        while self.playing:
            self.game.game_loop()

