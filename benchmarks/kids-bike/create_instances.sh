#!/bin/bash



for numfeat in $(seq 5 5 20)
do
    for numopt in $(seq 5 5 20)
    do
        python generate.py -f $numfeat -o $numopt
    done
done
