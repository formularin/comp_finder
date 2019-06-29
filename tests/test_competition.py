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


data_files = [file for file in os.listdir(f'{cwd}/tests') if 'data.txt' in file]
test_competitions = [comp(file) for file in data_files]

class TestCompetition(unittest.TestCase):

    def test_reached_competitor_limit(self):
        
        reached_competitor_limits = [False, True]
        
        for limit_reached, comp in zip(
            reached_competitor_limits, test_competitions):
            self.assertEqual(limit_reached, comp.reached_competitor_limit)

    def test_venue_address(self):
        
        venue_addresses = ['1 University Rd, Boston, MA 02215, USA', 
                           '1157 State Rte 55, Lagrangeville, NY 12540']

        for venue_address, comp in zip(
            venue_addresses, test_competitions):
            self.assertEqual(venue_address, comp.venue_address)

    def test_driving_distance(self):
        
        driving_distances = ['6 h 58 min', '5 h']

        for distance, comp in zip(
            driving_distances, test_competitions):
            self.assertEqual(distance, comp.driving_distance)

    def test_message(self):
        
        for file, comp in zip(
            [file for file in os.listdir(f'{cwd}/tests') 
                if 'message.txt' in file],
            test_competitions):
            
            with open(f'{cwd}/tests/{file}', 'r') as f:
                self.assertEqual(f.read(), str(comp))


if __name__ == '__main__':
    unittest.main()