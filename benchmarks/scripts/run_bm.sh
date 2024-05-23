#!/bin/bash

source benchmarks/scripts/vars.env

make clean-output

cd $BT_DIR
./bgen $RUNSCRIPT_PATH

for f in $(find $OUTPUT_DIR -type f -name "start.py");
do
    ./$f
done
