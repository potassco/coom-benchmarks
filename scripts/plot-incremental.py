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

SOLVER = ["clingo", "flingo"]
MODE = ["singleshot", "incremental", "multishot"]
ALGORITHM = ["linear", "exponential"]
STEP = {"linear": [1, 2, 4, 8, 16], "exponential": [2, 3, 4]}


COLOR = {
    "clingo": {
        "singleshot": COLORS["lightgreen"],
        "incremental": COLORS["green"],
        "multishot": COLORS["red"],
    },
    "flingo": {"singleshot": COLORS["lightblue"], "incremental": COLORS["blue"]},
}

LINE = {
    "singleshot": "-",
    "linear": "--",
    "exponential": ":",
}


def plot(df, domain, style="cactus"):
    """
    Plots the specified plot.
    """
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for run in df.columns.levels[0]:
        solver = "flingo" if "flingo" in run else "clingo"
        mode = run.split("_")[0].split("-")[0].strip()
        if "cargobike" in domain and mode == "singleshot":
            continue

        if mode in ["incremental", "multishot"]:
            algorithm = "exponential" if "exponential" in run else "linear"
            step = run.split("_")[-1]
            if (algorithm == "linear" and step != "1") or (
                algorithm == "exponential" and step != "2"
            ):
                continue
        else:
            algorithm = "singleshot"
            step = None

        try:
            x, y = get_plot_data(df[run, "time"][domain], style)

        except KeyError:
            print(f'Warning: Domain "{domain}" not contained in data')
            continue

        min_x = min(x) if min(x) > min_x else min_x
        max_y = max(y) if max(y) > max_y else max_y

        (plots[run],) = plt.plot(
            x,
            y,
            ls=LINE[algorithm],
            color=COLOR[solver][mode],
            lw=1,
            # marker=MARKER[domain],
            markevery=0.2,
            ms=3,
            label=f"{solver}-{mode}-{algorithm}-{step}",
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

    for name in [
        "restaurant",
        "travelbike",
        "cargobike",
        "cargobike-nested",
    ]:
        plot(results, name, style="cactus")
