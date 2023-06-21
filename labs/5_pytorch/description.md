# Lab 5

In this lab we will look into the world of deep learning and predict on the
[Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) using PyTorch.

In order to work with the `.ipynb` files, you need to start the jupyter server. 
To do so, execute the following command inside your virtual environment:
```jupyter notebook```
The jupyter server then starts in the background and opens up a new tab in your browser, where you can browse 
the repository and open the `.ipynb` files by clicking on them. Each of these files consists of multiple cells 
containing python code, which can be individually executed.

### Task 1:
Decide, whether you want to use [PyTorch](https://pytorch.org/get-started/locally/) on your local machine 
(should be already installed in your virtual environment) or whether you want to try out 
[Google Colab](https://colab.research.google.com/) (requires a Google account).

### Task 2:
Have a look at the notebook [`code_stub.ipynb`](code_stub.ipynb).
1. Go through the notebook and try to understand what is going on.
2. Make this code run on your machine (or on Google Colab).
2. Play around with the code and observe the effects on the accuracy of the test data:
    - Introduce a second hidden layer with size 5.
    - Change the learning rate to a very low value and a very high value. What is the effect on the training loss?
    - Train a smaller or bigger number of epochs.

### Task 3:
Make a prediction with the trained network on the data point: `[4.9, 3.0, 1.4, 0.2]`.
What are the probabilities for the different classes?
Hint: Since the network outputs raw scores, you need to apply the 
[softmax](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html)
function to normalize the network's output to probabilities.

### Bonus Task (not relevant for exam):
Train a model on the digits dataset and see how accurate you can get
(use https://github.com/pabair/ml-kurs-ss23/blob/main/2_Logistische_Regression_Digits.ipynb as template).
