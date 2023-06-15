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


def play_episode(q_values, epsilon):

    state, _ = env.reset()
    done = False
    r_s = []
    s_a = []
    while not done:
        # use q-values to implement epsilon-greedy
        action = choose_action(q_values, state, epsilon)

        s_a.append((state, action))
        state, reward, done, _, _ = env.step(action)
        r_s.append(reward)
    return s_a, r_s


def choose_action(q_values, state, epsilon):

    if random.random() > epsilon:
        # use optimal action
        max_indices = [i for i, v in enumerate(q_values[state]) if v == max(q_values[state])]
        return random.choice(max_indices)
    else:
        # explore randomly
        return random.randint(0, 3)


def main():
    no_episodes = 10000
    epsilons = [0.01, 0.1, 0.5, 1.0]

    plot_data = []

    for e in epsilons:
        q_values = np.zeros((no_states, no_actions))
        q_counter = np.zeros((no_states, no_actions))

        rewards = []
        for j in range(0, no_episodes):
            s, r = play_episode(q_values, e)
            rewards.append(sum(r))

            # update q-values with MC-prediction
            for i, (s, a) in enumerate(s):
                return_i = sum(r[i:])
                q_counter[s][a] += 1
                q_values[s][a] += (1 / q_counter[s][a]) * (return_i - q_values[s][a])

        plot_data.append(np.cumsum(rewards))

    # plot the rewards
    plt.figure()
    plt.xlabel("No. of episodes")
    plt.ylabel("Sum of Rewards")
    for i, e in enumerate(epsilons):
        plt.plot(range(0, no_episodes), plot_data[i], label=f"e={e}")
    plt.legend()
    plt.show()


main()
