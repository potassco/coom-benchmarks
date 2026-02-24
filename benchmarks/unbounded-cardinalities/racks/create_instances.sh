#!/bin/bash

# MODELDIR=models
INSTANCEDIR=instances

# rm -rf $MODELDIR
# mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

# # Simple model benchmarks
# TEMPLATE=model-simple.coom
# NAME=racks-simple

for num_elements in {1..20}
do
    userFile=$INSTANCEDIR/racks_user-input-${num_elements}.coom
    touch $userFile

    i=0
    for type in A B C D; do
        for j in $(seq 0 $(($num_elements-1))); do
            current_element="elements[${i}]"
            echo "add $current_element" >> $userFile
            echo "set $current_element.type[0]=$type" >> $userFile
            i=$(($i+1))
        done
    done
done

