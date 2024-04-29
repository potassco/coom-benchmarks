"""
Generates benchmark instances for the kids bike encoding.
"""

import argparse
import os
from random import choices, sample
from typing import Any, List

parser = argparse.ArgumentParser(
    prog="GenerateKids",
    description="Generates a benchmark instance for the kids bike encoding",
)
parser.add_argument("--features", "-f", type=int)
parser.add_argument("--options", "-o", type=int)

OUTDIR = "instances"


def make_row(num_cols: int, options: List[str]) -> str:
    return " ".join([f"F{i}" for i in choices(options, k=num_cols)])


def make_constraint(
    num_cols: int, num_rows: int, features: List[Any], options: List[Any]
) -> str:
    cols = " ".join([f"feat{i}" for i in sample(features, num_cols)])
    combinations = f"combinations ({cols})"

    rows = "\n".join(
        [f"allow ({make_row(num_cols, options)})" for i in range(num_rows)]
    )
    constraint = "behavior{\n" + combinations + "\n" + rows + "\n}"
    return constraint


if __name__ == "__main__":
    args = parser.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)

    FEATURES = "\n".join([f"Feat{i} feat{i}" for i in range(args.features)])
    OPTIONS = " ".join([f"F{i}" for i in range(args.options)])
    ENUMERATIONS = "\n".join(
        [f"enumeration Feat{i}{{ {OPTIONS} }}" for i in range(args.features)]
    )

    output = []

    output.append(f"product{{ {FEATURES} }}")
    output.append("")

    output.append(ENUMERATIONS)
    output.append("")

    output.append(
        make_constraint(
            args.features,
            args.options,
            list(range(args.features)),
            list(range(args.options)),
        )
    )
    output.append("")

    # CONSTRAINTS = [sample(list(range(args.features)), 5)]
    # print(CONSTRAINTS)
    outfile = os.path.join(OUTDIR, f"instance{args.features}_{args.options}.coom")
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(output))
