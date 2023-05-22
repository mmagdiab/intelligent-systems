

# DataFlair Iris Classification
# Import Packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels'] # As per the iris dataset information



# Load the data
df = pd.read_csv('iris.data', names=columns)




df.head()




# Some basic statistical analysis about the data
df.describe()




# Visualize the whole dataset
sns.pairplot(df, hue='Class_labels')




# Seperate features and target  
data = df.values
X = data[:,0:4]
Y = data[:,4]





# Split the data to train and test dataset.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)





# Support vector machine algorithm
from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, y_train)





# Predict from the test dataset
predictions = svn.predict(X_test)





# Calculate the accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)




# A detailed classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))





X_new = np.array([[3, 2, 1, 0.2], [  4.9, 2.2, 3.8, 1.1 ], [  5.3, 2.5, 4.6, 1.9 ]])
#Prediction of the species from the input vector
prediction = svn.predict(X_new)
print("Prediction of Species: {}".format(prediction))





# Save the model
import pickle
with open('SVM.pickle', 'wb') as f:
    pickle.dump(svn, f)





# Load the model
with open('SVM.pickle', 'rb') as f:
    model = pickle.load(f)





model.predict(X_new)






