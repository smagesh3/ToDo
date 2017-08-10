import pygame
from pygame.locals import *

#initialize pyGame and set up display window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width,height))

#load bunny image
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
keys = [False, False, False, False]
playerpos = [100,100]

while 1:
	#clear the screen before drawing it again
	screen.fill(0)
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100)) #this loop is to redo the grass tile over the window
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle, (0,345))
	screen.blit(player, playerpos)
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type ==pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] =True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False
	#This loop is to change the playerpos
	if keys[0]:
		playerpos[1] -= 5 #updown movement
	elif keys[2]:
		playerpos[1] += 5	
	if keys[1]:
		playerpos[0] -= 5
	elif keys[3]:
		playerpos[0] += 5 