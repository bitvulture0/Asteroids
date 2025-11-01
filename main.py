"""
Author: Dylan Hodkinson
Date: 31/10/25
Program: Asteroids game
"""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player

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
	Player_0 = Player(x, y)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		Player_0.update(dt)
		screen.fill((0, 0, 0))
		Player_0.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
