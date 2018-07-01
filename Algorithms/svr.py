import sys
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import numpy as np
#from sklearn import linear_model
import matplotlib.pyplot as plt
from datetime import date, timedelta

dates = []
prices = []

#defining the model
svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma=0.1)

# convert the date
def convert_to_integer(dt_time):
    return 10000*dt_time.year + 1000*dt_time.month + dt_time.day
	
#read the csv file
def get_data(filename):
	df = pd.read_csv(filename)
	global dates 
	global prices 
	for row in df.iterrows():
		if row[1][1] == 'EQ':
			dates.append(pd.to_datetime(row[1][2]))
			prices.append(row[1][9])
	
	dates = [ convert_to_integer(i) for i in dates ]
	dates = np.reshape(dates, (len(dates),1)) # converting to matrix of n X 1
	return



def plot_graph():
	global svr_rbf
	#svr_rbf.fit(dates, prices) # fitting the data points in the models
	X_train, X_test, y_train, y_test = train_test_split(dates,prices,test_size=0.2)
	svr_rbf.fit(X_train, y_train)
	#print(svr_rbf.score(X_test, y_test))
	print "Accuracy is " , svr_rbf.score(X_test, y_test)
	
	svr_rbf.fit(dates, prices) # fitting the data points in the models

	plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	# plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	# plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()


def prediction():
	global svr_rbf
	predict_price = []

	for i in range(0,30):
		predict_price.append(convert_to_integer((date.today()+timedelta(days=i))))

	#print(predict_price)

	predict_price = [ svr_rbf.predict(i)[0] for i in predict_price ]

	today_price = predict_price[0]

	k=0
	for i in predict_price:
		print "The price for %dth day is %f "% (k,i)
		k=k+1


	buy = 0
	for i in predict_price:
		if(i-today_price <= 2):
			buy= buy+1
	if buy>15:
		print "You Should not buy this stock for short term inverstement"
	else:
		print "You can buy it, their are fair chances of hike the stock price"

## start

filename =sys.argv[1]

get_data(filename)

plot_graph()

prediction()