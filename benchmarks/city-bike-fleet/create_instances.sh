#!/bin/bash

TEMPLATE=model.coom
OUTDIR=instances
NAME=citybike

rm -rf $OUTDIR
mkdir $OUTDIR

for numBikes in $(seq 10 10 150)
do
    outFile=$OUTDIR/${NAME}-n${numBikes}.coom
    sed -e "s/NUMBIKES/${numBikes}/g" $TEMPLATE > $outFile
done
