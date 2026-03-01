import gym
from gym import spaces
import numpy as np
import os


class ChefsHatEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(ChefsHatEnv, self).__init__()

        # ===== REQUIRED FIXES =====
        self.episodeNumber = 0
        self.logDirectory = "./logs"
        self.verbose = False
        self.saveLog = False

        os.makedirs(self.logDirectory, exist_ok=True)

        # ===== SIMPLE ENV DESIGN (STABLE) =====
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Box(
            low=0, high=100, shape=(1,), dtype=np.float32
        )

        self.state = 0
        self.max_steps = 20
        self.current_step = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.episodeNumber += 1
        self.current_step = 0
        self.state = np.random.randint(0, 10)

        return np.array([self.state], dtype=np.float32)

    def step(self, action):
        self.current_step += 1

        reward = float(action)  # simple reward logic
        self.state = (self.state + action) % 100

        done = self.current_step >= self.max_steps

        return (
            np.array([self.state], dtype=np.float32),
            reward,
            done,
            {}
        )

    def render(self, mode="human"):
        print(f"State: {self.state}")

    def close(self):
        pass