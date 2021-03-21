
from collections import deque
from boat import Boat
from game import Game
from polar import polar_function
from constants import *
from buoy import Buoy

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness param
        self.gamma = 0    # Discount factor
        self.memory = deque(maxlen=MAX_MEMORY)
        self.record = 1000

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass


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
            if time < record:
                record = time
                # agent.model.save()

            print(f'Game {agent.n_games}, time: {time}, record: {record}')
            #TODO some plotting ?


if __name__ == '__main__':
    print('Running agent.py: train the model')
    train()
