import pygame

from game.overlay.hotbar import Hotbar


class Overlay:
    def __init__(self, player):
        self.player = player
        self.hotbar = Hotbar(self.player)

    def display(self, surface):
        surface.blit(self.hotbar.hotbar_image, self.hotbar.hotbar_rect)
        for i in range(1, 10):
            if self.hotbar.slots[str(i)]['item']:
                surface.blit(self.hotbar.slots[str(i)]['item'].img, self.hotbar.slots[str(i)]['rect'])
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