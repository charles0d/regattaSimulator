import random
from collections import deque
from boat import Boat
from game import Game
from game import Action
from polar import polar_function
from constants import *
from buoy import Buoy
import numpy as np

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon0, self.eps_rate = 0.05, 10 # randomness param
        self.gamma = 0    # Discount factor
        self.memory = deque(maxlen=MAX_MEMORY)
        self.record = 1000
        self.model = None  # TODO
        self.trainer = None  # TODO

    @staticmethod
    def get_state(game):
        return np.array([game.boat.x, game.boat.y, game.boat.tacking, game.buoy.x, game.buoy.y, game.boat.bearing],
                        dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):'''
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)'''
    pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass
        #self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        epsilon = self.epsilon0 - np.exp(-self.n_games / self.eps_rate)
        # if tacking do not do anything
        if state[2] or random.random() < 3/4:
            return Action(0, 0, 0)
        if random.random() < 1/8:
            return Action(1, 0, 0)
        if random.random() < 1/2:
            return Action(0, 1, 0)
        return Action(0, 0, 1)


def train():
    vr_polar = polar_function("polar.pol")

    boat = Boat('1', WIDTH // 2 + 50, HEIGHT - 400, 45, vr_polar)
    buoy = Buoy(WIDTH // 2 + 50, 100)
    scores_hist = []
    mean_scores = []

    agent = Agent()
    game = Game(boat, buoy, False)

    while True:
        state = agent.get_state(game)
        action = agent.get_action(state)
        reward, done, time = game.play_step(action)

        state_new = agent.get_state(game)
        agent.train_short_memory(state, action, reward, state_new, done)
        agent.remember(state, action, reward, state_new, done)

        if done:
            # experience replay
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()
            if time < agent.record:
                agent.record = time
                # agent.model.save()

            print(f'Game {agent.n_games}, time: {time}, record: {agent.record}')
            #TODO some plotting ?


if __name__ == '__main__':
    print('Running agent.py: train the model')
    train()
