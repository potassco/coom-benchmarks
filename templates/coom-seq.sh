#!/bin/bash
# https://github.com/arminbiere/runlim

cd "$(dirname $0)"

runner=( "{root}/programs/runlim" \
  {options} \
  --space-limit={memout} \
  --output-file=runsolver.watcher \
  --real-time-limit={timeout} \
  "{root}/programs/{solver}" \
  {sys_cmd} {setting_cmd} {inst_cmd} \
  {sys_cmd_post} {setting_cmd_post} {inst_cmd_post} )

instance={files}

if [[ $instance == *"user-input"* ]]; then
    model=$(echo $instance | sed "s/instances/models/" | sed "s/_user-input.*/\.coom/")
    userinput=$instance
else
    model=$instance
    userinput=""
fi

input=(  )

if [[ ! -e .finished ]]; then
  "${{runner[@]}}" $model -u "$userinput" > runsolver.solver
fi

touch .finished
