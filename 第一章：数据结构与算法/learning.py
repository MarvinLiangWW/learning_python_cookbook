# 需要掌握一些基础的包 以及内置的常用函数，加快处理

from collections import Counter
# most_common


# 没有理解的这个*号
a = slice(5, 50, 2)
s = 'HelloWorld'
a.indices(len(s)) # (5, 10, 2)
for i in range(*a.indices(len(s))):
  print(s[i])
