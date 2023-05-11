# Lab 1

In this first lab we play around with the [FrozenLake environment](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/) and try to learn a good policy from experience.
Take a look at the file `code_stub.py` to have a starting point for the following tasks:

### Task 1:
- Write a helper function `def play_episode(env, policy=None)` to play an entire episode in the environment `env`, using the given `policy` (if `policy` is `None`, use a random policy -- in that case, `rand_int` is your friend).
- Run episodes using a random policy until the agent reaches the goal (total reward for that episode > 0).
- Print how many runs it took to create a successful episode.
- Remember the states and actions that were taken in this episode. How many actions did it take to reach the goal?
- Given these results, write an algorithm that generates a minimal policy, which reaches the goal faster.
- Run one episode using this new policy and compare the results: was it successful? how many steps did it take?

### Task 2:
- Increase the map size using the 8x8 env:
 `env_8x8 = gym.make("FrozenLake-v1", is_slippery=False, map_name="8x8")`
- Compare the results to task 1.

### Task 3:
- Use the learned policy from Task 1 and execute it in an 4x4 environment that is slippery:
`env_slippery = gym.make("FrozenLake-v1", is_slippery=True)`
- What is the problem with the learned policy?
- How can we learn a good policy in such an environment?
