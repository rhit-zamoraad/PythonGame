import pygame


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.hamster_score = 0
        self.farmer_score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        hamster_score_string = "Hamster Score: {}".format(self.hamster_score)
        hamster_score_image = self.font.render(hamster_score_string, True, (0, 0, 0))

        farmer_score_string = "Farmer Score: {}".format(self.farmer_score)
        farmer_score_image = self.font.render(farmer_score_string, True, (0, 0, 0))

        self.screen.blit(hamster_score_image, (5, 5))
        self.screen.blit(farmer_score_image, (5, 25))

