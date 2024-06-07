#!/bin/bash

source scripts/vars.env

echo "Cleaning up old output"
make clean-output
make copy-runscripts

echo
echo "Mode: ${MODE}"
echo

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Generating run scripts"
./bgen $RUNSCRIPT_PATH

echo "Running benchmarks"
if [ $MODE == "seq" ]; then
    echo "Running start.py file"
    ./${OUTPUT_DIR}/${PROJECT}/${MACHINE}/start.py
elif [ $MODE == "pbs" ]; then
    echo "Running start.sh file"
    ./${OUTPUT_DIR}/${PROJECT}/${MACHINE}/start.sh
else
    echo "Invalid mode"
fi
