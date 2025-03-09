import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw a circle
        pygame.draw.circle(surface=screen,
                           color="white",
                           center=self.position,
                           radius=self.radius,
                           width=2)
        
    def update(self, dt):
        # Update position based on velocity and time
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # If the asteroid was small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # If the asteroid was large/medium
        else:
            # Randomize the angle of the split
            random_angle = random.uniform(20, 50)

            # New velocities for 2 new asteroids
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)

            # Create 2 new asteroids
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = vel1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = vel2 * 1.2
