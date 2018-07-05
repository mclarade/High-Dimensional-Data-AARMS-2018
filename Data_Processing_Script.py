import numpy as np
import sklearn.preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data_features = np.loadtxt('Data_T1N0.csv', delimiter=',', usecols=range(1,2001), skiprows=1)
target = np.loadtxt('Data_T1N0.csv', delimiter=',', usecols=2001, skiprows=1)
normalized_features = sklearn.preprocessing.maxabs_scale(data_features, axis=1)
estimator = sklearn.linear_model.LinearRegression()
feature_selector = RFE(estimator, 1000)
selected_features = feature_selector.fit_transform(normalized_features, target)
feature_train, feature_test, target_train, target_test =train_test_split(selected_features, target)
classifier = SVC(kernel='linear')
classifier.fit(feature_train, target_train)
print classifier.predict(feature_test)
print target_test
print classifier.score(feature_test, target_test)