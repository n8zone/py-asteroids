from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
	
	def update(self, dt):
		self.position += (self.velocity * dt)
	
	def split(self):
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		angle = random.uniform(20, 50)

		vec1 = self.velocity.rotate(angle)
		vec2 = self.velocity.rotate(-angle)

		new_radius = self.radius - ASTEROID_MIN_RADIUS

		child_one = Asteroid(self.position.x, self.position.y, new_radius)
		child_one.velocity = vec1 * 1.2

		child_two = Asteroid(self.position.x, self.position.y, new_radius)
		child_two.velocity = vec2 * 1.2
