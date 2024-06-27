#!/bin/bash

source scripts/vars.env

echo "Re-running failed instances"
echo

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Removing .finished files of failed instances"

for i in $(find $1 -name "runsolver.watcher" -exec grep -q "runlim error" {} \; -print); do
    rm -f "${i/runsolver.watcher/".finished"}"
done

echo "Generating new run scripts"
for rs in $RUNSCRIPT_PATH; do
    echo "Running ${rs}"
    ./bgen $rs
done

echo "Running benchmarks"
if [ $MODE == "pbs" ]; then
    for d in $(ls ./${OUTPUT_DIR}); do
        echo "Running ${d} start.sh file."
        ./${OUTPUT_DIR}/${d}/${PROJECT}/${MACHINE}/start.sh
    done
else
    echo "Invalid mode"
fi
