import math
import numpy as np
import pandas as pd
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


class MyKNeighborsClassifier:
  def __init__(self, n_neighbours: int = 5, weights: str = "uniform", metric: str = "euclidean"):
    if metric not in ["manhattan", "euclidean"]:
      raise ValueError("This type of metric is not supported: {}".format(metric))
    if weights not in ["uniform", "distance"]:
      raise ValueError("This type of weights is not supported: {}".format(weights))
    
    self.n_neighbours = n_neighbours
    self.weights = weights
    self.metric = metric

    self.train_X = None
    self.train_y = None

  def fit(self, X: np.ndarray, y: np.ndarray) -> None:
    self.train_X = X
    self.train_y = y
  
  def euclidean(self, p1: np.array, p2: np.array):
    dist = 0.0
    for i in range(p1.shape[0]):
      dist += (p2[i] - p1[i]) ** 2
    return math.sqrt(dist)
  
  def manhattan(self, p1: np.array, p2: np.array):
    dist = 0.0
    for i in range(p1.shape[0]):
      dist += abs(p1[i] - p2[i])
    return dist

  def predict(self, X: np.ndarray) -> np.ndarray:
    result = []
    for i in range(X.shape[0]):
      dists = [] # keeps distances to points and its indices
      for j in range(self.train_X.shape[0]):
        if self.metric == "manhattan":
          dists.append([j, self.manhattan(X[i], self.train_X[j])])
        else:
          dists.append([j, self.euclidean(X[i], self.train_X[j])])
      dists = sorted(dists, key=lambda x: x[1])
    
      type1 = 0
      type2 = 0
      for k in range(self.n_neighbours):
        weight = 1
        if self.weights == "distance":
          weight /= dists[k][1]
        if self.train_y[dists[k][0]] == 0:
          type1 += weight
        else:
          type2 += weight
      if type1 < type2:
        result.append(1)
      else:
        result.append(0)
    return np.array(result)

# generating data

X, y = make_moons(n_samples=500, noise=0.3, random_state=42)
plt.scatter(X[:, 0], X[:, 1], c=y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# comparing models: default params

model1 = MyKNeighborsClassifier()
model1.fit(X_train, y_train)

sk_model1 = KNeighborsClassifier()
sk_model1.fit(X_train, y_train)

y_pred = model1.predict(X_test)
sk_y_pred = sk_model1.predict(X_test)
print("My classifier:", accuracy_score(y_test, y_pred))
print("Sk classifier:", accuracy_score(y_test, sk_y_pred))

my_accurancies = []
sk_accurancies = []
ks = []

for k in range(1, 11):
  ks.append(k)
  model1 = MyKNeighborsClassifier(n_neighbours=k)
  model1.fit(X_train, y_train)
  sk_model1 = KNeighborsClassifier(n_neighbors=k)
  sk_model1.fit(X_train, y_train)
  y_pred = model1.predict(X_test)
  sk_y_pred = sk_model1.predict(X_test)

  my_accurancies.append(accuracy_score(y_test, y_pred))
  sk_accurancies.append(accuracy_score(y_test, sk_y_pred))

plt.plot(ks, my_accurancies)
plt.plot(ks, sk_accurancies, 'r--')


