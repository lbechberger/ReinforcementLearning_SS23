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

q_values = np.zeros((no_states, no_actions))
q_counter = np.zeros((no_states, no_actions))


def play_episode(q_values=None):
    state, _ = env.reset()
    done = False
    r_s = []
    s_a = []
    while not done:
        if q_values is None:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_values[state])
        s_a.append((state, action))
        state, reward, done, _, _ = env.step(action)
        r_s.append(reward)
    return s_a, r_s


def main():
    successful_episodes = 1000
    while successful_episodes > 0:
        s_a, rewards = play_episode()

        # Task 1: update Q-values using MC
        for i, (s,a) in enumerate(s_a):
            return_i = sum(rewards[i:])
            q_counter[s][a] += 1
            q_values[s][a] += (1/q_counter[s][a]) * (return_i - q_values[s][a])

        if sum(rewards) > 0:
            # Task 1: print Q-values using MC
#            print(q_values)
            # Task 2: play 100 episodes using current Q-values and greedy policy
            all_rewards = 0
            for i in range(100):
                _, r = play_episode(q_values)
                all_rewards += sum(r)
            print(all_rewards/100)
            successful_episodes -= 1


main()
