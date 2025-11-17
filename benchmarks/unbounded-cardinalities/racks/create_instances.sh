#!/bin/bash

MODELDIR=models
INSTANCEDIR=instances

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

# Simple model benchmarks
TEMPLATE=model-simple.coom
NAME=racks-simple

for max in 10 20 30; do
    modelName=${NAME}-${max}
    modelFile=$MODELDIR/${modelName}.coom
    sed -e "s/MAX/${max}/g" $TEMPLATE > $modelFile

    steps=10
    step=$((max / steps))
    for ((i = 0; i < steps; i++)); do
        numElements=$((1 + i*step))
        userFile=$INSTANCEDIR/${modelName}_user-input-${numElements}.coom
        echo "set numA[0] = ${numElements}" > $userFile
        echo -e "set numB[0] = ${numElements}" >> $userFile
    done
done

# Complex model benchmarks
TEMPLATE=model-complex.coom
NAME=racks-complex

max=10
modelName=${NAME}-${max}
modelFile=$MODELDIR/${modelName}.coom
sed -e "s/MAX/${max}/g" $TEMPLATE > $modelFile

for numElements in 1 2 3 4 5 6 7 8 9 10; do
    userFile=$INSTANCEDIR/${modelName}_user-input-${numElements}.coom
        echo "set numA[0] = ${numElements}" > $userFile
        echo -e "set numB[0] = ${numElements}" >> $userFile
        echo -e "set numC[0] = ${numElements}" >> $userFile
        echo -e "set numD[0] = ${numElements}" >> $userFile
done
