import unittest
import subprocess
import os


comp_finder_dir = '/'.join(os.getcwd().split('/')[:-1])


class TestCompFinder(unittest.TestCase):

    def test_comp_finder(self):
        
        # test with states specified when running
        subprocess.run([comp_finder_dir + '/tests/find_comps.sh', '1600-Pennsylvania-Ave-NW,-Washington,-DC-20500',  
                        comp_finder_dir + '/output.txt', comp_finder_dir + '/states.txt'])


if __name__ == '__main__':
    unittest.main()
