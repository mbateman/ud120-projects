#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print(len(enron_data))
### print(len(next (iter (enron_data.values()))))
### print(next (iter (enron_data.values())))
### print(enron_data["PRENTICE JAMES"]["total_stock_value"])
### print(enron_data["PRENTICE JAMES"].keys())
### print(enron_data["COLWELL WESLEY"].keys())
### print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
### print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
### print(enron_data["SKILLING JEFFREY K"]["total_payments"])
### print(enron_data["LAY KENNETH L"]["total_payments"])
### print(enron_data["FASTOW ANDREW S"]["total_payments"])
### data[person_name]["poi"]==1

### dict_you_want = { person_name: old_dict[person_name] for person_name in your_keys }
### print(dict((key,value) for key, value in enron_data.items() if key == person_name))
### print(len({k: v for k, v in enron_data.items() if v["poi"] == True}))
###for key, value in enron_data.items():
###	print(value)
mykeys = ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]
### print([(v["total_payments"], k) for k, v in enron_data.items() if k in mykeys])
### [v for k, v in enron_data.items() if k in mykeys]
### print([(v["salary"], k) for k, v in enron_data.items() if k in mykeys])
### print([(v["salary"], k) for k, v in enron_data.items() if not v["salary"] == 'NaN'])
print(len([(v["salary"], k) for k, v in enron_data.items() if not v["salary"] == 'NaN']))
print(len([(v["email_address"], k) for k, v in enron_data.items() if not v["email_address"] == 'NaN']))
print(len([(v["total_payments"], k) for k, v in enron_data.items() if v["total_payments"] == 'NaN']))
print(len([(v["total_payments"], k) for k, v in enron_data.items() if (v["total_payments"] == 'NaN') and (v["poi"] == True)]))
print(len({k: v for k, v in enron_data.items() if v["poi"] == True}))
### print([(v["email_address"], k) for k, v in enron_data.items()])

