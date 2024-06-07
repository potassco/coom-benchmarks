#!/usr/bin/env python

# from cProfile import label
import os
import math
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools
# import seaborn as sns
from pandas_ods_reader import read_ods
# import scipy
# from scipy import stats
# import re
# import tikzplotlib

BT_DIR = "benchmarks/benchmark-tool"
ODS_FILE ="results/evaluated.ods"

SOLVER = ["clingo", "fclingo"]
DOMAIN = ["kidsbike", "citybike", "travelbike", "restaurant"]

def clean_df(df):
    stats_set = set(df.iloc[0][:])
    stats_set.discard('')

    # Drop min max median
    df.drop(df.columns[-3 * len(stats_set):], axis=1, inplace=True)

    # Remove last computed values
    df.drop(df.tail(9).index, inplace=True)

    # Rename instances
    df[df.columns[0]] = df[df.columns[0]].apply(lambda x: x[2:].replace(".coom",""))

    # Make instances names index of dataframe
    df.index = df.loc[:,df.columns[0]].tolist()

    # Remove first column
    df.drop(df.columns[0], axis=1, inplace=True)

    # Rename columns
    solver = [
        c.split("/")[-1] for i, c in enumerate(df.columns)
        if i % len(stats_set) == 0
    ]
    df.columns = list(np.repeat(solver, len(stats_set)))
    df.columns = [f"{c}-{s}" for c,s in zip(df.columns,list(df.iloc[0]))]

    # Remove unused out values
    df.drop(df.index[0], inplace=True)

    # Convert datatypes
    df = df.convert_dtypes()

    return df

def get_subdf(df, domain, solver):
    subdf = df.filter(like=domain,axis=0).filter(regex=f"^{solver}",axis=1)

    # print(subdf)
    # all_constraints = [
    #     c.split("/")[-1] for i, c in enumerate(all_constraints)
    #     if i % n_all_stats == 0
    # ]
    # all_stats = df.iloc[0][1:n_all_stats + 1]
    # new_cols = [
    #     p for c, p in list(itertools.product(all_constraints, all_stats))
    # ]
    # new_cols = ["instance-name"] + new_cols

    # df.drop(df.index[0], inplace=True)  # Remove unused out values

    # df.columns = new_cols


    return subdf

if __name__=='__main__':
    ods_path = os.path.join(BT_DIR, ODS_FILE)
    df = read_ods(ods_path)
    df = clean_df(df)

    kidsbike_clingo_df = get_subdf(df, domain="kidsbike", solver="fclingo")
    print(kidsbike_clingo_df)
    kidsbike_clingo_df.to_csv("evaluated.csv")
