# defining cost function in this python program
import numpy as np
import matplotlib.pyplot as plt
c= 50000
from actual_price import Prices, x
m =x.shape[0]
y = Prices

# loop 
for i in range(m):
    def cost_function(x, c,  prices): 
        cost_sum = 0
        for i in range(m):
            f_wb = m*x[i] + c
            cost = (f_wb - y[i])**2
            cost_sum = cost_sum + cost
            total_cost = (1/(2*m) * cost_sum)
   
        return total_cost


cost_values= [cost_function(x,c,Prices)]

