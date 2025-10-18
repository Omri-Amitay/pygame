import random

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


def pickRandom(rangeOfNumbers, numberOfRandoms, canHaveMultiple):
    randomArr = []
    for i in range(numberOfRandoms):
        randomNum = random.randint(0, rangeOfNumbers)
        while (randomNum in randomArr) and (not canHaveMultiple):

            randomNum = random.randint(0, rangeOfNumbers)

        randomArr.append(randomNum)
    return randomArr


shoot_sound = None
def initSound():
    pygame.mixer.init()
    global shoot_sound
    shoot_sound = pygame.mixer.Sound("assets/shoot.mp3")
    shoot_sound.set_volume(0.5)


def initMap():
    pygame.display.set_caption("Space Chicken Defenders 🐔")
    verticleSpacing = Constants.SCREEN_HEIGHT / (Constants.COLUMN_COUNT + 1)
    for r in range(Constants.ROW_COUNT): # num of rows
        currentRow = []
        for c in range(Constants.COLUMN_COUNT):
            x = Constants.SCREEN_WIDTH - (r + 1) * 100
            y =  (c + 1) * verticleSpacing - Constants.EGG_SIZE/2 #evenly space the eggs out
            currentRow.append(Egg((x , y), screen, EggValues.ENEMY))

        map.append(currentRow)
    friendlyRows = pickRandom(Constants.ROW_COUNT - 1, Constants.NUM_OF_FRIENDLY, True) # can have multiple because on the same row they can be multiple
    friendlyColumns = pickRandom(Constants.COLUMN_COUNT - 1, Constants.NUM_OF_FRIENDLY, False) # I don't want 2 friendlys on eachother

    for i,v in enumerate(friendlyRows):

        map[v][friendlyColumns[i]].changeEggLevel(EggValues.FRIENDLY)

score = 0
def changeScore(scoreAddition):
    global score
    score = score + scoreAddition

def writeText(text, color, position, centerOrigin):

    text = font.render(text,True,color)
    if centerOrigin:
        text_rect = text.get_rect()
        text_rect.center = (position)
        screen.blit(text, text_rect)
    else:
        screen.blit(text, position)

font = pygame.font.SysFont("Arial",Constants.TEXT_SIZE,  bold=True )
def refreshScoreboard():
    writeText("Score: " + str(score), (0,0,0), (0,0), False)

def refreshGameInstructions():
    gameInstructions = "How to Play: \nW/S curveBullet \nUP/DOWN arrow keys to move \nshoot enemy eggs to earn points \nfriendly eggs shot lower score"
    lines = gameInstructions.split("\n")
    offset = Constants.SCREEN_HEIGHT - len(lines) * Constants.TEXT_SIZE
    for line in lines:
        writeText(line, (0,0,0), (0,offset), False)
        offset += Constants.TEXT_SIZE

def refreshAll():
    refreshScoreboard()
    refreshGameInstructions()
    player.refresh()

    for _,row in enumerate(map): #refresh all eggs
        for _,egg in enumerate(row):
            changeScore(egg.refresh())


def isGameOver(): #check if all enemys are dead

    for r in range(len(map)):
        for c,egg in enumerate(map[r]):
            if egg._eggLevel == EggValues.ENEMY:
                return False
    return True


running = True
initMap()
initSound()


clock = pygame.time.Clock()
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
                if keys[pygame.K_w]:
                    player.shoot(1)
                elif keys[pygame.K_s]:
                    player.shoot(-1)
                else:
                    player.shoot(0)
                shoot_sound.play()
                # player.shoot(1)
                #how to check here if im holding down w or s?


    screen.fill((100,255,100))
    refreshAll()
    if isGameOver() == True:
        writeText("Game Over!", (0, 0, 0), (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2), True)
        writeText("Final Score: " + str(score), (0,0,0), (Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2 + 30), True)




    pygame.display.update()

    clock.tick(60)

