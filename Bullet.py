import pygame
from Constants import Constants

class Bullet:
    _Bullet = None
    _rect = None
    _pos = (None, None)
    _screen = None
    _bulletHitTarget = False
    _totalTravelDistance = 0

    def __init__(self, pos, screen):

        self._Bullet = pygame.image.load("assets/Bullet.png").convert_alpha()
        self._Bullet = pygame.transform.scale(self._Bullet, (Constants.BULLET_SIZE, Constants.BULLET_SIZE))
        self._rect = self._Bullet.get_rect()
        self._screen = screen
        self._pos = pos

        self._totalTravelDistance = Constants.SCREEN_WIDTH - pos[0]
        self.refresh()

    def getRect(self):
        return self._Bullet.get_rect()

    def hit(self):
        self._bulletHitTarget = True
    def refresh(self): # return true if bullet end return false if it needs to continue
        self._pos = (self._pos[0] + Constants.BULLET_SPEED, self._pos[1])
        self._screen.blit(self._Bullet, self._pos)
        # print("Width: " + str(Constants.SCREEN_WIDTH) + "Pos: " + str(self._pos[0]))
        if self._pos[0] > Constants.SCREEN_WIDTH or self._bulletHitTarget:
            return True
        else:
            return False

