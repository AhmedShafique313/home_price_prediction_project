# using formula to calculate the actual price of house using formula which is y = m*x + c 
# and based on it I will create a graph for visulaization
# its also a linear regression with straight line prediction of houses


# basic libraries are imported 
import numpy as np
import matplotlib.pyplot as plt

# now create a random dataset using numpy 

np.random.seed(24)
# now generating square feet dataset of random numbers 
# X = size means its a square feet

x = np.random.randint(100, 900, 250)
# it created a dataset of 250 numbers between 100 to 900

# unit of size means that the size increases = price increases 50 times 
unit = 50
m = unit
# constant rate of land for house  = if m*x is zero then the will be 50000 rupees in Pakistan 

rate = 50000
c = rate

# lets calculate the following price of house
def calculating_prices(size):
    return m*size + c


# Now calculating actual list of prices of houses 
Prices = [calculating_prices(size) for size in x]

# if you want to print the data then 
# print(Prices)

# plotting the data 

# plt.style.use("D:\AIoT Engineering\House Price Prediction project without Skitlearn/deeplearning.mplstyle")
plt.scatter(x, Prices, color = 'red', label = 'Prices of Houses')
plt.xlabel('Size of houses')
plt.ylabel('Prices of houses')
plt.legend()
plt.show()
