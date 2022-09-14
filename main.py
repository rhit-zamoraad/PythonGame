import pygame
from Game import Game
from Controller import Controller
from View import View

# Andrew Zamora, Yuxuan Jiang


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller

    frame_rate = 60

    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        controller.check_for_points()
        # game.run_one_cycle()
        viewer.draw_everything()


main()
