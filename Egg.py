import pygame
from Constants import Constants
from Constants import EggValues
from Player import Player
class Egg:

    _egg = None
    _eggLevel = None
    _screen = None
    _startingPoint = (None, None)
    def __init__(self,startingPoint ,screen,  eggLevel):

        if hasattr(self, "_initialized") and self._initialized: #for singleton
            return

        self._eggLevel = eggLevel
        self._screen = screen
        self._startingPoint = startingPoint

        self._egg = pygame.image.load("assets/egg.png").convert_alpha()
        self._egg = pygame.transform.scale(self._egg, (Constants.EGG_SIZE,Constants.EGG_SIZE))



    def checkHit(self):
        #highestNum = 0
        for i,v in enumerate(Player.getInstance().getBulletArr()):
            if pygame.Rect.colliderect(v.getRect(),self._egg.get_rect()):
                print("target hit")

        #     if i > highestNum:
        #         highestNum = i
        # print(highestNum)
    def refresh(self):
        self._screen.blit(self._egg, self._startingPoint)
        self.checkHit()
