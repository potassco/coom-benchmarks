#!/bin/bash

DOMAIN=$1

source scripts/vars.env

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Cleaning up old results"
if [ -d $RESULTS_DIR ]; then
    rm -f ${RESULTS_DIR}/${DOMAIN}.*
else
    mkdir $RESULTS_DIR
fi

echo "Evaluating results for ${DOMAIN}"
eval_file=${RESULTS_DIR}/${DOMAIN}.xml
./beval $RUNSCRIPT_PATH > ${eval_file} 2> ${eval_file}.error

echo "Computing .ods file"
ods_file=${RESULTS_DIR}/${DOMAIN}.ods
./bconv -m time,models,timeout,error,memout ${eval_file} > ${ods_file} 2> ${ods_file}.error
