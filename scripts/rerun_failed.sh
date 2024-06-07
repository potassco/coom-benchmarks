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
./bgen -e $RUNSCRIPT_PATH

echo "Running benchmarks"
if [ $MODE == "pbs" ]; then
    echo "Running start.sh file"
    ./${OUTPUT_DIR}/${PROJECT}/${MACHINE}/start.sh
else
    echo "Invalid mode"
fi
