#!/usr/bin/python

import sys
import pickle
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
# bonus long_tern_incentive
features_list = ['poi','salary','bonus', 'long_term_incentive'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
# names=data_dict.keys()
# for name in names:
#     if (data_dict[name]["bonus"]=="NaN" and data_dict[name]["salary"]=="NaN" and data_dict[name]["from_poi_to_this_person"]=="NaN" and data_dict[name]["from_this_person_to_poi"]=="NaN" and data_dict[name]["total_stock_value"]=="NaN" and data_dict[name]["shared_receipt_with_poi"]=="NaN"):
        # print(name)
        # data_dict.pop(name,0)
data_dict.pop("TOTAL",0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK",0)
data_dict.pop("YEAP SOON",0)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html


# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
# GausssianNB() completes quickly
# Accuracy: 0.77300	Precision: 0.36969	Recall: 0.19150	F1: 0.25231	F2: 0.21193
# Total predictions: 10000	True positives:  383	False positives:  653	False negatives: 1617	True negatives: 7347
# clf = GaussianNB()
from sklearn.svm import SVC
# SVC(kernel="linear", C=0.025) does not terminate
# clf = SVC(kernel="linear", C=0.025)
# AttributeError: 'tuple' object has no attribute 'fit'
# clf = SVC(gamma=2, C=1),

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
# Got a divide by zero when trying out:
# GaussianProcessClassifier(copy_X_train=True,
#   kernel=1**2 * RBF(length_scale=1), max_iter_predict=100,
#   multi_class='one_vs_rest', n_jobs=1, n_restarts_optimizer=0,
#   optimizer='fmin_l_bfgs_b', random_state=None, warm_start=True)
# Precision or recall may be undefined due to a lack of true positive predicitons.
# clf = GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True)

# from sklearn.dummy import DummyClassifier
# Accuracy: 0.69610	Precision: 0.20633	Recall: 0.18250	F1: 0.19369	F2: 0.18682
# Total predictions: 10000	True positives:  365	False positives: 1404	False negatives: 1635	True negatives: 6596
# clf = DummyClassifier(strategy='stratified', random_state=None, constant=None);

# from sklearn.tree import DecisionTreeClassifier
# clf = DecisionTreeClassifier(random_state=0)
# Accuracy: 0.68560	Precision: 0.22762	Recall: 0.23900	F1: 0.23317	F2: 0.23663
# Total predictions: 10000	True positives:  478	False positives: 1622	False negatives: 1522	True negatives: 6378

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
clf1 = LogisticRegression(random_state=1)
clf2 = RandomForestClassifier(random_state=1)
clf3 = GaussianNB()
clf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)])

# Accuracy: 0.78040	Precision: 0.36275	Recall: 0.12950	F1: 0.19086	F2: 0.14861
# Total predictions: 10000	True positives:  259	False positives:  455	False negatives: 1741	True negatives: 7545


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Using a VotingClassifier gives a precision of .36275 i.e. better than .3

# Example starting point. Try investigating other evaluation techniques!

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
