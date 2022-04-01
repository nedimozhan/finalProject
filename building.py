# -*- coding: utf-8 -*-
import pygame
import random

class Building(pygame.sprite.Sprite):
    
    def __init__(self,countOfBuildings,economy,episode):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.episode = episode[0]
        left_right = random.randint(0, 2)
        
        if left_right>1:
            x_pos = random.randint(0, 350)
        else:
            x_pos = random.randint(450, 800)
        y_pos = random.randint(0, 800)
        
        countOfBuildings[0]+=1
        if economy[0]>20:
            economy[0] -= 20
        self.rect.center = (x_pos,y_pos)
    
    def update(self,economy,episode):
        if((episode[0]-self.episode)%5 == 0):
            economy[0] += 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        