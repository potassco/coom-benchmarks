#!/bin/bash

TEMPLATE=instance.coom
OUTDIR=instances

rm -rf $OUTDIR
mkdir $OUTDIR

for numtable in $(seq 5 5 30)
do
    maxplaces=$(($numtable*7))
    init=$(($numtable*2))
    for totalplaces in $(seq $init 10 $maxplaces)
    do
        OUTFILE=$OUTDIR/instance${numtable}_${totalplaces}.coom
        sed -e "s/NUMTABLE/${numtable}/g" -e "s/TOTALPLACES/${totalplaces}/g" $TEMPLATE > $OUTFILE
    done
done
