import sys

cwd = '/'.join(__file__.split('/')[:-1])
sys.path.append(f'/Users/{cwd.split("/")[2]}/Desktop/comp_finder')

from comp_finder.find_comps import find_comps

# finds nearby states
with open(sys.argv[3], 'r') as f:
    states = f.read().split('\n')

if states == [] or states == ['']:
    raise Exception(f'No states in {sys.argv[3]}.' + 
                    ' States in file should be separated in file by newline characters.')

location = sys.argv[2].replace('-', ' ')

find_comps(sys.argv[1], states, location)

