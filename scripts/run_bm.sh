#!/bin/bash

DOMAIN=$1

source scripts/vars.env

echo "Copying runscripts"
make copy-runscripts

echo
echo "Mode: ${MODE}"
echo

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Cleaning up old output"
rm -rf ${OUTPUT_DIR}/${DOMAIN}

echo "Generating run scripts"
./bgen $RUNSCRIPT_PATH

echo "Running benchmarks"
if [ $MODE == "seq" ]; then
    echo "Running start.py file"
    ./${OUTPUT_DIR}/${DOMAIN}/${PROJECT}/${MACHINE}/start.py
elif [ $MODE == "pbs" ]; then
    echo "Running start.sh file for ${DOMAIN}"
    ./${OUTPUT_DIR}/${DOMAIN}/${PROJECT}/${MACHINE}/start.sh
else
    echo "Invalid mode"
fi
