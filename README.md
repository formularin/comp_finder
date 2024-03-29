# Comp Finder
Comp Finder is a python program that logs information about all the WCA cubing competitions in a given set of states.
It checks the WCA website and updates the log every 30 minutes.

Comp Finder has only been tested on mac OS X, but should work on any Unix-based operating system. Windows support is coming soon...

## Installation
Use [git](https://git-scm.com/) to install Comp Finder:
```bash
git clone https://github.com/lol-cubes/comp_finder
```
Use the command below to add comp_finder.sh to your ```PATH``` and create an alias for Comp Finder:
```bash
./initialize.sh
```
This just allows you to run Comp Finder from any directory and not have to use the ".sh" extesnion.

## Usage
```bash
comp_finder /path/to/output_file.txt address /path/to/states_file.txt
```

The address is of the place you want to know the driving time to the competition from. 
Instead of spaces it should include '-' characters.
This can either be a standard postal service address or coordinates.

```states_file.txt``` must contain state names separated by newlines and capitalized properly.

The contents of an example states file:
```
New York
West Virginia
Arizona
```

## Output
Comp Finder redirects its output into the output file.
The format of the output should be as depicted below:
```
====================================================================================================

NAME OF COMPETITION:
https://www.worldcubeassociation.org/competitions/NameOfCompetition

date: Feb 30, 2020
venue: Example Venue Name - 11 Wall Street New York, NY
distance: 6 h 9 min
reached competitor limit
```
If the competitor limit is not yet reached, the output will not have a line for that.

Comp Finder also outputs to a file called ```comp_finder_errors.txt```, where the STDERR (all the errors) 
of the daemon process (the one running in the background) will go. 
This file should stay empty, but if it isn't feel free to create an issue, and I'll do my best to help.

## Dependencies
All dependencies (except python 3.x) are installed during initialization.
The python libraries incorporated into for Comp Finder are:
 - selenium
 - python-daemon
