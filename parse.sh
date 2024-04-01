#!/bin/bash

parse_file=parser/parse.py
asp_dir=examples/asp

instance_name=$(basename $1)
outfile=$asp_dir/${instance_name/.coom/.lp}

if [ ! -d $asp_dir ]
then
    mkdir $asp_dir
fi

if [ -e $1 ]
then
    python $parse_file $1 > $outfile
fi
