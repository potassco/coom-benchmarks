#!/bin/bash

parse_file=../../parser/parse.py
asp_dir=asp
coom_dir=coom

parse_benchmark_set () {
    current_asp_dir=${1}${asp_dir}
    if [ ! -d $current_asp_dir ]
    then
        mkdir $current_asp_dir
    fi

    current_coom_dir=${1}${coom_dir}
    for instance in $(ls $current_coom_dir)
    do
        outfile=$current_asp_dir/${instance/.coom/.lp}
        python $parse_file $current_coom_dir/$instance > $outfile
    done
}

if [ -n "$1" ]
then
    echo "Parsing ${1}"
    parse_benchmark_set $1
else
    echo "Parsing all benchmarks sets"
    for dir in $(ls -d -- */)
    do
        parse_benchmark_set $dir
    done
fi





