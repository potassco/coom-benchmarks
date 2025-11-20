"""
Utility functions for plotting benchmarks
"""

from itertools import product

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, MultiIndex

COLORS = {
    "green": "#77B762",
    "blue": "#4477CC",
    "red": "#CF3A19",
    "purple": "#5C4B84",
    "lightpurple": "#9477BF90",
    "orange": "#D78C1F",
    "yellow": "#D7CF1F",
    "greenblue": "#226367",
}

COLOR = {
    "core": COLORS["green"],
    "citybike": COLORS["blue"],
    "travelbike": COLORS["red"],
    "restaurant": COLORS["yellow"],
    "box": COLORS["orange"],
    "cargobike": COLORS["green"],
    "racks": COLORS["blue"],
    "house": COLORS["red"],
}
MARKER = {
    "core": "D",
    "citybike": "o",
    "travelbike": "x",
    "restaurant": "s",
    "box": "*",
    "cargobike": "D",
    "racks": "o",
    "house": "x",
}  # , "+"]

LABEL = {
    "core": "Core",
    "citybike": "CityBikeFleet",
    "travelbike": "TravelBikeFleet",
    "restaurant": "Restaurant",
    "box": "Box",
    "cargobike": "CargoBike",
    "racks": "Racks",
    "house": "House",
}
LINE = {
    "clingo-base": "-",
    "flingo-base": "--",
    "clingo-cautious": "-",
    "clingo-brave": "--",
    "clingo-bounds-linear": "-",
    "flingo-bounds-linear": "--",
    "multishot-linear": "-.",
    "clingo-bounds-exponential": "-",
    "flingo-bounds-exponential": "--",
    "multishot-exponential": "-.",
}

PAIRS = {
    "base": [
        ("clingo-base", "box"),
        ("clingo-base", "citybike"),
        ("clingo-base", "restaurant"),
        ("clingo-base", "travelbike"),
        ("flingo-base", "citybike"),
        ("flingo-base", "restaurant"),
        ("flingo-base", "travelbike"),
    ],
    "consequences": list(
        product(
            ["clingo-brave", "clingo-cautious"],
            ["box", "citybike", "restaurant", "travelbike"],
        )
    ),
    "unbounded-linear": list(
        product(
            [
                "clingo-bounds-linear",
                "flingo-bounds-linear",
                "multishot-linear",
            ],
            ["cargobike", "racks", "house"],
        )
    ),
    "unbounded-exponential": list(
        product(
            [
                "clingo-bounds-exponential",
                "flingo-bounds-exponential",
                "multishot-exponential",
            ],
            ["cargobike", "racks", "house"],
        )
    ),
}


def clean_df(df):
    """
    Prepares and cleans the pandas dataframe containing the results
    """
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
    instances = MultiIndex.from_tuples(instances)

    # Create multi index for columns
    columns = MultiIndex(
        levels=[solvers, stats],
        codes=[
            np.repeat(range(len(solvers)), len(stats)).tolist(),
            list(range(len(stats))) * len(solvers),
        ],
    )

    # Get data
    data = df.iloc[1:, 1:].values  # needed? convert_dtypes()

    return DataFrame(index=instances, columns=columns, data=data)


def get_plot_data(df, style="cactus"):
    """
    Returns the plot data as two arrays: one for the x and y axis, respectively
    """
    if style == "cactus":
        y = np.insert(df.sort_values().to_numpy(), 0, 0)
        x = np.arange(len(y + 1)) * (100 / (len(y) - 1))
    else:
        raise ValueError("Unknown plot style.")
    # elif domain == "citybike":
    #     y = runtimes.to_numpy()
    #     # x = np.arange(1, len(y) + 1)
    #     x = [int(n.replace("citybike-n", "")) for n in df.index.tolist()]
    return x, y


def make_legend(plots, pairs, plotname):
    if plotname == "base":
        clingo_legend = plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "clingo-base"],
            labels=[LABEL[d] for s, d in pairs if s == "clingo-base"],
            loc="upper center",
            prop={"style": "italic"},
            title="clingo-base",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(clingo_legend)

        plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "flingo-base"],
            labels=[LABEL[d] for s, d in pairs if s == "flingo-base"],
            loc="center",
            bbox_to_anchor=(0.5, 0.55),
            prop={"style": "italic"},
            title="flingo-base",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )

    if plotname == "consequences":
        cautious_legend = plt.legend(
            handles=[plots[f"{s}-{d}"] for s, d in pairs if s == "clingo-cautious"],
            labels=[LABEL[d] for s, d in pairs if s == "clingo-cautious"],
            loc="upper center",
            prop={"style": "italic"},
            title="clingo-cautious",
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
            title="clingo-brave",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )

    if plotname == "unbounded-linear":
        clingo_singleshot_legend = plt.legend(
            handles=[
                plots[f"{s}-{d}"] for s, d in pairs if "clingo" in s and "linear" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "clingo" in s],
            loc="upper left",
            prop={"style": "italic"},
            title="clingo linear single-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(clingo_singleshot_legend)

        flingo_singleshot_legend = plt.legend(
            handles=[
                plots[f"{s}-{d}"] for s, d in pairs if "flingo" in s and "linear" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "flingo" in s],
            loc="upper left",
            bbox_to_anchor=(0, 0.75),
            prop={"style": "italic"},
            title="flingo linear single-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(flingo_singleshot_legend)

        plt.legend(
            handles=[
                plots[f"{s}-{d}"]
                for s, d in pairs
                if "multishot" in s and "linear" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "multishot" in s],
            loc="upper left",
            bbox_to_anchor=(0, 0.5),
            prop={"style": "italic"},
            title="clingo linear multi-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
    if plotname == "unbounded-exponential":
        clingo_singleshot_legend = plt.legend(
            handles=[
                plots[f"{s}-{d}"]
                for s, d in pairs
                if "clingo" in s and "exponential" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "clingo" in s],
            loc="upper left",
            prop={"style": "italic"},
            title="clingo exponential single-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(clingo_singleshot_legend)

        flingo_singleshot_legend = plt.legend(
            handles=[
                plots[f"{s}-{d}"]
                for s, d in pairs
                if "flingo" in s and "exponential" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "flingo" in s],
            loc="upper left",
            bbox_to_anchor=(0, 0.75),
            prop={"style": "italic"},
            title="flingo exponential single-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )
        plt.gca().add_artist(flingo_singleshot_legend)

        plt.legend(
            handles=[
                plots[f"{s}-{d}"]
                for s, d in pairs
                if "multishot" in s and "exponential" in s
            ],
            labels=[LABEL[d] for s, d in pairs if "multishot" in s],
            loc="upper left",
            bbox_to_anchor=(0, 0.5),
            prop={"style": "italic"},
            title="clingo exponential multi-shot",
            title_fontproperties={"weight": "bold"},
            alignment="left",
        )

    return plots
