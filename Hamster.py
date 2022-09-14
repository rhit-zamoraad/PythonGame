import pygame

empty = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/empty.png")
empty = pygame.transform.scale(empty,(140,100))
show_up = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/show_up.png")
show_up = pygame.transform.scale(show_up,(150,100))


class Hamster:
    def __init__(self, screen):
        self.screen = screen

        self.can_peek = True
        self.time_hit = 0

        self.time_peek_pressed = 0
        self.time_since_peek_checked = False
        self.checking_for_points = False

        self.peek_left = False
        self.peek_right = False
        self.peek_up = False
        self.peek_down = False

        self.image_up = empty
        self.image_down = empty
        self.image_left = empty
        self.image_right = empty

    def draw(self):
        self.screen.blit(self.image_up, (220, 60))
        self.screen.blit(self.image_down, (220, 350))
        self.screen.blit(self.image_left, (60, 200))
        self.screen.blit(self.image_right, (420, 200))


