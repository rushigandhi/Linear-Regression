import pandas
from sklearn import linear_model
import matplotlib.pyplot as graph

data = pandas.read_fwf('temp_vs_alt.txt')
x_vals = data[['Altitude']]
y_vals = data[['Temperature']]

regression = linear_model.LinearRegression()
regression.fit(x_vals, y_vals)

graph.scatter(x_vals, y_vals)
graph.plot(x_vals, regression.predict(x_vals))
graph.show()

