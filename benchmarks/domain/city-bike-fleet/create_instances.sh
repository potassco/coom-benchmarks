#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances
NAME=citybike

rm -rf $OUTDIR
mkdir $OUTDIR

for numbikes in $(seq 1 5)
do
    OUTFILE=$OUTDIR/${NAME}${numbikes}.coom
    sed -e "s/NUMBIKES/${numbikes}/g" $TEMPLATE > $OUTFILE
done
