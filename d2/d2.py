import pandas as pd
import os
import csv
import numpy as np


def d2_1():
    data = pd.read_csv("input_2.csv", delimiter = " ", names = ["direction", "amount"])
    data["amount"] = np.where(data["direction"] == "up", -1 * data["amount"], data["amount"])
    data["movement_type"] = np.where(data["direction"] == "forward", "horizontal", "vertical")
    vertical = data[data["movement_type"] == "vertical"]["amount"].sum()
    horizontal = data[data["movement_type"] == "horizontal"]["amount"].sum()
    print(vertical * horizontal)

def d2_2():
    data = pd.read_csv("input_2.csv", delimiter = " ", names = ["direction", "amount"])
    data["amount"] = np.where(data["direction"] == "up", -1 * data["amount"], data["amount"])
    data["movement_type"] = np.where(data["direction"] == "forward", "horizontal", "vertical")

    data["aim"] = data[data["movement_type"] == "vertical"]["amount"].cumsum()
    data["aim"] = data["aim"].ffill()
    data["additional"] = np.where(data["movement_type"] == "horizontal", data["amount"] * data["aim"], 0)
    
    vertical = data["additional"].sum()
    horizontal = data[data["movement_type"] == "horizontal"]["amount"].sum()
    print(int(vertical * horizontal))


d2_1()
d2_2()
