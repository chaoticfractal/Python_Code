""" 
--------------------------------------------------------------------------------------------
This one of the longer problems from the learning moduals
It pretty much involves importing data from a text file and creating numpy arrays with them
It requires the user to use slicing methods to collect the correct data from the text file's 
rows and columns
---------------------------------------------------------------------------------------------


Wind Statistics
----------------

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71
   
   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   cities in Ireland on that day.
   
   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds in Ireland.  In other words, reduce all the wind measurements
   from all the days and all the locations to a single set of statistics 
   for the entire dataset. 

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds for each of the cities (columns).  You should end up with 12
   results for each of the statistics.
   
4. Calculate the min, max and mean windspeed and standard deviations of the 
   windspeeds for every day (rows) in the data set.  Here you'll reduce all 
   the cities numbers to a set of statistics for each day.  There a thousands
   of days, so your resulting data sets will be large.
   
5. Find the city which has the greatest windspeed on each day 
   (an integer column number for each day). 

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each city.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months.


Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

"""

from numpy import loadtxt

wind_data = loadtxt('<Dir. where file is located>')

data_set = wind_data[:,3:]

#2 The Whole set of Data
print 'Whole Min:', data_set.min()
print 'Whole Max:', data_set.max()
print 'Whole Mean:', data_set.mean()
print 'Whole SD:', data_set.std()

#3 The Cities only
print 'City Min:', data_set.min(axis=0)
print 'City Max:', data_set.max(axis=0)
print 'City Mean:', data_set.mean(axis=0)
print 'City SD:', data_set.std(axis=0)

#4 The Wind speeds for everyday
print 'Everyday Min:', data_set.min(axis=1)
print 'Everyday Max:', data_set.max(axis=1)
print 'Everyday Mean:', data_set.mean(axis=1)
print 'Everyday SD:', data_set.std(axis=1)

#5 City with greatest windspeed
print 'City with greatest windspeed:', data_set.argmax(axis=1)

#6 Find the year, month and day on which the greatest windspeed was recorded.
daily_max = data_set.max(axis=1)
max_row = daily_max.argmax()

print 'Year:', int(wind_data[max_row,0])
print 'Month:', int(wind_data[max_row,1])
print 'Day:', int(wind_data[max_row,2])

#7 Average for January
january_indices = wind_data[:,1] == 1
january_data = data_set[january_indices]

print 'Mean for January;', january_data.mean(axis=0)
