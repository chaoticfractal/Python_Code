"""
This is a 3D version of the Brownian motion program. I am planning on making a 2nd version that 
will be more elaborate
"""


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, projection='3d')

z = np.random.standard_normal(100)
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)

ax1.scatter(x,y,z)
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.set_zlabel('Z-Axis')
ax1.set_title('3D Brownian Motion')
plt.show()