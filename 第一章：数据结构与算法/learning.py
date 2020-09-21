# 需要掌握一些基础的包 以及内置的常用函数，加快处理
# 学习这个用来记笔记的话还是用jupyter notebook比较好一点

from collections import Counter
# most_common


# 没有理解的这个*号
a = slice(5, 50, 2)
s = 'HelloWorld'
a.indices(len(s)) # (5, 10, 2)
for i in range(*a.indices(len(s))):
  print(s[i])


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
