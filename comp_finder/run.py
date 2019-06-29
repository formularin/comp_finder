import sys
import os

cwd = os.getcwd()
sys.path.append(f'/Users/{cwd.split("/")[2]}/Desktop/comp_finder')

from comp_finder.find_comps import find_comps

find_comps()
