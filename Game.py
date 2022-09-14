import pygame
import time
from Hamster import Hamster
from Farmer import Farmer
from Scoreboard import Scoreboard

# Andrew Zamora, Yuxuan Jiang

empty = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/empty.png")
empty = pygame.transform.scale(empty,(140,100))
show_up = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/show_up.png")
show_up = pygame.transform.scale(show_up,(150,100))


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.hamster = Hamster(self.screen)
        self.farmer = Farmer(self.screen)
        self.scoreboard = Scoreboard(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.hamster.draw()
        self.farmer.draw()
        self.scoreboard.draw()

    def reset_hamster(self):
        self.hamster.peek_left = False
        self.hamster.peek_right = False
        self.hamster.peek_up = False
        self.hamster.peek_down = False

        self.hamster.image_left = empty
        self.hamster.image_right = empty
        self.hamster.image_up = empty
        self.hamster.image_down = empty


        if self.hamster.can_peek is False:
            if time.time() - self.hamster.time_hit >= 2:
                self.hamster.can_peek = True

    def reset_farmer(self):
        self.farmer.hit_left = False
        self.farmer.hit_right = False
        self.farmer.hit_up = False
        self.farmer.hit_down = False

        if self.farmer.can_hit is False:
            if time.time() - self.farmer.time_swung >= 2:
                self.farmer.can_hit = True