# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:19:47 2022

@author: nedim
"""

import pygame
import random
import building
import enemy
import army
import agent

# FRAME INFO
WIDTH = 800
HEIGHT = 800
FPS = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Strategy Emulator")
clock = pygame.time.Clock()

# INPUTS
health = [3]
countOfBuildings = [0]
economy = [100]
episode = [0]
countOfEnemies = [0]
countOfArmies = [0]
done = [False]

# Colors
WHITE = (255,255,255)
GREEN = (175,215,70) 
GREY = (192,192,192)

war_way = pygame.Surface((100,800))
war_way.fill(GREY)

running = True

#SPRITE GROUPS
buildings_sprite = pygame.sprite.Group()
enemy_sprite = pygame.sprite.Group()
army_sprite = pygame.sprite.Group()

while running:
    clock.tick(FPS)
    episode[0] += 1
    for event in pygame.event.get():
        keystate = pygame.key.get_pressed()
        
        #BUILDING
        if keystate[pygame.K_LEFT]:
            buildings_sprite.add(building.Building(countOfBuildings,economy,episode))
        #ENEMY
        if keystate[pygame.K_RIGHT]:
            enemy_sprite.add(enemy.Enemy(episode,countOfEnemies))
        #ARMY
        if keystate[pygame.K_UP]:
            army_sprite.add(army.Army(episode,economy,countOfArmies))
        
        
        if event.type == pygame.QUIT:
            running = False
    
    # draw
    screen.fill(GREEN)
    screen.blit(war_way,(350,0))
    
    #Buildings
    buildings_sprite.draw(screen)
    buildings_sprite.update(economy, episode)
    
    #Armies
    army_sprite.draw(screen)
    army_sprite.update(episode,countOfArmies)
    
    #Enemies
    enemy_sprite.draw(screen)
    enemy_sprite.update(episode,countOfEnemies,health,done)
    
    hits = pygame.sprite.groupcollide(army_sprite, enemy_sprite, True, True)
    if hits:
        countOfEnemies[0] -= 1
        countOfArmies[0] -= 1
        
    print("Health : {},Economy : {}, Enemies : {} , Armies : {}".
          format(health[0],economy[0],countOfEnemies[0],countOfArmies[0]))
    
    pygame.display.flip()
pygame.quit()
























