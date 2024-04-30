#!/bin/bash



for numfeat in $(seq 10 2 20)
do
    for numopt in $(seq 10 5 50)
    do
        python generate.py -f $numfeat -o $numopt
    done
done
