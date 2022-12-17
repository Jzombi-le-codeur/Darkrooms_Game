import pygame

class Entity:
    def __init__(self):
        self.skin_hide = pygame.image.load("Assets\Images\Entity\entity.png")
        self.skin_show = pygame.image.load("Assets\Images\Entity\entity.png")
        self.skin = self.skin_hide
        self.mode = 0

    def change_mode(self):
        if self.mode == 0:
            self.mode = 1

        elif self.mode == 1:
            self.mode = 0

    def change_skin(self):
        self.change_mode()
        if self.mode == 0:
            self.skin = self.skin_hide

        elif self.mode == 1:
            self.skin = self.skin_show
