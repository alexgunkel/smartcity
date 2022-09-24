#!/usr/bin/env python3

import argparse as ap
from pathlib import Path
from csv import DictReader
import numpy as np
import matplotlib.pyplot as plt


class Mission:
    def __init__(self):
        parser = ap.ArgumentParser()
        parser.add_argument("path", type=Path)
        given = parser.parse_args()
        self.path = given.path
        if not self.path.is_dir():
            raise Exception(self.path + " is not a directory")
        self.files = [x.resolve() for x in self.path.iterdir()]


def main():
    barWidth = 0.15
    m = Mission()
    res = extract_listings(m)
    categories = res.keys()
    cities = list(res.values())[0].keys()
    to_plot = dict()
    for cat in categories:
        to_plot[cat] = []
        for city in cities:
            to_plot[cat].append(81-int(res[cat][city]["2022"]))
    X = np.arange(len(cities))
    idx = 0
    for cat in categories:
        plt.bar(X + (idx*barWidth), to_plot[cat], width=barWidth, edgecolor='white', label=cat)
        idx += 1
    plt.xlabel('Stadt')
    plt.xticks(X + (barWidth*len(categories)/2), cities)
    plt.legend()
    plt.show()


def extract_listings(m):
    res = dict()
    for file in m.files:
        res[file.stem] = dict()
        reader = DictReader(file.open())
        for row in reader:
            if row["Stadt"].strip() not in res[file.stem].keys():
                res[file.stem][row["Stadt"].strip()] = dict()
            res[file.stem][row["Stadt"].strip()][row["Jahr"].strip()] = row["Platz"]
    return res


if __name__ == "__main__":
    main()
