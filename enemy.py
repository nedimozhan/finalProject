# -*- coding: utf-8 -*-
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,episode,countOfEnemies):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.x_pos = 380
        self.y_pos = 0
        self.rect.center = (self.x_pos,self.y_pos)
        self.episode = episode[0]
        countOfEnemies[0] += 1
        
    def update(self,episode,countOfEnemies,health,running,reward):
        if(self.y_pos>=770):
            countOfEnemies[0] -= 1
            health[0] -= 1
            reward[0] -= 200
            if health[0] <= 0:
                running[0] = False
            self.kill()   
            
        elif((episode[0]-self.episode)%5 == 0):
            self.y_pos += 10
            self.rect.y = self.y_pos
            
        
    
    
    
    
    