#!/bin/bash

source scripts/vars.env

echo "Entering benchmark-tool directory"
cd $BT_DIR

echo "Cleaning up old results"
rm -rf $RESULTS_DIR
mkdir $RESULTS_DIR

echo "Evaluating results"
EVAL_FILE=${RESULTS_DIR}/${EVAL_NAME}.xml
./beval $RUNSCRIPT_PATH > ${EVAL_FILE} 2> ${EVAL_FILE}.error


ODS_FILE=${RESULTS_DIR}/${EVAL_NAME}.ods
echo "Computing .ods file"
if [ -s ${EVAL_FILE} ]; then
    # mv $DIR/$NAME.beval $DIR/$NAME.bevaltmp
    # cat $DIR/$NAME.bevaltmp | sed 's/measure name="status" type="float" val="2"\/>/measure name="status" type="float" val="2"\/>\n<measure name="atoms" type="float" val="NaN"\/>\n<measure name="bodies" type="float" val="NaN"\/>\n<measure name="calls" type="float" val="NaN"\/>\n<measure name="choices" type="float" val="NaN"\/>\n<measure name="conflicts" type="float" val="NaN"\/>\n<measure name="cons" type="float" val="NaN"\/>\n<measure name="csolve" type="float" val="NaN"\/>\n<measure name="ctime" type="float" val="NaN"\/>\n<measure name="equiv" type="float" val="NaN"\/>\n<measure name="models" type="float" val="NaN"\/>\n<measure name="ptime" type="float" val="NaN"\/>\n<measure name="rchoices" type="float" val="NaN"\/>\n<measure name="restarts" type="float" val="NaN"\/>\n<measure name="roriginal" type="float" val="NaN"\/>\n<measure name="rules" type="float" val="NaN"\/>\n<measure name="vars" type="float" val="NaN"\/>/g' > $DIR/$NAME.beval
    ./bconv -m time,models,timeout,error,memout ${EVAL_FILE} > ${ODS_FILE} 2> ${ODS_FILE}.error
else
    echo "${EVAL_FILE} is empty"
fi

