# 学到了，用round还可以处理百位，


# decimal包用来处理浮点数的
from decimal import Decimal
from decimal import localcontext


#bin(),oct(),hex()

# 复数
import cmath
a = complex(2, 4)
a.real
a.imag
a.conjugate()

from fractions import Fraction

from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
  
# 这个函数比下面的strptime方法快7倍
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')

from pytz import timezone



