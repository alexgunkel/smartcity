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
    barWidth = 0.25
    m = Mission()
    res = extract_listings(m)
    categories = res.keys()
    cities = list(res.values())[0].keys()
    to_plot = dict()
    for city in cities:
        to_plot[city] = []
        for c in categories:
            to_plot[city].append(res[c][city]["2022"])

    pDD = np.arange(len(categories))
    pLE = [x + barWidth for x in pDD]
    pCH = [x + barWidth for x in pLE]

    plt.bar(pDD, to_plot["Dresden"], color='#ff0000', width=barWidth, edgecolor='white', label='Dresden')
    plt.bar(pLE, to_plot["Leipzig"], color='#00ff00', width=barWidth, edgecolor='white', label='Leipzig')
    plt.bar(pCH, to_plot["Chemnitz"], color='#0000ff', width=barWidth, edgecolor='white', label='Chemnitz')

    plt.xlabel('Kategorie')
    plt.xticks([r + barWidth for r in range(len(categories))], categories)
    plt.legend()
    plt.show()
    print(to_plot)


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
