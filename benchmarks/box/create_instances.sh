#!/bin/bash

TEMPLATE=model.coom
MODELDIR=models
INSTANCEDIR=instances
NAME=box

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

for side in $(seq 50 25 150)
do
    maxvolume=$((($side**3)/1000))

    # Model
    MODELNAME=${NAME}-s${side}
    MODELFILE=$MODELDIR/$MODELNAME.coom
    sed -e "s/SIDE/${side}/g" -e "s/MAXVOLUME/${maxvolume}/g" $TEMPLATE > $MODELFILE

    # for totalplaces in $(seq $init 100 $maxplaces)
    for ratio in 2 4 6 8
    do
        requiredvolume=$((maxvolume*ratio/10))
        USERFILE=$INSTANCEDIR/${MODELNAME}_user-input-${requiredvolume}.coom
        echo "set requestedVolume[0] = ${requiredvolume}" > $USERFILE
    done
done
