""" 
This is a program that calculates the numerical and actual derivative of Sin(x)
"""
from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import plot, show, legend, title

#Calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)
dy = y[1:]-y[:-1]
dx = x[1:]-x[:-1]
dy_dx = dy/dx
centers_x = (x[1:]+x[:-1])/2.0

plot(centers_x, dy_dx,'rx', centers_x, cos(centers_x),'b-')
title(r"$\rm{Derivative\ of}\ sin(x)$")
legend(('numerical', 'actual'), loc='lower left')
show()