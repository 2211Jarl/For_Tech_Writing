from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

iris=datasets.load_iris()
x=iris.data
y=iris.target

x_train, x_test, y_train, y_test = tts(x,y,test_size=0.3,random_state=10)

#build an SVM model with linear kernel
clf=SVC(kernel='linear')

#fit the model
clf.fit(x_train,y_train)

#predict the labels
y_pred=clf.predict(x_test)

#calculate the accuracy
acc=accuracy_score(y_test,y_pred)
print("Accuracy: ", acc)

#get the hyperplane parameters
w=clf.coef_[0]
b=clf.intercept_[0]

#calculate the slope and intercept
slope = -w[0]/w[1]
y_int = -b/w[1]

#plot the dataset and hyperplane
plt.scatter(x[:,0], x[:,1], c=y)
axes=plt.gca()
x_vals=np.array(axes.get_xlim())
y_vals=y_int+slope*x_vals
plt.plot(x_vals, y_vals, '--')
plt.show()