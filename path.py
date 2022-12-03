import pygame
import random

class Path(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path_1 = pygame.image.load("Assets\Images\Rooms\Dark_Hallways\Paths\Path 1.png")
        self.path_2 = pygame.image.load("Assets\Images\Rooms\Dark_Hallways\Paths\Path 2.png")
        self.path_3 = pygame.image.load("Assets\Images\Rooms\Dark_Hallways\Paths\Path 3.png")
        self.path_4 = pygame.image.load("Assets\Images\Rooms\Dark_Hallways\Paths\Path 4.png")
        self.path = self.path_1

    def change_room(self):
        path = random.randint(1, 4)
        print(f"Path: {path}")
        if path == 1:
            self.path = self.path_1

        elif path == 2:
            self.path = self.path_2

        elif path == 3:
            self.path = self.path_3

        elif path == 4:
            self.path = self.path_4
