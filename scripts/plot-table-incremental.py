#!/usr/bin/env python

import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np

# from pandas_ods_reader.main import read_ods
from pandas import DataFrame, MultiIndex, read_excel
from utils import COLORS, LABEL, clean_df, get_plot_data, highlight_group_minima

OUTDIR = "results/plots/incremental"
parser = ArgumentParser(
    prog="COOMBenchmarkPlotter", description="Plots COOM Benchmarks"
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
# parser.add_argument("--name", type=str, required=True, help="Name of plot")
args = parser.parse_args()

SOLVER = ["clingo", "flingo", "multishot"]
# MODE = ["singleshot", "incremental"]
ALGORITHM = ["linear", "exponential"]
# STEP = {"linear": [1, 2, 4, 8, 16], "exponential": [2, 3, 4]}


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

FORMAT = {
    "linear": {
        "option": "\\code{--step}",
        "column_format": "l|llllllllll",
    },
    "exponential": {
        "option": "\\code{--base}",
        "column_format": "l|lllllllllll",
    },
}


def format_param(p: str, algorithm: str):
    if algorithm == "linear":
        return int(p)
    return float(p)


def create_avg_table(data, algorithm, solver):
    """
    Creates tables for the averages of each algorithm and parameter
    """
    columns = [c for c in data.columns if algorithm in c and solver in c]
    if columns == []:
        return

    current_df = data[columns].rename(
        columns=lambda c: format_param(c.split("_")[-1], algorithm),
        # level=1,
        # inplace=True,
    )
    current_df.sort_index(axis="columns", inplace=True)

    # current_df.rename_axis(columns=["", FORMAT[algorithm]["option"]], inplace=True)

    styled = (
        current_df.style.format(precision=0, na_rep="-").format_index(
            precision=2, axis=1
        )
        # .apply(highlight_group_minima, axis=1)
        .highlight_min(axis=1, props="textbf:--rwrap;")
    )

    latex_out = styled.to_latex(
        column_format=FORMAT[algorithm]["column_format"],
        position="ht",
        position_float="centering",
        hrules=True,
        clines="all;data",
        label=f"tab:results:{algorithm}",
        caption=f"Average runtimes (in seconds) for {FORMAT[algorithm]["option"]} parameters of {algorithm} search algorithm for {solver}",
        multicol_align="c",
    )

    outfile = os.path.join(OUTDIR, f"incremental-{algorithm}-{solver}.tex")

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(latex_out)
    print(f"Saved {outfile}")


def create_avg_param_boxplots(data, domain):
    """
    Plots averages of parameters for incremental approaches
    """
    avg = data.mean()
    # avg.rename(index=LABEL, inplace=True)

    labels = [(a, s) for s in SOLVER for a in ALGORITHM]

    # labels.sort()
    columns = [[c for c in avg.index if (a in c and s in c)] for (a, s) in labels]
    x = [avg[c].to_numpy() for c in columns]

    plt.boxplot(
        x,
        tick_labels=[f"{a}\n{s}" for (a, s) in labels],
        # patch_artist=True,
        showmeans=True,
        meanline=True,
    )

    # Set axis labels
    plt.ylabel("Runtime (s)")

    # Set axis limits
    plt.ylim(bottom=0, top=600)

    outfile = os.path.join(OUTDIR, f"incremental-{domain}-params.pdf")
    plt.savefig(outfile, dpi=1200, bbox_inches="tight")
    print(f"Saved {outfile}")
    plt.clf()


def get_best_runs(data, runs):
    best_runs = [c for c in runs if "singleshot" in c]
    for solver in SOLVER:
        for algorithm in ALGORITHM:
            current_runs = [c for c in runs if solver in c and algorithm in c]
            best_runs.append(data[current_runs].mean().idxmin())
    return best_runs


def get_parameters(run):
    solver = "flingo" if "flingo" in run else "clingo"
    mode = run.split("_")[0].split("-")[0].strip()
    if mode in ["incremental", "multishot"]:
        algorithm = "exponential" if "exponential" in run else "linear"
        step = run.split("_")[-1]
    else:
        algorithm = "singleshot"
        step = None
    return solver, mode, algorithm, step


def get_label(solver, mode, algorithm, step):
    if mode == "singleshot":
        return f"{solver}-{mode}"
    else:
        mode = "inc" if mode == "incremental" else "multishot"
        algorithm = "lin" if algorithm == "linear" else "exp"
        if mode == "multishot":
            return f"{mode}-{algorithm}{step}"
        return f"{solver}-{mode}-{algorithm}{step}"


def create_cactus_plots(data, domain):
    """
    Plots the specified plot.
    """
    # min_x = 0
    # max_y = 0

    # Get subplots
    plots = {}
    runs = [
        c for c in data.columns if not ("cargobike" in domain and "singleshot" in c)
    ]

    runs = get_best_runs(data, runs)

    for run in runs:
        solver, mode, algorithm, step = get_parameters(run)
        x, y = get_plot_data(data[run], "cactus")

        # min_x = min(x) if min(x) > min_x else min_x
        # max_y = max(y) if max(y) > max_y else max_y

        (plots[run],) = plt.plot(
            x,
            y,
            ls=LINE[algorithm],
            color=COLOR[solver][mode],
            lw=1,
            # marker=MARKER[domain],
            markevery=0.2,
            ms=3,
            label=get_label(solver, mode, algorithm, step),
        )

    # Create legend
    plt.legend(
        handles=plots.values(),
        # labels=list(plots.keys()),
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
    plt.xlim(0, 100)
    plt.ylim(bottom=0, top=500)  # max_y / 3 * 2)

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

    # Drop City Bike
    try:
        results.drop(index="citybike", level=0, inplace=True)
    except KeyError:
        pass

    time_only = results.xs("time", axis=1, level=1)

    avg = time_only.groupby(level=0).mean()
    avg.rename(index=LABEL, inplace=True)

    # Create tables
    for a in ALGORITHM:
        for s in SOLVER:
            create_avg_table(avg, a, s)

    domains = set([i[0] for i in time_only.index])
    # bug with time_only.index.levels, citybike still appears...

    # Create plots
    for d in list(domains):
        current_df = time_only.loc[d]
        create_avg_param_boxplots(current_df, d)
        create_cactus_plots(current_df, d)
