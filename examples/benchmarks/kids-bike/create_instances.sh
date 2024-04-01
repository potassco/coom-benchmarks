#!/bin/bash

name=instance
outdir=coom


if [ ! -d $outdir ]
then
    mkdir $outdir
fi

for numcolors in $(seq 50 10 200)
do
    outfile=$outdir/${name}_${numcolors}.coom

    colors=$(for i in $(seq 1 $numcolors); do printf "Color%d " "$i"; done)
    enumeration=$(printf "enumeration Color { %s}" "$colors")
    sed -e "s/COLORS/${enumeration}/g" ${name}.coom > $outfile
done
