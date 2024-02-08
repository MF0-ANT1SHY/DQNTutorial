"""
 # @ Author: Shuo YANG
 # @ Create Time: 2024-02-08 18:40:47
 # @ Modified by: Shuo YANG
 # @ Modified time: 2024-02-08 18:43:11
 """

from tkinter import W
import gymnasium as gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple, deque
from itertools import count

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

env = gym.make("CartPole-v1")

print(env.action_space.n)  # type: ignore
