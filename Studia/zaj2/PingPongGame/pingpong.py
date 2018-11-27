import pygame
import sys
from pygame.locals import *
from resources import racket,colors
class PingPong():
    def __init__(self):
        pygame.init()

        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 400

        self.game_screen = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT),0,32)
        pygame.display.set_caption("Ping Pong!")

        self.RACKET_1_POS = (350,360) #List of x,y value of starting point
        self.racket_1 = pygame.Surface([racket.RACKET_WIDTH, racket.RACKET_WYS])
        self.racket_1.fil(colors.BLUE)
        
        self.racket_1_rect = racket_1.get_rect()
        self.racket_1_rect.x = self.RACKET_1_POS[0]
        self.racket_1_rect.y = self.RACKET_1_POS[1]
        
        self.AI_speed = 3
