#!/bin/bash

source scripts/vars.env

echo "Entering benchmark-tool directory"
cd $BT_DIR

# echo "Cleaning up old results"
# rm -rf $RESULTS_DIR
# mkdir $RESULTS_DIR

echo "Evaluating results"
for rs in $RUNSCRIPT_PATH; do
    eval=${RESULTS_DIR}/$(echo $rs | cut -d'-' -f 4)
    name=${eval%.*}
    echo "Calculating ${eval}"
    ./beval $RUNSCRIPT_PATH > ${eval} 2> ${name}.error
done

# ODS_FILE=${RESULTS_DIR}/${EVAL_NAME}.ods
echo "Computing .ods files"
for eval in $(ls $RESULTS_DIR); do
    if [[ "${eval}" == *.xml ]]; then
        name=${eval%.*}
        ./bconv -m time,models,timeout,error,memout ${eval} > ${name}.ods 2> ${name}.error
    fi
