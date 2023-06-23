# Lab 6 - Solution


- What dimension is the input and output tensor of the neural network and what does every dimension mean?
    1. In the `act`-method of the client?
    > [1, 8] und [1, 4]; 1 = Size of the batch: one data point; 8 = Size of the State array, 4 = Number of actions
    2. In the `learn`-method of the client?
    > [64, 8] und [64, 4]; 64 = Size of the batch: 64 data points; 8 = Size of the State array, 4 = Number of actions
- How does a state look in this environment?
> A vector of size 8
- In which cases does the loop in cell 9 terminate?
> `MAX_EPISODES` reached OR `mean_score >= 200`
- How often is a training step of the network performed?
> every `UPDATE_EVERY=4` time steps
- On how many data points is the network trained in one training step?
> `BATCH_SIZE = 64`
- Which role does the `done`-flag play during learning?
> if `done == 1`, then `rewards + (GAMMA * max_action_values * (1 - dones))` is zero
> i.e. in the last step before the episode is done, only the reward is considered
- Which values are contained in the tensor `Q_excpected` in the `learn`-method?
> The currently predicted Q-values from the network for every action
- What is the role of `eps` and how does it evolve? Plot its value over time.
> It starts with `EPS_START=1` and decreases every episode by factor `EPS_DECAY=0.99` until it reaches `EPS_MIN=0.01


