#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

### your code goes here

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.3, random_state=42)
# print('features', features)
# print('xtrain=', xtrain)
# print('xtest=', xtest)
# print('ytrain=', ytrain)
# print('ytest=', ytest)


pois = [elem for elem in ytest if elem == 1]
print('poi size:', len(pois))
print('test set size:', len(ytest))

pred_zero = [0.] * 29
accuracy = accuracy_score(ytest, pred_zero)
print ("Zero Accuracy: ", accuracy)

# precision = precision_score(ytest, pred_zero)
# print ("Precision: ", precision)
#
# recall = recall_score(ytest, pred_zero)
# print ("Recall: ", recall)

# print(ytrain)
# print(ytest)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

counter = 0
for pred, actual in zip(predictions, true_labels):
    if pred == 1 and actual == 1:
        counter+=1
print('true positives=', counter)

counter = 0
for pred, actual in zip(predictions, true_labels):
    if pred == 0 and actual == 0:
        counter+=1
print('true negatives=', counter)

counter = 0
for pred, actual in zip(predictions, true_labels):
    if pred == 1 and actual == 0:
        counter+=1
print('false positives=', counter)

counter = 0
for pred, actual in zip(predictions, true_labels):
    if pred == 0 and actual == 1:
        counter+=1
print('false negatives=', counter)

precision = precision_score(true_labels, predictions)
print ("Test Precision: ", precision)

recall = recall_score(true_labels, predictions)
print ("Test Recall: ", recall)


clf = tree.DecisionTreeClassifier()
#clf.fit(features, labels)
clf.fit(xtrain, ytrain)
pred = clf.predict(xtest)
# print('pred', pred)

acc = accuracy_score(ytest, pred)
print ("Accuracy: ", acc)

precision = precision_score(ytest, pred)
print ("Precision: ", precision)

recall = recall_score(ytest, pred)
print ("Recall: ", recall)

