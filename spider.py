import csv
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import argparse as ap
from pathlib import Path


class Arguments:
    def __init__(self):
        parser = ap.ArgumentParser()
        parser.add_argument('file')
        args = parser.parse_args()
        self.theme = Path(args.file).stem
        self.file = open(args.file)


def read_file(arguments: Arguments):
    r = csv.DictReader(arguments.file)
    for row in r:
        city = row["Stadt"]
        del row["Stadt"]
        year = row["Jahr"]
        del row["Jahr"]
        fig = build_figure(row)
        fig.write_image('./build/' + arguments.theme + '_' + city + '_' + year + '.jpg')


def build_figure(row):
    df = pd.DataFrame(dict(
        r=map(float, row.values())
    ))
    fig = px.line_polar(df, r='r', theta=row.keys(), line_close=True, range_r=[0, 100])
    return fig


def main():
    args = Arguments()
    read_file(args)


if __name__ == '__main__':
    main()
