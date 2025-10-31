"""
Author: Dylan Hodkinson
Date: 31/10/25
Program: Asteroids game
"""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
	pygame.init()
	print(
	f"Starting Asteroids!\n"
	f"Screen width: {SCREEN_WIDTH}\n"
	f"Screen height: {SCREEN_HEIGHT}\n"
	)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		pygame.display.flip()

if __name__ == "__main__":
    main()
