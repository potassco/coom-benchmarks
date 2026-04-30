#!/bin/bash

TEMPLATE=model.coom
MODELDIR=models-unbounded
INSTANCEDIR=instances
NAME=cargobike

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR


for range in 100 200 300 400 500; do

    # Model
    modelName=${NAME}-${range}
    modelFile=$MODELDIR/$modelName.coom
    sed -e "s/MAX/${range}/g" $TEMPLATE > $modelFile

    python generate.py --range $range --instances 5 --out $INSTANCEDIR --model $modelName
done
