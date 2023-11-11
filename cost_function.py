# defining cost function in this python program
import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(100, 900, 250)
c= 50000
from actual_price import Prices
def cost_function(x, c,  prices):
    m =x.shape[0]
    y = prices
    cost_sum = 0
    for i in range(m):
        f_wb = m*x[i] + c
        cost = (f_wb - y[i])**2
        cost_sum = cost_sum + cost
    total_cost = (1/(2*m) * cost_sum)
   
    return total_cost

print(cost_function(x, c, Prices))