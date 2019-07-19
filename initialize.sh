#!/bin/bash

# install package dependencies
pip3 install -r requirements.txt

# add comp_finder to your $PATH variable by editing your .bash_profile and create alias 'comp_finder' for 'comp_finder.sh'
cwd=$(pwd)
echo $'\n\n# setting PATH for comp_finder\nexport PATH\nexport PATH='${cwd}$':$PATH\nalias comp_finder=\'comp_finder.sh\'' >> ~/.bash_profile
