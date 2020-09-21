
import re 

# re.split()

# str.startswith()

# str.endswith()

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
        
from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')

fnmatch('foo.txt', '?oo.txt')

fnmatch('Dat45.csv', 'Dat[0-9]*')

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
