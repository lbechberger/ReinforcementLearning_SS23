import random
import gymnasium as gym
import numpy as np

env = gym.make("FrozenLake-v1", render_mode="ansi")
random.seed(0)
np.random.seed(0)
env.reset(seed=0)

print("## Frozen Lake ##")
print("Start state:")
print(env.render())

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

no_states = env.observation_space.n
no_actions = env.action_space.n


def play_episode():
    state, _ = env.reset()
    done = False
    r_s = []
    while not done:
        action = random.randint(0, 3)
        state, reward, done, _, _ = env.step(action)
        r_s.append(reward)
    return r_s


def main():
    successful_episodes = 100
    while successful_episodes > 0:
        rewards = play_episode()

        # Task 1: update Q-values using MC

        if sum(rewards) > 0:
            # Task 1: print Q-values using MC
            # Task 2: play 100 episodes using current Q-values and greedy policy
            successful_episodes -= 1


main()
