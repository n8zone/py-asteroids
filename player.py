from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.speed_multiplier = 1
	
	
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * (PLAYER_SPEED * self.speed_multiplier) * dt
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	def update(self, dt):
		keys = pygame.key.get_pressed()
		
		self.speed_multiplier = 1
		if keys[pygame.K_LSHIFT]:
			self.speed_multiplier = 3

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)