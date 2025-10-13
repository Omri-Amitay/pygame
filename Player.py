import pygame
from Utils import Utils
from Bullet import Bullet
from Constants import Constants
class Player:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def getInstance():

        return Player._instance

    _posX = 50
    _posY = 100

    _player = None
    _screen = None
    _activeBullets = []
    def __init__(self, screen):
        self._player = pygame.image.load("assets/chicken.png").convert_alpha()
        self._player = pygame.transform.scale(self._player, (Constants.PLAYER_SIZE, Constants.PLAYER_SIZE))
        self._screen = screen

        self.refresh()

    def move(self, direction): #-1 = down 0 = don't move 1 = up
        if(direction == 0):
            return
        elif(direction == 1):
            self._posY -= Constants.PLAYER_SPEED
        else:
            self._posY += Constants.PLAYER_SPEED
        self._posY = Utils.clamp(self._posY, 0, Constants.SCREEN_HEIGHT - Constants.PLAYER_SIZE) # 520 because 600 is height - chicken size


    def getBulletArr(self):
        return self._activeBullets
    def shoot(self):
        self._activeBullets.append(Bullet((self._posX, self._posY),self._screen))
        print("shoot")

    def refresh(self):
        self._screen.blit(self._player, (self._posX,self._posY))
        if self._activeBullets:
            for i,v in enumerate(self._activeBullets):
                if(v.refresh()):
                    self._activeBullets.pop(i)
                    print("removed bullet")
                # print("refreshed Bullet " + str(i))