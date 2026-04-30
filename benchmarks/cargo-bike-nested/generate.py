"""
Generate cargo bike benchmark instances.
"""

import argparse
import os

parser = argparse.ArgumentParser(
    prog="GenerateCargoBike",
    description="Generate cargo bike benchmark instances",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--range", type=int, default=200, help="Upper bound for domain of volume features"
)
parser.add_argument("--instances", type=int, default=10, help="Number of instances")
parser.add_argument(
    "--min",
    type=int,
    default=50,
    help="Minimum value for requested volume, in percent of range",
)
parser.add_argument(
    "--max",
    type=int,
    default=100,
    help="Maximum value for requested volume, in percent of range",
)
parser.add_argument("--out", type=str, default="instances", help="Out directory")
parser.add_argument("--model", type=str, help="Model name")


def get_user_input(max_volume: int, request: int) -> str:
    return f"set requestedVolume[0] = {int(max_volume * request / 100)}"


if __name__ == "__main__":
    args = parser.parse_args()

    # compute the requested volumes as percent of the range
    request_range = args.max - args.min
    request_step = request_range / (args.instances - 1)
    requests = [args.min + i * request_step for i in range(args.instances)]

    # get the user input for each request and write to file
    for i, request in enumerate(requests):
        user_input = get_user_input(args.range, request)

        outuser = os.path.join(args.out, f"{args.model}_user-input-{i}.coom")
        print(outuser)
        with open(outuser, "w", encoding="utf-8") as f:
            f.write(f"{user_input}\n")
