# Lab 6

In this lab we look into implementations of Deep Q-Networks (DQNs) in PyTorch.

### Task 1:
Check the file [`code_stub.ipynb`](code_stub.ipynb)
which implements a DQN on the [LunarLander](https://gymnasium.farama.org/environments/box2d/lunar_lander/) environment.

1. Execute the code on your machine and watch the recorded video (both training and recording may take quite some time!).
2. Read through the code and then start to understand how the DQN is implemented.
    - Hint 1: Start with section 3 in the notebook, which starts the training process, then go through the dependencies as you read along.
    - Hint 2: Put plenty of `print` statements in the code to see what is insides the variables. Alternatively, try to debug inside the jupyter notebook.
3. Answer the following questions about the code:
    - What dimension is the input and output tensor of the neural network and what does every dimension mean?
        1. In the `act`-method of the client?
        2. In the `learn`-method of the client?
    - How does a state look in this environment?
    - In which cases does the loop in cell 9 terminate?
    - How often is a training step of the network performed?
    - On how many data points is the network trained in one training step?
    - Which role does the `done`-flag play during learning?
    - Which values are contained in the tensor `Q_excpected` in the `learn`-method?
    - What is the role of `eps` and how does it evolve? Plot its value over time.

### Task 2:
Create a new notebook in which you solve the [CartPole](https://gymnasium.farama.org/environments/classic_control/cart_pole/)
environment using a DQN.
- Use the previous notebook as starting point and train until a mean reward of 200 is achieved.
- Play one episode with the trained model and record the outcome.

### Bonus Task (not relevant for exam):
Go through [this](https://pytorch.org/tutorials/intermediate/mario_rl_tutorial.html) tutorial, which shows how to use DQNs for playing Super Mario.


