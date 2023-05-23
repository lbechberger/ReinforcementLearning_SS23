# Lab 3

In the third lab, we continue working on the [FrozenLake environment](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/)
and implement the concept of model-free prediction with both the Monte Carlo method and Temporal Differencing.


### Task 1:
- Download and execute `code_stub.py` on GitHub.
This file plays episodes in the 4x4 lake environment using a random policy until a reward is earned.
This is repeated for 100 iterations.
- After every episode, calculate the Q-values with every-visit MC prediction:
    - there is no discount on the reward, i.e. the discount factor gamma is 1.
    - before the first episode, initialize all Q-values to zero.
    - always use the random policy for updating the Q-values
    - use the incremental mean method to update the Q-values, i.e.:
```
Q(s,a) =  Q(s,a) + 1/N(s,a) *  (G-Q(s,a))
```
- After every successful episode, print out the current Q-values.

### Task 2:
Use now the learned Q-values to simulate episodes:

- After every successful episode, in addition to printing the Q-values run 100 episodes using a greedy policy on the current Q-values.
- Print the average reward per episode for those 100 episodes.

### Task 3:
Repeat task 1 and 2, but this time use TD-Prediction for estimating the Q-values.
Use `alpha = 0.01`.
