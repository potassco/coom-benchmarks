#!/bin/bash

parse_file=../parser/parse.py
asp_dir=asp
coom_dir=coom


for dir in $(ls -d -- */)
do
    current_asp_dir=${dir}${asp_dir}
    if [ ! -d $current_asp_dir ]
    then
        mkdir $current_asp_dir
    fi

    current_coom_dir=${dir}${coom_dir}
    for instance in $(ls $current_coom_dir)
    do
        outfile=$current_asp_dir/${instance/.coom/.lp}
        python $parse_file $current_coom_dir/$instance > $outfile
    done
done



