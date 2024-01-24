import pygame
import pytmx

from game.config import FARMHOUSE_LAYERS, BLACK
from game.sprites.camera_group import CameraGroup
from game.sprites.player import Player
from game.sprites.sprites import Interaction, Generic
from game.states.state import State


class Farmhouse(State):
    def __init__(self, game_manager, name, inventory):
        State.__init__(self, game_manager, name)
        self.inventory = inventory
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        map_data = pytmx.load_pygame(r'C:\Users\april\OneDrive\Documents\Tiled Maps\farmhouse_base.tmx')
        for x, y, surf in map_data.get_layer_by_name("Ground").tiles():
            transformed_surf = pygame.transform.scale(surf, (36, 36))
            Generic((x*36, y*36), transformed_surf, self.all_sprites, FARMHOUSE_LAYERS['ground'])

        for x, y, surf in map_data.get_layer_by_name("Furniture Floor").tiles():
            transformed_surf = pygame.transform.scale(surf, (36, 36))
            Generic((x*36, y*36), transformed_surf, self.all_sprites, FARMHOUSE_LAYERS['furniture floor'])

        for x, y, surf in map_data.get_layer_by_name("Furniture").tiles():
            transformed_surf = pygame.transform.scale(surf, (36, 36))
            Generic((x*36, y*36), transformed_surf, self.all_sprites, FARMHOUSE_LAYERS['furniture'])

        for x, y, surf in map_data.get_layer_by_name("Collisions").tiles():
            Generic((x*36, y*36), pygame.Surface((36, 36)), self.collision_sprites)

        for obj in map_data.get_layer_by_name("Player"):

            if obj.name == "Exit farmhouse":
                Interaction((685, 1115), (obj.width, obj.height), self.interaction_sprites, obj.name)

            if obj.name == "Bed":
                Interaction((489, 763), (obj.width*2, obj.height*2), self.interaction_sprites, obj.name)

            if obj.name == "Farmhouse Start":
                self.player = Player((688, 1016), self.game_manager, self.all_sprites, self.collision_sprites, None, self.interaction_sprites, self.game_manager.zone, self.game_manager.state_stack[-1].soil_layer)
                self.player.inventory = self.inventory

    def update(self, dt, actions):
        self.game_manager.screen.fill(BLACK)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)