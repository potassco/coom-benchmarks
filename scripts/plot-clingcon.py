#!/usr/bin/env python
import os
from argparse import ArgumentParser
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import read_excel
from utils import COLORS, MARKER, clean_df, get_plot_data, make_legend

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.labelsize": 16,
        "xtick.labelsize": 13,
        "ytick.labelsize": 13,
        "legend.fontsize": 12,
        "legend.title_fontsize": 13,
    }
)

OUTDIR = "results/plots/clingcon"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()


SOLVERS = ["clingo", "flingo", "clingcon"]
DOMAINS = ["randomcore", "citybike", "travelbike", "restaurant", "metro"]

COLOR = {
    "clingo": COLORS["green"],
    "flingo": COLORS["blue"],
    "clingcon": COLORS["red"],
}


def plot(df, domain, style="cactus"):
    """
    Plots the specified plot.
    """

    # Get solver-domain data pairs
    pairs = []
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for s in SOLVERS:
        try:
            x, y = get_plot_data(df[f"base_{s}"][domain], style)
        except KeyError:
            print(f'Warning: Domain "{domain}" not contained in data for solver {s}')
            continue
        pairs.append((s, d))
        min_x = max(min_x, min(x))
        max_y = max(max_y, max(y))

        (plots[s],) = plt.plot(
            x,
            y,
            # ls=LINE[s],
            color=COLOR[s],
            lw=1,
            # marker=MARKER[d],
            markevery=0.2,
            ms=3,
            label=(s),
        )

    # Create legends
    # make_legend(plots, pairs, "base")
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

    outfile = os.path.join(OUTDIR, f"{domain}.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    results = clean_df(read_excel(args.input))
    time_only = results.xs("time", axis=1, level=1)

    for d in DOMAINS:
        plot(time_only, d, style="cactus")
