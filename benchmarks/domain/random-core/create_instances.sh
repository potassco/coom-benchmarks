#!/bin/bash

OUTDIR=instances
NAME=randomcore

rm -rf $OUTDIR

for numfeat in $(seq 30 20 70); do
    for numopt in $(seq 30 30 90); do
        for consize in 2 3 4; do
            python generate.py -f $numfeat -o $numopt -c $consize --name $NAME --out $OUTDIR
        done
    done
done
