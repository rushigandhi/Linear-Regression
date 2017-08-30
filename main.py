import pandas
from sklearn import linear_model
import matplotlib.pyplot as graph

data = pandas.read_fwf('temp_vs_alt.txt')
x_vals = data[['Altitude']]
y_vals = data[['Temperature']]

# Graphing the Line of Best Fit
regression = linear_model.LinearRegression()
regression.fit(x_vals, y_vals)

graph.scatter(x_vals, y_vals)
graph.plot(x_vals, regression.predict(x_vals))

x_vals = list(x_vals.values.T.flatten())
y_vals = list(y_vals.values.T.flatten())

# Mean of x and y values
x_mean = 0
y_mean = 0
for i in range(len(x_vals)):
    x_mean += x_vals[i]
    y_mean += y_vals[i]

x_mean = x_mean/len(x_vals)
y_mean = y_mean/len(y_vals)

# Finding delta x and delta y values from the means
x_delta_vals = list()
y_delta_vals = list()

for i in range(len(x_vals)):
    x_delta_vals.append(x_vals[i] - x_mean)
    y_delta_vals.append(y_vals[i] - y_mean)

# Sum of the square of the delta x values
sum_x_squares = 0

for i in range(len(x_delta_vals)):
    sum_x_squares += x_delta_vals[i]**2

# Sum of the product of delta x and delta y values
sum_deltas = 0
for i in range(len(x_delta_vals)):
    sum_deltas += x_delta_vals[i]*y_delta_vals[i]

# Calculating the slope
slope = sum_deltas/sum_x_squares

# Calculating the y-intercept
y_intercept = y_mean - (slope*x_mean)


# Predicting the temperature using the equation of the line of best fit
def predict_temperature(altitude):
    temperature = slope*int(altitude) + y_intercept
    print("The predicted temperature for that altitude is " + str(temperature) + " degrees Celsius")


print("Please enter the altitude (km):")
predict_temperature(int(input()))
#graph.show()
