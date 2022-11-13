import os
from os.path import getsize, join

for root, dirs, files in os.walk('C:/Users/petyo/Downloads'):
    for name in files:
        print(name, getsize(join(root, name)), 'Kb')
