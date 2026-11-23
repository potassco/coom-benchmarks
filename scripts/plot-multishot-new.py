#!/usr/bin/env python

import os
from argparse import ArgumentParser
from itertools import product

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import read_excel
from utils import COLORS, LABEL, clean_df, get_plot_data, make_legend

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

OUTDIR = "results/plots/multishot-new"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()

# SOLVER = ["clingo"]  # , "flingo"]
# MODE = ["multishot"]
ALGORITHMS = ["linear", "exponential"]
OPTIONS = ["stepwise", "jump-extend", "jump-full"]
# STEP = {"linear": [1, 2, 4, 8, 16], "exponential": [2, 3, 4]}


COLOR = {
    "stepwise": COLORS["red"],
    "jump-extend": COLORS["yellow"],
    "jump-full": COLORS["greenblue"],
}

LINE = {
    "linear": "-",
    "exponential": "--",
}


def get_best_runs(data, runs):
    best_runs = []
    for algorithm in ALGORITHMS:
        for option in OPTIONS:
            current_runs = [
                c
                for c in runs
                if algorithm in c and option in c and "fix-externals" in c
            ]
            best_runs.append(data[current_runs].mean().idxmin())

            current_runs = [
                c
                for c in runs
                if algorithm in c and option in c and "fix-externals" not in c
            ]
            best_runs.append(data[current_runs].mean().idxmin())
    return best_runs


def plot(df, domain, style="cactus"):
    """
    Plots the specified plot.
    """
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}

    runs = [c for c in df.columns]
    runs = get_best_runs(df, runs)

    for run in runs:
        if "fix-externals" not in run:
            continue
        # solver = "flingo" if "flingo" in run else "clingo"
        # mode = run.split("_")[0].split("-")[0].strip()

        algorithm = "exponential" if "exponential" in run else "linear"
        fix_externals = "fix-externals" in run
        step = run.split("_")[-2]
        option = run.split("_")[-1]
        # if (algorithm == "linear" and step != "1") or (
        #     algorithm == "exponential" and step != "2"
        # ):
        #     continue

        try:
            df[run]
            x, y = get_plot_data(df[run][domain], style)

        except KeyError:
            print(f'Warning: Domain "{domain}" not contained in data')
            continue

        min_x = max(min_x, min(x))
        max_y = max(y) if max(y) > max_y else max_y  # noqa: FURB136

        (plots[run],) = plt.plot(
            x,
            y,
            ls=LINE[algorithm],
            color=COLOR[option],
            # alpha=1 if fix_externals else 0.5,
            lw=1,
            # marker=MARKER[domain],
            markevery=0.2,
            ms=3,
            label=f"{algorithm}-{option}-{step}-{'fix-externals' if fix_externals else ''}",
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

    outfile = os.path.join(OUTDIR, f"multishot-new-fix-externals-{domain}.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    results = clean_df(read_excel(args.input))
    time_only = results.xs("time", axis=1, level=1)

    for name in [
        "restaurant",
        "travelbike",
        "cargobike-nested",
    ]:
        plot(time_only, name, style="cactus")
