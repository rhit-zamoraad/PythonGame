import pygame


class Farmer:
    def __init__(self, screen):
        self.screen = screen

        self.checking_for_points = True

        self.can_hit = True
        self.time_swung = 0

        self.hit_left = False
        self.hit_right = False
        self.hit_up = False
        self.hit_down = False

    def draw(self):
        if self.hit_left:
            pygame.draw.line(self.screen, (255, 0, 255), (320, 320), (0, 320))
        if self.hit_right:
            pygame.draw.line(self.screen, (255, 0, 255), (320, 320), (640, 320))
        if self.hit_up:
            pygame.draw.line(self.screen, (255, 0, 255), (320, 320), (320, 0))
        if self.hit_down:
            pygame.draw.line(self.screen, (255, 0, 255), (320, 320), (320, 640))