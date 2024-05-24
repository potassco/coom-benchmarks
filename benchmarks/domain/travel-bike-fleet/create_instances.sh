#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances
NAME=travelbike

rm -rf $OUTDIR
mkdir $OUTDIR

for numbikes in $(seq 1 10)
do
    OUTFILE=$OUTDIR/${NAME}${numbikes}.coom
    sed -e "s/NUMBIKES/${numbikes}/g" $TEMPLATE > $OUTFILE
done
