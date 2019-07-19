import os
import sys

cwd = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
if cwd not in sys.path:
    sys.path.append(cwd)

import comp_finder

print(comp_finder.__doc__)