"""
Author: Dylan Hodkinson
Date: 31/10/25
Program: Asteroids game
"""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print(
	f"Starting Asteroids!\n"
	f"Screen width: {SCREEN_WIDTH}\n"
	f"Screen height: {SCREEN_HEIGHT}\n"
	)

	clock = pygame.time.Clock()
	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable, drawable, shots)

	player = Player(x, y)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for a in asteroids:
			if a.collision_check(player):
				print("Game over!")
				sys.exit()

		for a in asteroids:
			for s in shots:
				if a.collision_check(s):
					s.kill()
					a.split()

		screen.fill((0, 0, 0))
		for thing in drawable:
			thing.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
