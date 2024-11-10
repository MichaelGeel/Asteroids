import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			vector1 = pygame.math.Vector2.rotate(self.velocity, angle)
			vector2 = pygame.math.Vector2.rotate(self.velocity, -angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			child_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
			child_asteroid_1.velocity = vector1 * 1.2
			child_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
			child_asteroid_1.velocity = vector2 * 1.2

