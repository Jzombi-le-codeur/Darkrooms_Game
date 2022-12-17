import pygame
from game import Game

pygame.init()

game = Game()

screen = game.screen

launched = True

while launched:
    path = game.path.path
    screen.blit(path, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.path.change_room()
                game.add_stress()

            elif event.key == pygame.K_RIGHT and game.path.path == game.path.path_3 or game.path.path == game.path.path_4:
                game.path.change_room()
                game.screamer()

            elif event.key == pygame.K_LEFT and game.path.path == game.path.path_2 or game.path.path == game.path.path_4:
                game.path.change_room()
                game.screamer()
