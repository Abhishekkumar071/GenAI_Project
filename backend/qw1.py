import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Build GMM model
gmm = GaussianMixture(n_components=3, random_state=42)

# Train model using EM algorithm
gmm.fit(X_scaled)

# Predict clusters
labels = gmm.predict(X_scaled)

# Evaluate clustering
score = silhouette_score(X_scaled, labels)

print("Silhouette Score:", score)

# Visualize clusters
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=labels)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.title("Gaussian Mixture Model Clustering")

plt.show()