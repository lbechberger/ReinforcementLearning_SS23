import gymnasium as gym
import random

env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="ansi")
discount = 1

random.seed(0)
env.reset(seed=0)

actions = range(0, env.env.action_space.n)
states = range(0, env.env.observation_space.n)
tp_matrix = env.env.P

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}
print(env.render())

# put your solution here





