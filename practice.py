from sklearn import tree

#decision tree is like a flow chart

#[height, weight, shoe size]

X = [[181, 80, 44], [177, 70, 43], [160,60,38], [154,54,37], [166,65,40], [190,90,47],[175,64,39],[177,70,40],[159,67,40],[171,75,42],[181,85,43]]

Y = ['male', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediciton = clf.predict([[190,70,43]])

print (prediciton)
