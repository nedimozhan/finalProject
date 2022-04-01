# -*- coding: utf-8 -*-

import pygame
import random
import building
import enemy
import army
import agent

class Environment(pygame.sprite.Sprite):
    def __init__(self):
         
         pygame.sprite.Sprite.__init__(self)
         
         # FRAME INFO
         self.WIDTH = 800
         self.HEIGHT = 800
         self.FPS = 30
         pygame.init()
         self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
         pygame.display.set_caption("Strategy Emulator")
         self.clock = pygame.time.Clock() 
        
        # # INPUTS
         self.health = [3]
         self.countOfBuildings = [0]
         self.economy = [100]
         self.episode = [0]
         self.countOfEnemies = [0]
         self.countOfArmies = [0]
         self.reward = [0]
         self.totalReward = 0
        
         # Colors
         self.WHITE = (255,255,255)
         self.GREEN = (175,215,70) 
         self.GREY = (192,192,192)
        
         self.war_way = pygame.Surface((100,800))
         self.war_way.fill(self.GREY)
        
        
        # #SPRITE GROUPS
         self.buildings_sprite = pygame.sprite.Group()
         self.enemy_sprite = pygame.sprite.Group()
         self.army_sprite = pygame.sprite.Group()
        
        # #AGENT
         self.agent = agent.Agent()
        
        
    def step(self,action):
        state_list = []
        
        if action == 0: # BUILDING
            self.buildings_sprite.add(building.Building(self.countOfBuildings,self.economy,self.episode))
        elif action == 1: # ARMY
            self.army_sprite.add(army.Army(self.episode,self.economy,self.countOfArmies))
        
    def reset(self):
        self.health = [3]
        self.countOfBuildings = [0]
        self.economy = [100]
        self.episode = [0]
        self.countOfEnemies = [0]
        self.countOfArmies = [0]
        self.reward = [0]
        self.totalReward = 0
        
        self.buildings_sprite = pygame.sprite.Group()
        self.enemy_sprite = pygame.sprite.Group()
        self.army_sprite = pygame.sprite.Group()
    
    def run(self):
        
        self.running = [True]
        state = [self.health[0],self.countOfBuildings[0],
                 self.economy[0],self.countOfEnemies[0],
                 self.countOfArmies[0]]
        
        batch_size = 24
        
        while self.running[0]:
            self.clock.tick(self.FPS)
            self.episode[0] += 1
            self.reward[0] = 0
            for event in pygame.event.get():
                keystate = pygame.key.get_pressed()

                #ENEMY
                if keystate[pygame.K_RIGHT]:
                    self.enemy_sprite.add(enemy.Enemy(self.episode,self.countOfEnemies))
                
                if event.type == pygame.QUIT:
                    self.running[0] = False
                    
            if(self.episode[0] % 20 == 0):
                action = self.agent.act(state)
                self.step(action)
                next_state = [self.health[0],self.countOfBuildings[0],
                      self.economy[0],self.countOfEnemies[0],
                      self.countOfArmies[0]]
                self.reward[0] += (state[2]-next_state[2])*0.1
                self.totalReward += self.reward[0]
                self.agent.remember(state, action, self.reward, next_state, self.running)
            
                state = [self.health[0],self.countOfBuildings[0],
                      self.economy[0],self.countOfEnemies[0],
                      self.countOfArmies[0]]
            
            # Training 
                self.agent.replay(batch_size)
            
            # Epsilon Greedy
                #self.agent.adaptiveGreedy()
            
                print("Health : {},Economy : {}, Enemies : {} , Armies : {}".
                   format(self.health[0],self.economy[0],self.countOfEnemies[0],self.countOfArmies[0]))
            
            
            # draw
            self.screen.fill(self.GREEN)
            self.screen.blit(self.war_way,(350,0))
            
            #Buildings
            self.buildings_sprite.draw(self.screen)
            self.buildings_sprite.update(self.economy, self.episode)
            
            # #Armies
            self.army_sprite.draw(self.screen)
            self.army_sprite.update(self.episode,self.countOfArmies)
            
            # #Enemies
            self.enemy_sprite.draw(self.screen)
            self.enemy_sprite.update(self.episode,self.countOfEnemies,self.health,self.reward,self.running)
            
            hits = pygame.sprite.groupcollide(self.army_sprite, self.enemy_sprite, True, True)
            if hits:
                 self.countOfEnemies[0] -= 1
                 self.countOfArmies[0] -= 1
                
            pygame.display.flip()
        pygame.quit()
    
if __name__ == "__main__":
    env = Environment()
    liste = []
    t = 0
    while True:
        t += 1
        print("Episode",t)
        #liste.append(env.totalReward)
        
        env.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


