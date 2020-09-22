
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

# fnmatch的匹配能力介于简单的字符串方法和强大的正则表达式之间
# glob模块用于 文件名的匹配

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

# 这种情况replace函数会比使用translate()或者正则表达式要快很多
# 你需要执行任何复杂字符对字符的重新映射或者删除操作的话， translate() 方法会非常的快

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
    
text = ''.join(sample())
print(text)

#看完了，但是有很多不会，需要抽空再看一遍，练习一下才行。
