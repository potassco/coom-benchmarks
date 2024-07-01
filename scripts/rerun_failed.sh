#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

DOMAIN=$1

source scripts/vars.env

echo "Re-running failed instances of ${DOMAIN}"
echo

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Removing .finished files of failed instances"

for i in $(find . -name "runsolver.watcher" -exec grep -q "runlim error" {} \; -print); do
    rm -f "${i/runsolver.watcher/".finished"}"
done

echo "Generating new run scripts"
./bgen $RUNSCRIPT_PATH

echo "Running benchmarks"
if [ $MODE == "pbs" ]; then
    ./${OUTPUT_DIR}/${DOMAIN}/${PROJECT}/${MACHINE}/start.sh
else
    echo "Invalid mode"
fi
