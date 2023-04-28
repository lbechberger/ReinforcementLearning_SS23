# Course: Introduction to Reinforcement Learning

Code and exercises from the lecture "Introduction to Reinforcement Learning" held in the summer term 2023 at H-KA.

This repository is heavily based on analogous repositories for this 
course by Prof. Patrick Baier (https://github.com/pabair) in previous 
semesters.

## Setup

The recommended way to set up your development environment is to use Conda inside PyCharm.
1. Download and install Miniconda for your OS from here: 
[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).
2. Download and install PyCharm Community Edition from here: 
[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
3. Follow these instructions to create a virtual environment named `rl-course` with Python 3.8: 
[https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html)
4. Use the PyCharm package installer 
(see [https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)) 
to install the following packages, making sure that you use "conda" to install them 
(alternatively, open the virtual environment with `conda activate rl-course` and then install them 
by executing `conda install <package-name>`):
    1. gymnasium
    2. pandas
    3. matplotlib
    4. scikit-learn
    5. jupyter
    6. pytorch

You can test your setup by running the file `labs/1_AI_gym_intro/code_stub.py` (either from PyCharm, by opening the file and 
clicking the run button, or by opening the conda terminal, activating the environment, and executing `labs/1_AI_gym_intro/code_stub.py`).

## Structure

The files in this repository are structured into the following folders:
- `python_intro` contains the code snippets shown in the python crash course as well as exemplary solutions 
for the four tasks.
- `labs` contains for each lab (i.e., practical part of the lecture) a description (as markdown file), 
the code stub to start with, as well as the solutions.