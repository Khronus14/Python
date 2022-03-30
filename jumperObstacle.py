"""
Rock for Jumper game.

Author: DR, https://github.com/Khronus14
"""

import pygame


class Obstacle:

    def __init__(self, jumper_game):
        self.screen = jumper_game.screen
        self.screen_rect = jumper_game.screen_rect
        self.speed = jumper_game.settings.speed

        self.obstacle_surf_s1 = pygame.image.load('jumperSprites/Stalfos1.png').convert_alpha()
        self.obstacle_surf_s2 = pygame.image.load('jumperSprites/Stalfos2.png').convert_alpha()
        self.obstacle_walk = [self.obstacle_surf_s1,
                              self.obstacle_surf_s2]
        self.obstacle_index = 0
        self.obstacle_surf = self.obstacle_walk[self.obstacle_index]
        self.obstacle_rect = self.obstacle_surf.get_rect(bottomleft=(800, 300))

    def blitme(self):
        self.player_animation()
        self.screen.blit(self.obstacle_surf, self.obstacle_rect)

    def player_animation(self):
        self.obstacle_index += 0.2
        if self.obstacle_index >= len(self.obstacle_walk):
            self.obstacle_index = 0
        self.obstacle_surf = self.obstacle_walk[int(self.obstacle_index)]

    def update(self):
        self.obstacle_rect.x -= self.speed
        if self.obstacle_rect.x < -50:
            self.obstacle_rect.x = 900
