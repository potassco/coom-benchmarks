#!/bin/bash

TEMPLATE=model.coom
MODELDIR=models
INSTANCEDIR=instances
NAME=citybike

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

for maxBikes in 50 100 150 200
do
    modelName=${NAME}-max${maxBikes}
    modelFile=$MODELDIR/${modelName}.coom
    sed -e "s/MAXBIKES/${maxBikes}/g" $TEMPLATE > $modelFile

    for ratio in 4 3 2 1
    do
        numBikes=$((maxBikes/ratio))

        userFile=$INSTANCEDIR/${modelName}_user-input-n${numBikes}.coom
        for n in $(seq 0 $(($numBikes-1)))
        do
            echo "add bikes[${n}]" >> $userFile
        done
    done
done
