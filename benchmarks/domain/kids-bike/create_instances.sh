#!/bin/bash

OUTDIR=instances
rm -rf $OUTDIR

for numfeat in $(seq 10 2 20); do
    for numopt in $(seq 10 10 50); do
        for consize in 2 3 4; do
            python generate.py -f $numfeat -o $numopt -c $consize --out $OUTDIR
        done
    done
done
