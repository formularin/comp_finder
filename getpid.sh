#!/bin/bash

processLines=$(ps -ef | grep run.py | tr ' ' $'\n') 
i=0
for line in $processLines ; do
  if [ $i = 1 ] ; then
    echo $line
  fi
  ((i++))
done
