#!/bin/bash

# incorrect number of arguments given
if [ "$#" != 3 ] ; then

  # help option
  if [ "$1" = '-h' ] || [ "$1" = '--help' ] ; then
    # script prints comp_finder docstring
    python3 man.py

  else
    echo 'incorrect number of arguments'
    echo 'Use -h or --help for info about usage.'
  fi

# correct number of arguments given
else

  # run script with arguments
  python3 comp_finder/run.py $@
fi
