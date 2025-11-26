#!/usr/bin/env python

import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np
from pandas_ods_reader.main import read_ods
from utils import COLOR, LINE, MARKER, PAIRS, clean_df, get_plot_data, make_legend

OUTDIR = "results/plots"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument("--ods", type=str, required=True, help="Path to input .ods file")
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()


def plot(df, plotname, style="cactus"):
    """
    Plots the specified plot.
    """

    # Get solver-domain data pairs
    pairs = PAIRS[plotname]

    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for s, d in pairs:
        name = f"{s}-{d}"
        x, y = get_plot_data(df[s, "time"][d], style)
        min_x = min(x) if min(x) > min_x else min_x
        max_y = max(y) if max(y) > max_y else max_y

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

    # Create legends
    make_legend(plots, pairs, plotname)

    # Set axis labels
    plt.xlabel("% of instances solved")
    plt.ylabel("Runtime (s)")

    # Set axis limits
    plt.xlim(min_x, 100)
    plt.ylim(bottom=0, top=max_y / 3 * 2)

    # Set x-axis ticks
    plt.xticks(np.arange(0, 110, 10))

    # tikzplotlib.save(outpath)

    outfile = os.path.join(OUTDIR, f"{plotname}.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    results = clean_df(read_ods(args.ods))

    for n in "base", "consequences", "unbounded-linear", "unbounded-exponential":
        plot(results, n, style="cactus")
