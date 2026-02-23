#!/bin/bash

TEMPLATE=model.coom
MODELDIR=models
INSTANCEDIR=instances
NAME=metro

rm -rf $MODELDIR
mkdir $MODELDIR

rm -rf $INSTANCEDIR
mkdir $INSTANCEDIR



for minlength in 10 20 30 40 50
do
    minlength_mm=$(($minlength*1000))
    maxlength_mm=$(($minlength*2000))
    minload=$(($minlength*5))
    maxload=$(($minlength*20))
    maxseats=$((minlength*8))

    modelName=${NAME}-${minlength}
    MODELFILE=$MODELDIR/${modelName}.coom
    sed -e "s/MINLENGTH/${minlength_mm}/g" -e "s/MAXLENGTH/${maxlength_mm}/g" -e "s/MINLOAD/${minload}/g" -e "s/MAXLOAD/${maxload}/g" -e "s/MAXSEAT/${maxseats}/g" $TEMPLATE > $MODELFILE


    ### Create sequence of user actions as user inputs
    # User Action 1: Set num_passengers to minlength*16
    USERFILE1=$INSTANCEDIR/${modelName}_user-input-1.coom
    numpassengers=$(($minlength*16))
    echo "set num_passengers[0] = ${numpassengers}" > $USERFILE1


    # User Action 2: Add minlength*3 seats
    USERFILE2=$INSTANCEDIR/${modelName}_user-input-2.coom
    # echo "set num_passengers[0] = ${numpassengers}" > $USERFILE2
    cp $USERFILE1 $USERFILE2

    numseats=$(($minlength*3))
    for i in $(seq 0 $(($numseats-1)))
    do
        echo "add seat[${i}]" >> $USERFILE2
    done

    # User Action 3: Set standing room to minlength*14
    USERFILE3=$INSTANCEDIR/${modelName}_user-input-3.coom
    cp $USERFILE2 $USERFILE3
    standingroom=$(($minlength*14))
    echo "set standing_room[0] = ${standingroom}" >> $USERFILE3

    # User Action 4: Delete the last minlength seats (equals adding minlength*2 seats)
    USERFILE4=$INSTANCEDIR/${modelName}_user-input-4.coom
    cp $USERFILE1 $USERFILE4
    echo "set standing_room[0] = ${standingroom}" >> $USERFILE4

    numseats=$(($minlength*2))
    for i in $(seq 0 $(($numseats-1)))
    do
        echo "add seat[${i}]" >> $USERFILE4
    done

    # User Action 5: Set every 20th seat as special
    USERFILE5=$INSTANCEDIR/${modelName}_user-input-5.coom
    cp $USERFILE4 $USERFILE5
    for special in $(seq 0 20 $(($numseats-1)))
    do
        echo "set seat[${j}].type[0] = Special" >> $USERFILE5
    done

    # User Action 6: Maximization (skip for now)

    # User Action 7: Set Handrail type to Premium
    USERFILE7=$INSTANCEDIR/${modelName}_user-input-7.coom
    cp $USERFILE5 $USERFILE7
    echo "set handrail[0].type[0] = Premium" >> $USERFILE7
done
