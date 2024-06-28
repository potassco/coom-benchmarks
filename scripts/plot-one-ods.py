#!/usr/bin/env python

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas
from pandas_ods_reader import read_ods

RESULTS_DIR = "benchmarks/results"
ODS_FILE = "evaluated.ods"
OUTDIR = "benchmarks/plots"

SOLVER = [
    "clingo-n1",
    "fclingo-n1",
    "clingo-n10",
    "fclingo-n10",
    "clingo-n30",
    "fclingo-n30",
]
DOMAIN = ["citybike"]  # [citybike", "travelbike", "restaurant", "randomcore"]


GREEN = "#77B762"
BLUE = "#4477CC"
RED = "#CF3A19"
PURPLE = "#5C4B84"
PURPLE_LIGHT = "#9477BF90"
ORANGE = "#D78C1F"
YELLOW = "#D7CF1F"
GREENBLUE = "#226367"

COLORS = [GREEN, BLUE, RED, PURPLE, ORANGE, YELLOW]
MARKERS = ["D", "o", "x", "s", "*", "+"]

TITLE = {
    "randomcore": "Random COOM core",
    "citybike": "City Bike Fleet",
    "travelbike": "Travel Bike Fleet",
    "restaurant": "Restaurant",
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
    # subdf.rename(columns=lambda x: x.split("-")[1], inplace=True)
    subdf.rename(columns=lambda x: x.replace(f"{solver}-", ""), inplace=True)
    return subdf


def get_plot_data(df, domain):
    runtimes = df["time"]
    if domain in ("randomcore", "restaurant", "travelbike"):
        y = runtimes.sort_values().to_numpy()
        x = np.arange(len(y))
    elif domain == "citybike":
        y = runtimes.to_numpy()
        # x = np.arange(1, len(y) + 1)
        x = [int(n.replace("citybike-n", "")) for n in df.index.tolist()]
    return x, y


def plot(dfs, domain):
    outfile = f"{domain}.pdf"
    outpath = os.path.join(OUTDIR, outfile)

    for i, s in enumerate(dfs.keys()):
        if domain in ("randomcore", "restaurant", "travelbike", "all"):
            marker = "none"
        elif domain == "citybike":
            marker = MARKERS[i]

        x, y = get_plot_data(dfs[s], domain)
        plt.plot(
            x,
            y,
            ls="solid",
            color=COLORS[i],
            lw=1,
            marker=marker,
            ms=3,
            label=s,
        )

    plt.xlim(min(x))

    plt.legend()
    plt.title(f"{TITLE[domain]}", fontsize=12, fontweight=0)

    if domain in ("randomcore", "restaurant", "travelbike"):
        plt.xlabel("#Instances solved")
        plt.ylim(bottom=0, top=650)
        plt.gca().xaxis.get_major_locator().set_params(integer=True)
    elif domain == "citybike":
        plt.ylim(bottom=0, top=650)
        plt.xlabel("#Bikes")
        plt.xticks(x)

    plt.ylabel("Runtime (s)")

    plt.savefig(outpath, dpi=300, bbox_inches="tight")
    print(f"Saved {outpath}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    ods_path = os.path.join(RESULTS_DIR, ODS_FILE)
    df = read_ods(ods_path)

    df = clean_df(df)
    print(df)
    # plot(df,"all")

    # for d in DOMAIN:
    #     sub_dfs = {s: get_subdf(df, domain=d, solver=s) for s in SOLVER}
    #     print(sub_dfs)
    #     plot(sub_dfs, d)
