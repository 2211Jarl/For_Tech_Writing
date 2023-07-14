import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# load moons dataset
x, y = datasets.make_moons(n_samples=100, noise=0.15, random_state=42)

# create SVM classifier with a radial basis function (RBF) kernel
clf = SVC(kernel='rbf', gamma=2)

# train the classifier on the dataset
clf.fit(x, y)

# create a meshgrid of points to plot the decision boundary
x_min, x_max = x[:, 0].min() - 0.1, x[:, 0].max() + 0.1
y_min, y_max = x[:, 1].min() - 0.1, x[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# create a contour plot of the decision boundary
plt.contourf(xx, yy, z, cmap=plt.cm.RdBu, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.RdBu_r)

# set the plot labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('SVM Decision Boundary')

# show the plot
plt.show()