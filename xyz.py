import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('bpp_training_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)