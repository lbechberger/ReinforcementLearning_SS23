# Lab 4

In this lab, we will continue our work on the [FrozenLake environment](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/) by introducing MC-Control, SARSA and Q-learning.


### Task 1:
In the last lab, we calculated Q-values using MC prediction. We will now extend this code to implement MC control as we have seen it in the lecture:

- Take the code from the file [code_stub.py](code_stub.py) as starting point.
This code uses a random policy and plots the collected rewards over time (x-axis: number of episodes, y-axis: cumulative reward summed over the first x episodes).
- Integrate the code for calculating Q-values after every episode [from the last lab](../3_model_free_prediction/solution_task_1.py).
- Change the `play_episode` method, such that it uses an epsilon-greedy policy based on the current Q-values.
- Try out the following epsilons: `[0.01, 0.1, 0.5, 1.0]` (where `epsilon = 1.0` corresponds to an entire random policy) and show all results for all epsilons together in one plot (i.e. every epsilon one curve in the plot).

### Task 2:
Implement now SARSA as comparison control strategy:

- Redo task 1 using SARSA instead of MC (use `alpha=0.5`).
- As above, try out the different epsilons and compare them in one plot.


### Task 3:
Implement now Q-learning as comparison control strategy:

- Redo task 1 using Q-Learning (use `alpha=0.5`).
- As above, try out the different epsilons and compare them in one plot.
