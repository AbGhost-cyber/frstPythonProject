"""
KNN (K-Nearest Neighbors) is a popular machine learning algorithm used for classification and regression tasks.
It is a simple algorithm that takes into account the K-nearest data points (neighbors) to classify a new data point.
It is useful in situations when there is no prior knowledge of the underlying structure of the data.

this is a simple example of KNN in Python which classifies a set of data points into two classes
(blue and red) based on their x and y coordinates. In this example, we will use a dataset that
has 300 data points, with 150 belonging to the blue class and 150 belonging to the red class.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


def example():
    # GENERATE RANDOM DATA POINTS
    np.random.seed(0)
    X = np.random.rand(300, 2)
    y = np.concatenate([np.ones(150), np.zeros(150)])

    # PLOT THE DATA POINTS
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.title("Dataset")
    plt.show()

    # INITIALIZE THE CLASSIFIER
    clf = KNeighborsClassifier(n_neighbors=3)

    # TRAIN THE CLASSIFIER
    clf.fit(X, y)

    # CREATE NEW DATA POINT TO CLASSIFY
    new_X = np.array([[0.5, 2.0]])

    # PREDICT THE CLASS OF THE NEW DATA POINT
    predicted_class = clf.predict(new_X)

    # PRINT THE PREDICTED CLASS
    print(f"Predicted class: {predicted_class}")


"""
In this example, we first generate random data points using the numpy library.
 We then plot the data points on a scatter plot with blue and red points representing the two classes.

Next, we initialize a KNeighborsClassifier with three neighbors and train the model 
with the data points and their associated classes.

Finally, we create a new data point with coordinates (0.5, 2.0) and 
use the trained classifier to predict its class. The predicted class is then 
printed to the console as either 0 (blue) or 1 (red).

Overall, this example demonstrates how KNN can be used to classify data 
points based on their proximity to other data points belonging to a particular class.
"""

if __name__ == '__main__':
    example()
#    x axis  [10 21]
# y axis  [20 30]
