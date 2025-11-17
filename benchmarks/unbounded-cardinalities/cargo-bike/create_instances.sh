#!/bin/bash

MODELDIR=models
INSTANCEDIR=instances
NAME=cargobike

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

for model in simple complex; do
    template=model-${model}.coom

    for range in 100 200 300 400 500; do

        # Model
        modelName=${NAME}-${model}-${range}
        modelFile=$MODELDIR/$modelName.coom
        sed -e "s/MAX/${range}/g" $template > $modelFile

        python generate.py --range $range --instances 20 --out $INSTANCEDIR --model $modelName
    done
done
