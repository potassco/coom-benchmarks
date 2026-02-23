#!/bin/bash

TEMPLATE=model.coom
MODELDIR=models
INSTANCEDIR=instances
NAME=travelbike

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

for maxBikes in 5 10 15 20
do
    maxPrice=$((100*maxBikes))
    maxVolume=$((100*maxBikes))
    modelName=${NAME}-max${maxBikes}
    modelFile=$MODELDIR/$modelName.coom
    sed -e "s/MAXBIKES/${maxBikes}/g" -e "s/MAXPRICE/${maxPrice}/g" -e "s/MAXVOLUME/${maxVolume}/g" $TEMPLATE > $modelFile

    for i in {1..10}
    do
        userVolume=$((1 + $RANDOM % $maxVolume))
        userPrice=$((1 + $RANDOM % $maxPrice))

        userFile=$INSTANCEDIR/${modelName}_user-input-p${userPrice}-v${userVolume}.coom

        echo "set maxPrice[0] = ${userPrice}" >> $userFile
        echo "set requestedVolume[0] = ${userVolume}" >> $userFile
    done
done
