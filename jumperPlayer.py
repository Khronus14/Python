"""
Player for Jumper game.

Author: DR, https://github.com/Khronus14
"""

import pygame


class Player:

    def __init__(self, jumper_game):
        self.screen = jumper_game.screen
        self.screen_rect = jumper_game.screen_rect

        self.player_surf_idle = pygame.image.load('jumperSprites/Link_idle.png').convert_alpha()
        self.player_surf_walk1 = pygame.image.load('jumperSprites/Link_walk1.png').convert_alpha()
        self.player_surf_walk2 = pygame.image.load('jumperSprites/Link_walk2.png').convert_alpha()
        self.player_surf_walk3 = pygame.image.load('jumperSprites/Link_walk3.png').convert_alpha()
        self.player_walk = [self.player_surf_walk1,
                            self.player_surf_walk2,
                            self.player_surf_walk3]
        self.player_index = 0
        self.player_surf = self.player_walk[self.player_index]
        self.player_rect = self.player_surf_idle.get_rect(bottomleft=(120, 300))

        self.gravity = 0

    def blitme(self):
        self.player_animation()
        self.screen.blit(self.player_surf, self.player_rect)

    def player_animation(self):
        if self.player_rect.bottom < 300:
            self.player_surf = self.player_surf_walk3
        else:
            self.player_index += 0.2
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.player_surf = self.player_walk[int(self.player_index)]

    def update(self):
        self.gravity += 1
        self.player_rect.y += self.gravity
        if self.player_rect.bottom >= 300:
            self.player_rect.bottom = 300
