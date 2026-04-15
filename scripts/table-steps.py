#!/usr/bin/env python

from argparse import ArgumentParser

from pandas import DataFrame, MultiIndex, notna, read_excel
from utils import LABEL, clean_df

parser = ArgumentParser(
    prog="COOMBenchmarkTable",
    description="Get table of COOM Benchmarks with step parameters for incremental bounds",
)
parser.add_argument(
    "--input", "-i", type=str, required=True, help="Path to input .xlsx file"
)
args = parser.parse_args()

COL_FORMAT = {"linear": "l|lllll|lllll|lllll", "exponential": "l|lll|lll|lll"}


def highlight_group_minima(row):
    """Highlight minima independently for each first-level column group."""
    styles = [""] * len(row)
    for group in row.index.get_level_values(0).unique():
        positions = [i for i, col in enumerate(row.index) if col[0] == group]
        values = row.iloc[positions]
        minimum = values.min(skipna=True)

        if notna(minimum):
            for pos, value in zip(positions, values):
                if value == minimum:
                    styles[pos] = "textbf:--rwrap;"

    return styles


def format(name):
    solver = "f" if "flingo" in name else "c"

    if "singleshot" in name:
        return f"{solver}-singleshot"
    else:
        mode = "i" if "incremental" in name else "m"
        # algorithm = "exponential" if "exponential" in name else "linear"
        step = name.split("_")[-1]

        return f"{solver}{mode}{step}"


if __name__ == "__main__":
    results = clean_df(read_excel(args.input))
    avg = results.xs("time", axis=1, level=1).groupby(level=0).mean()

    # Drop City Bike
    avg.drop(index="citybike", inplace=True)
    avg.rename(index=LABEL, inplace=True)

    solver = ["clingo", "flingo", "multishot"]

    for algorithm in ["linear", "exponential"]:
        # for solver in ["clingo", "flingo", "multishot"]:
        # for mode in ["incremental","multishot"]:

        columns = [c for c in avg.columns if algorithm in c]

        multi_columns = MultiIndex.from_tuples(
            [(s, c) for c in columns for s in solver if s in c]
        )

        current_df = DataFrame(
            index=avg.index, columns=multi_columns, data=avg.loc[:, columns].values
        )

        current_df.rename(
            columns=lambda c: int(c.split("_")[-1]), level=1, inplace=True
        )
        # Keep first-level order as-is and sort only second-level values per group.
        first_level_order = list(dict.fromkeys(current_df.columns.get_level_values(0)))
        sorted_columns = [
            (level_0, level_1)
            for level_0 in first_level_order
            for level_1 in sorted(current_df[level_0].columns)
        ]
        current_df = current_df.loc[:, MultiIndex.from_tuples(sorted_columns)]
        current_df.rename_axis(columns=["", "\\code{--step}"], inplace=True)

        styled = (
            current_df.style.format(precision=0, na_rep="-")
            .apply(highlight_group_minima, axis=1)
            .highlight_min(axis=1, props="underline:--rwrap;")
        )

        latex_out = styled.to_latex(
            column_format=COL_FORMAT[algorithm],
            position="ht",
            position_float="centering",
            hrules=True,
            clines="all;data",
            label=f"tab:results:{algorithm}",
            caption=f"Benchmark results of step parameters for {algorithm} search algorithm",
            multicol_align="c",
        )

        outfile = args.input.replace(".xlsx", f"-{algorithm}.tex")
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(latex_out)
        print(f"Saved {outfile}")
