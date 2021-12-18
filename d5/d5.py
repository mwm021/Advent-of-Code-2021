import pandas as pd
import os
import csv
import numpy as np
from itertools import cycle
from collections import Counter

def d5_1():
    data = pd.read_csv("input_5.csv", header = None, delimiter = "->", engine = "python")
    data[["x1", "y1"]] = data[0].str.split(",", expand = True).astype(int)
    data[["x2", "y2"]] = data[1].str.split(",", expand = True).astype(int)
    data = data.drop(columns = [0, 1])
    data = data[(data["x1"] == data["x2"]) | (data["y1"] == data["y2"])]

    tuples = []

    for index, row in data.iterrows():
        if row["x2"] > row["x1"]:
            xrange = [*range(row["x1"], row["x2"] + 1)]
        else:
            xrange = [*range(row["x2"], row["x1"] + 1)]
        if row["y2"] > row["y1"]:
            yrange = [*range(row["y1"], row["y2"] + 1)]
        else:
            yrange = [*range(row["y2"], row["y1"] + 1)]

        if len(xrange) > len(yrange):
            tuples.extend(list(zip(xrange, cycle(yrange))))
        if len(xrange) < len(yrange):
            tuples.extend(list(zip(cycle(xrange), yrange)))

    tuples = [str(item) for item in tuples]
    frequency = {}

    for item in tuples:
       if item in frequency:
          frequency[item] += 1
       else:
          frequency[item] = 1

    freq_df = pd.DataFrame.from_dict(frequency, orient = "index", columns = ["count"])
    print(len(freq_df[freq_df["count"] > 1]))

def getType(x1, x2, y1, y2):
    if x1 == x2:
        return "vertical"
    if y1 == y2:
        return "horizontal"
    else:
        return "diagonal"

def d5_2():
        data = pd.read_csv("input_5.csv", header = None, delimiter = "->", engine = "python")
        data[["x1", "y1"]] = data[0].str.split(",", expand = True).astype(int)
        data[["x2", "y2"]] = data[1].str.split(",", expand = True).astype(int)
        data = data.drop(columns = [0, 1])
        data["type"] = data.apply(lambda row: getType(row["x1"], row["x2"], row["y1"], row["y2"]), axis = 1)

        tuples = []

        for index, row in data.iterrows():
            if row["type"] != "diagonal":
                if row["x2"] > row["x1"]:
                    xrange = [*range(row["x1"], row["x2"] + 1)]
                else:
                    xrange = [*range(row["x2"], row["x1"] + 1)]
                if row["y2"] > row["y1"]:
                    yrange = [*range(row["y1"], row["y2"] + 1)]
                else:
                    yrange = [*range(row["y2"], row["y1"] + 1)]
                if len(xrange) > len(yrange):
                    tuples.extend(list(zip(xrange, cycle(yrange))))
                if len(xrange) < len(yrange):
                    tuples.extend(list(zip(cycle(xrange), yrange)))
            if row["type"] == "diagonal":
                if row["x2"] > row["x1"]:
                    xrange = [*range(row["x1"], row["x2"] + 1)]
                else:
                    xrange = [*range(row["x1"], row["x2"] - 1, -1)]
                if row["y2"] > row["y1"]:
                    yrange = [*range(row["y1"], row["y2"] + 1)]
                else:
                    yrange = [*range(row["y1"], row["y2"] - 1, -1)]
                tuples.extend(list(zip(xrange, yrange)))


        tuples = [str(item) for item in tuples]
        frequency = {}

        for item in tuples:
           if item in frequency:
              frequency[item] += 1
           else:
              frequency[item] = 1

        freq_df = pd.DataFrame.from_dict(frequency, orient = "index", columns = ["count"])
        print(len(freq_df[freq_df["count"] > 1]))

d5_1()
d5_2()
