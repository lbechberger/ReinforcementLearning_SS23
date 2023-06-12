import random
import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make("FrozenLake-v1", render_mode="ansi")
random.seed(0)
np.random.seed(0)
env.reset(seed=0)

print("## Frozen Lake ##")
print("Start state:")
print(env.render())

no_states = env.observation_space.n
no_actions = env.action_space.n
q_values = np.zeros((no_states, no_actions))
q_counter = np.zeros((no_states, no_actions))


def play_episode(q_values):

    state, _ = env.reset()
    done = False
    r_s = []
    s_a = []
    while not done:
        # TODO: use q-values to implement epsilon-greedy
        action = random.randint(0, 3)

        s_a.append((state, action))
        state, reward, done, _, _ = env.step(action)
        r_s.append(reward)
    return s_a, r_s


def main():
    no_episodes = 1000
    rewards = []
    for j in range(0, no_episodes):
        s, r = play_episode(q_values)
        rewards.append(sum(r))

        # TODO: update q-values with MC-prediction

    plot_data = np.cumsum(rewards)

    # plot the rewards
    plt.figure()
    plt.xlabel("No. of episodes")
    plt.ylabel("Sum of Rewards")
    plt.plot(range(0, no_episodes), plot_data, label="random")
    plt.legend()
    plt.show()


main()
