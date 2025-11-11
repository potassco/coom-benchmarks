#!/usr/bin/env python

import os
from glob import glob
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tikzplotlib
from pandas_ods_reader import read_ods

RESULTS = "results/all.ods"
OUTDIR = "plots"

SOLVER = ["clingo", "flingo"]
DOMAIN = ["core", "city", "travel"]

GREEN = "#77B762"
BLUE = "#4477CC"
RED = "#CF3A19"
PURPLE = "#5C4B84"
PURPLE_LIGHT = "#9477BF90"
ORANGE = "#D78C1F"
YELLOW = "#D7CF1F"
GREENBLUE = "#226367"

COLOR = {"core": GREEN, "city": BLUE, "travel": RED, "restaurant": YELLOW}
MARKER = {"core": "D", "city": "o", "travel": "x", "restaurant": "s"}  # , "*", "+"]

LABEL = {
    "core": "Core",
    "city": "CityBikeFleet",
    "travel": "TravelBikeFleet",
    "restaurant": "Restaurant",
}


def clean_df(df):
    # Remove last computed values
    df.drop(df.tail(9).index, inplace=True)

    # Get stats
    stats_set = set(df.iloc[0][:])
    stats_set.discard("")
    stats_set.discard(None)

    # Drop min max median
    df.drop(df.columns[-3 * len(stats_set) :], axis=1, inplace=True)

    stats = df.iloc[0, 1 : len(stats_set) + 1].values

    # Get solvers and reasoning modes
    solvers = [
        c.split("/")[-1] for i, c in enumerate(df.columns) if i % len(stats) == 1
    ]

    # Get instances
    instances = [i.replace("./", "") for i in df.iloc[1:, 0]]

    # Create multi index for columns
    columns = pd.MultiIndex(
        levels=[solvers, stats],
        codes=[
            np.repeat(range(len(solvers)), len(stats)).tolist(),
            list(range(len(stats))) * len(solvers),
        ],
    )

    # Get data
    data = df.iloc[1:, 1:].values  # needed? convert_dtypes()

    # # Remove first column
    # df.drop(df.columns[0], axis=1, inplace=True)

    # # Get columns
    # solvers = [
    #     c.split("/")[-1] for i, c in enumerate(df.columns) if i % len(stats) == 0
    # ]

    # Get instance names
    # df[df.columns[0]] = df[df.columns[0]].apply(lambda x: x[2:].replace(".coom", ""))
    # df[df.columns[0]] = df[df.columns[0]].apply(lambda x: x[2:].replace("./", ""))

    # Make instances names index of dataframe
    # df.index = df.loc[:, df.columns[0]].tolist()

    # df.columns = list(np.repeat(solvers, len(stats)))
    # df.columns = [f"{c}-{s}" for c, s in zip(df.columns, list(df.iloc[0]))]

    return pd.DataFrame(index=instances, columns=columns, data=data)


def get_subdf(df, solver):
    # subdf = df.filter(like=domain, axis=0).filter(regex=f"^{solver}", axis=1)
    subdf = df.filter(regex=f"^{solver}", axis=1)
    # subdf.rename(columns=lambda x: x.split("-")[1], inplace=True)
    return subdf.rename(columns=lambda x: x.replace(f"{solver}-", ""))


def get_plot_data(df, type):
    runtimes = df["time"]
    if type == "cactus":
        y = np.insert(runtimes.sort_values().to_numpy(), 0, 0)
        x = np.arange(len(y + 1)) * (100 / (len(y) - 1))
    # elif domain == "citybike":
    #     y = runtimes.to_numpy()
    #     # x = np.arange(1, len(y) + 1)
    #     x = [int(n.replace("citybike-n", "")) for n in df.index.tolist()]
    return x, y


def get_label(solver, domain):
    return f"{TITLE[domain]}-{solver}"


def plot(dfs):
    outpath = os.path.join(OUTDIR, "all.pdf")

    plots = {}
    for sd in dfs.keys():
        s, d = sd.split("-")
        x, y = get_plot_data(dfs[sd], type="cactus")
        (plots[sd],) = plt.plot(
            x,
            y,
            ls="-" if s == "clingo" else "--",
            color=COLOR[d],
            lw=1,
            marker=MARKER[d],
            markevery=0.2,
            ms=3,
            label=(sd),
        )

    plt.xlim(min(x), 15)

    clingo_legend = plt.legend(
        handles=[plots[f"clingo-{d}"] for d in DOMAIN],
        labels=[LABEL[d] for d in DOMAIN],
        loc="upper center",
        prop={"style": "italic"},
        title="clingo",
        title_fontproperties={"weight": "bold"},
        alignment="left",
    )
    plt.gca().add_artist(clingo_legend)

    plt.legend(
        handles=[plots[f"flingo-{d}"] for d in DOMAIN],
        labels=[LABEL[d] for d in DOMAIN],
        loc="center",
        bbox_to_anchor=(0.5, 0.6),
        prop={"style": "italic"},
        title="flingo",
        title_fontproperties={"weight": "bold"},
        alignment="left",
    )

    # plt.legend(loc="upper right")
    # plt.gca().yaxis._set_scale("log")
    # plt.title("Benchmarks", fontsize=12, fontweight=0)

    # if domain in ("randomcore", "restaurant", "travelbike"):
    plt.xlabel("% of instances solved")
    plt.ylim(bottom=0, top=200)
    plt.xticks(np.arange(0, 110, 10))

    # plt.gca().xaxis.get_major_locator().set_params(integer=True)
    # elif domain == "citybike":
    #     plt.ylim(bottom=0, top=650)
    #     plt.xlabel("#Bikes")

    plt.ylabel("Runtime (s)")

    # tikzplotlib.save(outpath)

    plt.savefig(outpath, dpi=1200, bbox_inches="tight")
    print(f"Saved {outpath}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    # ods_paths = glob(f"{RESULTS_DIR}/all.ods")
    results = clean_df(read_ods(RESULTS))
    print(results)

    # all_dfs = {
    #     f"{s}-{d}": get_subdf(dfs[d], solver=s) for s, d in product(SOLVER, dfs.keys())
    # }

    # plot(all_dfs)
