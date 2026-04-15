#!/usr/bin/env python

import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import read_excel
from utils import COLORS, LABEL, clean_df, get_plot_data, make_legend

OUTDIR = "results/plots/incremental/steps"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()

SOLVER = ["clingo", "flingo"]
ALGORITHM = ["linear", "exponential"]
STEP = {"linear": [1, 2, 4, 8, 16], "exponential": [2, 3, 4]}

COLOR = {
    "1": COLORS["green"],
    "2": COLORS["blue"],
    "3": COLORS["green"],
    "4": COLORS["red"],
    "8": COLORS["yellow"],
    "16": COLORS["purple"],
}

LINE = {
    "clingo": {
        "linear": "-",
        "exponential": "--",
    },
    "flingo": {
        "linear": "-.",
        "exponential": ":",
    },
}


def plot(df, domain, mode, style="cactus"):
    """
    Plots the specified plot.
    """
    min_x = 0
    max_y = 0

    # Get subplots
    plots = {}
    for run in df.columns.levels[0]:
        if mode not in run:
            continue
        solver = "flingo" if "flingo" in run else "clingo"

        algorithm = "exponential" if "exponential" in run else "linear"
        step = run.split("_")[-1]

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
            ls=LINE[solver][algorithm],
            color=COLOR[step],
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

    outfile = os.path.join(OUTDIR, f"{mode}-{domain}.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)

    results = clean_df(read_excel(args.input))

    for domain in [
        "restaurant",
        "citybike",
        "travelbike",
        "cargobike",
        "cargobike-nested",
    ]:
        for mode in ["multishot", "incremental"]:
            if "cargobike" in domain and mode == "singleshot":
                continue
            plot(results, domain, mode, style="cactus")
