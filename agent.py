# -*- coding: utf-8 -*-
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.layers import InputLayer
import random
import tensorflow as tf

class Agent:
    
    def __init__(self):
        # parameter / hyper parameter
        
        self.state_size = 5    
        self.action_size = 2   
        
        self.gamma = 0.95
        self.learning_rate = 0.001
        
        self.epsilon = 1
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        
        self.memory = deque(maxlen=1000)
        self.model = self.build_model()

    def build_model(self):
        #neural network for deep q learning
        # model = Sequential()
        # model.add(Dense(24,input_dim=self.state_size,activation="tanh"))
        # #model.add(Dense(self.state_size,activation="tanh"))
        # model.add(Dense(self.action_size,activation="linear"))
        # model.compile(loss="mse",optimizer=Adam(lr = self.learning_rate))
        
        
        model = Sequential()
        model.add(InputLayer(batch_input_shape=(1,5)))
        model.add(Dense(20, activation='relu'))
        model.add(Dense(2, activation='linear'))
        model.compile(loss='mse', optimizer='adam', metrics=['mae'])
        return model
    
    def remember(self,state,action,reward,next_state,done):
        #storage
        self.memory.append((state,action,reward[0],next_state,done[0]))
    
    def act(self,state):
        state = np.array(state)
        
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])
        
    def replay(self,batch_size):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state , action, reward, next_state , done in minibatch:
            state = np.array(state)
            next_state = np.array(next_state)
            if done:
                target = reward
            else:
                target = reward + self.gamma*np.amax(self.model.predict(next_state)[0])
            train_target = self.model.predict(state)
            train_target[0][action] = target
            self.model.fit(state,train_target,verbose = 0)
            
    def adaptiveGreedy(self):
        if self.epsilon>self.epsilon_min:
            self.epsilon *= self.epsilon_decay
            
            
            
            
            
            