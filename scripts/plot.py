#!/usr/bin/env python
import os
from argparse import ArgumentParser
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import read_excel
from utils import COLOR, LINE, MARKER, clean_df, get_plot_data, make_legend

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

OUTDIR = "results/plots"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()


PAIRS = {
    "base": [
        ("clingo-base", "box"),
        ("clingo-base", "citybike"),
        ("clingo-base", "travelbike"),
        ("clingo-base", "restaurant"),
        ("clingo-base", "metro"),
        # ("clingo-base", "spacecollider"),
        ("flingo-base", "citybike"),
        ("flingo-base", "travelbike"),
        ("flingo-base", "restaurant"),
        ("flingo-base", "metro"),
        # ("flingo-base", "spacecollider"),
    ],
    "consequences": list(
        product(
            ["clingo-brave", "clingo-cautious"],
            [
                "box",
                "citybike",
                "travelbike",
                "restaurant",
                "metro",
            ],  # , "spacecollider"],
        )
    ),
}


def plot(df, plotname, style="cactus"):
    """
    Plots the specified plot.
    """

    # Get solver-domain data pairs
    pairs = []
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for s, d in PAIRS[plotname]:
        name = f"{s}-{d}"
        try:
            x, y = get_plot_data(df[s, "time"][d], style)
        except KeyError:
            print(f'Warning: Domain "{d}" not contained in data')
            continue
        pairs.append((s, d))
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

    results = clean_df(read_excel(args.input))

    for n in "base", "consequences":  # , "unbounded-linear", "unbounded-exponential":
        plot(results, n, style="cactus")
