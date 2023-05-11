# Lab 2

In this second lab we implement the `policy iteration algorithm` that we saw in the lecture, in order to find the best policy for the `FrozenLake` environment.

### Task:
- Use the file `code_stub.py` as a starting point to implement your solution.
- Implement the `policy iteration algorithm` that we saw in the lecture to find the best policy. Use a discount factor of `gamma=1`.
Hint: You can access the transition probability matrix of the environment with `env.env.P` , all states with `env.env.observation_space.n` and all actions with `env.env.action_space.n`. 

The following code shows how you can work with `env.env.P`:

```
tp_matrix = env.env.P
for p, s_next, reward, _ in tp_matrix[s][a]
	print(p)
	print(s_next)
	print(reward)
```

This will give you for a given state `s` and action `a` all possible next states, the transition probability and the associated reward.