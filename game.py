import random
import pygame
from path import Path
from entity import Entity

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1125, 720))
        self.path = Path()
        self.entity = Entity()
        self.stress = 0

    def add_stress(self):
        self.stress += random.randint(0, 2)
        print(f"Stress: {self.stress}")

    def screamer(self):
        self.add_stress()
        if self.stress >= 10 and self.stress <= 11:
            print("SCREAMER")
            self.entity.change_skin()

