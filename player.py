from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.speed_multiplier = 1
		self.firing_cooldown = 0
	
	
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
		print(forward)
		self.position += forward * (PLAYER_SPEED * self.speed_multiplier) * dt
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def shoot(self):
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		shot.velocity = pygame.Vector2(0, 1)
		shot.velocity = shot.velocity.rotate(self.rotation)
		print(shot.velocity)
		shot.velocity.scale_to_length(PLAYER_SHOOT_SPEED)

		self.firing_cooldown = 0.3

	
	def update(self, dt):
		keys = pygame.key.get_pressed() 
		if self.firing_cooldown > 0:
			self.firing_cooldown = max(0, self.firing_cooldown - dt)
		
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

		if keys[pygame.K_SPACE] and self.firing_cooldown <= 0:
			self.shoot()