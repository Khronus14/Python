"""
Score object for Jumper game.

Author: DR, https://github.com/Khronus14
"""

import pygame

class Score:

    def __init__(self, jumper_game):
        self.jumper_game = jumper_game
        self.screen = jumper_game.screen
        self.screen_rect = jumper_game.screen_rect
        self.score_font = jumper_game.score_font

    def blitme(self):
        self.current_time = (pygame.time.get_ticks() // 1000) - self.jumper_game.start_time
        self.score_count = str(self.current_time)
        self.score_surface = self.score_font.render('Score: ' + self.score_count, False, 'White')
        self.score_rect = self.score_surface.get_rect(topleft = (675, 30))
        self.screen.blit(self.score_surface, self.score_rect)
