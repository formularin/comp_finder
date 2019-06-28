#!/bin/bash

source venv/bin/activate
nohup python -m comp_finder.py >/dev/null 2>&1
PID=$$
echo $PID > save_pid.txt
