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
for rs in $RUNSCRIPT_PATH; do
    echo "Running ${rs}"
    ./bgen $rs
done

echo "Running benchmarks"
if [ $MODE == "seq" ]; then
    echo "Running start.py file"
    ./${OUTPUT_DIR}/${PROJECT}/${MACHINE}/start.py
elif [ $MODE == "pbs" ]; then
    echo "Running start.sh file(s)"
    for d in $(ls ./${OUTPUT_DIR}); do
        echo "Running ${d} start.sh file."
        ./${OUTPUT_DIR}/${d}/${PROJECT}/${MACHINE}/start.sh
    done
else
    echo "Invalid mode"
fi
