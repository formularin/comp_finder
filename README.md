# comp_finder
comp_finder is a python program that logs information about all the WCA cubing competitions in a set of given states.

comp_finder has only been tested on mac OS X, but should work on any Unix-based operating system. Windows support is coming soon...

## Installation
Use [git](https://git-scm.com/) to install comp_finder:
```bash
git clone https://github.com/lol-cubes/comp_finder.git
```
Use the command below to add comp_finder.sh to your ```PATH``` and create an alias for comp_finder:
```bash
./initialize.sh
```
This just allows you to run comp_finder from anywhere and not have to use the ".sh" extesnion.

## Usage

```bash
comp_finder /path/to/output_file.txt address /path/to/states_file.txt
```

The address should be a standard postal service address, but it can also be coordinates.

```states_file.txt``` must contain state names separated by newlines and capitalized properly.

The contents of an example states file:
```
New York
West Virginia
Arizona
```

## Dependencies
All dependencies (except python 3.x) are installed during initialization.
The python libraries incorporated into for comp_finder are:
 - selenium
 - python-daemon
