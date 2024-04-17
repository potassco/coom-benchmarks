#!/bin/bash

name=instance
outdir=coom


if [ ! -d $outdir ]
then
    mkdir $outdir
fi

for numbikes in $(seq 1 10)
do
    outfile=$outdir/${name}_${numbikes}.coom
    sed -e "s/NUMBIKES/${numbikes}/g" ${name}.coom > $outfile
done
