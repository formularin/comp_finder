#!/bin/bash

# this file adds comp_finder to your $PATH variable by editing your .bash_profile
cwd=$(pwd)
echo $'\n\n# setting PATH for comp_finder\nexport PATH\nexport PATH='${cwd}$':$PATH\nalias comp_finder=\'comp_finder.sh\'' >> ~/.bash_profile
