import pygame

class Entity:
    def __init__(self):
        self.skin_hide = pygame.image.load("Assets\Images\Entity\Hide.png")
        self.skin_show = pygame.image.load("Assets\Images\Entity\entity.png")
        self.skin = self.skin_hide
        self.mode = 0

    def change_mode(self):
        if self.mode == 0:
            self.mode = 1

        elif self.mode == 1:
            self.mode = 0

    def change_skin(self):
        print(f"Mode: {self.mode}")
        if self.mode == 0:
            self.skin = self.skin_hide

        elif self.mode == 1:
            self.skin = self.skin_show

    def screamer(self):
        self.change_mode()
        scream = pygame.mixer.music.load("Assets\Sounds\Sounds\scream.mp3")
        pygame.mixer.music.set_volume(1 )
        pygame.mixer.music.play()
