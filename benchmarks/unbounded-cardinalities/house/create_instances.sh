#!/bin/bash

# MODELDIR=models
INSTANCEDIR=instances
NAME=house

# rm -rf $MODELDIR
# mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR

maxThings=5

for numPersons in $(seq 10 10 200); do
    userFile=$INSTANCEDIR/house_user-input-${numPersons}.coom
    touch $userFile

    for p in $(seq 0 $((numPersons-1))); do
        current_person="persons[${p}]"
        echo "add $current_person" >> $userFile

        maxShortThings=$((1 + $RANDOM % $maxThings))
        for t in $(seq 0 $((maxShortThings-1))); do
            current_thing="${current_person}.things[${t}]"
            echo "add $current_thing" >> $userFile

            echo "set $current_thing=Short" >> $userFile
        done

        maxLongThings=$((1 + $RANDOM % $maxThings))
        for t in $(seq 0 $((maxLongThings-1))); do
            current_thing="${current_person}.things[${t}]"
            echo "add $current_thing" >> $userFile

            echo "set $current_thing=Long" >> $userFile
        done
    done
done
