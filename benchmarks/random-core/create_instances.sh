#!/bin/bash

OUTDIR=instances
NAME=randomcore

rm -rf $OUTDIR
mkdir $OUTDIR

for numFeat in 25 50 100 200 400; do
    for numOpt in 50 150 250; do
        for conSize in 2 3 4; do
            python generate.py -f $numFeat -o $numOpt -c $conSize --name $NAME --out $OUTDIR
        done
    done
done
