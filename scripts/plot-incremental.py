#!/usr/bin/env python

import os
from argparse import ArgumentParser
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import read_excel
from utils import COLORS, LABEL, clean_df, get_plot_data, make_legend

OUTDIR = "results/plots/incremental"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()

SOLVER = [
    "clingo-base",
    "flingo-base",
    "clingo-bounds-linear",
    "clingo-bounds-exponential",
    "flingo-bounds-linear",
    "flingo-bounds-exponential",
    "multishot-linear",
    "multishot-exponential",
]
COLOR = {
    "clingo-base": COLORS["lightgreen"],
    "flingo-base": COLORS["lightblue"],
    "clingo-bounds-linear": COLORS["green"],
    "flingo-bounds-linear": COLORS["blue"],
    "clingo-bounds-exponential": COLORS["green"],
    "flingo-bounds-exponential": COLORS["blue"],
    "multishot-linear": COLORS["red"],
    "multishot-exponential": COLORS["red"],
}

MARKER = {
    "core": "D",
    "citybike": "o",
    "travelbike": "x",
    "restaurant": "s",
    "spacecollider": "<",
    "metro": "1",
    "box": "*",
    "cargobike": "D",
    "racks": "o",
    "house": "x",
}  # , "+"]


LINE = {
    "clingo-base": "-.",
    "flingo-base": "-.",
    "clingo-bounds-linear": "-",
    "flingo-bounds-linear": "-",
    "clingo-bounds-exponential": "--",
    "flingo-bounds-exponential": "--",
    "multishot-linear": "-",
    "multishot-exponential": "--",
}


def plot(df, domain, style="cactus"):
    """
    Plots the specified plot.
    """
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for s in SOLVER:
        if domain == "cargobike" and "base" in s:
            continue

        try:
            x, y = get_plot_data(df[s, "time"][domain], style)

        except KeyError:
            print(f'Warning: Domain "{domain}" not contained in data')
            continue

        min_x = min(x) if min(x) > min_x else min_x
        max_y = max(y) if max(y) > max_y else max_y

        (plots[s],) = plt.plot(
            x,
            y,
            ls=LINE[s],
            color=COLOR[s],
            lw=1,
            # marker=MARKER[domain],
            markevery=0.2,
            ms=3,
            label=s,
        )

    # Create legend
    plt.legend(
        handles=plots.values(),
        labels=list(plots.keys()),
        # loc="upper center",
        prop={"style": "italic"},
        # title="clingo-base",
        title_fontproperties={"weight": "bold"},
        # alignment="left",
    )

    # Set axis labels
    plt.xlabel("% of instances solved")
    plt.ylabel("Runtime (s)")

    # Set axis limits
    plt.xlim(min_x, 100)
    plt.ylim(bottom=0, top=max_y / 3 * 2)

    # Set x-axis ticks
    plt.xticks(np.arange(0, 110, 10))

    # tikzplotlib.save(outpath)

    outfile = os.path.join(OUTDIR, f"incremental-{domain}.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    results = clean_df(read_excel(args.input))
    # print(results)
    # exit()
    for name in ["restaurant", "citybike", "travelbike", "cargobike"]:
        plot(results, name, style="cactus")
