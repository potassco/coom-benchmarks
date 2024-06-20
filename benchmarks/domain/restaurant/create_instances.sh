#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances
NAME=restaurant

rm -rf $OUTDIR
mkdir $OUTDIR

for numtable in 20 50 100
do
    maxplaces=$(($numtable*7))
    init=$(($numtable*2))
    for totalplaces in $(seq $init 70 $maxplaces)
    do
        OUTFILE=$OUTDIR/${NAME}${numtable}_${totalplaces}.coom
        sed -e "s/NUMTABLE/${numtable}/g" -e "s/TOTALPLACES/${totalplaces}/g" $TEMPLATE > $OUTFILE
    done
done
