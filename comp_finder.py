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


class Competition:
    """Object to hold all information about a WCA competition"""
    def __init__(self, date, location, url, venue):
        # all attributes defined here can be found in the WCA competitions page
        # the @property methods find information that must be found on the competition's individual page.
        self.date = date
        self.location = location
        self.url = url
        self.venue = venue


    @property
    def reached_competitor_limit(self):
        """tells if the competitor limit for the competition has been reached
        
        Returns:
            bool -- True if it has been reached, False if not
        """
        pass


    @property
    def driving_distance(self, current_location):
        """Finds the driving distance from your location to the competition
        
        Args:
            current_location -- address of where you want to drive to the competition from

        Returns:
            str -- hours h minutes min
        """
        pass


    @property
    def text(self):
        """Creates message containing complete information
        
        Message to be written to text file with other competitions
        """
        pass

driver.get(PAGE_URL)

competitions_elements = driver.find_elements_by_xpath('//li[@class="list-group-item not-past"]')
