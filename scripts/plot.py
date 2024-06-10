#!/usr/bin/env python

# from cProfile import label
import itertools
import math
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import seaborn as sns
from pandas_ods_reader import read_ods

# import scipy
# from scipy import stats
# import re
# import tikzplotlib

RESULTS_DIR = "benchmarks/results"
ODS_FILE = "evaluated.ods"
OUTDIR = "benchmarks/plots"

SOLVER = ["clingo", "fclingo"]
DOMAIN = ["kidsbike", "citybike", "travelbike", "restaurant"]


GREEN = "#77B762"
BLUE = "#4477CC"
RED = "#CF3A19"
PURPLE = "#5C4B84"
PURPLE_LIGHT = "#9477BF90"
ORANGE = "#D78C1F"
YELLOW = "#D7CF1F"
GREENBLUE = "#226367"
COLORS = {
    "clingo": BLUE,
    "fclingo": RED,
}


def clean_df(df):
    stats_set = set(df.iloc[0][:])
    stats_set.discard("")

    # Drop min max median
    df.drop(df.columns[-3 * len(stats_set) :], axis=1, inplace=True)

    # Remove last computed values
    df.drop(df.tail(9).index, inplace=True)

    # Rename instances
    df[df.columns[0]] = df[df.columns[0]].apply(lambda x: x[2:].replace(".coom", ""))

    # Make instances names index of dataframe
    df.index = df.loc[:, df.columns[0]].tolist()

    # Remove first column
    df.drop(df.columns[0], axis=1, inplace=True)

    # Rename columns
    solver = [
        c.split("/")[-1] for i, c in enumerate(df.columns) if i % len(stats_set) == 0
    ]
    df.columns = list(np.repeat(solver, len(stats_set)))
    df.columns = [f"{c}-{s}" for c, s in zip(df.columns, list(df.iloc[0]))]

    # Remove unused out values
    df.drop(df.index[0], inplace=True)

    # Convert datatypes
    df = df.convert_dtypes()

    return df


def get_subdf(df, domain, solver):
    subdf = df.filter(like=domain, axis=0).filter(regex=f"^{solver}", axis=1)
    subdf.rename(columns=lambda x: x.split("-")[1], inplace=True)
    return subdf


def get_plot_data(df, domain):
    runtimes = df["time"]

    if domain in ("kidsbike", "restaurant"):
        y = runtimes.sort_values().to_numpy()
        x = np.arange(len(y))
    elif domain in ("citybike", "travelbike"):
        y = runtimes.to_numpy()
        print(y)
        x = np.arange(len(y))
    return x, y


def plot(dfs, domain):
    outfile = f"{domain}.pdf"
    outpath = os.path.join(OUTDIR, outfile)

    for s in dfs.keys():
        x, y = get_plot_data(dfs[s], domain)
        plt.plot(
            x,
            y,
            ls="solid",
            color=COLORS[s],
            lw=1,
            # marker=approaches_markers[name],
            ms=3,
            label=s,
        )

    plt.xlim(left=0)
    plt.ylim(bottom=0, top=600)

    plt.legend()
    plt.title(f"{domain}", fontsize=12, fontweight=0)
    plt.xlabel("Instances solved")
    plt.ylabel("Runtime (s)")
    # if args.range is not None:
    #     tr = [int(i) for i in args.range.split(',')]
    #     plt.xticks(list(range(tr[0], tr[1], tr[2])))
    # # plt.xticks(ticks=ticks_num, labels=ticks_label)
    # # plt.xticks(list(range(0,3000,500)))

    plt.savefig(outpath, dpi=300, bbox_inches="tight")
    print(f"Saved {outpath}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    ods_path = os.path.join(RESULTS_DIR, ODS_FILE)
    df = read_ods(ods_path)
    df = clean_df(df)

    for d in DOMAIN:
        sub_dfs = {s: get_subdf(df, domain=d, solver=s) for s in SOLVER}
        plot(sub_dfs, d)
