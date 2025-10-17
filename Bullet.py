import pygame
from Constants import Constants
from Utils import Utils
class Bullet:
    _Bullet = None
    _rect = None

    _screen = None
    _bulletHitTarget = False

    _spinDirecton = 0
    def __init__(self,startingPos, screen, spinDirection): # spindirection 1 is up 0 is none -1 is down
        self._spinDirecton = Utils.clamp(spinDirection, -1, 1 )
        self._Bullet = pygame.image.load("assets/Bullet.png").convert_alpha()
        self._Bullet = pygame.transform.scale(self._Bullet, (Constants.BULLET_SIZE, Constants.BULLET_SIZE))
        self._rect = self._Bullet.get_rect(topleft=startingPos)
        self._screen = screen

    def getRect(self):
        return self._rect

    def hit(self):
        self._bulletHitTarget = True
    def refresh(self): # return true if bullet end return false if it needs to continue
        self._rect.x = self._rect[0] + Constants.BULLET_SPEED
        self._rect.y = self._rect[1] + -self._spinDirecton * Constants.BULLET_SPIN_SPEED
        self._screen.blit(self._Bullet, self._rect)
        print("Width: " + str(Constants.SCREEN_WIDTH) + "Pos: " + str(self._rect[0]))
        if self._rect[0] > Constants.SCREEN_WIDTH or self._bulletHitTarget:
            return True
        else:
            return False

