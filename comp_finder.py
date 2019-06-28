#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""Checks WCA competitions (in the USA) and records information about ones close to you.

Usage:
python comp_finder.py current_location state1 [state2 state3 ...]
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

    # if states not specified when script was run
    if states == []:
        raise Exception('No states inputted')

    with open(f'{cwd}/states.txt', 'w+') as f:
        f.write('\n'.join(states))


# create webdriver without physical window
op = ChromeOptions()
op.add_argument('headless')
driver = Chrome(f'{cwd}/chromedriver', options=op)


class Competition:
    """Object to hold all information about a WCA competition"""
    def __init__(self, name, date, location, url, venue):
        # all attributes defined here can be found in the WCA competitions page
        # the @property methods find information that must be found on the competition's individual page.
        self.name = name
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
        return ''


    @property
    def venue_address(self):
        """Finds address to competition venue"""
        return ''
 

    @property
    def driving_distance(self):
        """Finds the driving distance from your location to the competition
        
        Args:
            current_location -- address of where you want to drive to the competition from

        Returns:
            str -- hours h minutes min
        """
        return ''

    def __str__(self):
        """Creates message containing complete information
        
        Message to be written to text file with other competitions
        """
        info_list = [
                ''.join(['=' for i in range(100)]),
                '',
                self.name.upper() + ':',
                self.url,
                '',
                f'date: {self.date}',
                f'location: {self.location}',
                f'venue: {self.venue} - {self.venue_address}',
                f'distance: {self.driving_distance}',
            ]
        
        if self.reached_competitor_limit:
            info_list.append('reached competitor limit')
        
        string = '\n'.join(info_list)

        return string

    __repr__ = __str__


# Various XPaths for competition info elements
COMPETITION = '//li[@class="list-group-item not-past"]'
LOCATION = './/div[@class="location"]'
LINK = './/div[@class="competition-link"]/a'
DATE = './/span[@class="date"]'
VENUE = './/div[@class="venue-link"]/p'

driver.get(PAGE_URL)

# finds all list elements for competitions on competitions page
competitions_elements = driver.find_elements_by_xpath(COMPETITION)

# list to be filled with Competition objects
competitions = []

for elem in competitions_elements:
    comp_location = elem.find_element_by_xpath(LOCATION).text
    
    # checks if competition is in any of the local states
    if comp_location.split(', ')[-1] in states:
        # find various info about competition

        comp_name = elem.find_element_by_xpath(LINK).text
        comp_date = elem.find_element_by_xpath(DATE).text
        comp_venue = elem.find_element_by_xpath(VENUE).text
        comp_link = elem.find_element_by_xpath(LINK).get_attribute('href')

        competitions.append(
            Competition(comp_name, comp_date, comp_location, comp_link, comp_venue)
            )

    with open(f'{cwd}/output.txt', 'w+') as f:
        f.write('\n\n'.join([str(i) for i in competitions]))
