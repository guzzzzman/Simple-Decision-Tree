from sklearn.linear_model import LinearRegression

#Tv Size in inches

X = [ [32], [80], [100], [24], [42]]

#price of Tv (in USD) based on how big it is

Y = [ [100], [200], [500], [90], [140]]

model = LinearRegression()

model.fit(X,Y)

tv = [ [90] ]
price = model.predict(tv)
print(price)
