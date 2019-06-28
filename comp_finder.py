#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""Checks WCA competitions (in the USA) and records information about ones close to you.

Usage:
python comp_finder.py state1 [state2 state3 ...]
"""

from selenium.webdriver import Chrome, ChromeOptions
import os
import time

PAGE_URL = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=USA&search=&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'
cwd = os.getcwd()

# finds nearby states
with open(f'{cwd}/states.txt', 'r') as f:
    states = f.read().split('\n')

if states == []:
    import sys

    states = sys.argv[2:]

    with open(f'{cwd}/states.txt', 'w+') as f:
        f.write('\n'.join(states))


# create webdriver without physical window
op = ChromeOptions()
op.add_argument('headless')
driver = Chrome(f'{cwd}/chromedriver', options=op)

driver.get(PAGE_URL)

