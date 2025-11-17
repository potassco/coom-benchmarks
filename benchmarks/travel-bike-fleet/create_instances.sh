#!/bin/bash

TEMPLATE=model.coom
OUTDIR=instances
NAME=travelbike

rm -rf $OUTDIR
mkdir $OUTDIR

# MAX_PER_BIKE=500

for numBikes in $(seq 1 1 15); do
    # for maxprice in 300 500; do
    maxPrice=$((200*numBikes))
    OUTFILE=$OUTDIR/${NAME}-${numBikes}.coom
    sed -e "s/NUMBIKES/${numBikes}/g" -e "s/MAXPRICE/${maxPrice}/g" $TEMPLATE > $OUTFILE
    # done
done
