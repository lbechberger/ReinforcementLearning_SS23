import gymnasium as gym
import random

env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="ansi")
discount = 1

random.seed(0)
env.reset(seed=0)

actions = range(0, env.env.action_space.n)
states = range(0, env.env.observation_space.n)
model = env.env.P

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}
print(env.render())


def print_state_values(state_values):
    print([i for i in state_values[0:4]])
    print([i for i in state_values[4:8]])
    print([i for i in state_values[8:12]])
    print([i for i in state_values[12:16]])
    print("\n")


def policy_evaluation(policy):
    # set initially all state values to zero
    state_values = [0 for i in states]

    counter = 0
    while True:
        counter += 1
        delta = 0
        new_state_values = state_values.copy()
        for s in states:
            v_s = 0
            for a in actions:
                v_a = 0
                for p, s_next, reward, _ in model[s][a]:
                    v_a += p*(reward + discount*state_values[s_next])
                v_s += policy[s][a] * v_a
            new_state_values[s] = v_s
            diff = abs(new_state_values[s] - state_values[s])
            delta = max(delta, diff)

        state_values = new_state_values.copy()
        if delta < 0.001:
            print(f"Policy evaluation finished after {counter} iterations.")
            return state_values


def update_policy(state_values):
    policy = []
    for s in states:
        q_s = [0, 0, 0, 0]
        for a in actions:
            for p, s_next, reward, _ in model[s][a]:
                q_s[a] += p * (reward + discount * state_values[s_next])

        max_q = max(q_s)  # find the maximum q-values
        max_count = len([v for v in q_s if v == max_q]) # number of maximums
        p_new = [1/max_count if v == max_q else 0 for v in q_s]
        policy.append(p_new)

    return policy


# start wit a random policy
policy = [[0.25, 0.25, 0.25, 0.25] for i in states]

while True:
    state_values = policy_evaluation(policy)
    print_state_values(state_values)
    new_policy = update_policy(state_values)
    print(new_policy)
    if new_policy == policy:
        print("Found best policy!")
        exit(0)

    policy = new_policy
