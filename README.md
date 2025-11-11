# COOM Benchmarks
Benchmark sets in COOM language.

## Installation

```sh
pip install -r requirements.txt
```

## How to run (on laptop for debugging)

1. Generate the benchmark folder structure and scripts

```sh
btool gen runscripts/runscript-coom-laptop.xml
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
btool eval runscripts/runscript-coom-laptop.xml | btool conv results/all.ods
```


<!-- ```sh
./benchmarks/scripts/run_bm.sh
./benchmarks/scripts/evaluate.sh
``` -->
