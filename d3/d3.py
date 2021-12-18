import pandas as pd
import os
import csv
import numpy as np


def d3_1():
    data = pd.read_csv("input_3.csv", names = ["values"])
    data["values"] = data["values"].astype(str).apply(lambda x: x.zfill(len(str(max(data["values"])))))
    data = data["values"].str.extractall('(.)').unstack()
    data = data.astype(int)
    gamma = "".join(data.median(axis = 0).astype(int).astype(str).tolist())
    epsilon = "".join(['1' if i == '0' else '0' for i in gamma])
    print(int(gamma, 2) * int(epsilon, 2))

def d3_2():
    data = pd.read_csv("input_3.csv", names = ["values"])
    data["values"] = data["values"].astype(str).apply(lambda x: x.zfill(len(str(max(data["values"])))))
    data = data["values"].str.extractall('(.)').unstack()
    data = data.astype(int)

    oxygen = get_value(data, "oxygen")
    CO2 = get_value(data, "CO2")

    print(oxygen * CO2)

def get_value(data, type):
    if type == "oxygen":
        for col in data.columns:
            stat = data[col].value_counts()
            if len(data) == 1:
                return int("".join(data.astype(str).values.tolist()[0]), 2)
            elif len(data) == 2:
                if data.iloc[0][col] == data.iloc[1][col]:
                    continue
                else:
                    return int("".join(data[data[col] == 1].astype(str).values.tolist()[0]), 2)
            else:
                if stat[1] < stat[0]:
                    data = data[data[col] == 0]
                else:
                    data = data[data[col] == 1]

    if type == "CO2":
        for col in data.columns:
            stat = data[col].value_counts()
            if len(data) == 1:
                return int("".join(data.astype(str).values.tolist()[0]), 2)
            elif len(data) == 2:
                if data.iloc[0][col] == data.iloc[1][col]:
                    continue
                else:
                    return int("".join(data[data[col] == 0].astype(str).values.tolist()[0]), 2)
            else:
                if stat[1] < stat[0]:
                    data = data[data[col] == 1]
                else:
                    data = data[data[col] == 0]



d3_1()
d3_2()
