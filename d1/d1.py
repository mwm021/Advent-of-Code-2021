import pandas as pd
import os
import csv
import numpy as np


def d1_1():
    data = pd.read_csv("input_1.csv", names = ["depth"])
    data["shifted"] = np.where(data["depth"] - data["depth"].shift(1) > 0, 1, 0)
    print(sum(data["shifted"]))

def d1_2():
    data = pd.read_csv("input_1.csv", names = ["depth"])
    data["shifted"] = np.where(data["depth"].rolling(3).sum() - data["depth"].rolling(3).sum().shift(1) > 0, 1, 0)
    print(sum(data["shifted"]))


d1_1()
d1_2()
