#!/bin/bash
# https://github.com/arminbiere/runlim

cd "$(dirname $0)"

instance={run.files}

if [[ $instance == *"user-input"* ]]; then
    model=$(echo $instance | sed "s/instances/models/" | sed "s/_user-input.*/\.coom/")
    userinput=$instance
else
    model=$instance
    userinput=""
fi

[[ -e .finished ]] || "{run.root}/programs/runlim" \
	--space-limit={run.memout} \
	--output-file=runsolver.watcher \
	--real-time-limit={run.timeout} \
    --kill-delay=1000 \
	"{run.root}/programs/{run.solver}" $model {run.args} -u "$userinput" > runsolver.solver


touch .finished
