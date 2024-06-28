#!/bin/bash

source scripts/vars.env

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Cleaning up old results"
rm -rf $RESULTS_DIR
mkdir $RESULTS_DIR

echo "Evaluating results"
for rs in $RUNSCRIPT_PATH; do
    eval=$(echo $rs | cut -d'-' -f 4)
    name=${eval%.*}

    echo "Calculating ${name}"
    eval_file=${RESULTS_DIR}/${eval}
    ./beval $rs > ${eval_file} 2> ${eval_file}.error

    echo "Computing .ods file"
    ods_file=${RESULTS_DIR}/${name}.ods
    ./bconv -m time,models,timeout,error,memout ${eval_file} > ${ods_file} 2> ${ods_file}.error
done
