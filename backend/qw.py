import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# generate synthetic data
data = np.concatenate([
    np.random.normal(110,5,100),
    np.random.normal(170,5,100)
]).reshape(-1,1)

# create GMM model
gmm = GaussianMixture(n_components=2)

# train model
gmm.fit(data)

# predict clusters
labels = gmm.predict(data)

# visualize
plt.scatter(data, labels)
plt.title("Gaussian Mixture Model Clustering")
plt.xlabel("Height")
plt.ylabel("Cluster")
plt.show()