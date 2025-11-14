#!/bin/bash

model=model.coom
user=user-input.coom
outdir=instances
name=box

rm -rf $outdir
mkdir $outdir

for side in $(seq 50 5 150)
do
    volume=$((($side**3)/1000))

    # Model
    outfile=$outdir/${name}-s${side}.coom
    sed -e "s/SIDE/${side}/g" -e "s/VOLUME/${volume}/g" $template > $outfile

    # User input
    outfile=$outdir/${name}-s${side}.coom
    sed -e "s/SIDE/${side}/g" -e "s/VOLUME/${volume}/g" $template > $outfile
done
