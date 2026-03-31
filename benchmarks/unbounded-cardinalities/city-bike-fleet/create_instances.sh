#!/bin/bash

# TEMPLATE=model.coom
# MODELDIR=models
INSTANCEDIR=instances
NAME=citybike

# rm -rf $MODELDIR
# mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

for numBikes in 12 16 25 33 50 66 75 88 100 125 150 175 200
do
    userFile=$INSTANCEDIR/citybike_user-input-n${numBikes}.coom
    for n in $(seq 0 $(($numBikes-1)))
    do
        echo "add bikes[${n}]" >> $userFile
    done
done
