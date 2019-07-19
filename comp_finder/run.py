import sys
import os
import daemon

cwd = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
if cwd not in sys.path:
    sys.path.append(cwd)

from comp_finder.find_comps import find_comps


def main():
    """runs find_comps() with given args"""
    with open(sys.argv[3], 'r') as f:
        states = f.read().split('\n')

    if states == [] or states == ['']:
        raise Exception(f'No states in {sys.argv[3]}.' + 
                        ' States in file should be separated in file by newline characters.')

    location = sys.argv[2].replace('-', ' ')

    find_comps(sys.argv[1], states, location)


def run():
    """Runs main() as daemon process"""
    with daemon.DaemonContext(
        stderr=open(f'{cwd}/comp_finder_errors.txt', 'w+')):
        main()


print('Comp Finder is running. To kill it, use the commands below:')
print()
print('processDetails=$(ps -ef | grep run.py)[0]\ndetailsArray=($processDetails)\npid="${detailsArray[1]}"\nkill $pid')


if __name__ == '__main__':
    run()
