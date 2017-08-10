import pygame
import datetime
import time

x = 400#int(input("Enter a number: "))
y = 400#int(input("Enter a number:"))
screen = pygame.display.set_mode((x, y))
running = 1

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	if now.weekday() == True:
		screen.fill((50, 50, 50))
	screen.fill((0, 30, 50))
	pygame.display.flip()
