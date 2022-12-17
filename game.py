import random
import pygame
from path import Path

class Game:
    def __init__(self):
        self.path = Path()
        self.stress = 0

    def add_stress(self):
        self.stress += random.randint(0, 2)
        print(f"Stress: {self.stress}")

    def screamer(self):
        self.add_stress()
        if self.stress >= 10 and self.stress <= 11:
            print("SCREAMER")
            self.stress = 0
