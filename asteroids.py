import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # velocity should default to a vector
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, "White", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)