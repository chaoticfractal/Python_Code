"""
This programs calculates the integral of Sin(x) and again shows the comparision between 
numerical (calculated by the Trapizoid rule) and the actual integral of Sin(x) 
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, legend, suptitle

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)
dx = x[1:]-x[:-1]
avg_height = (y[1:]+y[:-1])/2.0
int_sin = cumsum(dx * avg_height)

closed_form = 1 - cos(x)
plot(x[1:], int_sin,'rx', x, closed_form,'b-')
legend(('numerical', 'actual'))
suptitle(r"$\int \, \sin(x) \, dx$")
show()

