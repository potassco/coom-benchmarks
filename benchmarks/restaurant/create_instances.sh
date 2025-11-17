#!/bin/bash

TEMPLATE=instance.coom
MODELDIR=models
INSTANCEDIR=instances
NAME=restaurant

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR



for numtable in 100 500 1000 1500 2000
do
    maxplaces=$(($numtable*7))
    init=$(($numtable*2))

    MODELFILE=$MODELDIR/${NAME}-${numtable}.coom
    sed -e "s/NUMTABLE/${numtable}/g" -e "s/MAXPLACES/${maxplaces}/g" $TEMPLATE > $MODELFILE

    # for totalplaces in $(seq $init 100 $maxplaces)
    for ratio in 2 4 6
    do
        requiredplaces=$((numtable*ratio))
        USERFILE=$INSTANCEDIR/${NAME}-${numtable}_user-input-${requiredplaces}.coom
        echo "set totalPlaces[0] = ${requiredplaces}" > $USERFILE
        # sed -e "s/NUMTABLE/${numtable}/g" -e "s/TOTALPLACES/${requiredplaces}/g" $TEMPLATE
    done
done
