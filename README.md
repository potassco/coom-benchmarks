# COOM Suite Benchmarks

This repository contains benchmarks for the COOM Suite.
The instances can be found in the [benchmarks](benchmarks) folder.

## Installation

```sh
pip install -r requirements.txt
```

## How to run (on laptop for debugging)

Replace `laptop` by `cluster` for runing on cluster.

1. Generate the benchmark folder structure and scripts

```sh
btool gen runscripts/runscript-all-laptop.xml
```

2. Run the benchmarks

```sh
 ./output/coom-benchmark-project/laptop/start.py
```

4. Verify results

```sh
btool verify output/coom-benchmark-project/laptop/results
```

3. Evaluate and convert the results

```sh
btool eval runscripts/runscript-all-laptop.xml | btool conv -o results/all.ods
```
4. Plot results

```sh
./scripts/plot.py --ods results/all.ods
```
