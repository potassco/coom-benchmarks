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
    maxVolume=$((($side**3)/1000))

    # Model
    modelName=${NAME}-s${side}
    modelFile=$MODELDIR/$modelName.coom
    sed -e "s/SIDE/${side}/g" -e "s/MAXVOLUME/${maxVolume}/g" $TEMPLATE > $modelFile

    # for totalplaces in $(seq $init 100 $maxplaces)
    for ratio in 2 4 6 8
    do
        requiredvolume=$((maxVolume*ratio/10))
        userFile=$INSTANCEDIR/${modelName}_user-input-${requiredvolume}.coom
        echo "set requestedVolume[0] = ${requiredvolume}" > $userFile
    done
done
