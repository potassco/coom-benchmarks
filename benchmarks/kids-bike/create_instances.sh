#!/bin/bash

name=instance
outdir=coom


if [ ! -d $outdir ]
then
    mkdir $outdir
fi

for numfeat in $(seq 5 5 100)
do
    outfile=$outdir/${name}_${numfeat}.coom

    features=$(for i in $(seq 1 $numfeat); do printf "Color part%d " "$i"; done)
    # echo $features
    # enumeration=$(printf "enumeration Color { %s}" "$features")
    sed -e "s/PART/${features}/g" ${name}.coom > $outfile
done
