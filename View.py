import pygame
from Game import Game

# Andrew Zamora, Yuxuan Jiang


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game
        self.background_color = pygame.Color("white")

    def draw_everything(self):
        self.screen.fill(self.background_color)
        self.game.draw_game()
        pygame.display.update()
        self.game.reset_hamster()
        self.game.reset_farmer()