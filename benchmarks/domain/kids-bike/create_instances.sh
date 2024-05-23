#!/bin/bash

for numfeat in $(seq 10 2 20); do
    for numopt in $(seq 10 5 50); do
        for consize in 2 3 4; do
            python generate.py -f $numfeat -o $numopt -c $consize
        done
    done
done
