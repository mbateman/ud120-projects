#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# shorten training set
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 




#########################################################
### your code goes here ###

#########################################################

# clf = svm.SVC(kernel='linear')
# try several values of C (say, 10.0, 100., 1000., and 10000.)
clf = svm.SVC(kernel='rbf', C=10000)
t0 = time()
clf.fit(features_train, labels_train) 
print "training time:", round(time()-t0, 3), "s"
t1 = time()
prediction = clf.predict(features_test)
print "prediction @ 10", prediction[10]
print "prediction @ 26", prediction[26]
print "prediction @ 50", prediction[50]
print "prediction time:", round(time()-t1, 3), "s"
print "score:", accuracy_score(prediction, labels_test)
chris = filter(lambda x: x == 1, prediction)
sara = filter(lambda x: x == 0, prediction)
print "total number of predictions: ", len(prediction)
print "total chris predictions: ", len(chris)
print "total sara predictions: ", len(sara)
# full set outcomes
# training time: 243.996 s
# prediction time: 24.866 s
# score: 0.984072810011
# subset outcomes
# training time: 0.123 s
# with C on subset at 10000:
# training time: 0.155 s
# prediction time: 1.342 s
# score: 0.892491467577
# prediction time: 1.215 s
# score: 0.884527872582
