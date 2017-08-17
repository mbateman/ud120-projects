import math
from math import ceil
### left_term = 0.5
### right_term = 0.5
left_term = 2.0/3.0
right_term = 1.0/3.0
res = - left_term * math.log(left_term, 2) - right_term * math.log(right_term, 2) 
print("%.4f" % res)
