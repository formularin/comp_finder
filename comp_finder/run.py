import sys
import os

cwd = os.getcwd()

sys.path.append(cwd)

from comp_finder.find_comps import find_comps
import daemon



def main():
    with open(sys.argv[3], 'r') as f:
        states = f.read().split('\n')

    if states == [] or states == ['']:
        raise Exception(f'No states in {sys.argv[3]}.' + 
                        ' States in file should be separated in file by newline characters.')

    location = sys.argv[2].replace('-', ' ')

    find_comps(sys.argv[1], states, location)


def run():
    with daemon.DaemonContext():
        main()


pid = os.getpid()
file = f'/Users/{cwd.split("/")[2]}/comp_finder_PID.txt'
with open(file, 'w+') as f:
    f.write(str(pid))
print('The PID for this process is %s' % pid)
print('To kill this process, use the command:\nkill %s' % pid)
print('The PID is stored in %s' % file)

if __name__ == '__main__':
    run()
