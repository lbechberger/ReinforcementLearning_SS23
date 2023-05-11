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

def play_episode(env, policy=None):
    state, _ = env.reset()
    done = False
    total_reward = 0
    states = [state]
    actions = []

    while not done:
        if policy is None or state not in policy:
            action = random.randint(0, no_of_actions-1)  # choose a random action
        else:
            action = policy[state]
        actions.append(action)
        state, reward, done, _, _ = env.step(action)
        states.append(state)
        total_reward += reward

    return states, actions, total_reward

# TASK 1
print("##############")
print("### TASK 1 ###")
print("##############")

count = 0
while True:
    s, a, r = play_episode(env)
    count += 1
    if r > 0:
        break

print(f"Needed {count} episodes, random policy took {len(s)} steps.")
print(f"states: {s}")
print(f"actions: {a}")

policy = {}
for i, v in enumerate(s[:-1]):
    policy[v] = a[i]
print(f"new policy: {policy}")

s, a, r = play_episode(env, policy)
if r > 0:
    print(f"Success: new policy needed {len(s)} steps")
else:
    print(f"New policy failed!")

# TASK 2
print("##############")
print("### TASK 2 ###")
print("##############")
env_8x8 = gym.make("FrozenLake-v1", is_slippery=False, map_name="8x8")

count = 0
while True:
    s, a, r = play_episode(env_8x8)
    count += 1
    if r > 0:
        break

print(f"Converged after {count} episodes")
print(f"Took {len(s)} steps")

policy_8x8 = {}
for i, v in enumerate(s[:-1]):
    policy_8x8[v] = a[i]
print(f"New policy: {policy_8x8}")

s, a, r = play_episode(env_8x8, policy_8x8)
if r > 0:
    print(f"Success! Took {len(s)} steps")
else:
    print(f"Failure!")

# TASK 3
print("##############")
print("### TASK 3 ###")
print("##############")
env_slippery = gym.make("FrozenLake-v1", is_slippery=True)
try:
    s, a, r = play_episode(env_slippery, policy)
    if r > 0:
        print(f"Success! Took {len(s)} steps")
    else:
        print(f"Failure!")
except KeyError as e:
    print(f"unknown state: {e}")