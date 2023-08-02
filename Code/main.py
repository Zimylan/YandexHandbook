import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data_table = [
    ["id", "Name", "Age", "Work"],
    [1, 'Sandy', 21, "Doctor"],
    [2, "Mandy", 32, "Lector"],
    [3, "Carl", 33, "Driver"],
    [4, "Mars", 100, "God of war"],
    [5, "Kris", 12, "Not working"],
]
data = ""
for i in data_table:
    for j in i:
        if j != i[-1]:
            data += str(j) + ","
        else:
            data += str(j) + "\n"


with open("data_test.csv", "w") as file:
    file.write(data)