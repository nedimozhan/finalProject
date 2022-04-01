# -*- coding: utf-8 -*-
import pygame
import random

class Army(pygame.sprite.Sprite):
    def __init__(self,episode,economy,countOfArmies):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.x_pos = 380
        self.y_pos = 770
        self.rect.center = (self.x_pos,self.y_pos)
        self.episode = episode[0]
        economy[0] -= 200
        countOfArmies[0] += 1
        
    def update(self,episode,countOfArmies):
        if self.y_pos <=30:
            countOfArmies[0] -= 1
            self.kill()
            
        elif((episode[0]-self.episode)%5 == 0):
            self.y_pos -= 10
            self.rect.y = self.y_pos

    