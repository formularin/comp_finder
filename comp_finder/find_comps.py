import sys
import os

cwd = os.getcwd()
sys.path.append(f'/Users/{cwd.split("/")[2]}/Desktop/comp_finder')

from selenium.webdriver import Chrome, ChromeOptions
from comp_finder.competition import Competition
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


# Various XPaths for competition info elements
COMPETITION = '//li[@class="list-group-item not-past"]'
LOCATION = './/div[@class="location"]'
LINK = './/div[@class="competition-link"]/a'
DATE = './/span[@class="date"]'
VENUE = './/div[@class="venue-link"]/p'

def find_comps():
    # update output.txt every 30 minutes
    while True:

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
                comp_link = 'https://www.worldcubeassociation.org' + \
                    elem.find_element_by_xpath(LINK).get_attribute('href')

                competitions.append(
                    Competition(comp_name, comp_date, comp_location, 
                                    comp_link, comp_venue, driver)
                    )
            
            time.sleep(900)

        with open(f'{cwd}/output.txt', 'w+') as f:
            f.write('\n\n'.join([str(i) for i in competitions]))
