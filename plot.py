#!/usr/bin/env python

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import tikzplotlib
from pandas_ods_reader import read_ods

# from glob import glob
# from itertools import product
# from pathlib import Path


RESULTS = "results/all.ods"
OUTDIR = "results/plots"

SOLVER = ["clingo", "flingo"]
DOMAIN = ["core", "citybike", "travelbike", "restaurant", "box"]

GREEN = "#77B762"
BLUE = "#4477CC"
RED = "#CF3A19"
PURPLE = "#5C4B84"
PURPLE_LIGHT = "#9477BF90"
ORANGE = "#D78C1F"
YELLOW = "#D7CF1F"
GREENBLUE = "#226367"

COLOR = {
    "core": GREEN,
    "citybike": BLUE,
    "travelbike": RED,
    "restaurant": YELLOW,
    "box": ORANGE,
}
MARKER = {
    "core": "D",
    "citybike": "o",
    "travelbike": "x",
    "restaurant": "s",
    "box": "*",
}  # , "+"]

LABEL = {
    "core": "Core",
    "citybike": "CityBikeFleet",
    "travelbike": "TravelBikeFleet",
    "restaurant": "Restaurant",
    "box": "Box",
}
LINE = {
    "clingo": "-",
    "flingo": "--",
    "clingo-cautious": "-",
    "clingo-brave": "--",
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
    instances = [i.replace("./", "").split("-") for i in df.iloc[1:, 0]]
    instances = pd.MultiIndex.from_tuples(instances)

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

    return pd.DataFrame(index=instances, columns=columns, data=data)


def get_plot_data(df, type):
    if type == "cactus":
        y = np.insert(df.sort_values().to_numpy(), 0, 0)
        x = np.arange(len(y + 1)) * (100 / (len(y) - 1))
    # elif domain == "citybike":
    #     y = runtimes.to_numpy()
    #     # x = np.arange(1, len(y) + 1)
    #     x = [int(n.replace("citybike-n", "")) for n in df.index.tolist()]
    return x, y


def plot(df, pairs, outfile, type="cactus"):
    outpath = os.path.join(OUTDIR, outfile)

    plots = {}
    for s, d in pairs:
        name = f"{s}-{d}"
        x, y = get_plot_data(df[s, "time"][d], type)
        (plots[name],) = plt.plot(
            x,
            y,
            ls=LINE[s],
            color=COLOR[d],
            lw=1,
            marker=MARKER[d],
            markevery=0.2,
            ms=3,
            label=(name),
        )

    plt.xlim(min(x), 15)

    if outfile == "singlemodel.pdf":
        clingo_legend = plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "clingo"],
            labels=[LABEL[d] for s, d in pairs if s == "clingo"],
            loc="upper center",
            prop={"style": "italic"},
            title="clingo",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(clingo_legend)

        plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "flingo"],
            labels=[LABEL[d] for s, d in pairs if s == "flingo"],
            loc="center",
            bbox_to_anchor=(0.5, 0.55),
            prop={"style": "italic"},
            title="flingo",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )

    if outfile == "cautiousbrave.pdf":
        cautious_legend = plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "clingo-cautious"],
            labels=[LABEL[d] for s, d in pairs if s == "clingo-cautious"],
            loc="upper center",
            prop={"style": "italic"},
            title="clingo cautious",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(cautious_legend)

        plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "clingo-brave"],
            labels=[LABEL[d] for s, d in pairs if s == "clingo-brave"],
            loc="center",
            bbox_to_anchor=(0.5, 0.54),
            prop={"style": "italic"},
            title="clingo brave",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
    # plt.legend(loc="upper right")
    # plt.gca().yaxis._set_scale("log")
    # plt.title("Benchmarks", fontsize=12, fontweight=0)

    # if domain in ("randomcore", "restaurant", "travelbike"):
    plt.xlabel("% of instances solved")
    plt.ylim(bottom=0, top=20)
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

    # Plot clingo and flingo for getting single model
    plot(
        results,
        [
            ("clingo", "box"),
            ("clingo", "citybike"),
            ("clingo", "restaurant"),
            ("clingo", "travelbike"),
            ("flingo", "citybike"),
            ("flingo", "restaurant"),
            ("flingo", "travelbike"),
        ],
        "singlemodel.pdf",
        type="cactus",
    )

    # Plot clingo cautious and brave
    plot(
        results,
        [
            ("clingo-brave", "box"),
            ("clingo-brave", "citybike"),
            ("clingo-brave", "restaurant"),
            ("clingo-brave", "travelbike"),
            ("clingo-cautious", "box"),
            ("clingo-cautious", "citybike"),
            ("clingo-cautious", "restaurant"),
            ("clingo-cautious", "travelbike"),
        ],
        "cautiousbrave.pdf",
        type="cactus",
    )
