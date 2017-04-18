"""
This is a simple program that models 1-D Brownian motion. I orginally got the idea from my
my final project in one of classes. The original code was in C and called the OpenGl library to 
plot the points. It also took over 100+ lines of code compared to just 12.
"""


import numpy as np
import matplotlib.pyplot as plt


#These two variables generate the 2 arrays of random numbers
#It uses a Normal Distr.
x1 = np.random.standard_normal(100)
x2 = np.random.standard_normal(100)

plt.plot(x1, 'Green')
plt.plot(x2, 'Purple')
plt.title('1-D Brownian Motion')
plt.xlabel('Step')
plt.ylabel('Distance from Origin')
plt.show()