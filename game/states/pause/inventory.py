import pygame

from game import config
from game.states.pause.inventory_item import InventoryItem
from game.support import Tilesheet


class Inventory:
    def __init__(self, player, game):
        self.player = player
        self.game = game

        self.seeds1 = Tilesheet("assets/items/seeds.png", 16, 16, 6, 7)

        self.image = pygame.transform.scale(pygame.image.load("assets/pause/pause_inventory.png"), (891, 417))
        self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2 - 50))
        self.selector_image = pygame.transform.scale(pygame.image.load("assets/overlay/hotbar_selector.png"), (50, 55))
        self.selector_rect = self.selector_image.get_rect(topleft=(294, 168))
        self.hotbar_image = pygame.transform.scale(pygame.image.load("assets/overlay/hotbar.png"), (500, 64))
        self.hotbar_rect = self.hotbar_image.get_rect(center=(config.SCREEN_WIDTH/2 + 130, config.SCREEN_HEIGHT/2 + 170))
        self.selected_slot = 1
        self.selected_menu = 'inventory'
        pickaxe = InventoryItem("pickaxe", 'tools', pygame.image.load("assets/overlay/pickaxe.png"))
        pickaxe.img = pygame.transform.scale(pickaxe.img, (48, 48))
        hoe = InventoryItem("hoe", 'tools', pygame.image.load("assets/overlay/hoe.png"))
        hoe.img = pygame.transform.scale(hoe.img, (48, 48))
        axe = InventoryItem("axe", 'tools', pygame.image.load("assets/overlay/axe.png"))
        axe.img = pygame.transform.scale(axe.img, (48, 48))
        water = InventoryItem("water", 'tools', pygame.image.load("assets/overlay/water.png"))
        water.img = pygame.transform.scale(water.img, (48, 48))
        self.tools = {
            'hoe': hoe,
            'water': water,
            'axe': axe,
            'pickaxe': pickaxe
        }
        self.items = {
            'seeds': {'strawberry': 3, 'carrot': 2},
            'tools': {},
            'materials': {},
            'forage': {},
            'crops': {},
            'misc': {},
            'coins': 500
        }
        self.slots = {
            'inventory': {
                '1': {'item': InventoryItem('strawberry', 'seeds', pygame.transform.scale(self.seeds1.get_tile(2, 0), (48, 48))), 'pos': (489, 270), 'amount': 3, 'rect': pygame.Rect(489, 270, 51, 54)},
                '2': {'item': InventoryItem('carrot', 'seeds', pygame.transform.scale(self.seeds1.get_tile(0, 0), (48, 48))), 'pos': (552, 270), 'amount': 2, 'rect': pygame.Rect(552, 270, 51, 54)},
                '3': {'item': None, 'pos': (615, 270), 'amount': 0, 'rect': pygame.Rect(615, 270, 51, 54)},
                '4': {'item': None, 'pos': (678, 270), 'amount': 0, 'rect': pygame.Rect(678, 270, 51, 54)},
                '5': {'item': None, 'pos': (741, 270), 'amount': 0, 'rect': pygame.Rect(741, 270, 51, 54)},
                '6': {'item': None, 'pos': (804, 270), 'amount': 0, 'rect': pygame.Rect(804, 270, 51, 54)},
                '7': {'item': None, 'pos': (867, 270), 'amount': 0, 'rect': pygame.Rect(867, 270, 51, 54)},
                '8': {'item': None, 'pos': (930, 270), 'amount': 0, 'rect': pygame.Rect(930, 270, 51, 54)},
                '9': {'item': None, 'pos': (993, 270), 'amount': 0, 'rect': pygame.Rect(993, 270, 51, 54)},
                '10': {'item': None, 'pos': (489, 336), 'amount': 0, 'rect': pygame.Rect(489, 336, 51, 54)},
                '11': {'item': None, 'pos': (552, 336), 'amount': 0, 'rect': pygame.Rect(552, 336, 51, 54)},
                '12': {'item': None, 'pos': (615, 336), 'amount': 0, 'rect': pygame.Rect(615, 336, 51, 54)},
                '13': {'item': None, 'pos': (678, 336), 'amount': 0, 'rect': pygame.Rect(678, 336, 51, 54)},
                '14': {'item': None, 'pos': (741, 336), 'amount': 0, 'rect': pygame.Rect(741, 336, 51, 54)},
                '15': {'item': None, 'pos': (804, 336), 'amount': 0, 'rect': pygame.Rect(804, 336, 51, 54)},
                '16': {'item': None, 'pos': (867, 336), 'amount': 0, 'rect': pygame.Rect(867, 336, 51, 54)},
                '17': {'item': None, 'pos': (930, 336), 'amount': 0, 'rect': pygame.Rect(930, 336, 51, 54)},
                '18': {'item': None, 'pos': (993, 336), 'amount': 0, 'rect': pygame.Rect(993, 336, 51, 54)},
                '19': {'item': None, 'pos': (489, 402), 'amount': 0, 'rect': pygame.Rect(489, 402, 51, 54)},
                '20': {'item': None, 'pos': (552, 402), 'amount': 0, 'rect': pygame.Rect(552, 402, 51, 54)},
                '21': {'item': None, 'pos': (615, 402), 'amount': 0, 'rect': pygame.Rect(615, 402, 51, 54)},
                '22': {'item': None, 'pos': (678, 402), 'amount': 0, 'rect': pygame.Rect(678, 402, 51, 54)},
                '23': {'item': None, 'pos': (741, 402), 'amount': 0, 'rect': pygame.Rect(741, 402, 51, 54)},
                '24': {'item': None, 'pos': (804, 402), 'amount': 0, 'rect': pygame.Rect(804, 402, 51, 54)},
                '25': {'item': None, 'pos': (867, 402), 'amount': 0, 'rect': pygame.Rect(867, 402, 51, 54)},
                '26': {'item': None, 'pos': (930, 402), 'amount': 0, 'rect': pygame.Rect(930, 402, 51, 54)},
                '27': {'item': None, 'pos': (993, 402), 'amount': 0, 'rect': pygame.Rect(993, 402, 51, 54)}},
            'hotbar': {
                '1': {'item': self.tools[self.player.selected_tool], 'pos': (532, 504), 'amount': None,
                      'rect': pygame.Rect(532, 504, 51, 54)},
                '2': {'item': None, 'pos': (585, 504), 'amount': 0, 'rect': pygame.Rect(585, 504, 51, 54)},
                '3': {'item': None, 'pos': (639, 504), 'amount': 0, 'rect': pygame.Rect(639, 504, 51, 54)},
                '4': {'item': None, 'pos': (692, 504), 'amount': 0, 'rect': pygame.Rect(692, 504, 51, 54)},
                '5': {'item': None, 'pos': (745, 504), 'amount': 0, 'rect': pygame.Rect(745, 504, 51, 54)},
                '6': {'item': None, 'pos': (799, 504), 'amount': 0, 'rect': pygame.Rect(799, 504, 51, 54)},
                '7': {'item': None, 'pos': (853, 504), 'amount': 0, 'rect': pygame.Rect(853, 504, 51, 54)},
                '8': {'item': None, 'pos': (907, 504), 'amount': 0, 'rect': pygame.Rect(907, 507, 51, 54)},
                '9': {'item': None, 'pos': (958, 504), 'amount': 0, 'rect': pygame.Rect(958, 504, 51, 54)},
            }
        }

    def render(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.hotbar_image, self.hotbar_rect)
        surface.blit(self.selector_image, self.slots[self.selected_menu][str(self.selected_slot)]['pos'])
        for i in range(1, 28):
            if self.slots['inventory'][str(i)]['item']:
                surface.blit(self.slots['inventory'][str(i)]['item'].img, self.slots['inventory'][str(i)]['rect'])
                self.game.game_manager.draw_text(surface, str(self.slots['inventory'][str(i)]['amount']), 30, config.BLACK, self.slots['inventory'][str(i)]['rect'].bottomright[0]-5, self.slots['inventory'][str(i)]['rect'].bottomright[1]-15)
        for i in range(1, 10):
            if self.slots['hotbar'][str(i)]['item']:
                surface.blit(self.slots['hotbar'][str(i)]['item'].img, self.slots['hotbar'][str(i)]['rect'])
                if i != 1:
                    self.game.game_manager.draw_text(surface, str(self.slots['hotbar'][str(i)]['amount']), 30,
                                                     config.BLACK,
                                                     self.slots['hotbar'][str(i)]['rect'].bottomright[0] - 10,
                                                     self.slots['hotbar'][str(i)]['rect'].bottomright[1] - 15)

    def move_cursor(self, actions):
        if actions['right']:
            self.selected_slot += 1
            if self.selected_menu == 'inventory':
                if self.selected_slot > 27:
                    self.selected_slot = 1
            else:
                if self.selected_slot > 9:
                    self.selected_slot = 1
        if actions['left']:
            self.selected_slot -= 1
            if self.selected_slot < 1:
                if self.selected_menu == 'inventory':
                    self.selected_slot = 27
                else:
                    self.selected_slot = 9
        if actions['down']:
            if self.selected_menu == 'inventory':
                self.selected_slot += 9
                if self.selected_slot > 27:
                    self.selected_slot -= 27
        if actions['up']:
            if self.selected_menu == 'inventory':
                self.selected_slot -= 9
                if self.selected_slot < 1:
                    self.selected_slot += 27
        if actions['tab']:
            if self.selected_menu == 'inventory':
                self.selected_slot = 1
                self.selected_menu = 'hotbar'
            else:
                self.selected_menu = 'inventory'
        self.selector_rect.topleft = self.slots[self.selected_menu][str(self.selected_slot)]['pos']
        if actions['enter']:
            if self.selected_menu == 'inventory':
                if self.slots['inventory'][str(self.selected_slot)]['item']:
                    for i in range(1, 10):
                        if self.slots['hotbar'][str(i)]['item'] == self.slots['inventory'][str(self.selected_slot)]['item']:
                            break
                        if self.slots['hotbar'][str(i)]['item'] is None:
                            self.slots['hotbar'][str(i)]['item'] = self.slots['inventory'][str(self.selected_slot)]['item']
                            self.slots['hotbar'][str(i)]['amount'] = self.slots['inventory'][str(self.selected_slot)][
                                'amount']
                            break
            if self.selected_menu == 'hotbar':
                if self.selected_slot != 1:
                    if self.slots['hotbar'][str(self.selected_slot)]['item']:
                        self.slots['hotbar'][str(self.selected_slot)]['item'] = None
                        self.slots['hotbar'][str(self.selected_slot)]['amount'] = 0

    def update_hotbar(self):
        self.slots['hotbar']['1']['item'] = self.tools[self.player.selected_tool]

    def update(self, dt, actions):
        self.move_cursor(actions)
        self.update_hotbar()
        self.game.game_manager.reset_keys()
        self.render(self.game.game_manager.screen)

    def add(self, item, amount):
        for i in range(1, 28):
            if not self.slots['inventory'][str(i)]['item']:
                self.slots['inventory'][str(i)]['item'] = item
                self.slots['inventory'][str(i)]['amount'] = amount
                break