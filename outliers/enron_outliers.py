#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import operator

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
features = ["salary", "bonus"]
# features = ["exercised_stock_options"]
data_dict.pop("TOTAL", 0 )
data = featureFormat(data_dict, features)
sorted_data = sorted(data, key=operator.itemgetter(0, 1))
# sorted_data = sorted(data, key=operator.itemgetter(0, 0))
print(sorted_data[0])
print(sorted_data[len(sorted_data)-1])
print([(v['salary'], v['bonus'], k)
    for k, v in data_dict.items()
       if not v["salary"] == 'NaN' and v["salary"] > 1000000. and not v["bonus"] == 'NaN' and v["bonus"] > 5000000.])
print([(v['salary'], v['bonus'], k)
    for k, v in data_dict.items()
       if not v["salary"] == 'NaN' and v["salary"] < 1000.])

# print([(v['salary'], v['bonus'], k)
#        for k, v in data_dict.items()
#        if v["salary"] == 'NaN'])

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
