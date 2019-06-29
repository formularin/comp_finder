#!/bin/bash

# install package dependencies
pip install -r requirements.txt

# start process and save PID
nohup python -m comp_finder/__init__.py >/dev/null 2>&1
processInfo=$(ps -ef | grep "__init__.py")
i=0
function get_pid {
  for line in $(echo $processInfo | tr " " "\n")
  do
    if [ $i == 0 ];
    then
        echo $line
    fi
  i=$((i + 1))
  done
}

PID=$(get_pid)

# echo PID to console and file
echo $PID > save_pid.txt
echo 'The PID for comp_finder.py is' $PID
echo 'to kill the process:\nkill' $PID
