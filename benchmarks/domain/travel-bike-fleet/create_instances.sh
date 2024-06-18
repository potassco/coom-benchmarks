#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances
NAME=travelbike

rm -rf $OUTDIR
mkdir $OUTDIR

MAX_PER_BIKE=500

for numbikes in $(seq 1 5); do
    for maxprice in $(seq 200 100 500); do
        MAXPRICE_TOTAL=$(($maxprice*numbikes))
        OUTFILE=$OUTDIR/${NAME}${numbikes}_${MAXPRICE_TOTAL}.coom
        sed -e "s/NUMBIKES/${numbikes}/g" -e "s/MAXPRICE/${MAXPRICE_TOTAL}/g" $TEMPLATE > $OUTFILE
    done
done
