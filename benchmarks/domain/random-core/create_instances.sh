#!/bin/bash

OUTDIR=instances
NAME=randomcore

rm -rf $OUTDIR

for numfeat in 50 100; do
    for numopt in 50 100 150; do
        for consize in 2 3 4; do
            python generate.py -f $numfeat -o $numopt -c $consize --name $NAME --out $OUTDIR
        done
    done
done
