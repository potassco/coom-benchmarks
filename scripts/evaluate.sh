#!/bin/bash

source scripts/vars.env

cd $BT_DIR

rm -rf $RESULTS_DIR
mkdir $RESULTS_DIR

./beval $RUNSCRIPT_PATH > ${RESULTS_DIR}/evaluated.xml
