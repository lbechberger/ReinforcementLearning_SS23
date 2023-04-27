# Lab 0

Note: This lab is not relevant for the exam, but important to get you more familiar with the concepts in Python.

Open the file `code_stub.py` and execute it (either in PyCharm or on the command line with `python labs/0_tic_tac_toe/code_stub.py`).
It implements a tic tac toe game, in which the human player uses a "x" symbol and the computer
player uses "o". Whoever has first three of its symbols in a row wins
(rows can be horizontal, vertical or diagonal).

In the current state, the game is not complete.
Your task is to finish the steps, which are marked with "Task" to finish the implementation of the game:
- update the board state, if a correct position was given (print error message otherwise)
- decide, whether the game is over and print out who won
- implement a simple strategy for the computer player (hint: use randint() in combination with update_board())
