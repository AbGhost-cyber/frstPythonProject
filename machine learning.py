import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import joblib
import matplotlib.pyplot as plt

# step 1: import the data
music_data = pd.read_csv('/Users/mac/PycharmProjects/music.csv')

# step 2: clean / preparing the data to remove duplicates or null values etc.
# however we don't have this issue because our data set is small and unique, no nulls etc.
# step 3: split the data into training
# in this step we will drop the genre column, and also create an output Set
# X represents our input data Set, y represents our output dataset
X = music_data.drop(columns=["genre"])
y = music_data['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# step 4: create a model
model = DecisionTreeClassifier()

# step 5: train the model
# builds a decision tree classifier from a given input set of X train and output set of y train
model.fit(X.values, y)
# joblib.dump(model, 'music-recommender.joblib')
# model = joblib.load('music-recommender.joblib')
# step 6: make predictions
predication = model.predict([[21, 1]])

tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all', rounded=True, filled=True)

# step 7: evaluation of performance
# score = accuracy_score(y_test, predication)
if __name__ == '__main__':
    # print(f"model accuracy score: {score * 100}")
    print(predication)
