# Lab 1

In this first lab we play around with the [FrozenLake environment](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/) and try to learn a good policy from experience.
Take a look at the file `1_FrozenLake_Random.py` to have a starting point for the following tasks:

### Task 1:
- Run episodes using a random policy until the agent reaches the goal (reward > 0).
- Print how many runs it took to create a successful episode.
- Remember the states and actions that were taken in this episode. How many actions did it take to reach the goal?
- Given these results, write an algorithm that generates a policy that reaches the goal faster.
- Run one episode using this new policy and compare the results.

### Task 2:
- Increase the map size using the 8x8 env:
 `env_8x8 = gym.make("FrozenLake-v1", is_slippery=False, map_name="8x8")`
- Compare the results to task 1.

### Task 3:
- Use the learned policy from Task 1 and execute it in an 4x4 environment that is slippery:
`env_slippery = gym.make("FrozenLake-v1", is_slippery=True)`
- What is the problem with the learned policy?
- How can we learn a good policy in such an environment?
