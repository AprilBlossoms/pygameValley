from random import randint

import pygame

from game import config
from game.states.pause.inventory import Inventory
from game.states.transition import Transition
from game.support import Tilesheet, Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, game, group, collision_sprites, tree_sprites, interactions, zone, soil_layer):
        super().__init__(group)
        self.game = game
        self.z = config.FARM_LAYERS['main']
        self.zone = zone
        self.soil_layer = soil_layer
        self.collision_sprites = collision_sprites
        self.tree_sprites = tree_sprites
        self.interactions = interactions
        self.sleep = False
        self.base_tiles = Tilesheet("assets/player/base.png", 64, 64, 14, 13)
        self.axe_tiles = Tilesheet("assets/player/axe.png", 128, 128, 5, 5)
        self.pickaxe_tiles = Tilesheet("assets/player/pickaxe.png", 128, 128, 5, 5)
        self.shovel_tiles = Tilesheet("assets/player/shovel.png", 64, 64, 9, 8)
        self.water_tiles = Tilesheet("assets/player/watering.png", 64, 64, 9, 8)

        self.animations = {
            'up_idle': [self.base_tiles.get_tile(10, 4).convert_alpha()],
            'down_idle': [self.base_tiles.get_tile(2, 6).convert_alpha()],
            'left_idle': [self.base_tiles.get_tile(6, 5).convert_alpha()],
            'right_idle': [self.base_tiles.get_tile(11, 6).convert_alpha()],
            'up': [self.base_tiles.get_tile(10, 4).convert_alpha(),
                   self.base_tiles.get_tile(11, 4).convert_alpha(),
                   self.base_tiles.get_tile(12, 4).convert_alpha(),
                   self.base_tiles.get_tile(0, 5).convert_alpha(),
                   self.base_tiles.get_tile(1, 5).convert_alpha(),
                   self.base_tiles.get_tile(2, 5).convert_alpha(),
                   self.base_tiles.get_tile(3, 5).convert_alpha(),
                   self.base_tiles.get_tile(4, 5).convert_alpha(),
                   self.base_tiles.get_tile(5, 5).convert_alpha()],
            'down': [self.base_tiles.get_tile(2, 6), self.base_tiles.get_tile(3, 6), self.base_tiles.get_tile(4, 6),
                     self.base_tiles.get_tile(5, 6), self.base_tiles.get_tile(6, 6), self.base_tiles.get_tile(7, 6),
                     self.base_tiles.get_tile(8, 6), self.base_tiles.get_tile(9, 6), self.base_tiles.get_tile(10, 6)],
            'left': [self.base_tiles.get_tile(6, 5).convert_alpha(),
                     self.base_tiles.get_tile(7, 5).convert_alpha(),
                     self.base_tiles.get_tile(8, 5).convert_alpha(),
                     self.base_tiles.get_tile(9, 5).convert_alpha(),
                     self.base_tiles.get_tile(10, 5).convert_alpha(),
                     self.base_tiles.get_tile(11, 5).convert_alpha(),
                     self.base_tiles.get_tile(12, 5).convert_alpha(),
                     self.base_tiles.get_tile(0, 6).convert_alpha(),
                     self.base_tiles.get_tile(1, 6).convert_alpha()],
            'right': [self.base_tiles.get_tile(11, 6), self.base_tiles.get_tile(12, 6),
                      self.base_tiles.get_tile(0, 7), self.base_tiles.get_tile(1, 7),
                      self.base_tiles.get_tile(2, 7), self.base_tiles.get_tile(3, 7),
                      self.base_tiles.get_tile(4, 7), self.base_tiles.get_tile(5, 7),
                      self.base_tiles.get_tile(6, 7)],
            'down_sowing': [self.base_tiles.get_tile(6, 8), self.base_tiles.get_tile(7, 8),
                            self.base_tiles.get_tile(8, 8), self.base_tiles.get_tile(9, 8),
                            self.base_tiles.get_tile(10, 8), self.base_tiles.get_tile(11, 8)],
            'up_sowing': [self.base_tiles.get_tile(7, 7), self.base_tiles.get_tile(8, 7),
                          self.base_tiles.get_tile(9, 7), self.base_tiles.get_tile(10, 7),
                          self.base_tiles.get_tile(11, 7), self.base_tiles.get_tile(12, 7)],
            'left_sowing': [self.base_tiles.get_tile(0, 8), self.base_tiles.get_tile(1, 8),
                            self.base_tiles.get_tile(2, 8), self.base_tiles.get_tile(3, 8),
                            self.base_tiles.get_tile(4, 8), self.base_tiles.get_tile(5, 8)],
            'right_sowing': [self.base_tiles.get_tile(12, 8), self.base_tiles.get_tile(0, 9),
                             self.base_tiles.get_tile(1, 9), self.base_tiles.get_tile(2, 9),
                             self.base_tiles.get_tile(3, 9), self.base_tiles.get_tile(4, 9)],
            'death': [self.base_tiles.get_tile(5, 13), self.base_tiles.get_tile(6, 13),
                      self.base_tiles.get_tile(7, 13), self.base_tiles.get_tile(8, 13),
                      self.base_tiles.get_tile(9, 13), self.base_tiles.get_tile(10, 13)],
            'up_axe': [self.axe_tiles.get_tile(0, 0), self.axe_tiles.get_tile(1, 0),
                       self.axe_tiles.get_tile(2, 0), self.axe_tiles.get_tile(3, 0),
                       self.axe_tiles.get_tile(4, 0), self.axe_tiles.get_tile(0, 1)],
            'left_axe': [self.axe_tiles.get_tile(1, 1), self.axe_tiles.get_tile(2, 1),
                         self.axe_tiles.get_tile(3, 1), self.axe_tiles.get_tile(4, 1),
                         self.axe_tiles.get_tile(0, 2), self.axe_tiles.get_tile(1, 2)],
            'down_axe': [self.axe_tiles.get_tile(2, 2), self.axe_tiles.get_tile(3, 2),
                         self.axe_tiles.get_tile(4, 2), self.axe_tiles.get_tile(0, 3),
                         self.axe_tiles.get_tile(1, 3), self.axe_tiles.get_tile(2, 3)],
            'right_axe': [self.axe_tiles.get_tile(3, 3), self.axe_tiles.get_tile(4, 3),
                          self.axe_tiles.get_tile(0, 4), self.axe_tiles.get_tile(1, 4),
                          self.axe_tiles.get_tile(2, 4), self.axe_tiles.get_tile(3, 4)],
            'up_pickaxe': [self.pickaxe_tiles.get_tile(0, 0), self.pickaxe_tiles.get_tile(1, 0),
                           self.pickaxe_tiles.get_tile(2, 0), self.pickaxe_tiles.get_tile(3, 0),
                           self.pickaxe_tiles.get_tile(4, 0), self.pickaxe_tiles.get_tile(0, 1)],
            'left_pickaxe': [self.pickaxe_tiles.get_tile(1, 1), self.pickaxe_tiles.get_tile(2, 1),
                             self.pickaxe_tiles.get_tile(3, 1), self.pickaxe_tiles.get_tile(4, 1),
                             self.pickaxe_tiles.get_tile(0, 2), self.pickaxe_tiles.get_tile(1, 2)],
            'down_pickaxe': [self.pickaxe_tiles.get_tile(2, 2), self.pickaxe_tiles.get_tile(3, 2),
                             self.pickaxe_tiles.get_tile(4, 2), self.pickaxe_tiles.get_tile(0, 3),
                             self.pickaxe_tiles.get_tile(1, 3), self.pickaxe_tiles.get_tile(2, 3)],
            'right_pickaxe': [self.pickaxe_tiles.get_tile(3, 3), self.pickaxe_tiles.get_tile(4, 3),
                              self.pickaxe_tiles.get_tile(0, 4), self.pickaxe_tiles.get_tile(1, 4),
                              self.pickaxe_tiles.get_tile(2, 4), self.pickaxe_tiles.get_tile(3, 4)],
            'up_hoe': [self.shovel_tiles.get_tile(0, 0), self.shovel_tiles.get_tile(1, 0),
                       self.shovel_tiles.get_tile(2, 0), self.shovel_tiles.get_tile(3, 0),
                       self.shovel_tiles.get_tile(4, 0), self.shovel_tiles.get_tile(5, 0),
                       self.shovel_tiles.get_tile(6, 0)],
            'left_hoe': [self.shovel_tiles.get_tile(0, 1), self.shovel_tiles.get_tile(1, 1),
                         self.shovel_tiles.get_tile(2, 1), self.shovel_tiles.get_tile(3, 1),
                         self.shovel_tiles.get_tile(4, 1), self.shovel_tiles.get_tile(5, 1),
                         self.shovel_tiles.get_tile(6, 1)],
            'down_hoe': [self.shovel_tiles.get_tile(0, 2), self.shovel_tiles.get_tile(1, 2),
                         self.shovel_tiles.get_tile(2, 2), self.shovel_tiles.get_tile(3, 2),
                         self.shovel_tiles.get_tile(4, 2), self.shovel_tiles.get_tile(5, 2),
                         self.shovel_tiles.get_tile(6, 2)],
            'right_hoe': [self.shovel_tiles.get_tile(0, 3), self.shovel_tiles.get_tile(1, 3),
                          self.shovel_tiles.get_tile(2, 3), self.shovel_tiles.get_tile(3, 3),
                          self.shovel_tiles.get_tile(4, 3), self.shovel_tiles.get_tile(5, 3),
                          self.shovel_tiles.get_tile(6, 3)],
            'up_water': [self.water_tiles.get_tile(0, 0), self.water_tiles.get_tile(1, 0),
                         self.water_tiles.get_tile(2, 0), self.water_tiles.get_tile(3, 0),
                         self.water_tiles.get_tile(4, 0), self.water_tiles.get_tile(5, 0),
                         self.water_tiles.get_tile(6, 0), self.water_tiles.get_tile(7, 0)],
            'left_water': [self.water_tiles.get_tile(0, 1), self.water_tiles.get_tile(1, 1),
                           self.water_tiles.get_tile(2, 1), self.water_tiles.get_tile(3, 1),
                           self.water_tiles.get_tile(4, 1), self.water_tiles.get_tile(5, 1),
                           self.water_tiles.get_tile(6, 1), self.water_tiles.get_tile(7, 1)],
            'down_water': [self.water_tiles.get_tile(0, 2), self.water_tiles.get_tile(1, 2),
                           self.water_tiles.get_tile(2, 2), self.water_tiles.get_tile(3, 2),
                           self.water_tiles.get_tile(4, 2), self.water_tiles.get_tile(5, 2),
                           self.water_tiles.get_tile(6, 2), self.water_tiles.get_tile(7, 2)],
            'right_water': [self.water_tiles.get_tile(0, 3), self.water_tiles.get_tile(1, 3),
                            self.water_tiles.get_tile(2, 3), self.water_tiles.get_tile(3, 3),
                            self.water_tiles.get_tile(4, 3), self.water_tiles.get_tile(5, 3),
                            self.water_tiles.get_tile(6, 3), self.water_tiles.get_tile(7, 3)]

        }
        self.display_inventory = False
        self.frame_index = 0
        self.status = "down_idle"

        self.image = pygame.transform.scale(self.animations[self.status][self.frame_index], (80, 80))
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy().inflate((-30, -20))
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'seed use': Timer(350),
            'switch item': Timer(200),
            'inventory': Timer(200)
        }
        self.selected_hotbar = 1
        self.tools = ['hoe', 'axe', 'water', 'pickaxe']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        self.inventory = Inventory(self, self.game)

    def use_tool(self):
        if self.selected_tool == 'axe':
            for tree in self.tree_sprites.sprites():
                if tree.rect.collidepoint(self.target_pos):
                    tree.damage()
        if self.selected_tool == 'hoe':
            self.soil_layer.till_soil(self.target_pos)
            if self.game.raining:
                self.soil_layer.water_all()
        if self.selected_tool == 'water':
            self.soil_layer.water_soil(self.target_pos)

    def use_seed(self, seed_item):
        if self.soil_layer.plant_seed(self.target_pos, seed_item.name):
            self.inventory.slots['hotbar'][str(self.selected_hotbar)]['amount'] -= 1
            if self.inventory.slots['hotbar'][str(self.selected_hotbar)]['amount'] == 0:
                self.inventory.slots['hotbar'][str(self.selected_hotbar)]['item'] = None
            for i in range(1, 28):
                if self.inventory.slots['inventory'][str(i)]['item']:
                    if self.inventory.slots['inventory'][str(i)]['item'].name == seed_item.name and self.inventory.slots['inventory'][str(i)]['item'].item_type == 'seeds':
                        self.inventory.slots['inventory'][str(i)]['amount'] -= 1
                        if self.inventory.slots['inventory'][str(i)]['amount'] == 0:
                            self.inventory.slots['inventory'][str(i)]['item'] = None
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)], (80, 80))


    def input(self, actions):
        if not self.timers['tool use'].active and not self.timers['seed use'].active:
            if actions['inventory'] and not self.timers['inventory'].active:
                self.timers['inventory'].activate()
                if not self.display_inventory:
                    self.display_inventory = True
                else:
                    self.display_inventory = False
                    self.game.paused = False
            if not self.display_inventory:
                if actions['move up']:
                    self.status = 'up'
                    self.direction.y = -1
                elif actions['move down']:
                    self.status = 'down'
                    self.direction.y = 1
                else:
                    self.direction.y = 0

                if actions['move left']:
                    self.status = 'left'
                    self.direction.x = -1
                elif actions['move right']:
                    self.status = 'right'
                    self.direction.x = 1
                else:
                    self.direction.x = 0

                if actions['hotbar left'] and not self.timers['switch item'].active:
                    self.timers['switch item'].activate()
                    self.selected_hotbar -= 1
                    if self.selected_hotbar == 0:
                        self.selected_hotbar = 9

                if actions['hotbar right'] and not self.timers['switch item'].active:
                    self.timers['switch item'].activate()
                    self.selected_hotbar += 1
                    if self.selected_hotbar == 10:
                        self.selected_hotbar = 1

                if actions['enter']:
                    collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interactions, False)
                    if collided_interaction_sprite:
                        if collided_interaction_sprite[0].name == 'Enter Farmhouse':
                            self.zone("Farmhouse")
                        if collided_interaction_sprite[0].name == 'Bed':
                            self.sleep = True
                    if self.selected_hotbar == 1:
                        self.timers['tool use'].activate()
                        self.direction = pygame.math.Vector2()
                        self.frame_index = 0
                    elif self.inventory.slots['hotbar'][str(self.selected_hotbar)]['item']:
                        if self.inventory.slots['hotbar'][str(self.selected_hotbar)]['item'].item_type == 'seeds':
                            self.timers['seed use'].activate()
                            self.use_seed(self.inventory.slots['hotbar'][str(self.selected_hotbar)]['item'])

                if actions['left'] and not self.timers['switch item'].active:
                    self.timers['switch item'].activate()
                    self.tool_index -= 1
                    if self.tool_index < 0:
                        self.tool_index = len(self.tools) - 1
                    self.selected_tool = self.tools[self.tool_index]

                if actions['right'] and not self.timers['switch item'].active:
                    self.timers['switch item'].activate()
                    self.tool_index += 1
                    if self.tool_index > len(self.tools) - 1:
                        self.tool_index = 0
                    self.selected_tool = self.tools[self.tool_index]

    def toggle_inventory(self):
        if self.display_inventory:
            self.game.paused = True
            self.inventory.render(self.game.game_manager.screen)
            self.inventory.update(self.game.game_manager.dt, self.game.game_manager.actions)
    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + "_idle"
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + "_" + self.selected_tool
        if self.timers['seed use'].active:
            self.status = self.status.split('_')[0] + "_sowing"

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision("horizontal")

        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision("vertical")

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def collision(self, direction):
        for sprite in self.interactions.sprites():
            if hasattr(sprite, "name"):
                if sprite.name == 'Exit farmhouse':
                    if self.hitbox.colliderect(sprite):
                        self.zone("Farm")
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def get_target_pos(self):
        self.target_pos = self.rect.center + config.PLAYER_TOOL_OFFSET[self.status.split('_')[0]]

    def update(self, dt):
        self.input(self.game.game_manager.actions)
        self.toggle_inventory()
        self.get_status()
        self.update_timers()
        self.get_target_pos()
        self.move(dt)
        self.animate(dt)
        if self.sleep:
            self.transition()

    def transition(self):
        self.game.day += 1
        self.game.day_index += 1
        if self.game.day_index == 7:
            self.game.day_index = 0
        if self.game.day == 29:
            self.game.day = 1
            self.game.season_index += 1
            if self.game.season_index == 4:
                self.game.year += 1
                self.game.season_index = 0
        self.sleep = False
        self.soil_layer.update_plants()
        self.soil_layer.remove_water()
        self.game.raining = randint(0, 10) > 3
        new_state = Transition(self.game.game_manager, "Transition")
        new_state.enter_state()
