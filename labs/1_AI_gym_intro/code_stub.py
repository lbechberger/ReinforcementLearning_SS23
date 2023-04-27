import gymnasium as gym
import random

env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")

random.seed(0)
env.reset(seed=0)

print("## Frozen Lake ##")
print("Start state:")
print(env.render())

no_of_actions = env.env.action_space.n
action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

state, _ = env.reset()
done = False

while not done:
    action = random.randint(0, no_of_actions-1)  # choose a random action
    state, reward, done, _, _ = env.step(action)
    print(f"\nAction:{action2string[action]}, new state:{state}, reward:{reward}")
    print(env.render())
