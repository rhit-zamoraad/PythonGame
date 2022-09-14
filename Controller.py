import pygame
import time
import sys
from Game import Game

empty = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/empty.png")
empty = pygame.transform.scale(empty,(140,100))
show_up = pygame.image.load("../99z-Capstone_Team_Project-202220-jiangy10-zamoraad/src/show_up.png")
show_up = pygame.transform.scale(show_up,(150,100))

# Andrew Zamora, Yuxuan Jiang


class Controller:
    def __init__(self, game: Game):
        self.game = game
        self.key_pressed = False

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()

        if self.game.hamster.can_peek:
            if pressed_keys[pygame.K_LEFT]:
                self.key_pressed = True
                self.game.hamster.peek_left = True
                self.game.hamster.image_left = show_up
                if self.game.hamster.time_since_peek_checked is False:
                    self.game.hamster.time_peek_pressed = time.time()
                    self.game.hamster.time_since_peek_checked = True
                    self.game.hamster.checking_for_points = True
                self.game.draw_game()

            elif pressed_keys[pygame.K_RIGHT]:
                self.game.hamster.peek_right = True
                self.key_pressed = True
                self.game.hamster.image_right = show_up
                if self.game.hamster.time_since_peek_checked is False:
                    self.game.hamster.time_peek_pressed = time.time()
                    self.game.hamster.time_since_peek_checked = True
                    self.game.hamster.checking_for_points = True
                self.game.draw_game()

            elif pressed_keys[pygame.K_UP]:
                self.game.hamster.peek_up = True
                self.key_pressed = True
                self.game.hamster.image_up = show_up
                if self.game.hamster.time_since_peek_checked is False:
                    self.game.hamster.time_peek_pressed = time.time()
                    self.game.hamster.time_since_peek_checked = True
                    self.game.hamster.checking_for_points = True
                self.game.draw_game()

            elif pressed_keys[pygame.K_DOWN]:
                self.game.hamster.peek_down = True
                self.key_pressed = True
                self.game.hamster.image_down = show_up
                if self.game.hamster.time_since_peek_checked is False:
                    self.game.hamster.time_peek_pressed = time.time()
                    self.game.hamster.time_since_peek_checked = True
                    self.game.hamster.checking_for_points = True
                self.game.draw_game()

            else:
                self.game.hamster.time_since_peek_checked = False
                self.game.hamster.checking_for_points = True
                self.key_pressed = False

        if self.game.farmer.can_hit:
            if pressed_keys[pygame.K_a]:
                self.game.farmer.hit_left = True
                self.game.draw_game()
                self.game.farmer.can_hit = False
                self.game.farmer.time_swung = time.time()

            elif pressed_keys[pygame.K_d]:
                self.game.farmer.hit_right = True
                self.game.draw_game()
                self.game.farmer.can_hit = False
                self.game.farmer.time_swung = time.time()

            elif pressed_keys[pygame.K_w]:
                self.game.farmer.hit_up = True
                self.game.draw_game()
                self.game.farmer.can_hit = False
                self.game.farmer.time_swung = time.time()

            elif pressed_keys[pygame.K_s]:
                self.game.farmer.hit_down = True
                self.game.draw_game()
                self.game.farmer.can_hit = False
                self.game.farmer.time_swung = time.time()
            else:
                self.game.farmer.checking_for_points = True

    def check_for_points(self):
        if self.game.farmer.checking_for_points:
            if self.game.farmer.hit_left and self.game.hamster.peek_left:
                self.game.scoreboard.farmer_score = self.game.scoreboard.farmer_score + 1
                self.game.farmer.checking_for_points = False

                self.game.reset_farmer()
                self.game.reset_hamster()

                self.game.hamster.can_peek = False
                self.game.hamster.time_hit = time.time()

                self.game.hamster.checking_for_points = False

            if self.game.farmer.hit_right and self.game.hamster.peek_right:
                self.game.scoreboard.farmer_score = self.game.scoreboard.farmer_score + 1
                self.game.farmer.checking_for_points = False

                self.game.reset_farmer()
                self.game.reset_hamster()

                self.game.hamster.can_peek = False
                self.game.hamster.time_hit = time.time()

                self.game.hamster.checking_for_points = False

            if self.game.farmer.hit_up and self.game.hamster.peek_up:
                self.game.scoreboard.farmer_score = self.game.scoreboard.farmer_score + 1
                self.game.farmer.checking_for_points = False

                self.game.reset_farmer()
                self.game.reset_hamster()

                self.game.hamster.can_peek = False
                self.game.hamster.time_hit = time.time()

                self.game.hamster.checking_for_points = False

            if self.game.farmer.hit_down and self.game.hamster.peek_down:
                self.game.scoreboard.farmer_score = self.game.scoreboard.farmer_score + 1
                self.game.farmer.checking_for_points = False

                self.game.reset_farmer()
                self.game.reset_hamster()

                self.game.hamster.can_peek = False
                self.game.hamster.time_hit = time.time()

                self.game.hamster.checking_for_points = False

        if self.game.hamster.checking_for_points and self.key_pressed:
            if time.time() - self.game.hamster.time_peek_pressed >= 1:
                self.game.scoreboard.hamster_score = self.game.scoreboard.hamster_score + 1
                self.game.hamster.checking_for_points = False

                self.game.reset_farmer()
                self.game.reset_hamster()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False