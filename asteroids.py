import pygame
from circleshape import CircleShape
from constants import *
import random

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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle_create = random.uniform(20, 50)
        random_angle = self.velocity.rotate(angle_create) * 1.2
        negative_random_angle = self.velocity.rotate(-angle_create) * 1.2
        
        radius_new = self.radius - ASTEROID_MIN_RADIUS

        # Create new asteroids - they'll automatically be added to Asteroid.containers
        asteroid_first = Asteroid(self.position.x, self.position.y, radius_new)
        asteroid_second = Asteroid(self.position.x, self.position.y, radius_new)

        # Set their velocities
        asteroid_first.velocity = random_angle
        asteroid_second.velocity = negative_random_angle