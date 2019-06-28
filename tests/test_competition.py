import sys
import os

cwd = os.getcwd()
sys.path.append(f'/Users/{cwd.split("/")[2]}/Desktop/comp_finder')

from comp_finder.find_comps import driver
from comp_finder.competition import Competition
import unittest


# Competition objects for testing
def comp(file):
    """Takes file and returns Competition object with data from file"""
    with open(f'{cwd}/tests/{file}', 'r') as f:
        comp_data = f.read().split('\n')

    comp_data.append(driver)
    
    return Competition(*comp_data)


data_files = [file for file in os.listdir(f'{cwd}/tests') if '.txt' in file]
test_competitions = [comp(file) for file in data_files]

class TestCompetition(unittest.TestCase):

    def test_reached_competitor_limit(self):
        
        reached_competitor_limits = [False, True]
        
        for limit_reached, comp in zip(
            reached_competitor_limits, test_competitions):
            self.assertEqual(limit_reached, comp.reached_competitor_limit)

    def test_venue_address(self):
        pass

    def test_driving_distance(self):
        pass

    def test_message(self):
        pass


if __name__ == '__main__':
    unittest.main()
