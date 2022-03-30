"""
Jumper game

This game was designed to test understanding of Pygame and object orientated
programming fundamentals.

Player moves to the right and jumps to avoid rocks. Score is based on 
time without hitting rock. When player hits a rock the game is over.

Author: DR, https://github.com/Khronus14
Sprites: Ripped by MisterMike @ https://www.spriters-resource.com/
"""

import pygame
import sys
from jumperSettings import Settings
from jumperScore import Score
from jumperPlayer import Player
from jumperObstacle import Obstacle


class JumperGame:

    def __init__(self):
        pygame.init()
        self.game_active = True
        self.start_time = 0
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Jumper")
        self.score_font = pygame.font.Font('PressStart2P.ttf', 17)
        self.game_over_font = pygame.font.Font('PressStart2P.ttf', 70)
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.obstacle = Obstacle(self)
        self.score = Score(self)
        self.draw_ground()

    def draw_ground(self):
        self.ground_surface = pygame.image.load('jumperSprites/Ground.png').convert_alpha()
        self.ground_rect = self.ground_surface.get_rect()
        self.ground_rect.bottomleft = self.screen_rect.bottomleft

    def game_loop(self):
        while True:
            self._check_events()
            if self.game_active:
                self.player.update()
                self.obstacle.update()
                self.check_collision()
                self._update_screen()
            else:
                self.game_over_surface = self.game_over_font.render('GAME OVER', False, 'Red')
                self.game_over_rect = self.game_over_surface.get_rect(center=(450, 200))
                self.screen.blit(self.game_over_surface, self.game_over_rect)
                self.player.player_rect.y = 300
                self.player.gravity = 0
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)

    def _check_keydown(self, event):
        if event.key == pygame.K_r:
            self.game_active = True
            self.obstacle.obstacle_rect.x = 900
            self.start_time = pygame.time.get_ticks() // 1000
        elif event.key == pygame.K_q:
            self.game_over()
        elif event.key == pygame.K_SPACE and self.player.player_rect.bottom == 300:
            self.player.gravity = -18

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.obstacle.blitme()
        self.score.blitme()
        self.screen.blit(self.ground_surface, self.ground_rect)

    def check_collision(self):
        if self.player.player_rect.colliderect(self.obstacle.obstacle_rect) == 1:
            self.game_active = False

    def game_over(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    jumper_game = JumperGame()
    jumper_game.game_loop()
