import pygame
import pytmx

from game import config
from game.sprites.camera_group import CameraGroup
from game.sprites.player import Player
from game.sprites.sprites import Generic, Water, Farmable, Tree, Interaction, Stump
from game.states.state import State
from game.support import import_folder


class Farm(State):
    def __init__(self, game_manager, name):
        State.__init__(self, game_manager, name)
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.farmable_sprites = pygame.sprite.Group()
        self.tree_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()


        self.setup()

    def setup(self):
        map_data = pytmx.load_pygame(r'C:\Users\april\OneDrive\Documents\Tiled Maps\sim_farm.tmx')

        for x, y, surf in map_data.get_layer_by_name("Ground").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['ground'])

        for x, y, surf in map_data.get_layer_by_name("House Top").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['house top'])

        for x, y, surf in map_data.get_layer_by_name("House Base").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['buildings'])

        for x, y, surf in map_data.get_layer_by_name("Paths").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['paths/hills/fence'])

        for x, y, surf in map_data.get_layer_by_name("Hills").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['paths/hills/fence'])

        for x, y, surf in map_data.get_layer_by_name("Fence").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Generic((x*48, y*48), transformed_surf, self.all_sprites, config.FARM_LAYERS['paths/hills/fence'])

        water_frames = import_folder("assets/water")
        for x, y, surf in map_data.get_layer_by_name("Water").tiles():
            transformed_surf = pygame.transform.scale(surf, (48, 48))
            Water((x*48, y*48), water_frames, self.all_sprites)

        for x, y, surf in map_data.get_layer_by_name("Collisions").tiles():
            Generic((x*48, y*48), pygame.Surface((48, 48)), self.collision_sprites)

        for x, y, surf in map_data.get_layer_by_name("Farmable").tiles():
            Farmable((x*48, y*48), pygame.Surface((48, 48)), [self.all_sprites, self.farmable_sprites])

        for obj in map_data.get_layer_by_name("Trees"):
            if obj.name != 'xlStump':
                Tree(
                    pos=(obj.x * 3, obj.y * 3),
                    surf=pygame.transform.scale(obj.image, (96, 96)),
                    groups=[self.all_sprites, self.collision_sprites, self.tree_sprites],
                    name=obj.name,
                    player_add=self.game_manager.game.player_add
                )
            else:
                Stump(
                    pos=(obj.x*3, obj.y*3),
                    surf=pygame.transform.scale(obj.image, (160, 64)),
                    groups=[self.all_sprites, self.collision_sprites, self.tree_sprites],
                    name=obj.name,
                    player_add=self.game_manager.game.player_add
                )

        for obj in map_data.get_layer_by_name("Decorations"):
            if obj.name == 'Left Statue':
                Generic((obj.x*3, obj.y*3), pygame.transform.scale(obj.image, (200, 200)), [self.all_sprites, self.collision_sprites])

            if obj.name == 'Right Statue':
                Generic((obj.x*3, obj.y*3), pygame.transform.scale(obj.image, (200, 200)), [self.all_sprites, self.collision_sprites])

            if obj.name == 'Fountain':
                Generic((obj.x*3, obj.y*3), pygame.transform.scale(obj.image, (200, 200)), [self.all_sprites, self.collision_sprites])

            if obj.name == 'Mailbox':
                Generic((obj.x*3, obj.y*3), pygame.transform.scale(obj.image, (48, 48)), [self.all_sprites, self.collision_sprites])

            if obj.name == 'Shipping Bin':
                Generic((obj.x*3, obj.y*3), pygame.transform.scale(obj.image, (48, 48)), [self.all_sprites, self.collision_sprites])


        for obj in map_data.get_layer_by_name("Player"):
            if obj.name == 'Enter Farmhouse':
                Interaction((obj.x*3, obj.y*3), (obj.width, obj.height), self.interaction_sprites, obj.name)

            if obj.name == 'Exit Farm East':
                Interaction((obj.x*3, obj.y*3), (obj.width, obj.height), self.interaction_sprites, obj.name)

            if obj.name == 'Exit Farm South':
                Interaction((obj.x*3, obj.y*3), (obj.width, obj.height), self.interaction_sprites, obj.name)

            if obj.name == "Farmhouse Start":
                self.player = Player((obj.x * 3, obj.y * 3), self.game_manager.game, self.all_sprites, self.collision_sprites, self.tree_sprites, self.interaction_sprites, self.game_manager.game.zone)
                self.game_manager.game.player = self.player

    def update(self, delta_time, actions):
        self.game_manager.screen.fill(config.BLACK)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(delta_time)
