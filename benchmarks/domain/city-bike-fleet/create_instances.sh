#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances

rm -rf $OUTDIR
mkdir $OUTDIR

for numbikes in $(seq 1 10)
do
    OUTFILE=$OUTDIR/instance${numbikes}.coom
    sed -e "s/NUMBIKES/${numbikes}/g" $TEMPLATE > $OUTFILE
done
