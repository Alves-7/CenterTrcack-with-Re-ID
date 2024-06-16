# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 08:45:37 2021

@author: Alves
"""
import numpy as np
from numpy import random
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns
sns.set()


N = 20
R = random.randn(N, N)

fig = plt.figure()
sns_plot = sns.heatmap(R)
# fig.savefig("heatmap.pdf", bbox_inches='tight') # 减少边缘空白
plt.show()
