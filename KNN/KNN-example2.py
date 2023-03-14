"""
Suppose we have a dataset that contains information about fruits,
 including their weight and sweetness level, and we would like
 to classify a new fruit as either an apple or a banana based
 on its weight and sweetness level.

 Below is an example code that solves this problem using
  K-nearest neighbors classification algorithm in Python:

"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Create a dataset with two features: weight and sweetness
fruits = pd.DataFrame({'Weight': [70, 90, 80, 85, 75, 95],
                       'Sweetness': [20, 30, 25, 28, 22, 32],
                       'Label': ['Apple', 'Banana', 'Apple', 'Apple', 'Apple', 'Banana']})

# Separate the features and the labels
X = fruits.iloc[:, :-1].values
y = fruits.iloc[:, -1].values

# Create a KNN classifier with k=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# Fit the model with the data
knn.fit(X, y)

# Classify a new fruit with weight 78 and sweetness 26
new_fruit = [[78, 26]]
label = knn.predict(new_fruit)

print('The predicted label is:', label[0])
