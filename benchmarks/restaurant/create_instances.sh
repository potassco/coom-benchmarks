#!/bin/bash

name=instance
outdir=coom


if [ ! -d $outdir ]
then
    mkdir $outdir
fi

for numtable in $(seq 5 5 50)
do
    maxplaces=$(($numtable*7))
    init=$(($numtable*2))
    for totalplaces in $(seq $init 10 $maxplaces)
    do
        outfile=$outdir/${name}_${numtable}_${totalplaces}.coom
        sed -e "s/NUMTABLE/${numtable}/g" -e "s/TOTALPLACES/${totalplaces}/g" ${name}.coom > $outfile
    done
done
