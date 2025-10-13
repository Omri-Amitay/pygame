import pygame
from Player import Player
from Constants import Constants
from Constants import EggValues
from Egg import Egg
import time
pygame.init()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH,Constants.SCREEN_HEIGHT))
player = Player(screen)

map = []
def initMap():
    verticleSpacing = Constants.SCREEN_HEIGHT / (Constants.COLUMN_COUNT + 1)
    for r in range(Constants.ROW_COUNT): # num of rows
        currentRow = []
        for c in range(Constants.COLUMN_COUNT):
            x = r * 100 + 300
            y =  (c + 1) * verticleSpacing - Constants.EGG_SIZE/2 #evenly space the eggs out
            currentRow.append(Egg((x , y), screen, EggValues.ENEMY))

        map.append(currentRow)
def refreshAll():

    player.refresh()

    for _,row in enumerate(map): #refresh all eggs
        for _,egg in enumerate(row):
            egg.refresh()


running = True
initMap()

while running:

    keys = pygame.key.get_pressed()

    movementDirection = 0
    if keys[pygame.K_UP]:
        movementDirection = 1
    elif keys[pygame.K_DOWN]:
        movementDirection = -1

    player.move(movementDirection)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.shoot()



    screen.fill((100,255,100))
    refreshAll()
    pygame.display.update()