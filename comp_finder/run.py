import sys
import os
import daemon

usr = os.getcwd().split("/")[2]
sys.path.append(f'/Users/{usr}/Desktop/comp_finder')

from comp_finder.find_comps import find_comps

def main():
    with open(sys.argv[3], 'r') as f:
        states = f.read().split('\n')

    if states == [] or states == ['']:
        raise Exception(f'No states in {sys.argv[3]}.' + 
                        ' States in file should be separated in file by newline characters.')

    location = sys.argv[2].replace('-', ' ')

    find_comps(sys.argv[1], states, location)


pid = os.getpid()
with open(f'/Users/{usr}/comp_finder_PID.txt', 'w+') as f:
    f.write(str(pid))
print('The PID for this process is %s' % pid)
print('To kill this process, use the command:\nkill %s' % pid)
print('The PID is stored in %s' % f'/Users/{usr}/comp_finder_PID.txt')

with daemon.DaemonContext():
    main()
