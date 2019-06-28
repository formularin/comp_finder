"""Checks WCA competitions (in the USA) and records information about ones close to you.

Usage:
python comp_finder.py current_location state1 [state2 state3 ...]
"""
import sys
import os

cwd = os.getcwd()
sys.path.append(f'/Users/{cwd.split("/")[2]}/Desktop/comp_finder')

from comp_finder.find_comps import find_comps
