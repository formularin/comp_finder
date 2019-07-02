import sys
import os

cwd = os.getcwd()

sys.path.append(cwd)

from comp_finder.find_comps import find_comps
import daemon
import subprocess


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


# get PID
subprocess.run(['cd', '..'])
subprocess.run(['chmod', '+x', 'getpid.sh'])
pid = subprocess.check_output('./getpid.sh', shell=True).decode('UTF-8').strip()

# write PID to file and print messages
file = f'/Users/{cwd.split("/")[2]}/comp_finder_PID.txt'
with open(file, 'w+') as f:
    f.write(str(pid))

print('The PID for this process is %s' % pid)
print('To kill this process, use the command:\nkill %s' % pid)
print('The PID is stored in %s' % file)

if __name__ == '__main__':
    run()
