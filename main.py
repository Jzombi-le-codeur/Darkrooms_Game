import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((1125, 720))

launched = True

game = Game()

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

            elif event.key == pygame.K_RIGHT and game.path.path == game.path.path_3 or game.path.path == game.path.path_4:
                game.path.change_room()

            elif event.key == pygame.K_LEFT and game.path.path == game.path.path_2 or game.path.path == game.path.path_4:
                game.path.change_room()
