import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

# Generate the make_moons dataset with 100 samples and noise level of 0.05
X, y = make_moons(n_samples=100, noise=0.05, random_state=42)

# Create a scatter plot of the dataset
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu_r)

# Set the plot labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('make_moons dataset')

# Show the plot
plt.show()