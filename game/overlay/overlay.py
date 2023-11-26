import pygame

from game import config
from game.overlay.hotbar import Hotbar


class Overlay:
    def __init__(self, player):
        self.player = player
        self.hotbar = Hotbar(self.player)
        self.time_image = pygame.transform.scale(pygame.image.load("assets/overlay/time_box.png"), (110, 64))
        self.time_rect = self.time_image.get_rect(center=(config.SCREEN_WIDTH - 80, 30))
        self.date_img = pygame.transform.scale(pygame.image.load("assets/overlay/date_box.png"), (148, 63))
        self.date_rect = self.date_img.get_rect(center=(config.SCREEN_WIDTH-80, 86))
        self.season_img = pygame.transform.scale(pygame.image.load("assets/overlay/season_box.png"), (128, 53))
        self.season_rect = self.season_img.get_rect(center=(config.SCREEN_WIDTH-80, 140))

    def display(self, surface):
        surface.blit(self.date_img, self.date_rect)
        surface.blit(self.time_image, self.time_rect)
        surface.blit(self.season_img, self.season_rect)
        self.player.game.game_manager.draw_text(surface, f"{self.player.game.hour} {self.player.game.minute}0", 30, config.BLACK, self.time_rect.centerx, self.time_rect.centery + 2)
        self.player.game.game_manager.draw_text(surface, f"{self.player.game.days[self.player.game.day_index]}  {self.player.game.day}", 36, config.BLACK, self.date_rect.centerx, self.date_rect.centery + 2)
        self.player.game.game_manager.draw_text(surface, f"{self.player.game.seasons[self.player.game.season_index]} {self.player.game.year}", 22, config.BLACK, self.season_rect.centerx, self.season_rect.centery + 6)
        surface.blit(self.hotbar.hotbar_image, self.hotbar.hotbar_rect)
        for i in range(1, 10):
            if i != 1:
                if self.player.inventory.slots['hotbar'][str(i)]['item']:
                    self.hotbar.slots[str(i)]['item'] = self.player.inventory.slots['hotbar'][str(i)]['item']
                    self.hotbar.slots[str(i)]['amount'] = self.player.inventory.slots['hotbar'][str(i)]['amount']
            if self.hotbar.slots[str(i)]['item']:
                surface.blit(self.hotbar.slots[str(i)]['item'].img, self.hotbar.slots[str(i)]['rect'])
                if i != 1:
                    self.player.game.game_manager.draw_text(surface, str(self.hotbar.slots[str(i)]['amount']), 30, config.BLACK, self.hotbar.slots[str(i)]['rect'].bottomright[0]-10, self.hotbar.slots[str(i)]['rect'].bottomright[1]-15)
        if self.player.selected_hotbar == 1:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar1)
        if self.player.selected_hotbar == 2:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar2)
        if self.player.selected_hotbar == 3:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar3)
        if self.player.selected_hotbar == 4:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar4)
        if self.player.selected_hotbar == 5:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar5)
        if self.player.selected_hotbar == 6:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar6)
        if self.player.selected_hotbar == 7:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar7)
        if self.player.selected_hotbar == 8:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar8)
        if self.player.selected_hotbar == 9:
            surface.blit(self.hotbar.selector_image, self.hotbar.hotbar9)