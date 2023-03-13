import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier

cols = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', "class"]
df = pd.read_csv('magic04.data', names=cols)
df["class"] = (df["class"] == "g").astype(int)

train, valid, test = np.split(df.sample(frac=1), [int(0.6 * len(df)), int(0.8 * len(df))])


def scale_dataset(dataframe, over_sample=False):
    # feature vectors
    X = dataframe[dataframe.columns[:-1]].values
    # label
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if over_sample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)

    data = np.hstack((X, np.reshape(y, (-1, 1))))

    return data, X, y


train, X_train, y_train = scale_dataset(train, over_sample=True)
valid, X_valid, y_valid = scale_dataset(valid, over_sample=False)
test, X_test, y_test = scale_dataset(test, over_sample=False)
knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(X_train, y_train)
y_predict = knn_model.predict(X_test)

def plot():
    for label in cols[:-1]:
        plt.hist(df[df["class"] == 1][label], color='blue', label='gamma', alpha=0.7, density=True)
        plt.hist(df[df["class"] == 0][label], color='red', label='hadron', alpha=0.7, density=True)
        plt.title(label)
        plt.ylabel("Probability")
        plt.xlabel(label)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    print(y_predict)
