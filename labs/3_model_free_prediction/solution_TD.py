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
alpha = 0.01


def play_episode(q_values=None):
    state, _ = env.reset()
    done = False
    r_s = []
    while not done:
        if q_values is None:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_values[state])
        state, reward, done, _, _ = env.step(action)
        r_s.append(reward)
    return r_s


def learn_q_table():

    state, _ = env.reset()
    action = random.randint(0, 3)
    done = False

    r_s = []

    while not done:
        next_state, reward, done, _, _ = env.step(action)
        next_action = random.randint(0, 3)

        q_values[state, action] += alpha * (reward + q_values[next_state, next_action] - q_values[state, action])
        state = next_state
        action = next_action

        r_s.append(reward)

    return r_s


def main():
    successful_episodes = 1000
    while successful_episodes > 0:
        rewards = learn_q_table()

        if sum(rewards) > 0:
            # Task 3: print Q-values using TD
            #print(q_values)
            # Task 3: play 100 episodes using current Q-values and greedy policy
            all_rewards = 0
            for i in range(100):
                rewards = play_episode(q_values)
                all_rewards += sum(rewards)
            print(all_rewards/100)
            successful_episodes -= 1


main()
